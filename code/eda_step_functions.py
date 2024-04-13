import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def generate_report(data):
    def basic_info(data):
        # Number of rows and columns
        num_rows, num_cols = data.shape
        
        # Data types of columns
        data_types = data.dtypes
        
        # Any missing values
        missing_values = data.isnull().sum()
        
        return num_rows, num_cols, data_types, missing_values

    def summary_stats(data):
        # Summary statistics
        return data.describe()

    def descriptive_stats(data):
        # Visualizations for numerical columns
        for column in data.select_dtypes(include=['int64', 'float64']).columns:
            plt.figure(figsize=(8, 6))
            plt.hist(data[column], bins=20, color='skyblue', edgecolor='black')
            plt.title(f'Histogram of {column}')
            plt.xlabel(column)
            plt.ylabel('Frequency')
            plt.grid(True)
            plt.savefig(f'{column}_histogram.png')  # Save each plot as an image
            plt.close()

    def missing_values_analysis(data):
        # Number of missing values for each column
        missing_values = data.isnull().sum()
        
        # Percentage of missing values for each column
        missing_percentage = (missing_values / len(data)) * 100
        
        return missing_values, missing_percentage

    def duplicates_analysis(data):
        # Number of duplicate rows
        num_duplicates = data.duplicated().sum()
        
        # Percentage of duplicate rows
        duplicate_percentage = (num_duplicates / len(data)) * 100
        
        return num_duplicates, duplicate_percentage

    def skewness_calculation(data):
        # Calculate skewness for numerical columns (even if data has NaN values)
        return data.skew()

    def univariate_analysis(data):
        # Visualizations for numerical columns
        for column in data.select_dtypes(include=['int64', 'float64']).columns:
            plt.figure(figsize=(8, 6))
            sns.boxplot(data[column])
            plt.title(f'Boxplot of {column}')
            plt.show()
        
        # Bar plots for categorical columns
        for column in data.select_dtypes(include=['object']).columns:
            plt.figure(figsize=(8, 6))
            data[column].value_counts().plot(kind='bar', color='skyblue')
            plt.title(f'Bar plot of {column}')
            plt.xlabel(column)
            plt.ylabel('Frequency')
            plt.show()

    def bivariate_analysis(data):
        # Correlation matrix
        corr_matrix = data.corr()
        
        # Heatmap for correlations
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Correlation Heatmap')
        plt.show()
        
        # Scatter plots for numerical vs numerical columns
        sns.pairplot(data.select_dtypes(include=['int64', 'float64']))
        plt.title('Pairplot of Numerical Columns')
        plt.show()
        
        # Box plots for categorical vs numerical columns
        for column in data.select_dtypes(include=['object']).columns:
            plt.figure(figsize=(10, 6))
            sns.boxplot(x=column, y='target_variable', data=data)
            plt.title(f'Boxplot of {column} vs target_variable')
            plt.xlabel(column)
            plt.ylabel('target_variable')
            plt.show()

    def outliers_detection(data):
        # Use IQR method to detect outliers
        numerical_cols = data.select_dtypes(include=['int64', 'float64']).columns
        for column in numerical_cols:
            Q1 = data[column].quantile(0.25)
            Q3 = data[column].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
            print(f"Number of outliers in {column}: {len(outliers)}")

    # Execute all functions
    num_rows, num_cols, data_types, missing_values = basic_info(data)
    print(f"Number of rows: {num_rows}")
    print(f"Number of columns: {num_cols}")
    print("Data types of columns:")
    print(data_types)
    print("Missing values:")
    print(missing_values)
    print("\nSummary Statistics:")
    print(summary_stats(data))
    print("\nDescriptive Statistics:")
    descriptive_stats(data)
    missing_values, missing_percentage = missing_values_analysis(data)
    print("\nMissing Values Analysis:")
    print("Number of missing values for each column:")
    print(missing_values)
    print("\nPercentage of missing values for each column:")
    print(missing_percentage)
    num_duplicates, duplicate_percentage = duplicates_analysis(data)
    print("\nDuplicates Analysis:")
    print(f"Number of duplicate rows: {num_duplicates}")
    print(f"Percentage of duplicate rows: {duplicate_percentage}%")
    print("\nSkewness Calculation:")
    print(skewness_calculation(data))
    print("\nUnivariate Analysis:")
    univariate_analysis(data)
    print("\nBivariate Analysis:")
    bivariate_analysis(data)
    print("\nOutliers Detection:")
    outliers_detection(data)

