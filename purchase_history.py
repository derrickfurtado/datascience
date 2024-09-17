import numpy as np
import pandas as pd

purchase_data = pd.read_csv('empirical_data/amazonhistory_df.csv')

print(purchase_data.columns)

# print(purchase_data)

purchase_year = purchase_data["Order Date"]

# print(purchase_year)

purchase_year_2019 = purchase_data.loc[purchase_data["Order Date"].str[:4] == '2019', :]
purchase_year_2020 = purchase_data.loc[purchase_data["Order Date"].str[:4] == '2020', :]
purchase_year_2021 = purchase_data.loc[purchase_data["Order Date"].str[:4] == '2021', :]
purchase_year_2022 = purchase_data.loc[purchase_data["Order Date"].str[:4] == '2022', :]
purchase_year_2023 = purchase_data.loc[purchase_data["Order Date"].str[:4] == '2023', :]


sorted_2023 = purchase_year_2023.sort_values('Unit Price', ascending=False)

top_5_spend_2023 = sorted_2023.iloc[:5]
