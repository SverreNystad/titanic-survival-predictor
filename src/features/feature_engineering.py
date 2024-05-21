""" This module contains functions to prepare the data for the model. """

import pandas as pd
import numpy as np


def engineer_features(features: pd.DataFrame) -> pd.DataFrame:
    """
    Conduct the required feature engineering.

    Args:
        features: The features to engineer.

    Returns:
        The engineered features.
    """
    # TODO Add relevant feature engineering
    features['relatives'] = features['SibSp'] + features['Parch']
    features.loc[features['relatives'] > 0, 'traveled_alone'] = 'No'
    features.loc[features['relatives'] == 0, 'traveled_alone'] = 'Yes'
    return features

def _add_family_size_feature(features: pd.DataFrame) -> pd.DataFrame:
    features['FamilySize'] = features['SibSp'] + features['Parch'] + 1
    
    features['FamilySize'] = features['FamilySize'].apply(lambda size: 'Single' if size == 1 else 'Small' if size < 5 else 'Large')
    return features

def _process_missing_cabin(features: pd.DataFrame) -> pd.DataFrame:
    features['Cabin'] = features['Cabin'].fillna('U')
    features['Cabin'] = features['Cabin'].apply(lambda cabin: cabin[0])

    
    return features

def _add_age_bucket_feature(features: pd.DataFrame) -> pd.DataFrame:
    pass

def _add_title_feature(features: pd.DataFrame) -> pd.DataFrame:
    TITLES = {
        'Capt': 'Officer',
        'Col': 'Officer',
        'Major': 'Officer',
        'Jonkheer': 'Royalty',
        'Don': 'Royalty',
        'Sir': 'Royalty',
        'Dr': 'Officer',
        'Rev': 'Officer',
        'the Countess': 'Royalty',
        'Mme': 'Mrs',
        'Mr': 'Mr',
        'Mrs': 'Mrs',
        'Miss': 'Mrs',
        'Master': 'Master',
        'Lady': 'Royalty',
    }
    
    features['Title'] = features['Name'].apply(lambda name: TITLES.get(name.split(',')[1].split('.')[0].strip(), 'Other'))
    features['Title'] = features['Title'].map(TITLES)
    return features