from kedro.runner.sequential_runner import SequentialRunner
import pandas as pd

from catfood.pipelines.data_processing import create_pipeline


def test_preprocessing_pipeline(
    data_preprocessing_catalog, model_input_table_test: pd.DataFrame
):
    runner = SequentialRunner()
    pipeline = create_pipeline()
    outputs = runner.run(pipeline=pipeline, catalog=data_preprocessing_catalog)
    output_model_input_table = outputs["model_input_table"]
    pd.testing.assert_frame_equal(model_input_table_test, output_model_input_table)
