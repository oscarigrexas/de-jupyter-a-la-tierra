from kedro.pipeline import Pipeline, node

from .nodes import preprocess_raw_data


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=preprocess_raw_data,
                inputs={"dataset": "catfood_dataset"},
                outputs="model_input_table",
                name="preprocess_raw_dataset",
            ),
        ]
    )
