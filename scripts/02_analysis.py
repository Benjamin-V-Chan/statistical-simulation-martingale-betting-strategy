import pandas as pd
import numpy as np
from scipy.stats import shapiro

df = pd.read_csv("outputs/simulation_results.csv")

def calculate_statistics(df):
    return {
        "mean_balance": np.mean(df["final_balance"]),
        "median_balance": np.median(df["final_balance"]),
        "std_dev": np.std(df["final_balance"]),
        "min_balance": np.min(df["final_balance"]),
        "max_balance": np.max(df["final_balance"]),
        "win_rate": np.mean(df["final_balance"] > STARTING_BALANCE)
    }

def hypothesis_testing(df):
    stat, p = shapiro(df["final_balance"])
    return "Normal distribution" if p > 0.05 else "Not normal distribution"

def analyze_ruin_probability(df):
    return np.mean(df["final_balance"] <= 0)

if __name__ == "__main__":
    stats = calculate_statistics(df)
    ruin_prob = analyze_ruin_probability(df)
    norm_test = hypothesis_testing(df)
    
    with open("outputs/analysis_summary.txt", "w") as f:
        f.write(str(stats) + "\n")
        f.write(f"Ruin Probability: {ruin_prob}\n")
        f.write(f"Normality Test: {norm_test}\n")
