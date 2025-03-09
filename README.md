# statistical-simulation-martingale-betting-strategy

## Project Overview
This project simulates and analyzes the **Martingale Betting Strategy**, a well-known stochastic process in gambling and finance. The strategy is based on doubling down on losses to recover previous bets and make a net profit equal to the initial bet. However, due to practical limitations such as finite bankrolls and betting limits, it often leads to eventual ruin.

### **Mathematical Foundation**
#### **Martingale Process Definition**
A Martingale process is a stochastic sequence $\( X_n \)$ where the expectation of the next value given past values remains unchanged:

$$E[X_{n+1} | X_0, X_1, ..., X_n] = X_n$$

For a discrete betting strategy, let:
- $\( B_n \)$ be the bet size at round $\( n \)$.
- $\( W_n \)$ be a Bernoulli random variable for win/loss outcome.
- $\( X_n \)$ be the player's balance after round $\( n \)$.

The recurrence relation follows:

$$X_{n+1} = X_n + B_n W_n - B_n (1 - W_n)$$

where:
- $\( W_n = 1 \)$ with probability $\( p \)$ (win)
- $\( W_n = 0 \)$ with probability $\( 1 - p \)$ (loss)
- $\( B_{n+1} = 2 B_n \)$ if loss, otherwise reset to initial bet.

#### **Expected Value and Ruin Probability**
##### **Expected Final Balance**
Define the **expected balance** after $\( N \)$ rounds:

$$E[X_N] = X_0 + N (2p - 1) B_0$$

If $\( p = 0.5 \)$, then $\( E[X_N] = X_0 \)$, implying an expectation-preserving game.

##### **Ruin Probability**
For an initial balance $\( X_0 \)$ and maximum betting limit $\( L \)$, the probability of bankruptcy $\( P_r \)$ follows:

$$P_r = 1 - \left( \frac{1 - (2p)^{\log_2 \frac{L}{B_0}}}{1 - (2p)^{\log_2 \frac{X_0}{B_0}}} \right)$$

For large $\( L \)$, the probability of eventual ruin approaches 1.

##### **Variance Growth**
The variance of the final balance grows as:

$$\sigma^2(X_N) = N B_0^2 (4p(1-p))$$

which increases exponentially if losses persist.

---

## Folder Structure
```
project-root/
├── scripts/
│   ├── 01_simulation.py       # Runs the simulation
│   ├── 02_analysis.py         # Statistical analysis of results
│   ├── 03_visualization.py    # Generates visualizations
│   ├── config.py              # Simulation settings
│   ├── utils.py               # Helper functions
├── outputs/                   # Stores results
│   ├── simulation_results.csv
│   ├── analysis_summary.txt
│   ├── visualizations/
│       ├── balance_distribution.png
│       ├── trajectory_examples.png
├── README.md
├── requirements.txt
```

---

## Usage

### **1. Setup the Project:**
Clone the repository.
Ensure you have Python installed.
Install required dependencies using the requirements.txt file.
```sh
pip install -r requirements.txt
```

### **2. Run the Simulation**
To simulate the Martingale betting strategy:
```sh
python scripts/01_simulation.py
```
This will generate `simulation_results.csv` in the `outputs/` folder.

### **3. Analyze the Results**
To compute statistical summaries:
```sh
python scripts/02_analysis.py
```
This will generate `analysis_summary.txt` with statistical insights.

### **4. Generate Visualizations**
To visualize betting trends and probability distributions:
```sh
python scripts/03_visualization.py
```
Plots will be saved in `outputs/visualizations/`.

---

## Requirements
- Python 3.x
- Required packages (installed via `requirements.txt`):
  - numpy
  - pandas
  - scipy
  - matplotlib
  - seaborn