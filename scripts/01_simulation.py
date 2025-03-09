import numpy as np
import pandas as pd
import random
from config import STARTING_BALANCE, BASE_BET, WIN_PROBABILITY, MAX_ROUNDS, STOP_LOSS, STOP_WIN, NUMBER_OF_SIMULATIONS

def run_martingale_simulation(starting_balance, base_bet, win_probability, max_rounds, stop_loss, stop_win):
    balance = starting_balance
    bet = base_bet
    rounds = 0
    history = []

    while rounds < max_rounds and balance > stop_loss and balance < stop_win:
        outcome = random.random() < win_probability
        if outcome:
            balance += bet
            bet = base_bet
        else:
            balance -= bet
            bet *= 2
            if bet > balance:  # Prevent betting more than remaining balance
                bet = balance
        rounds += 1
        history.append(balance)

    return {"final_balance": balance, "rounds_played": rounds, "history": history}

def run_multiple_simulations(n):
    results = []
    for _ in range(n):
        res = run_martingale_simulation(STARTING_BALANCE, BASE_BET, WIN_PROBABILITY, MAX_ROUNDS, STOP_LOSS, STOP_WIN)
        results.append(res)
    
    df = pd.DataFrame(results)
    df.to_csv("outputs/simulation_results.csv", index=False)

if __name__ == "__main__":
    run_multiple_simulations(NUMBER_OF_SIMULATIONS)
