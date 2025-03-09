# statistical-simulation-martingale-betting-strategy

## Project Overview
This project simulates and analyzes the **Martingale Betting Strategy**, a well-known stochastic process in gambling and finance. The strategy is based on **doubling down on losses** to recover previous bets and make a net profit equal to the initial bet. However, due to practical limitations such as finite bankrolls and betting limits, it often leads to **eventual ruin**.



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