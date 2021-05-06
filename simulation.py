import numpy as np
import pandas as pd
np.random.seed(124)

# 1. How likely is it that you roll doubles when rolling two dice?

die_1 = np.random.choice([1, 2, 3, 4, 5, 6], size = 10_000)
die_2 = np.random.choice([1, 2, 3, 4, 5, 6], size = 10_000)
(die_1 == die_2).mean()
#  returns p of 0.164

# or
n_trials = nrows = 10_000
n_dice = ncols= 2

# possible outcomes for each roll
rolls = np.random.choice([1,2,3,4,5,6], n_trials * n_dice).reshape(nrows, ncols)
# assign to a df and use lambda to check for doubles 
df = pd.DataFrame(rolls).apply(lambda x : x[0] == x[1] in x.values, axis=1)
# gives the probability of rolling doubles >> 0.163
df.mean()

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

# 4. Codeup students buy, on average, 3 poptart packages (+- 1.5) a day from the snack vending machine. 
# If on monday the machine is restocked with 17 poptart packages, how likely is it that I will be able to buy some poptarts on 
# Friday afternoon?
mu, sigma = 3, 1.5 #mean and std deviation
 
consumed = np.random.normal(3, 1.5, size=(10_000, 5))
pops_bought = consumed.sum(axis =1)
poptarts_on_fri = 17 - pops_bought
(poptarts_on_fri >= 1).mean()
# returns p of 0.6204

# 5. Compare Heights
# Men have an average height of 178 cm and standard deviation of 8cm.
# Women have a mean of 170, sd = 6cm.
# If a man and woman are chosen at random, P(woman taller than man)?

# heights of men chosen at random
mu, sigma = 178, 8
men = np.random.normal(mu, sigma, size=(10_000, 1))

# heights of women chosent at random 
mu, sigma = 170, 6
women = np.random.normal(mu, sigma, size=(10_000, 1))

prob_woman_taller = (women > men).mean()
# returns p of 0.2131

# 6. When installing anaconda on a student's computer, there's a 1 in 250 chance that the download is corrupted and the installation fails. 
# What are the odds that after having 50 students download anaconda, no one has an installation issue? 
p_fail = 0.004
p_success = 0.996
n_cols = 50
n_rows = 10_000
trials = np.random.random((n_rows, n_cols))
successful_install = trials < p_success
(successful_install.sum(axis=1)== 50).mean()
# returns p of 0.8168

# What are the odds that after having 100 students download anaconda, no one has an installation issue?
p_fail = 0.004
p_success = 0.996
n_cols = 100
n_rows = 10_000
trials = np.random.random((n_rows, n_cols))
successful_install = trials < p_success
(successful_install.sum(axis=1)== 100).mean()
# returns p of 0.6707

# What is the probability that we observe an installation issue within the first 150 students that download anaconda?
p_fail = 0.004
p_success = 0.996
n_cols = 150
n_rows = 10_000
trials = np.random.random((n_rows, n_cols))
failed_install = trials < p_fail
(failed_install.sum(axis=1) > 0).mean()
# returns p of 0.4517

# How likely is it that 450 students all download anaconda without an issue?
p_fail = 0.004
p_success = 0.996
n_cols = 450
n_rows = 10_000
trials = np.random.random((n_rows, n_cols))
success_install = trials < p_success
(success_install.sum(axis=1) == 450).mean()
#  returns p  of 0.1657

# 7. There's a 70% chance on any given day that there will be at least one food truck at Travis Park. 
# However, you haven't seen a food truck there in 3 days. How unlikely is this?
n_cols = 3
n_rows = 10 ** 6
outcomes = [0,1]
p_truck = 0.7
p_notruck = 0.3
data = np.random.choice(outcomes, n_rows * n_cols, p = [p_notruck,p_truck]).reshape(n_rows, n_cols)
(data.sum(axis = 1)==0).mean()
# returns p of 0.027402

#  or with df
(pd.DataFrame(data).apply(lambda row: 1 not in row.values, axis =1)).mean()
# returns p of 0.027402

# How likely is it that a food truck will show up sometime this week?
n_cols = 7
n_rows = 10 ** 6
outcomes = [0,1]
p_truck = 0.7
p_notruck = 0.3
data = np.random.choice(outcomes, n_rows * n_cols, p = [p_notruck, p_truck]).reshape(n_rows, n_cols)
(data.sum(axis = 1)>0).mean()
# returns p of 0.972958

# 8. If 23 people are in the same room, what are the odds that two of them share a birthday?  40?
n_cols = 23
n_rows = 10 ** 5
outcomes = [0,1]
prob_one_bday = 365/365
prob_diff_bday = 364/365
prob_2ppl_diff_bdays = prob_one_bday * prob_diff_bday
prob_2ppl_same_bday = 1 - prob_2ppl_diff_bdays
same_bday = np.random.choice(outcomes, size = (n_cols,n_rows), p = [prob_2ppl_diff_bdays, prob_2ppl_same_bday]).reshape(n_rows, n_cols)
(same_bday.sum(axis=1)>0).mean()
#  returns p of 0.0605

# What if it's 20 people?
n_cols = 20
n_rows = 10 ** 5
outcomes = [0,1]
prob_one_bday = 365/365
prob_diff_bday = 364/365
prob_2ppl_diff_bdays = prob_one_bday * prob_diff_bday
prob_2ppl_same_bday = 1 - prob_2ppl_diff_bdays
same_bday = np.random.choice(outcomes, size = (n_cols,n_rows), p = [prob_2ppl_diff_bdays, prob_2ppl_same_bday]).reshape(n_rows, n_cols)
(same_bday.sum(axis=1)>0).mean()
# returns p of 0.0543

# What if it's 40 people?
n_cols = 40
n_rows = 10 ** 5
outcomes = [0,1]
prob_one_bday = 365/365
prob_diff_bday = 364/365
prob_2ppl_diff_bdays = prob_one_bday * prob_diff_bday
prob_2ppl_same_bday = 1 - prob_2ppl_diff_bdays
same_bday = np.random.choice(outcomes, size = (n_cols,n_rows), p = [prob_2ppl_diff_bdays, prob_2ppl_same_bday]).reshape(n_rows, n_cols)
(same_bday.sum(axis=1)>0).mean()
#  returns p of 0.10248