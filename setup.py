from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="insightgrid",
    version="0.1",
    author="Your Name",
    author_email="contact@itsmeharshal.com",
    description="A Python library for automating Exploratory Data Analysis (EDA) tasks.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/harshalpanchal2000/InsightGrid/",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "scipy",
        "scikit-learn"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
