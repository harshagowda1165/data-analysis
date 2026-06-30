# COVID-19 India Data Analysis Project

This project analyzes the COVID-19 pandemic in India using three datasets: confirmed case counts, statewise testing, and vaccination rollout. It follows the same load -> clean -> filter/aggregate -> visualize pattern used across the project.

## Project Files

1. **`covid_cases_analysis.py`**
   - Loads daily state-wise case data (`covid_19_india.csv`).
   - Filters to the latest date in the dataset and finds the top 10 states by confirmed cases and by deaths.
   - Computes case fatality rate (%) for the top states.
   - Plots: top 10 confirmed cases, top 10 deaths.

2. **`statewise_testing_analysis.py`**
   - Loads statewise testing data (`StatewiseTestingDetails.csv`).
   - Takes each state's latest cumulative testing snapshot, finds the top 10 states by total samples tested.
   - Computes test positivity rate (%) for those states.
   - Plots: top 10 states by samples tested, positivity rate by state.

3. **`vaccination_analysis.py`**
   - Loads statewise vaccination data (`covid_vaccine_statewise.csv`).
   - Takes each state's latest cumulative dose count, finds the top 10 states by total doses administered.
   - Compares first dose vs second dose administered.
   - Plots: top 10 states by total doses, first vs second dose comparison.

## Datasets

CSVs are in the `datasets/` folder:
- `covid_19_india.csv`
- `StatewiseTestingDetails.csv`
- `covid_vaccine_statewise.csv`

(Source: [COVID-19 in India dataset on Kaggle](https://www.kaggle.com/datasets/sudalairajkumar/covid19-in-india))

## Setup and Usage

```bash
python -m venv venv
source venv/bin/activate   # venv\Scripts\activate on Windows
pip install pandas matplotlib seaborn
```

Run any script:
```bash
python covid_cases_analysis.py
python statewise_testing_analysis.py
python vaccination_analysis.py
```

Each script prints intermediate dataframes to the console and saves chart images (`.png`) alongside displaying them.
