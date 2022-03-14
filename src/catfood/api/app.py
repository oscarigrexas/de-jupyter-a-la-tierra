from pathlib import Path

import uvicorn
from fastapi import FastAPI, Query
from kedro.framework.startup import _get_project_metadata, _add_src_to_path
from kedro.framework.session import KedroSession
from pydantic import BaseModel, Field


app = FastAPI(
    title="CatfoodAPI",
    version="0.1",
)


project_path = Path.cwd()
metadata = _get_project_metadata(project_path)
_add_src_to_path(metadata.source_dir, project_path)


class NutritionalInfo(BaseModel):
    dma_ash: float = Field(
        ..., description="Porcentaje de ceniza o materia inorgánica", ge=0, lt=100
    )
    dma_cals: float = Field(..., description="Las calorías por 100 g", ge=0)
    dma_carbs: float = Field(
        ...,
        description="Porcentaje de hidratos de carbono en muestra seca",
        ge=0,
        lt=100,
    )
    dma_prot: float = Field(
        ..., description="Porcentaje de proteínas en muestra seca", ge=0, lt=100
    )
    ga_moist: float = Field(..., description="Porcentaje de humedad", ge=0, lt=100)


class NutritionalScore(BaseModel):
    score: int = Field(..., description="The nutritional score from 1 to 5", ge=1, le=5)


@app.post("/predict_score", response_model=NutritionalScore)
def predict_score(nutritional_info: NutritionalInfo):
    with KedroSession.create(
        package_name=metadata.package_name,
        project_path=project_path,
        extra_params={"prediction_features": dict(nutritional_info)},
    ) as session:
        output = session.run(pipeline_name="pred")
    return NutritionalScore(score=output["score"])


def run():
    """Run the API using Uvicorn"""
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=1234,
        reload=True,
        reload_dirs=["src"],
    )
