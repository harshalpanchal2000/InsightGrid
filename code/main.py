import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def generate_report(data):
    def basic_info(data):
        num_rows, num_cols = data.shape
        data_types = data.dtypes
        missing_values = data.isnull().sum()
        
        print("### Basic Information:")
        print("| Statistic | Value |")
        print("|-----------|-------|")
        print(f"| Number of rows | {num_rows} |")
        print(f"| Number of columns | {num_cols} |")
        print(f"| Data types of columns | {data_types} |")
        print(f"| Missing values | {missing_values} |")

    def summary_stats(data):
        print("\n### Summary Statistics:")
        print(data.describe().to_markdown())

    def descriptive_stats(data):
        print("\n### Descriptive Statistics:")
        for column in data.select_dtypes(include=['int64', 'float64']).columns:
            plt.figure(figsize=(8, 6))
            plt.hist(data[column], bins=20, color='skyblue', edgecolor='black')
            plt.title(f'Histogram of {column}')
            plt.xlabel(column)
            plt.ylabel('Frequency')
            plt.grid(True)
            plt.show()

    def missing_values_analysis(data):
        missing_values = data.isnull().sum()
        missing_percentage = (missing_values / len(data)) * 100
        
        print("\n### Missing Values Analysis:")
        print("#### Number of missing values for each column:")
        print(missing_values.to_markdown())
        print("\n#### Percentage of missing values for each column:")
        print(missing_percentage.to_markdown())

    def duplicates_analysis(data):
        num_duplicates = data.duplicated().sum()
        duplicate_percentage = (num_duplicates / len(data)) * 100
        
        print("\n### Duplicates Analysis:")
        print(f"Number of duplicate rows: {num_duplicates}")
        print(f"Percentage of duplicate rows: {duplicate_percentage}%")

    def skewness_calculation(data):
        print("\n### Skewness Calculation:")
        print(data.skew().to_markdown())

    def univariate_analysis(data):
        print("\n### Univariate Analysis:")
        for column in data.select_dtypes(include=['int64', 'float64']).columns:
            plt.figure(figsize=(8, 6))
            sns.boxplot(data[column])
            plt.title(f'Boxplot of {column}')
            plt.show()
        
        for column in data.select_dtypes(include=['object']).columns:
            plt.figure(figsize=(8, 6))
            data[column].value_counts().plot(kind='bar', color='skyblue')
            plt.title(f'Bar plot of {column}')
            plt.xlabel(column)
            plt.ylabel('Frequency')
            plt.show()

    def bivariate_analysis(data):
        corr_matrix = data.corr()
        
        print("\n### Bivariate Analysis:")
        print("\n#### Correlation Matrix:")
        print(corr_matrix.to_markdown())
        
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Correlation Heatmap')
        plt.show()
        
        sns.pairplot(data.select_dtypes(include=['int64', 'float64']))
        plt.title('Pairplot of Numerical Columns')
        plt.show()
        
        for column in data.select_dtypes(include=['object']).columns:
            plt.figure(figsize=(10, 6))
            sns.boxplot(x=column, y='target_variable', data=data)
            plt.title(f'Boxplot of {column} vs target_variable')
            plt.xlabel(column)
            plt.ylabel('target_variable')
            plt.show()

    def outliers_detection(data):
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
    basic_info(data)
    summary_stats(data)
    descriptive_stats(data)
    missing_values_analysis(data)
    duplicates_analysis(data)
    skewness_calculation(data)
    univariate_analysis(data)
    bivariate_analysis(data)
    outliers_detection(data)
