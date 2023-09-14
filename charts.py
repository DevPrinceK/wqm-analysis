import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# read data
df = pd.read_csv('cleaned_calcium.csv')
# df = pd.read_csv('cleaned_ph.csv')
# df = pd.read_csv('cleaned_oxidation.csv')
# df = pd.read_csv('cleaned_fluoride.csv')

# plot the data
# sns.set_style("whitegrid")
# plt.figure(figsize=(8, 6))
# sns.kdeplot(df['Value'], fill=True, color='blue')
# plt.xlabel('Calcium Value')
# plt.ylabel('Density')
# plt.title('Density Plot of Calcium Values')
# plt.show()

# # plot time series data
# plt.figure(figsize=(20, 8))
# plt.plot(df['Reading Date'], df['Value'], color='blue')
# plt.xlabel('Reading Date')
# plt.ylabel('Calcium Value')
# plt.title('Time Series Plot of Calcium Values')
# plt.xticks(rotation=45)
# plt.show()

# plot time series data
plt.figure(figsize=(20, 8))
plt.plot(range(0, 100), df.iloc[0:100]['Value'], color='blue')
plt.xlabel('Reading Date')
plt.ylabel('OXIDATION Value')
plt.title('Time Series Plot of OXIDATION Values')
plt.xticks(rotation=45)
plt.show()