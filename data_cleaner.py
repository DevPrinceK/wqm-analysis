import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# read data
df = pd.read_excel('data/calcium.xlsx')
print("Dataframe")
print(df.head())
print(df.shape)

min_value = 0
max_value = 100

# extract records with calcium values between min_value and max_value
good_records = df[(df['Value'] >= min_value) & (df['Value'] <= max_value)]
unique_values = sorted(list(good_records['Value'].unique()))

mean_of_good_records = good_records['Value'].mean()
mode_of_good_records = good_records['Value'].mode()

# # extract records with calcium values outside min_value and max_value
bad_records = df[(df['Value'] < min_value) | (df['Value'] > max_value)]

# replace all the Values in bad_records with a random variable between the mean of good_records and mode of good_records
bad_records['Value'] = np.random.uniform(mode_of_good_records, mean_of_good_records, size=len(bad_records))
print("Bad records:")
# print(bad_records.head())
# print(bad_records.tail())
print(bad_records.shape)

# create a new dataframe with the good records and the updated bad records
new_df = pd.concat([good_records, bad_records])
# sort the new df by the 'Date' and 'Time' columns
new_df = new_df.sort_values(by=['Reading Date', 'Reading Time'])
print("New Dataframe:")
# print(new_df.head())
# print(new_df.tail())
print(new_df.shape)

# Group the existing DataFrame by 'Reading Date' and 'Probe Name', and calculate the mean value
grouped_df = new_df.groupby(['Reading Date', 'Probe Name']).agg({'Value': 'mean'}).reset_index()

# Create a new DataFrame with the desired columns
daily_grouped_df = pd.DataFrame({
    'Reading Date': grouped_df['Reading Date'],
    'Value': grouped_df['Value'],
    'Probe Name': grouped_df['Probe Name']
})

print("Grouped Dataframe: ", daily_grouped_df.head())


# density plot of the unique values
# sns.set_style("whitegrid")
# plt.figure(figsize=(8, 6))
# sns.kdeplot(new_df['Value'], fill=True, color='blue')
# plt.xlabel('Calcium Value')
# plt.ylabel('Density')
# plt.title('Density Plot of Calcium Values')
# plt.show()

# histogram of the unique values
# plt.figure(figsize=(8, 6))
# plt.hist(new_df['Value'], bins=20, color='blue')
# plt.xlabel('Calcium Value')
# plt.ylabel('Frequency')
# plt.title('Histogram of Calcium Values')
# plt.show()

# # boxplot of the unique values
# plt.figure(figsize=(8, 6))
# sns.boxplot(new_df['Value'], color='blue')
# plt.xlabel('Calcium Value')
# plt.title('Boxplot of Calcium Values')
# plt.show()

# time series plot of the new dataframe
# plt.figure(figsize=(20, 8))
# plt.plot(new_df['Reading Date'], new_df['Value'], color='blue')
# plt.xlabel('Reading Date')
# plt.ylabel('Calcium Value')
# plt.title('Time Series Plot of Calcium Values')
# plt.xticks(rotation=45)
# plt.show()

# time series plot of the new dataframe
# Specify the target date
# target_date = '2018-12-16'

# # Filter the dataframe for the target date
# target_df = new_df[new_df['Reading Date'] == target_date]

# # Plot the reading time against calcium values for the target date
# plt.figure(figsize=(144, 8))
# plt.plot(target_df['Reading Time'], target_df['Value'], color='blue')
# plt.xlabel('Reading Time')
# plt.ylabel('Calcium Value')
# plt.title('Time Series Plot of Calcium Values for ' + target_date)
# plt.xticks(rotation=45)
# plt.show()

# for item in unique_values:
#     print(item)
# print('Unique values: ', unique_values)
# sorted_values = np.sort(unique_values)
# print('Sorted values: ', sorted_values)
# mean_of_good_records = good_records['Value'].mean()
# mode_of_good_records = good_records['Value'].mode()
# median_of_good_records = good_records['Value'].median()
# minimum_of_good_records = good_records['Value'].min()
# maximum_of_good_records = good_records['Value'].max()
# print('Mean of good records: ', mean_of_good_records)
# print('Mode of good records: ', mode_of_good_records)
# print('Median of good records: ', median_of_good_records)
# print('Minimum of good records: ', minimum_of_good_records)
# print('Maximum of good records: ', maximum_of_good_records)

# # extract records with calcium values outside min_value and max_value
# bad_records = df[(df['Value'] < min_value) | (df['Value'] > max_value)]
