from code.eda_steps_functions import generate_report
import pandas as pd

# Load your dataset
data = pd.read_csv('data.csv')

# Generate EDA report
generate_report(data)
