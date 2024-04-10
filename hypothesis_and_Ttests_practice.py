import numpy as np
from scipy import stats

# Welcome back, Stellar Navigator! It appears as though your company has implemented a new project planning system.

# Now, you're looking to see if it has had any impact on the meeting hours of different teams. The provided code performs a T-test on the meeting hours for the management and developer teams to evaluate this.

# No alterations are necessary. Just hit Run!

# Assuming meeting hours for management and developer team before and after new project planning implementation
management_hours = np.array([3, 2, 3, 3, 3, 2, 3, 3])
developer_hours = np.array([2, 2, 2, 2, 3, 2, 2.5, 2])
print(f"Management hours mean:\n {management_hours.mean():.2f}")
print(f"Developer hours mean:\n {developer_hours.mean():.2f}")

t_statistic, p_value = stats.ttest_ind(management_hours, developer_hours)
print(f"t-statistic:\n {t_statistic:.2f}")
print(f"p-value:\n {p_value:.2f}")

significance_level = 0.05
if p_value < significance_level:
    print("We reject the null hypothesis. There is a significant difference in meeting hours.")
else:
    print("We fail to reject the null hypothesis. There is no significant difference in meeting hours.")

# In this space mission, you'll adjust the input data to see how it affects statistical evidence. Modify the parameters of np.random.normal to create a sample with a mean age significantly higher than 30. This will change the p-value and show if there's a different conclusion in hypothesis testing.

# Modify the input array parameters to have a different mean
ages_new = np.random.normal(loc=70, scale=3, size=1000) 
t_statistic, p_value = stats.ttest_1samp(ages_new, 30)
print(f"t-statistic:\n {t_statistic:.2f}")
print(f"p-value:\n {p_value:.2f}")

significance_level = 0.05
if p_value < significance_level:
    print("We reject the null hypothesis. The sample mean is significantly different from 30.")
else:
    print("We fail to reject the null hypothesis. The sample mean is not significantly different from 30.")

# Nice work, Space Explorer! You're doing a stellar job. Are you prepared for a more challenging task?

# In this workplace efficiency scenario, we have data on the working hours of two teams. Your mission is to test whether their average working hours are significantly different. Your task is simply to write the missing lines of code.

# Good luck!

working_hours_for_devs = np.array([8, 9, 7.5, 9, 8, 9, 8, 10, 8.5])
working_hours_for_sales = np.array([8, 8, 8.5, 7.5, 8, 8, 8, 8.5, 8])
print(f"Developers hours mean:\n {working_hours_for_devs.mean():.2f}")
print(f"Sales hours mean:\n {working_hours_for_sales.mean():.2f}")

# TODO: Implement the two-sample T-test method for the working_hours_for_devs and working_hours_for_sales
t_statistic, p_value = stats.ttest_ind(working_hours_for_devs, working_hours_for_sales)
print(f"t-statistic:\n {t_statistic:.2f}")
print(f"p-value:\n {p_value:.2f}") 

significance_level = 0.05
if p_value < significance_level:
    print("We reject the null hypothesis. There is a significant difference in working hours for developers and sales.")
else:
    print("We fail to reject the null hypothesis. There is no significant difference in working hours for developers and sales.")

# Stellar Navigator, we've studied the T-test for measuring whether a batch of data varies from a known mean. Let's see if you can implement a portion of this in Python. Look out for the missing code marked with TODO and inject your brilliance there!

# Data for efficiency hours of employees working remotely
remote_hours = np.array([7, 8, 7.5, 8, 8, 7, 7.5, 8, 7.5, 8])
print(f"Mean value:\n {remote_hours.mean():.2f}")

# TODO: Calculate the T-statistic and P-value to test if the mean efficiency hours significantly differ from 8 hours
t_statistic, p_value = stats.ttest_1samp(remote_hours, 8)

# TODO: print t-statistics and p-value
print(f"t_statistic:\n {t_statistic:.2f}")
print(f"p_value:\n {p_value:.2f}")

# TODO: print message about rejecting or failing to reject the null hypothesis
significance_level = 0.05
if p_value < significance_level:
    print("We reject the null hypothesis. There is a significant difference in efficiency hours of employees working remotely.")
else:
    print("We fail to reject the null hypothesis. There is no significant difference in efficiency hours of employees working remotely.")