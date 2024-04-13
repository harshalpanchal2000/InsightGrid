import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64

def generate_report(data):
    html_content = ""

    def basic_info(data):
        nonlocal html_content
        num_rows, num_cols = data.shape
        data_types = data.dtypes
        missing_values = data.isnull().sum()
        
        # Convert basic info to HTML
        basic_info_html = f"<h2>Basic Information:</h2>"
        basic_info_html += f"<p>Number of rows: {num_rows}</p>"
        basic_info_html += f"<p>Number of columns: {num_cols}</p>"
        basic_info_html += "<p>Data types of columns:</p>"
        basic_info_html += data_types.to_frame().to_html()
        basic_info_html += "<p>Missing values:</p>"
        basic_info_html += missing_values.to_frame().to_html()
        html_content += basic_info_html

    def summary_stats(data):
        nonlocal html_content
        summary_stats_html = f"<h2>Summary Statistics:</h2>"
        summary_stats_html += data.describe().to_html()
        html_content += summary_stats_html

    def descriptive_stats(data):
        nonlocal html_content
        descriptive_stats_html = f"<h2>Descriptive Statistics:</h2>"
        for column in data.select_dtypes(include=['int64', 'float64']).columns:
            plt.figure(figsize=(8, 6))
            plt.hist(data[column], bins=20, color='skyblue', edgecolor='black')
            plt.title(f'Histogram of {column}')
            plt.xlabel(column)
            plt.ylabel('Frequency')
            plt.grid(True)
            img_html = ""
            # Convert the plot to base64 and embed in HTML
            buffer = BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            img_base64 = base64.b64encode(buffer.read()).decode('utf-8')
            img_html += f"<img src='data:image/png;base64,{img_base64}'/>"
            plt.close()
            descriptive_stats_html += img_html
        html_content += descriptive_stats_html

    def missing_values_analysis(data):
        nonlocal html_content
        missing_values = data.isnull().sum()
        missing_percentage = (missing_values / len(data)) * 100
        
        # Convert missing values analysis to HTML
        missing_values_html = f"<h2>Missing Values Analysis:</h2>"
        missing_values_html += "<p>Number of missing values for each column:</p>"
        missing_values_html += missing_values.to_frame().to_html()
        missing_values_html += "<p>Percentage of missing values for each column:</p>"
        missing_values_html += missing_percentage.to_frame().to_html()
        html_content += missing_values_html

    def duplicates_analysis(data):
        nonlocal html_content
        num_duplicates = data.duplicated().sum()
        duplicate_percentage = (num_duplicates / len(data)) * 100
        
        # Convert duplicates analysis to HTML
        duplicates_analysis_html = f"<h2>Duplicates Analysis:</h2>"
        duplicates_analysis_html += f"<p>Number of duplicate rows: {num_duplicates}</p>"
        duplicates_analysis_html += f"<p>Percentage of duplicate rows: {duplicate_percentage}%</p>"
        html_content += duplicates_analysis_html

    def skewness_calculation(data):
        nonlocal html_content
        skewness = data.skew()
        
        # Convert skewness calculation to HTML
        skewness_html = f"<h2>Skewness Calculation:</h2>"
        skewness_html += skewness.to_frame().to_html()
        html_content += skewness_html

    def univariate_analysis(data):
        nonlocal html_content
        univariate_analysis_html = f"<h2>Univariate Analysis:</h2>"
        for column in data.select_dtypes(include=['int64', 'float64']).columns:
            plt.figure(figsize=(8, 6))
            sns.boxplot(data[column])
            plt.title(f'Boxplot of {column}')
            plt.xlabel(column)
            plt.show()
        
        for column in data.select_dtypes(include=['object']).columns:
            plt.figure(figsize=(8, 6))
            data[column].value_counts().plot(kind='bar', color='skyblue')
            plt.title(f'Bar plot of {column}')
            plt.xlabel(column)
            plt.ylabel('Frequency')
            plt.show()

    def bivariate_analysis(data):
        nonlocal html_content
        corr_matrix = data.corr()
        
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
        nonlocal html_content
        numerical_cols = data.select_dtypes(include=['int64', 'float64']).columns
        for column in numerical_cols:
            Q1 = data[column].quantile(0.25)
            Q3 = data[column].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
            html_content += f"<p>Number of outliers in {column}: {len(outliers)}</p>"

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

    # Write the HTML content to a file or return it
    with open("report.html", "w") as f:
        f.write(html_content)
