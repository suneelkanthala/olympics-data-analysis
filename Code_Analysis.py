#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file is stored in the variable path
data = pd.read_csv(path)
#Code starts here

# Data Loading 
data = data.rename(columns={"Total": "Total_Medals"})
#print(data.head(10))

# Summer or Winter
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'], 'Summer', 'Winter')
#print(data.head(10))

# Top 10
def top_ten(df, col):
    country_list = []
    top_t = df.nlargest(10, col)
    country_list = list(top_t['Country_Name'])
    return country_list


top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']].copy()
#print(top_countries.tail(1))
#top_countries.drop(top_countries.iloc[-1])
top_countries.drop(top_countries.tail(1).index, inplace = True)
#print(top_countries.tail(1))
top_10_summer = top_ten(top_countries, 'Total_Winter')
top_10_winter = top_ten(top_countries, 'Total_Summer')
top_10 = top_ten(top_countries, 'Total_Medals')
common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))
print(common)

# Plotting top 10
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

# Top Performing Countries
ax = summer_df.plot.bar(x='Country_Name', y='Total_Summer', rot=0, figsize=(20,10))
ax = winter_df.plot.bar(x='Country_Name', y='Total_Winter', rot=0, figsize=(20,10))
ax = top_df.plot.bar(x='Country_Name', y='Total_Medals', rot=0, figsize=(20,10))


# Best in the world 
summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] / summer_df['Total_Summer']
summer_max_ratio = max(summer_df['Golden_Ratio'])
summer_country_gold = summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = max(winter_df['Golden_Ratio'])
winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']

top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio = max(top_df['Golden_Ratio'])
top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']

data_1 = data[:-1]
data_1['Total_Points'] = data_1['Gold_Total'] * 3 + data_1['Silver_Total'] * 2 + data_1['Bronze_Total']
most_pints = max(data_1['Total_Points'])
best_country = data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']

print(most_pints, best_country)

# Plotting the best
best=data[data['Country_Name']==best_country]
best=best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked=True)
plt.xticks(rotation=45)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.show()

