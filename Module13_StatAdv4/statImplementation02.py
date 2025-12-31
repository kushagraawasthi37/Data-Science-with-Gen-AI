# =========================================
# 🎯 POPULATION vs SAMPLE (FOUNDATION)
# =========================================

import numpy as np
import pandas as pd
import seaborn as sns
import scipy.stats as stats
from statistics import mode

# -----------------------------------------
# 👥 POPULATION
# -----------------------------------------
# Population = poora group jisme se sample nikala jaata hai

population = np.random.randint(1, 100, 10)

# Population ke basic statistics
# Mean -> average
# Median -> middle value
# Mode -> most frequent value
# Std -> spread
# Var -> spread²

# print("Mean of population:", np.mean(population))
# print("Median of population:", np.median(population))
# print("Mode of population:", mode(population))
# print("Std of population:", np.std(population))
# print("Var of population:", np.var(population))

# -----------------------------------------
# 🎯 SAMPLE
# -----------------------------------------
# Sample = population ka chhota subset
# Random sampling (without bias)

sample = np.random.choice(population, 5)

# print("Mean of sample:", np.mean(sample))
# print("Median of sample:", np.median(sample))
# print("Mode of sample:", mode(sample))
# print("Std of sample:", np.std(sample))
# print("Var of sample:", np.var(sample))

# 📌 Interview point:
# Sample statistics population parameters ka estimate hote hain

# =========================================
# 📌 MULTIPLE SAMPLES & SAMPLING DISTRIBUTION
# =========================================

sample1 = np.random.choice(population, 5)
sample2 = np.random.choice(population, 5)
sample3 = np.random.choice(population, 5)
sample4 = np.random.choice(population, 5)
sample5 = np.random.choice(population, 5)

all_sample = [sample1, sample2, sample3, sample4, sample5]
mean_of_sample = []

# Har sample ka mean
# for sample in all_sample:
#     mean_of_sample.append(np.mean(sample))

# print(mean_of_sample)
# print("Mean of sample means:", np.mean(mean_of_sample))

# 📌 Interview line:
# "Mean of sample means ≈ population mean"

# =========================================
# 🔔 CENTRAL LIMIT THEOREM (CLT)
# =========================================

# Binomial population (non-normal)
population = np.random.binomial(10, 0.5, 10000)

# sns.distplot(population)

# CLT ke according:
# Agar sample size sufficiently large ho,
# to sample mean ka distribution NORMAL ho jaata hai

# for i in range(1000):
#     sample = np.random.choice(population, 100)
#     mean_of_sample.append(np.mean(sample))

# sns.distplot(mean_of_sample)

# 📌 Interview definition:
# "Regardless of population distribution,
# sampling distribution of mean tends to be normal"

# =========================================
# 🔔 NORMAL DISTRIBUTION DATA
# =========================================

from numpy.random import randn

population = randn(1000)  # mean≈0, std≈1
# sns.distplot(population)

np.mean(population)
# np.std(population)

# =========================================
# 📐 Z TEST (KNOWN POPULATION STD)
# =========================================

null_mean = 0.03  # H0: population mean = 0.03

from statsmodels.stats.weightstats import ztest

zscore, pvalue = ztest(population, value=null_mean, alternative='larger')

# Decision rule (p-value approach)
if pvalue < 0.05:
    print("Reject null hypothesis")
else:
    print("Accept null hypothesis")

# =========================================
# 📘 REAL LIFE Z-TEST EXAMPLE (CRITICAL VALUE)
# =========================================

# Given:
# Sample mean = 100
# Population mean = 90
# Population std = 16
# Sample size = 50
# Alpha = 0.05

sample_mean = 100
population_mean = 90
population_std = 16
sample_size = 50
alpha = 0.05

# Z-score formula
zscore = (sample_mean - population_mean) / (population_std / np.sqrt(sample_size))
print("Z-score:", zscore)

# Critical value approach
zcritical = stats.norm.ppf(1 - alpha)

