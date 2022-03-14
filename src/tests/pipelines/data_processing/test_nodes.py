import pandas as pd

from catfood.pipelines.data_processing.nodes import _parse_calorie_column


def test_parse_calorie_column(
    calorie_df: pd.DataFrame, parsed_calorie_df: pd.DataFrame
):
    pd.testing.assert_frame_equal(parsed_calorie_df, _parse_calorie_column(calorie_df))
