from ast import literal_eval

from pathlib import Path

import pandas as pd
import pytest


@pytest.fixture
def calorie_df() -> pd.DataFrame:
    data = ["313/100g", "90/100g", "123/100g"]
    return pd.DataFrame(data=data, columns=["dma_cals"])


@pytest.fixture
def parsed_calorie_df() -> pd.DataFrame:
    data = [313.0, 90.0, 123.0]
    return pd.DataFrame(data=data, columns=["dma_cals"])


@pytest.fixture
def data_preprocessing_catalog():
    from kedro.io.data_catalog import DataCatalog
    from kedro.extras.datasets.pandas import CSVDataSet

    catalog = DataCatalog(
        {
            "catfood_dataset": CSVDataSet(
                filepath=str(Path(__file__).with_name("catfood_dataset_test.csv"))
            )
        }
    )
    return catalog


@pytest.fixture
def model_input_table_test() -> pd.DataFrame:
    ingredient_cols = [
        "ingredients",
        "quality_ingredients",
        "questionable_ingredients",
        "potential_allergens",
    ]

    def parse_list_string(string: str):
        if string == "":
            return None
        else:
            return string.strip("[]").replace("'", "").split(", ")

    return pd.read_csv(
        str(Path(__file__).with_name("model_input_table_test.csv")),
        converters={col: parse_list_string for col in ingredient_cols},
    )
