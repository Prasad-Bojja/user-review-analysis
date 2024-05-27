import pandas as pd
import string
from textblob import TextBlob
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'C:\\python\\user_review.xls'
reviews_df = pd.read_excel(file_path)

# Clean the data
# Remove null values
reviews_df.dropna(inplace=True)

# Assuming 'review' is the column with text reviews, drop other unnecessary columns
# Adjust the columns list based on the actual dataset
columns_to_keep = ['review']  # Replace with actual column names if different
reviews_df = reviews_df[columns_to_keep]

# Text preprocessing
def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

reviews_df['cleaned_review'] = reviews_df['review'].apply(preprocess_text)

# Sentiment analysis
def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity < 0:
        return 'negative'
    else:
        return 'neutral'

reviews_df['sentiment'] = reviews_df['cleaned_review'].apply(analyze_sentiment)

# Generate summary report
sentiment_counts = reviews_df['sentiment'].value_counts()

# Plot the distribution of sentiments
plt.figure(figsize=(8, 6))
sentiment_counts.plot(kind='bar', color=['green', 'red', 'blue'])
plt.title('Distribution of Sentiments')
plt.xlabel('Sentiment')
plt.ylabel('Number of Reviews')
plt.show()

# Save the summary report
summary_report = sentiment_counts.to_frame(name='count')
summary_report.reset_index(inplace=True)
summary_report.rename(columns={'index': 'sentiment'}, inplace=True)

# Save to Excel
summary_report.to_excel('sentiment_summary_report.xlsx', index=False)

# Print the summary report
print(summary_report)
