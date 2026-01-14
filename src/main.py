from pathlib import Path
import pandas as pd

data_path = Path('C:\Users\Lenovo\Documents\GitHub\Housing-Prices-Project\data\house_prices.csv')
df = pd.read_csv(data_path)

print(df.head())