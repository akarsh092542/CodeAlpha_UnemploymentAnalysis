"""
CodeAlpha - Data Science Internship
Task 2: Unemployment Analysis with Python

Analyze real unemployment rate data across Indian states/regions, explore
the impact of Covid-19, and visualize key trends.

Dataset: Unemployment_Rate_upto_11_2020.csv
Source: CodeAlpha task dataset (India, monthly, by state/region, up to Nov 2020)

Key Concepts Used: pandas, data cleaning, exploratory data analysis,
time series visualization, matplotlib/seaborn
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

DATA_FILE = "Unemployment_Rate_upto_11_2020.csv"


def load_data(path=DATA_FILE):
    """Load the unemployment dataset from CSV."""
    df = pd.read_csv(path)
    return df


def clean_data(df):
    """Clean column names, parse dates, and handle duplicates."""
    print("=" * 50)
    print("DATA CLEANING")
    print("=" * 50)

    # Strip whitespace from column names (dataset has leading spaces, e.g. ' Date')
    df.columns = [c.strip() for c in df.columns]

    # Drop the duplicate 'Region.1' column (this dataset repeats Region as a
    # geographic zone name, e.g. South/North/East/West) - rename it instead
    if "Region.1" in df.columns:
        df = df.rename(columns={"Region.1": "Zone"})

    print(f"Columns: {list(df.columns)}")
    print(f"Initial shape: {df.shape}")
    print(f"Missing values:\n{df.isnull().sum()}")

    df = df.drop_duplicates()

    # Parse dates (format: DD-MM-YYYY)
    df["Date"] = pd.to_datetime(df["Date"].str.strip(), format="%d-%m-%Y")

    # Standardize numeric columns
    df["Estimated Unemployment Rate (%)"] = pd.to_numeric(
        df["Estimated Unemployment Rate (%)"], errors="coerce"
    )
    df["Estimated Labour Participation Rate (%)"] = pd.to_numeric(
        df["Estimated Labour Participation Rate (%)"], errors="coerce"
    )

    df = df.dropna(subset=["Estimated Unemployment Rate (%)"])
    df = df.sort_values(["Region", "Date"]).reset_index(drop=True)

    print(f"Shape after cleaning: {df.shape}\n")
    return df


def explore_data(df):
    """Print summary statistics and key figures."""
    print("=" * 50)
    print("DATA OVERVIEW")
    print("=" * 50)
    print(df.head())
    print(f"\nDate range: {df['Date'].min().date()} to {df['Date'].max().date()}")
    print(f"Number of regions/states: {df['Region'].nunique()}")
    print("\nUnemployment Rate summary statistics:")
    print(df["Estimated Unemployment Rate (%)"].describe())

    national_avg = df.groupby("Date")["Estimated Unemployment Rate (%)"].mean()
    peak_date = national_avg.idxmax()
    peak_value = national_avg.max()
    print(f"\nPeak national average unemployment: {peak_value:.2f}% on {peak_date.strftime('%B %Y')}\n")

    print("Top 5 states by average unemployment rate:")
    print(df.groupby("Region")["Estimated Unemployment Rate (%)"].mean()
          .sort_values(ascending=False).head())
    print()


def analyze_covid_impact(df):
    """Compare average unemployment rate before, during, and after the Covid-19 peak."""
    pre_covid = df[df["Date"] < "2020-04-01"]["Estimated Unemployment Rate (%)"].mean()
    covid_peak = df[(df["Date"] >= "2020-04-01") & (df["Date"] <= "2020-06-01")]["Estimated Unemployment Rate (%)"].mean()
    post_peak = df[df["Date"] > "2020-06-01"]["Estimated Unemployment Rate (%)"].mean()

    print("=" * 50)
    print("COVID-19 IMPACT ANALYSIS")
    print("=" * 50)
    print(f"Average unemployment BEFORE Covid (pre Apr 2020): {pre_covid:.2f}%")
    print(f"Average unemployment DURING Covid peak (Apr-Jun 2020): {covid_peak:.2f}%")
    print(f"Average unemployment AFTER peak (post Jun 2020): {post_peak:.2f}%")
    print(f"Increase during peak vs pre-Covid: {covid_peak - pre_covid:.2f} percentage points\n")


def visualize_trends(df):
    """Create and save visualizations of unemployment trends."""
    sns.set_theme(style="whitegrid")

    # 1. National trend over time
    national_avg = df.groupby("Date")["Estimated Unemployment Rate (%)"].mean().reset_index()
    plt.figure(figsize=(11, 5))
    plt.plot(national_avg["Date"], national_avg["Estimated Unemployment Rate (%)"],
              marker="o", color="crimson")
    plt.axvspan(pd.Timestamp("2020-04-01"), pd.Timestamp("2020-06-01"),
                color="orange", alpha=0.2, label="Covid-19 Peak (Lockdown)")
    plt.title("National Average Unemployment Rate Over Time (India)")
    plt.xlabel("Date")
    plt.ylabel("Unemployment Rate (%)")
    plt.legend()
    plt.tight_layout()
    plt.savefig("unemployment_national_trend.png", dpi=150)
    plt.close()
    print("Saved visualization: unemployment_national_trend.png")

    # 2. Trend by zone/region group
    if "Zone" in df.columns:
        plt.figure(figsize=(11, 6))
        zone_avg = df.groupby(["Date", "Zone"])["Estimated Unemployment Rate (%)"].mean().reset_index()
        for zone in zone_avg["Zone"].unique():
            zone_data = zone_avg[zone_avg["Zone"] == zone]
            plt.plot(zone_data["Date"], zone_data["Estimated Unemployment Rate (%)"], label=zone)
        plt.title("Unemployment Rate Trend by Zone")
        plt.xlabel("Date")
        plt.ylabel("Unemployment Rate (%)")
        plt.legend()
        plt.tight_layout()
        plt.savefig("unemployment_by_zone.png", dpi=150)
        plt.close()
        print("Saved visualization: unemployment_by_zone.png")

    # 3. Top 10 states by average unemployment (bar chart)
    top_states = df.groupby("Region")["Estimated Unemployment Rate (%)"].mean().sort_values(ascending=False).head(10)
    plt.figure(figsize=(9, 5))
    top_states.plot(kind="barh", color="darkred")
    plt.title("Top 10 States by Average Unemployment Rate")
    plt.xlabel("Average Unemployment Rate (%)")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig("unemployment_top10_states.png", dpi=150)
    plt.close()
    print("Saved visualization: unemployment_top10_states.png")

    # 4. Rural vs Urban comparison (if Area column present)
    if "Area" in df.columns:
        plt.figure(figsize=(7, 5))
        sns.boxplot(data=df, x="Area", y="Estimated Unemployment Rate (%)", palette="Set2")
        plt.title("Unemployment Rate: Rural vs Urban")
        plt.tight_layout()
        plt.savefig("unemployment_rural_vs_urban.png", dpi=150)
        plt.close()
        print("Saved visualization: unemployment_rural_vs_urban.png")


def main():
    df = load_data()
    df = clean_data(df)
    explore_data(df)
    analyze_covid_impact(df)
    visualize_trends(df)

    print("\nKey Insight: Unemployment across Indian states spiked sharply during the")
    print("Covid-19 lockdown period (Apr-Jun 2020), with some states affected far more")
    print("severely than others. This kind of regional breakdown can help target relief")
    print("and reskilling programs where they're needed most.")


if __name__ == "__main__":
    main()
