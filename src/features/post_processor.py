""" This module contains functions to post-process the data."""

import pandas as pd


def post_process(predictions: pd.DataFrame) -> pd.DataFrame:
    """Post-process the predictions."""
    predictions["Survived"] = predictions["Survived"].apply(
        lambda survived: 1 if survived >= 0.5 else 0
    )
    predictions["PassengerId"] = predictions.index + 892
    # Remove index
    predictions = predictions.set_index("PassengerId")

    return predictions
