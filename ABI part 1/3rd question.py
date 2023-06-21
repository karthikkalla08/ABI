import pandas as pd
import matplotlib.pyplot as plt

# Loading the Actuals dataset
actuals_df = pd.read_csv('actuals.csv')

# Clean the dataset and select required columns
actuals_cleaned = actuals_df[['Plant', 'Category', 'Period', 'Actuals']]

# Group the data by Plant and Category columns
grouped_data = actuals_cleaned.groupby(['Plant', 'Category'])

# Iterating over each group to plot the trend
for group_name, group_data in grouped_data:
    # Extract the Plant and Category names
    plant, category = group_name

    # Sort the data by Period for proper trend analysis
    sorted_data = group_data.sort_values('Period')

    # Plot the trend for the current Plant and Category
    plt.figure()
    plt.plot(sorted_data['Period'], sorted_data['Actuals'])
    plt.xlabel('Period')
    plt.ylabel('Actuals')
    plt.title(f'Trend Analysis for {category} in {plant}')
    plt.show()
