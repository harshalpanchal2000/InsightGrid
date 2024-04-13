# InsightGrid

InsightGrid is a Python library for automating Exploratory Data Analysis (EDA) tasks. It provides functions to generate comprehensive reports on your dataset directly in your IDE, including basic information, summary statistics, descriptive statistics, missing values analysis, duplicates analysis, skewness calculation, univariate analysis, bivariate analysis, and outliers detection.

## Installation

You can install InsightGrid using pip:
```
pip install insightgrid
```

## Usage

```python
import pandas as pd
from insightgrid import generate_report

# Load your dataset
data = pd.read_csv('data.csv')

# Generate EDA report
generate_report(data)
```

This will display the analysis results directly in your IDE's console.

## Features:

1. **Basic Information:** Provides statistics such as the number of rows and columns, data types of columns, and any missing values.

2. **Summary Statistics:** Descriptive statistics for numerical columns.

3. **Descriptive Statistics:** Histograms for numerical columns.

4. **Missing Values Analysis:** Number and percentage of missing values for each column.

5. **Duplicates Analysis:** Number and percentage of duplicate rows.

6. **Skewness Calculation:** Skewness values for numerical columns.

7. **Univariate Analysis:** Box plots for numerical columns and bar plots for categorical columns.

8. **Bivariate Analysis:** Correlation heatmap, pair plots, and box plots for categorical vs numerical columns.

9. **Outliers Detection:** Identification of outliers using the IQR method.

## Contributing
Contributions are welcome! Please feel free to open an issue or submit a pull request for any improvements or additional features you'd like to see.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
