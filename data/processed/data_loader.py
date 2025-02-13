import pandas as pd
import os

# defining file paths

RAW_DATA_PATH="data/raw/ad_click_data.csv"
PROCESSED_DATA_PATH ="data/processed/cleaned_ad_data.csv"

def load_data(file_path):
    """load raw data"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} not found")
    df= pd.read_csv(file_path)
    return df

def preprocess_data(df):
    """clean and preprocess the dataset"""
    #Droping missing values
    df= df.dropna()

    #convert categorical variables
    if 'ad_cattegory' in df.columns:
        df = pd.get_dummies(df, columns=['ad_category'], drop_first=True)

    #Normalizing numerical