import pandas as pd

# Loading the Actuals, Targets, Price, and bcr datasets
actuals_df = pd.read_csv('actuals.csv')
target_df = pd.read_csv('target.csv')
price_df = pd.read_csv('price.csv')
bcr_df = pd.read_csv('bcr.csv')

# Clean the datasets and select the required columns
actuals_cleaned = actuals_df[['Material number', 'Plant', 'Actuals']]
price_cleaned = price_df[['Material number', 'Bottle Price', 'Crate Price']]
bcr_cleaned = bcr_df[['Material', 'Bottle Quantity', 'Crate Quantity']]

# Merge Actuals with Price datasets using Material number and Plant as key columns
actuals_price = pd.merge(actuals_cleaned, price_cleaned, on=['Material number'], how='left')

# Merge Actuals/Price with bcr using Material number and Plant as key columns
consolidated_view = pd.merge(actuals_price, bcr_cleaned, left_on=['Material number', 'Plant'], right_on=['Material', 'Plant'], how='left')

# Calculate Bottle Rands and Crate Rands 
consolidated_view['Bottle Rands'] = consolidated_view['Bottle Price'] * consolidated_view['Bottle Quantity']
consolidated_view['Crate Rands'] = consolidated_view['Crate Price'] * consolidated_view['Crate Quantity']

# Select the desired columns for the consolidated view
consolidated_view = consolidated_view[['Material number', 'Plant', 'Bottle Price', 'Crate Price', 'Bottle Rands', 'Crate Rands']]

# Display the consolidated view
print(consolidated_view)
