import logging
from typing import Dict, Tuple

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split


def split_data(data: pd.DataFrame, parameters: Dict) -> Tuple:
    X = data[parameters["features"]]
    y = data[parameters["target"]]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=parameters["test_size"], random_state=parameters["random_state"]
    )
    return X_train, X_test, y_train, y_test


def train_model(
    X_train: pd.DataFrame, y_train: pd.Series, parameters: Dict
) -> LogisticRegression:
    regressor = LogisticRegression(
        multi_class=parameters["multi_class"], solver=parameters["solver"]
    )
    regressor.fit(X_train, y_train)
    return regressor


def evaluate_model(
    trained_model: LogisticRegression, X_test: pd.DataFrame, y_test: pd.Series
):
    y_pred = trained_model.predict(X_test)
    logger = logging.getLogger(__name__)
    class_rep = classification_report(y_true=y_test, y_pred=y_pred)
    logger.info(class_rep)
    f, ax = plt.subplots()
    sns.heatmap(
        data=confusion_matrix(y_test, y_pred), square=True, annot=True, fmt="d", ax=ax
    )
    ax.set_ylim([5, 0])
    return f
