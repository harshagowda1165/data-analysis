import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("datasets/StatewiseTestingDetails.csv")

print("Complete Dataset")
print(data)

print("\nFirst 5 Records")
print(data.head())

print("\nMissing values per column")
print(data.isna().sum())

# Drop rows where Positive count is missing (can't analyze positivity without it)
df = data.dropna(subset=['Positive']).copy()
df['Positive'] = df['Positive'].astype(float)

# Get the latest cumulative TotalSamples and Positive count per state
latest_per_state = df.sort_values('Date').groupby('State').tail(1)

# Total samples tested - top 10 states
top10_tested = latest_per_state.sort_values(by='TotalSamples', ascending=False)[:10]
print("\nTop 10 States by Total Samples Tested")
print(top10_tested[['State', 'Date', 'TotalSamples', 'Positive']])

plt.figure(figsize=(12, 6))
sns.barplot(x='State', y='TotalSamples', data=top10_tested, hue='State', legend=False)
plt.title("Top 10 States by Total COVID-19 Samples Tested")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("output_top10_tested.png")
plt.show()

# Positivity rate (Positive / TotalSamples) for the top 10 tested states
top10_tested = top10_tested.copy()
top10_tested['PositivityRate_%'] = (top10_tested['Positive'] / top10_tested['TotalSamples'] * 100).round(2)
print("\nPositivity Rate (%) - Top 10 Tested States")
print(top10_tested[['State', 'TotalSamples', 'Positive', 'PositivityRate_%']])

plt.figure(figsize=(12, 6))
sns.barplot(x='State', y='PositivityRate_%', data=top10_tested, hue='State', legend=False)
plt.title("COVID-19 Test Positivity Rate (%) - Top 10 Tested States")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("output_positivity_rate.png")
plt.show()
