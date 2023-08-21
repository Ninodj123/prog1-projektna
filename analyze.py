import pandas as pd
import numpy as np
from scipy.stats import pearsonr, f_oneway
import matplotlib.pyplot as plt

# Read data from CSV file
df = pd.read_csv('movies.csv')

# Data Cleaning
df['Budget'] = df['Budget'].str.replace(',', '').str.replace('-', '0').astype(float)
df['Revenue'] = df['Revenue'].str.replace(',', '').str.replace('-', '0').astype(float)
df['Release Date'] = pd.to_datetime(df['Release Date'], dayfirst=True)
df['Month'] = df['Release Date'].dt.month

# H1: Correlation between Genre and Score
df['Genre'] = df['Genre'].str.strip("[]").str.replace("'", "").str.split(', ')
df_exploded = df.explode('Genre')
grouped_scores = [df_exploded['Score'][df_exploded['Genre'] == genre] for genre in df_exploded['Genre'].unique()]
F_statistic, p_value_genre_score = f_oneway(*grouped_scores)
print(f"H1: ANOVA test between Genre and Score: F-statistic: {F_statistic:.2f}, P-value: {p_value_genre_score:.4f}")

# Interpretation for H1
if p_value_genre_score <= 0.05:
    print("There is a statistically significant difference in scores among the genres.")
else:
    print("There is no statistically significant difference in scores among the genres.")

# Visualization for H1
plt.figure(figsize=(10,6))
df_exploded.boxplot(column='Score', by='Genre')
plt.title('Score by Genre')
plt.xlabel('Genre')
plt.ylabel('Score')
plt.suptitle('')  # Suppress default title
plt.xticks(rotation=45)  # Rotate genre labels for better readability
plt.tight_layout()  # Ensure everything fits well
plt.show()

# H2: Correlation between Duration and Score
correlation_duration_score, p_value_duration_score = pearsonr(df['Duration'], df['Score'])
print(f"H2: Correlation between Duration and Score: {correlation_duration_score:.2f}, P-value: {p_value_duration_score:.4f}")

# Interpretation for H2
if p_value_duration_score <= 0.05:
    if correlation_duration_score > 0:
        print("There is a statistically significant positive correlation between Duration and Score.")
    else:
        print("There is a statistically significant negative correlation between Duration and Score.")
else:
    print("There is no statistically significant correlation between Duration and Score.")

# Visualization for H2
plt.scatter(df['Duration'], df['Score'], alpha=0.6)
plt.title('Duration vs. Score')
plt.xlabel('Duration')
plt.ylabel('Score')
plt.show()

# H3: Correlation between Budget and Revenue
budget_revenue_data = df[(df['Budget'] != 0) & (df['Revenue'] != 0)]
correlation_budget_revenue, p_value_budget_revenue = pearsonr(budget_revenue_data['Budget'], budget_revenue_data['Revenue'])
print(f"H3: Correlation between Budget and Revenue: {correlation_budget_revenue:.2f}, P-value: {p_value_budget_revenue:.4f}")

# Interpretation for H3
if p_value_budget_revenue <= 0.05:
    if correlation_budget_revenue > 0:
        print("There is a statistically significant positive correlation between Budget and Revenue.")
    else:
        print("There is a statistically significant negative correlation between Budget and Revenue.")
else:
    print("There is no statistically significant correlation between Budget and Revenue.")

# Visualization for H3
plt.scatter(budget_revenue_data['Budget'], budget_revenue_data['Revenue'], alpha=0.6)
plt.title('Budget vs. Revenue')
plt.xlabel('Budget')
plt.ylabel('Revenue')
plt.show()

# H4: Correlation between Month of Release and Score
correlation_month_score, p_value_month_score = pearsonr(df['Month'], df['Score'])
print(f"H4: Correlation between Month of Release and Score: {correlation_month_score:.2f}, P-value: {p_value_month_score:.4f}")

# Interpretation for H4
if p_value_month_score <= 0.05:
    if correlation_month_score > 0:
        print("There is a statistically significant positive correlation between the Month of Release and movie scores.")
    else:
        print("There is a statistically significant negative correlation between the Month of Release and movie scores.")
else:
    print("There is no statistically significant correlation between the Month of Release and movie scores.")

# Visualization for H4
df.boxplot(column='Score', by='Month', figsize=(10,6))
plt.title('Score by Month of Release')
plt.xlabel('Month')
plt.ylabel('Score')
plt.suptitle('')  # Suppress default title
plt.show()
