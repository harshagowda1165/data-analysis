import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("datasets/covid_19_india.csv")

print("Complete Dataset")
print(data)

print("\nFirst 5 Records")
print(data.head())

print("\nLast 5 Records")
print(data.tail())

# Select and rename relevant columns
df = data[['Date', 'State/UnionTerritory', 'Cured', 'Deaths', 'Confirmed']]
df.columns = ['Dt', 'St', 'Cure', 'Death', 'Conf']

print("\nSelected Columns")
print(df.head())

# Snapshot on the latest date in the dataset
latest_date = df['Dt'].max()
today = df[df['Dt'] == latest_date]
print(f"\nCOVID Data on {latest_date}")
print(today)

# Top 10 states by confirmed cases
top10_confirmed = today.sort_values(by='Conf', ascending=False)[:10]
print("\nTop 10 States by Confirmed Cases")
print(top10_confirmed)

plt.figure(figsize=(12, 6))
sns.barplot(x='St', y='Conf', data=top10_confirmed, hue='St', legend=False)
plt.title(f"Top 10 States by Confirmed COVID-19 Cases ({latest_date})")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("output_top10_confirmed.png")
plt.show()

# Top 10 states by deaths
top10_deaths = today.sort_values(by='Death', ascending=False)[:10]
print("\nTop 10 States by Deaths")
print(top10_deaths)

plt.figure(figsize=(12, 6))
sns.barplot(x='St', y='Death', data=top10_deaths, hue='St', legend=False)
plt.title(f"Top 10 States by COVID-19 Deaths ({latest_date})")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("output_top10_deaths.png")
plt.show()

# Case fatality rate (deaths / confirmed) for the top 10 confirmed states
top10_confirmed = top10_confirmed.copy()
top10_confirmed['CFR_%'] = (top10_confirmed['Death'] / top10_confirmed['Conf'] * 100).round(2)
print("\nCase Fatality Rate (%) - Top 10 States by Confirmed Cases")
print(top10_confirmed[['St', 'Conf', 'Death', 'CFR_%']])
