from typing import List

import pandas as pd


def _convert_percent_columns(dataset: pd.DataFrame) -> pd.DataFrame:
    percent_cols = [
        "dma_ash",
        "dma_carbs",
        "dma_fat",
        "dma_fiber",
        "dma_prot",
        "ga_ash",
        "ga_carbs",
        "ga_fat",
        "ga_fiber",
        "ga_moist",
        "ga_prot",
    ]
    for col in percent_cols:
        dataset[col] = dataset[col].str.rstrip("%").astype("float")
    return dataset


def _parse_calorie_column(dataset: pd.DataFrame) -> pd.DataFrame:
    dataset["dma_cals"] = (
        dataset["dma_cals"]
        .map(lambda x: x.split("/")[0].replace(",", ""))
        .astype("float")
    )
    return dataset


def _convert_score_columns(dataset: pd.DataFrame) -> pd.DataFrame:
    score_columns = [col for col in dataset.columns if "_paws" in col]
    for col in score_columns:
        dataset[col] = dataset[col].str[1].astype("int")
    return dataset


def _convert_ingredient_columns(dataset: pd.DataFrame) -> pd.DataFrame:
    ingredient_cols = [
        "ingredients",
        "quality_ingredients",
        "questionable_ingredients",
        "potential_allergens",
    ]
    for col in ingredient_cols:
        dataset[col].fillna("")
        dataset[col] = dataset[col].str.split(",")
    return dataset


def preprocess_raw_data(dataset: pd.DataFrame) -> pd.DataFrame:
    percents_converted = _convert_percent_columns(dataset=dataset)
    calories_parsed = _parse_calorie_column(dataset=percents_converted)
    scores_converted = _convert_score_columns(dataset=calories_parsed)
    ingredients_converted = _convert_ingredient_columns(dataset=scores_converted)
    return ingredients_converted
