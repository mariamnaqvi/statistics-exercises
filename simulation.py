import numpy as np
import pandas as pd

# 1. How likely is it that you roll doubles when rolling two dice?

die_1 = np.random.choice([1, 2, 3, 4, 5, 6], size = 10_000)
die_2 = np.random.choice([1, 2, 3, 4, 5, 6], size = 10_000)
(die_1 == die_2).mean()

# 2. If you flip 8 coins, what is the probability of getting exactly 3 heads? What is the probability of getting more than 3 heads?

coin_outcomes = [1, 0]
n_simulations = 100_000
n_trials = 8 
flips = np.random.choice(coin_outcomes, size = (n_simulations,n_trials))
count_heads = flips.sum(axis = 1)

p_exactly_3heads = (count_heads == 3).mean()
p_morethan_3heads = (count_heads > 3).mean()

print(p_exactly_3heads)
print(p_morethan_3heads)