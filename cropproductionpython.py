import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import seaborn as sns
import os

data_dir= 'data'
# Load the dataset

data = pd.read_csv(os.path.join(data_dir,'/Users/vandana/Desktop/Crop Production project/Crop Production data.csv'))

data.head()

# Display basic information about the dataset
data.info()

#Total rows and columns
print("Data Shape",data.shape)

 

#All Columns
columns=list(data)
print(columns)

#checking Null Values
missing_values=data.isnull().sum()
print("Missing Values:",missing_values)

# Calculate the median of 'Production' column
production_median = data['Production'].median()


# Fill NaN values in 'Production' column with the median of the 'Production' column itself
data['Production']= data['Production'].fillna(production_median)

# Check again for missing values
missing_values = data.isnull().sum()
print(missing_values)

#Data Formatting
print(data.dtypes)

# Calculate basic statistics for numeric columns
numeric_stats = data.describe()

# Print the calculated statistics
print("Basic Statistics",numeric_stats)

#Distribution Analysis
plt.figure(figsize=(10, 6))
sns.histplot(data['Production'], bins=50, kde=True, color='skyblue')
plt.title('Distribution of Production')
plt.xlabel('Production')
plt.ylabel('Frequency')

# Adjusting axis ticks format for better readability
plt.ticklabel_format(style='plain', axis='x')  # Display x-axis ticks in plain format

# Function to format y-axis ticks in plain format
def format_ticks(x, pos):
    """Format ticks to plain notation"""
    return '{:.0f}'.format(x)

# Apply custom formatter to y-axis
plt.gca().yaxis.set_major_formatter(FuncFormatter(format_ticks))
plt.grid(True)
plt.show()



# Correlation analysis for numeric columns only
numeric_data = data.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numeric_data.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Correlation Matrix')
plt.show()


# Trends over years
plt.figure(figsize=(12, 6))
sns.lineplot(data=data, x='Crop_Year', y='Production')
plt.title('Crop Production Trends Over the Years')
plt.xlabel('Year')
plt.ylabel('Production')
plt.grid(True)
plt.show()

# Production by state
state_production = data.groupby('State_Name')['Production'].sum().reset_index()
state_production = state_production.sort_values(by='Production', ascending=False)
plt.figure(figsize=(12, 8))
sns.barplot(data=state_production, x='Production', y='State_Name')
plt.title('Production by State')
plt.xlabel('Production')
plt.ylabel('State')
plt.grid(True)
plt.show()

# Seasonal analysis
season_production = data.groupby('Season')['Production'].sum().reset_index()
plt.figure(figsize=(8, 6))
sns.barplot(data=season_production, x='Season', y='Production')
plt.title('Production by Season')
plt.xlabel('Season')
plt.ylabel('Production')
plt.grid(True)
plt.show()




