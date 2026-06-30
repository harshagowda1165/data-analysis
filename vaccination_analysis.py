import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("datasets/covid_vaccine_statewise.csv")

print("Complete Dataset")
print(data)

print("\nFirst 5 Records")
print(data.head())

# Select relevant columns and rename for convenience
df = data[['Updated On', 'State', 'Total Doses Administered',
           'First Dose Administered', 'Second Dose Administered']].copy()
df.columns = ['Date', 'State', 'TotalDoses', 'FirstDose', 'SecondDose']

# Exclude the 'India' aggregate row so we only compare states
df = df[df['State'] != 'India']

# Convert date and get the latest cumulative figures per state
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y', errors='coerce')
latest_per_state = df.sort_values('Date').groupby('State').tail(1)

# Top 10 states by total doses administered
top10_doses = latest_per_state.sort_values(by='TotalDoses', ascending=False)[:10]
print("\nTop 10 States by Total Doses Administered")
print(top10_doses)

plt.figure(figsize=(12, 6))
sns.barplot(x='State', y='TotalDoses', data=top10_doses, hue='State', legend=False)
plt.title("Top 10 States by Total COVID-19 Vaccine Doses Administered")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("output_top10_doses.png")
plt.show()

# Compare first dose vs second dose for the top 10 states
top10_melted = top10_doses.melt(
    id_vars='State',
    value_vars=['FirstDose', 'SecondDose'],
    var_name='DoseType',
    value_name='Count'
)

plt.figure(figsize=(12, 6))
sns.barplot(x='State', y='Count', hue='DoseType', data=top10_melted)
plt.title("First vs Second Dose Administered - Top 10 States")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("output_dose_comparison.png")
plt.show()
