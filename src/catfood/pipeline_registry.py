from typing import Dict

from kedro.pipeline import Pipeline

from catfood.pipelines import data_processing as dp
from catfood.pipelines import data_science as ds
from catfood.pipelines import prediction as pred


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.

    """
    data_processing_pipeline = dp.create_pipeline()
    data_science_pipeline = ds.create_pipeline()
    prediction_pipeline = pred.create_pipeline()

    return {
        "__default__": data_processing_pipeline + data_science_pipeline,
        "dp": data_processing_pipeline,
        "ds": data_science_pipeline,
        "pred": prediction_pipeline,
    }
