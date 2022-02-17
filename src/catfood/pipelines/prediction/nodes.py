import logging
from typing import Dict

import numpy as np
from sklearn.linear_model import LogisticRegression


logger = logging.getLogger(__name__)


def predict_score(
    trained_model: LogisticRegression, prediction_features: Dict[str, float]
):
    logger.info(f"Predicting score for {prediction_features}")
    input_array = np.array(list(prediction_features.values())).reshape(1, -1)
    score = trained_model.predict(input_array)[0]
    logger.info(f"Predicted score: {score}")
    return score
