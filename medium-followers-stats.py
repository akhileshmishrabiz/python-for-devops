import pandas as pd
import matplotlib.pyplot as plt

downloaded_csv_from_medium = "akhilesh-mishra-subscriber-stats.csv"
# Load data from CSV file
df = pd.read_csv(downloaded_csv_from_medium)

# Convert period_start to datetime for better plotting
df['period_start'] = pd.to_datetime(df['period_start'])

# Sort the data by period_start
df = df.sort_values('period_start')

# Create the plot
plt.figure(figsize=(10,6))

# Plot Total Followers
plt.plot(df['period_start'], df['followers_total'], marker='o', linestyle='-', color='g', label='Total Followers')

# Plot Followers Gained
plt.plot(df['period_start'], df['followers_gained'], marker='o', linestyle='--', color='b', label='Followers Gained')

# Add titles and labels
plt.title('Total Followers and Followers Gained Over Time')
plt.xlabel('Date')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.grid(True)

# Show the legend
plt.legend()

# Display the plot
plt.tight_layout()
plt.show()
