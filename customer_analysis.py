import pandas as pd
from itertools import combinations


df = pd.read_csv("calls.csv")
df.head(3)


# Task 1
unique_customers = df['Cust'].unique()
print(unique_customers)

# Task 2
cust_citywise = df.groupby('City')['Cust'].unique().reset_index()
print(cust_citywise)

# Task 3
city_counts = df.groupby('Cust')['City'].nunique()
unique_cities = df['City'].unique()
all_combinations = []
for r in range(len(unique_cities), 1, -1):
    city_combinations = combinations(unique_cities, r)
    all_combinations.extend(city_combinations)
customers_by_combination = {}

for combination in all_combinations:
    combination_len = len(set(combination))
    customers = df[df.groupby('Cust')['City'].transform('nunique') == combination_len]['Cust'].to_list()
    customers_by_combination[combination] = list(set(customers))
print(customers_by_combination)


# Task 4
city_count = df.groupby('Cust')['City'].nunique().reset_index().groupby('City')['Cust'].unique()
print(city_count)