if zscore > zcritical:
    print("Reject the null hypothesis")
else:
    print("Fail to reject null hypothesis")

# P-value approach
p_value = 1 - stats.norm.cdf(zscore)

if p_value < alpha:
    print("Reject the null hypothesis")
else:
    print("Fail to reject null hypothesis")

# 📌 Interview point:
# Z-test tab use hota hai jab:
# ✔ Population std known ho
# ✔ Sample size large (n ≥ 30)

# =========================================
# 📐 T-TEST (UNKNOWN POPULATION STD)
# =========================================

# Jab:
# ❌ Population std unknown
# ❌ Sample size small (<30)

# -----------------------------------------
# ONE SAMPLE T-TEST
# -----------------------------------------

population = np.random.randint(10, 50, 50)
sample = np.random.choice(population, 20)

null_value = 25  # H0: mean = 25

stats.ttest_1samp(sample, null_value)

# Rule:
# p-value > 0.05 → fail to reject H0

# -----------------------------------------
# TWO SAMPLE T-TEST (INDEPENDENT)
# -----------------------------------------

virat_kohli_score = np.random.choice(population, 20)

rohit_sharma_score = [
    13, 25, 48, 28, 19, 12, 13, 18, 98, 40,
    18, 23, 34, 33, 45, 58, 46, 27, 50, 49
]

np.mean(rohit_sharma_score), np.mean(virat_kohli_score)

stats.ttest_ind(virat_kohli_score, rohit_sharma_score)

# Use case:
# Two different players / two independent groups

# -----------------------------------------
# PAIRED T-TEST
# -----------------------------------------

# Same entity, different time intervals

rohit_score_first_inning = [31,36,46,24,48,46,47,47,16,35,45,37,24,29,27,42,49,37,47,46]
rohit_score_second_inning = [31,76,46,24,48,23,49,47,37,35,45,37,74,39,27,42,49,37,47,46]

np.mean(rohit_score_first_inning), np.mean(rohit_score_second_inning)

stats.ttest_rel(rohit_score_first_inning, rohit_score_second_inning)

# 📌 Interview line:
# "Paired t-test same subject par lagta hai"

# =========================================
# 📊 CHI-SQUARE TEST (CATEGORICAL DATA)
# =========================================

data = sns.load_dataset("tips")

# Contingency table
data_table = pd.crosstab(data['sex'], data['smoker'])

observed_values = data_table.values

# Chi-square test (library method)
stats_test, p, dof, expected_values = stats.chi2_contingency(observed_values)

# -----------------------------------------
# MANUAL CHI-SQUARE CALCULATION
# -----------------------------------------

# DOF = (rows - 1) * (columns - 1)
dof = 1

from scipy.stats import chi2

# Formula:
# χ² = Σ (Observed - Expected)² / Expected
chisquare_test = sum([(o - e) ** 2 / e for o, e in zip(observed_values, expected_values)])
chisquare_stats = chisquare_test[0] + chisquare_test[1]

chi2_critical = chi2.ppf(1 - alpha, df=dof)

if chisquare_stats >= chi2_critical:
    print("Reject H0 → relationship exists")
else:
    print("Fail to reject H0 → no relationship")

# P-value method
p_value = 1 - chi2.cdf(x=chisquare_stats, df=dof)

if p_value <= alpha:
    print("Reject H0 → relationship exists")
else:
    print("Fail to reject H0 → no relationship")

# -----------------------------------------
# GOODNESS OF FIT CHI-SQUARE
# -----------------------------------------

# Expected vs Observed frequency
expected_data = [8, 5, 6, 8, 5, 7, 6]
observed_data = [7, 4, 7, 9, 4, 8, 6]

chsquare_stats, pvalue = stats.chisquare(observed_data, expected_data)

alpha = 0.05
dof = len(observed_data) - 1
critical_value = stats.chi2.ppf(1 - alpha, dof)

if chsquare_stats > critical_value:
    print("Reject the null hypothesis")
