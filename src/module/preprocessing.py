import pandas as pd

def run_prefecture(df):
    """
    Preprocess prefecture data

    Params:
        df: 'gs://tourism_statistics/prefecture.csv'
    Returns:
    df: Preprocessed prefecture data
    
    """

    # Rename columns
    df.columns = ['year', 'month', 'area_segment', 'data_segment', 'area_code', 'prefecture', 'population']
    # Create a year_month column
    df['year_month'] = df['year'].astype(str) + '-' + df['month'].astype(str).str.zfill(2)
    df['year_month'] = pd.to_datetime(df['year_month'])

    return df


def run_city(df):
    """
    Preprocess city data

    Params:
        df: 'gs://tourism_statistics/city.csv'
    Returns:
        df: Preprocessed city data

    """

    # Rename columns
    df.columns = [
        'year', 'month', 'area_segment', 'data_segment', 'prefecture_code', 'prefecture',
        'area_code', 'area', 'population'
    ]
    # Create a year_month column
    df['year_month'] = df['year'].astype(str) + '-' + df['month'].astype(str).str.zfill(2)
    df['year_month'] = pd.to_datetime(df['year_month'])

    return df