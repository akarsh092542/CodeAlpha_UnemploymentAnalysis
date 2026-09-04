# CodeAlpha_UnemploymentAnalysis

An exploratory data analysis project examining unemployment trends across
Indian states, with a focus on the impact of Covid-19, developed as part of
the **CodeAlpha Data Science Internship**.

## 📋 Description
Cleans and analyzes real monthly unemployment data across 27 Indian
states/regions (Jan–Oct 2020), quantifies the Covid-19 lockdown's impact on
unemployment, and visualizes regional and national trends.

## ✨ Features
- Data cleaning (column standardization, date parsing, deduplication)
- Exploratory statistics: national averages, peak periods, top-affected states
- Covid-19 impact analysis: pre-Covid vs lockdown-peak vs post-peak comparison
- Trend visualizations: national trend line, zone-wise trends, top-10 states,
  rural vs urban comparison

## 📊 Dataset
`Unemployment_Rate_upto_11_2020.csv` — real unemployment data for Indian
states, Jan 2020 to Oct 2020, including region, date, unemployment rate,
labour participation rate, and geographic zone.

**Source:** CodeAlpha Data Science Task dataset.

## 🛠 Requirements
```
pandas
numpy
matplotlib
seaborn
```
Install with:
```bash
pip install -r requirements.txt
```

## ▶️ How to Run
Make sure `Unemployment_Rate_upto_11_2020.csv` is in the same folder as the script, then:
```bash
python3 unemployment_analysis.py
```

## 📈 Key Findings
- National average unemployment peaked at **~23.24% in May 2020**
  (vs. ~9.76% pre-Covid) — a jump of nearly 13 percentage points.
- Certain states (e.g. Haryana, Tripura) were affected far more severely
  than the national average.
- Unemployment largely recovered to near pre-Covid levels by late 2020.

Generated visualizations:
- `unemployment_national_trend.png`
- `unemployment_by_zone.png`
- `unemployment_top10_states.png`
- `unemployment_rural_vs_urban.png`

## 🧠 Concepts Used
- pandas (data cleaning, groupby, aggregation)
- Time series analysis
- Exploratory data analysis (EDA)
- Data visualization (seaborn/matplotlib)

## 📜 License
This project is licensed under the MIT License.

## 🎓 Internship
This project was completed as part of the **CodeAlpha Data Science Internship**.
