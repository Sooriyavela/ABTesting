# %%
from scipy.stats import shapiro, levene, ttest_ind, mannwhitneyu
from scipy.stats import chi2_contingency
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# %%
df_ab = pd.read_csv("/Users/sooriya/Documents/marketing_AB.csv")
# %%
df_ab.shape
# %%
df_ab.info()
# %%
df_ab.isnull().sum()
# %%
df_ab.head()
# %%
# checking for any duplicate rows if exists
df_ab.duplicated(subset=['user id']).sum()
# %%
# dropping both
df_ab.drop(['Unnamed: 0', 'user id'], axis=1, inplace=True)
# %%
df_ab.head()
# %%
# check if the categorical columns have the appropriate number of levels
df = df_ab.drop(columns=['total ads'], axis=1)
# %%
df.head()
# %%
for i in df.columns:
    print(i.upper(), ":", df[i].unique())

# %%
# Univariate Analysis


def plot(variable):
    plt.figure(figsize=(12, 11))
    # count plot
    plt.subplot(1, 2, 1)
    sns.countplot(x=variable, data=df)
    plt.title(f'Count plot - {variable}')
    # pie chart
    plt.subplot(1, 2, 2)
    counts = df[variable].value_counts()
    plt.pie(counts, labels=counts.index, autopct='%0.2f%%')
    plt.title(f'Pie Chart - {variable}')
    plt.tight_layout()
    plt.show()
    return


variable = 'test group'
plot(variable)
# %%
variable = 'converted'
plot(variable)
# %%
variable = 'most ads day'
plot(variable)
# %%
variable = 'most ads hour'
plot(variable)
# %%
variable = 'total ads'
plt.figure(figsize=(6, 4))
# Histogram plot
plt.subplot(1, 2, 1)
sns.histplot(x=variable, data=df_ab)
plt.title(f'Histogram - {variable}')
# Box Plot
plt.subplot(1, 2, 2)
sns.boxplot(y=variable, data=df_ab)
plt.title(f'Boxplot - {variable}')
plt.tight_layout()
plt.show()
# %%
df_ab['total ads'].describe()
# %%
# Filtering the data for a value close to 75th percentile for a better visualization
variable = 'total ads'
plt.figure(figsize=(6, 4))
# Histogram plot
plt.subplot(1, 2, 1)
sns.histplot(x=variable, data=df_ab[df_ab['total ads'] < 50])
plt.title(f'Histogram - {variable}')
# Box Plot
plt.subplot(1, 2, 2)
sns.boxplot(y=variable, data=df_ab[df_ab['total ads'] < 50])
plt.title(f'Boxplot - {variable}')
plt.tight_layout()
plt.show()
# %%
# Bivariate Analysis
crosstab_output = pd.crosstab(
    df_ab['test group'], df_ab['converted'], normalize='index')
crosstab_output
# %%
crosstab_output.plot.bar(stacked=True)
# %%
crosstab_output = pd.crosstab(
    df_ab['most ads day'], df_ab['converted'], normalize='index')
print(crosstab_output.sort_values(by=True, ascending=False))
crosstab_output.sort_values(by=True, ascending=False).plot.bar(stacked=True)
# %%
crosstab_output = pd.crosstab(
    df_ab['most ads hour'], df_ab['converted'], normalize='index')
print(crosstab_output.sort_values(by=True, ascending=False))
crosstab_output.sort_values(by=True, ascending=False).plot.bar(stacked=True)
# %%
sns.boxplot(data=df_ab, x='converted', y='total ads')
# %%
sns.boxplot(data=df_ab[df_ab['total ads'] < 50], x='converted', y='total ads')

# %%
# Statistical Analysis
alpha = 0.05
for variable in df.columns:
    if variable != 'converted':
        # create a contigency table(cross-tabulation)
        Contigency_table = pd.crosstab(df[variable], df['converted'])
        # perform chi square test
        chi2, p, _, _ = chi2_contingency(Contigency_table)
        print(f"chi square value for {variable} vs converted is : {chi2}")
        print(f"The p-value is {p}")
        # check for significance
        if p < alpha:
            print(
                f"The differenece in conversion rate across the {variable} is statistically significant.")
        else:
            print(
                f"There is no significant difference in onversion rates across {variable}.")
# %%
# check assumptions
# Normality Assumption
shapiro_sta_true, shapiro_pvalue_true = shapiro(
    df_ab[df_ab['converted'] == True]['total ads'])
shapiro_sta_false, shapiro_pvalue_false = shapiro(
    df_ab[df_ab['converted'] == True]['total ads'])

print(f"shapiro-Wilk Test for normality : p_value = {shapiro_pvalue_true}")
print(f"shapiro-Wilk Test for normality : p_value = {shapiro_pvalue_false}")
# %%
# Equality of variances
levene_stat, levene_p_value, = levene(
    df_ab[df_ab['converted']]['total ads'], df_ab[~df_ab['converted']]['total ads'])
print(f"Levene's test for equality of variances:p-value= {levene_p_value}")
# %%
# Step 2: Perform a suitable test
alpha = 0.05
if shapiro_pvalue_true > alpha and shapiro_pvalue_false > alpha and levene_p_value > alpha:
    t_stat, t_p_value = ttest_ind(
        df_ab[df_ab['converted']]['total ads'], df_ab[~df_ab['converted']]['total ads'])
    print(f"Independent wo-sample t-test:p-Value = {t_p_value}")
else:
    u_stat, u_pvalue = mannwhitneyu(
        df_ab[df_ab['converted']]['total ads'], df_ab[~df_ab['converted']]['total ads'])
    print(f"Manwhiteney U test:p-value = {u_pvalue}")
# %%
