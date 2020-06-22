# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data = pd.read_csv(path)

#Code starts here
data.rename(columns={'Total':'Total_Medals'},inplace=True)
print(data.head(10))


# --------------
#Code starts here
a = data['Total_Summer']>data['Total_Winter']
b = data['Total_Summer']==data['Total_Winter']



data['Better_Event'] = np.where(a,'Summer',np.where(b,'Both','Winter'))
#data['Better_Event'] = np.where(b,'Both','nan')
#data['Better_Event'].fillna('Both')
better_event = data['Better_Event'].value_counts().idxmax()
print(better_event)


# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]
top_countries.drop(index=146,axis=0,inplace=True)
def top_ten(x_top_countries,col):
    country_list = []
    country_list = list((x_top_countries.nlargest(10,col)['Country_Name']))
    return country_list
top_10_summer = top_ten(top_countries,'Total_Summer')
print(top_10_summer)
top_10_winter = top_ten(top_countries,'Total_Winter')
print(top_10_winter)
top_10 = top_ten(top_countries,'Total_Medals')
print(top_10)
common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))
print(common)


# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]


# --------------
#Code starts here
summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] / summer_df['Total_Summer']
winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] / winter_df['Total_Winter']
top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']
summer_max_ratio = max(summer_df['Golden_Ratio'])
summer_df['Drop'] = np.where(summer_max_ratio==summer_df['Golden_Ratio'],summer_df['Country_Name'],None)
summer_country_gold = summer_df['Drop'].value_counts().idxmin()
summer_df.drop(['Drop'],inplace=True,axis=1)
winter_max_ratio = max(winter_df['Golden_Ratio'])
winter_df['Drop'] = np.where(winter_max_ratio==winter_df['Golden_Ratio'],winter_df['Country_Name'],None)
winter_country_gold = winter_df['Drop'].value_counts().idxmin()
winter_df.drop(['Drop'],inplace=True,axis=1)
top_max_ratio = max(top_df['Golden_Ratio'])
top_df['Drop'] = np.where(top_max_ratio==top_df['Golden_Ratio'],top_df['Country_Name'],None)
top_country_gold = top_df['Drop'].value_counts().idxmin()
top_df.drop(['Drop'],inplace=True,axis=1)







# --------------
#Code starts here
data_1 = data.drop(index=146,axis=0)
data_1['Total_Points'] = 3*data_1['Gold_Total'] + 2*data_1['Silver_Total'] + data_1['Bronze_Total']
most_points = max(data_1['Total_Points'])
data_1['Drop'] = np.where(most_points==data_1['Total_Points'],data_1['Country_Name'],None)
best_country = data_1['Drop'].value_counts().idxmin()
data_1.drop(['Drop'],inplace=True,axis=1)
print(most_points)
print(best_country)
print(type(best_country))


# --------------
#Code starts here
best = data[data['Country_Name']==best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
print(best)
best.plot.bar(stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


