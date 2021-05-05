import numpy as np
import pandas as pd
np.random.seed(124)

# 1. How likely is it that you roll doubles when rolling two dice?

die_1 = np.random.choice([1, 2, 3, 4, 5, 6], size = 10_000)
die_2 = np.random.choice([1, 2, 3, 4, 5, 6], size = 10_000)
(die_1 == die_2).mean()
#  returns p of 0.164

# 2. If you flip 8 coins, what is the probability of getting exactly 3 heads? What is the probability of getting more than 3 heads?

coin_outcomes = [1, 0]
n_simulations = 100_000
n_trials = 8 
flips = np.random.choice(coin_outcomes, size = (n_simulations,n_trials))
count_heads = flips.sum(axis = 1)

p_exactly_3heads = (count_heads == 3).mean()
p_morethan_3heads = (count_heads > 3).mean()

# returns p exactly 3 heads of 0.21741
# returns p more than 3 heads of 0.63873

# 3. There are approximitely 3 web development cohorts for every 1 data science cohort at Codeup. Assuming that Codeup 
# randomly selects an alumni to put on a billboard, what are the odds that the two billboards I drive past both have data 
# science students on them?

outcomes = [0,1]
n_simulations = n_rows = 10 ** 6
n_cols = 2
ds_billboard = np.random.choice(outcomes, size = (n_simulations, n_cols))

sum_trials = ds_billboard.sum(axis=1)
both_ds = (sum_trials == 2).mean()

#returns p of 0.250422


