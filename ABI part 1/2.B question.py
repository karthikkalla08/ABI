import pandas as pd

# Loading the Actuals and Target datasets
actuals_df = pd.read_csv('actuals.csv')
target_df = pd.read_csv('target.csv')

# Clean the datasets and select required columns
actuals_cleaned = actuals_df[['Plant', 'Category', 'Actuals']]
target_cleaned = target_df[['Plant', 'Category', 'Target']]

# Merge Actuals and Target using Plant and Category as the key columns
variance_analysis = pd.merge(actuals_cleaned, target_cleaned, on=['Plant', 'Category'], how='inner')

# Calculate the variance between Actuals and Target datasets
variance_analysis['Variance'] = variance_analysis['Actuals'] - variance_analysis['Target']

# Display the variance analysis
print(variance_analysis)
