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
