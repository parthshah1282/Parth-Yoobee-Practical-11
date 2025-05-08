import pandas as pd
file_name = "1026__annual__Total_Cooling_Degree_Days_for_18C__days.csv"
df = pd.read_csv(file_name)
print("\nFirst 5 rows of the data:")
print(df.head())
print("\nDataset info:")
print(df.info())
print("\nStatistical summary:")
print(df.describe())
