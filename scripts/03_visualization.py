import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("outputs/simulation_results.csv")

def plot_balance_distribution(df):
    plt.figure(figsize=(8, 6))
    sns.histplot(df["final_balance"], bins=30, kde=True)
    plt.title("Final Balance Distribution")
    plt.xlabel("Balance")
    plt.ylabel("Frequency")
    plt.savefig("outputs/visualizations/balance_distribution.png")

def plot_trajectory_examples(df):
    plt.figure(figsize=(8, 6))
    for history in df["history"].sample(5):
        plt.plot(eval(history))  # Convert string to list
    plt.title("Example Betting Trajectories")
    plt.xlabel("Rounds")
    plt.ylabel("Balance")
    plt.savefig("outputs/visualizations/trajectory_examples.png")

if __name__ == "__main__":
    plot_balance_distribution(df)
    plot_trajectory_examples(df)
