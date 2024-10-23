import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)


# Question 1
df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])
weekdays_df = df[df['hour_beginning'].dt.weekday < 5]

weekdays_df['day_of_week'] = weekdays_df['hour_beginning'].dt.day_name()
pedestrian_counts_by_day = weekdays_df.groupby('day_of_week')['Pedestrians'].sum()

day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
pedestrian_counts_by_day = pedestrian_counts_by_day.reindex(day_order)

plt.figure(figsize=(10, 6))
plt.plot(pedestrian_counts_by_day.index, pedestrian_counts_by_day.values, marker='o')
plt.title('Pedestrian Counts for Each Weekday')
plt.xlabel('Day of the Week')
plt.ylabel('Pedestrian Count')
plt.grid(True)
plt.show()


# Question 2
import seaborn as sns

brooklyn_df = df[(df['location'] == 'Brooklyn Bridge') & (df['hour_beginning'].dt.year == 2019)]
brooklyn_df_encoded = pd.get_dummies(brooklyn_df, columns=['Weather_Summary'], drop_first=True)

correlation_matrix = brooklyn_df_encoded.corr()
pedestrian_correlation = correlation_matrix['Pedestrian_Count'].filter(like='Weather_Summary')

plt.figure(figsize=(12, 8))
sns.heatmap(pedestrian_correlation.to_frame(), annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation between Weather Conditions and Pedestrian Counts at Brooklyn Bridge, 2019')
plt.show()


# Question 3
def categorize_time_of_day(hour):
    if 6 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 18:
        return 'Afternoon'
    elif 18 <= hour < 24:
        return 'Evening'
    else:
        return 'Night'

df['time_of_day'] = df['hour_beginning'].apply(categorize_time_of_day)

time_of_day_activity = df.groupby('time_of_day')['Pedestrians'].sum()
time_of_day_activity = time_of_day_activity.reindex(['Morning', 'Afternoon', 'Evening', 'Night'])

print("Pedestrian Activity by Time of Day:")
for time, count in time_of_day_activity.items():
    print(f"{time}: {count} pedestrians")