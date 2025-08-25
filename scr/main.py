import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Load the dataset
df = pd.read_csv('data/SuperLeague24_25-RegularSeason-PerPlayerAnalysis-Konstantelias.csv')

# Display the first few rows of the dataframe
print(df.head())

print(df.info())

print(df.describe())

# Changed Date type
df['Date'] = pd.to_datetime(df['Date'])
print(df.info())

# Name Cleaning
print(df['Player'])
df['Player']= 'Giannis Konstantelias'
print(df['Player'])

avg_rating = df['Rating'].mean()
total_goals = df['Goals'].sum()
total_tackles = df['Tackles'].sum()
yellow_card_matches = df[df['Yellowcards'] >0].shape[0]

print(f"Average Rating: {avg_rating:.2f}")
print(f"Total Goals: {total_goals}")
print(f"Total Tackles: {total_tackles}")
print(f"Matches with Yellow Cards: {yellow_card_matches}")


df = df.sort_values('Date')

plt.figure(figsize = (10,5))
plt.plot(df['Date'],df['Rating'],marker = 'o',linestyle = '--')
plt.title('Player Rating Over Time')
plt.xlabel('Date')
plt.ylabel('Rating')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


avg_tackles_no_goals = df[df['Goals'] == 0]['Tackles'].mean()
avg_tackles_with_goals = df[df['Goals'] > 0]['Tackles'].mean()


print(f"Average Tackles in Matches with No Goals: {avg_tackles_no_goals:.1f}")
print(f"Average Tackles in Matches with Goals: {avg_tackles_with_goals:.1f}")

# Create  column month

df['Month'] = df['Date'].dt.month_name()

monthly_stats = df.groupby('Month').agg({
    'Rating':'mean',
    'Goals':'sum',
    'Tackles':'sum',
}).reset_index()

# Bar plot for monthly stats

plt.figure(figsize=(10,5))
plt.bar(monthly_stats['Month'],monthly_stats['Rating'],color='green')
plt.title('Average Player Rating by Month')
plt.xlabel('Month')
plt.ylabel('Average Rating')
plt.xticks(monthly_stats['Month'],rotation = 45)
plt.tight_layout()
plt.show()

#Printing Monthly Statistics

print(monthly_stats)







