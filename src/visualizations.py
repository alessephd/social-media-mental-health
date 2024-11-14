# visualizations.py
import matplotlib.pyplot as plt

def plot_sentiment_distribution(sentiments):
    """Plots the distribution of sentiment classifications."""
    sentiments.value_counts().plot(kind='bar', color=['green', 'grey', 'red'])
    plt.xlabel('Sentiment')
    plt.ylabel('Frequency')
    plt.title('Sentiment Distribution')
    plt.show()
  
