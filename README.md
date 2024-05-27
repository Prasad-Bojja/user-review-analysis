# User Review Analysis

## Overview
This project performs sentiment analysis on user reviews. The main tasks include data cleaning, text preprocessing, and sentiment analysis using the TextBlob library. The results are summarized in a bar plot and an Excel file showing the distribution of sentiments.

## Project Structure
├── user-review-analysis.py
├── user_review.xls
├── requirements.txt
└── sentiment_summary_report.xlsx


## Setup Instructions

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Setting Up the Virtual Environment
1. **Navigate to your project directory**:
    ```sh
    cd C:\python
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    ```sh
    .\venv\Scripts\activate
    ```

### Install Dependencies
1. **Create `requirements.txt` file** (if not already created):
    ```sh
    echo pandas > requirements.txt
    echo openpyxl >> requirements.txt
    echo textblob >> requirements.txt
    echo matplotlib >> requirements.txt
    ```

2. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Analysis
1. **Ensure the virtual environment is activated**:
    ```sh
    .\venv\Scripts\activate
    ```

2. **Run the script**:
    ```sh
    python review_analysis.py
    ```

## Results
- The sentiment distribution is saved in `sentiment_summary_report.xlsx`.
- A bar plot visualizing the distribution of sentiments is displayed.

## Summary Report
The script processes the user reviews and classifies each review as positive, negative, or neutral based on its sentiment polarity. The results are summarized in an Excel file and visualized in a bar plot.

## Files
- `user-review-analysis.py`: The main Python script for performing sentiment analysis.
- `user_review.xls`: The input dataset containing user reviews.
- `requirements.txt`: A list of dependencies required to run the script.
- `sentiment_summary_report.xlsx`: The summary report showing the distribution of sentiments.

## Challenges and Assumptions
- **Challenges**: Ensuring correct columns were selected for analysis required assumptions based on typical datasets. Handling and preprocessing text data efficiently to improve the accuracy of sentiment analysis.
- **Assumptions**: The dataset contains a column named 'review' with the text of user reviews. Only this column is necessary for sentiment analysis. Sentiment classification is done based on the polarity score from TextBlob.
