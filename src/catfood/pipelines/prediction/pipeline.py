from kedro.pipeline import Pipeline, node

from .nodes import predict_score


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=predict_score,
                inputs=["trained_model", "params:prediction_features"],
                outputs="predicted_score",
                name="predict_score",
            ),
        ]
    )
