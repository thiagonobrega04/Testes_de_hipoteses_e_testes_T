import numpy as np
from scipy import stats

# Lesson Introduction
# Welcome to our exciting lesson! We shall embark on learning and mastering Hypothesis Testing using Python. It might sound complicated, but it’s like deciding if a toy is worth buying based on its reviews. We'll focus on the T-test, a way to tell if two groups are different.

# Python has useful tools, Scipy and Statsmodels, which help us do these tests quickly and accurately. By the end, you'll understand Hypothesis Testing, know what a T-test is, and be able to do a T-test using Python. So, let's start!

# What is Hypothesis Testing?
# A hypothesis is a guess about a group. For example, "adult males in the U.S. average 180 lbs." In Hypothesis Testing, we try to prove or disprove these guesses using collected data.

# 1. Null Hypothesis (H0): The guess we're challenging. For example, "adult males in the U.S. do not average 180 lbs."

# 2. Alternative Hypothesis (HA): The guess we're trying to prove (e.g., "Adult males in the U.S. average 180 lbs.").

# Think of it like a courtroom trial. The null hypothesis is on trial, and the alternative hypothesis offers the evidence.

# How Does a T-test Work?
# Let's understand the T-test better. It checks if the two groups' mean values are truly different. It's like testing if two pots of coffee are different temperatures due to one being under an AC vent or just by chance.

# There are three main types of T-tests:

# 1. One-sample T-test: "Does this coffee look like it came from a pot that averages 70 degrees?"
# 2. Two-sample T-test: "Are men's and women's average weights different?"
# 3. Paired-sample T-test: "Did people's average stress levels change after using a meditation app for a month?"

# T-test gives us two values: the t-statistic and the p-value. The t-statistic represents the size of the difference relative to the variation in your sample data. Put simply, the bigger the t-statistic, the more difference there is between groups mean values. The p-value is the probability that the results could be random (i.e., happened by chance). If the p-value is less than 0.05, usually, we conclude that the difference is statistically significant and not due to randomness.

# Performing T-tests in Python
# Python has powerful tools, Scipy and Statsmodels, for Hypothesis Testing.

# For example, to do a one-sample T-test in Python, we can use Scipy's ttest_1samp() function.

# Let's begin by assuming that the null hypothesis is that the mean age of users (provided as the ages array) equals 30. Therefore, the alternative hypothesis states that the mean age is not 30. Let’s illustrate how we can test this:

ages = np.array([20, 22, 25, 25, 27, 27, 27, 29, 30, 31, 33])  # mean = 26.9
mean_ages = np.mean(ages)
print(f"Mean Ages: {mean_ages:.2f}")

t_statistic, p_value = stats.ttest_1samp(ages, 30)
print(f"t-statistic:, {t_statistic:.2f}")  # 0.5665
print(f"p-value:, {p_value:.2f}")  # 0.5835

# In this case, we fail to reject the null hypothesis because the p-value is greater than 0.05 (the conventional cutoff). It means that we don't have enough statistical evidence to claim that the mean age of users is different from 30.

# Now let's modify our numpy array to contain a normally distributed sample with a mean that differs from 30:

ages = np.random.normal(loc=33, scale=5, size=90)  # mean = 33
t_statistic, p_value = stats.ttest_1samp(ages, 30)
print("t-statistic:", t_statistic)  # 7.5934
print("p-value:", p_value)  # 0.000

# We might reject the null hypothesis in this case as the p_value is less than 0.05. It suggests strong evidence against the null hypothesis, implying that the average age of users is significantly different from 30.

# Two-Sample T-test
# Imagine you want to test if two teams in your office work the same hours. After collecting data, you can use a two-sample T-test to find out.

# 1. The null hypothesis is that the mean working hours of Team A is equal to the mean working hours of Team B.
# 2. The alternative hypothesis is that the mean working hours of Team A is different from the mean working hours of Team B.
# We will use the stats.ttest_ind function for the two-sample T-test. Here’s an example:

team_A_hours = np.array([8.5, 7.5, 8, 8, 8, 8, 8, 8.5, 9])
team_B_hours = np.array([9, 8, 9, 9, 9, 9, 9, 9, 9.5])
t_statistic, p_value = stats.ttest_ind(team_A_hours, team_B_hours)
print("t-statistic:", t_statistic)  # -4
print("p-value:", p_value)  # 0.00103

# The p-value is less than 0.05, so we can reject the null hypothesis, meaning we have sufficient statistical evidence to say that there's a significant difference between the mean working hours of Teams A and B.