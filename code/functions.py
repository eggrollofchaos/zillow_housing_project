import pandas as np

def melt_data(df):
    '''
    Takes in a Zillow Housing Data File (ZHVI) as a DataFrame in wide format
    and returns a melted DataFrame
    '''
    melted = pd.melt(df, id_vars=['RegionID', 'RegionName', 'City', 'State', 'StateName', 'Metro', 'CountyName', 'SizeRank', 'RegionType'], var_name='date')
    melted['date'] = pd.to_datetime(melted['date'], infer_datetime_format=True)
    melted = melted.dropna(subset=['value'])
    return melted
