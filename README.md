# Social Media Usage and Mental Health Analysis - REPORT

This project analyzes social media data to detect trends and patterns in mental health discussions, specifically focusing on anxiety.

*Developed by Alesse Nunes*

## Project Structure
- `data/` - Datasets and data processing scripts
- `notebooks/` - Jupyter notebooks for data analysis
- `src/` - Source code for data processing and analysis
- `models/` - Machine learning models
- `results/` - Analysis results and visualizations

## Installation
- List any necessary Python packages
- Add instructions for setting up the environment


## Summary

This report presents the results of an analysis on social media usage and its impact on users' mental health. By analyzing engagement metrics such as daily usage time, posts, likes, comments, and messages sent, patterns of emotional states associated with online behavior were identified.

## Key Insights

### 1. **Social Media Usage Patterns**

- **Average Daily Usage Time:** 95.95 minutes.
- **Posts Per Day:** 3.32 posts on average.
- **Likes Received Per Day:** 39.90 likes on average.
- **Comments Received Per Day:** 15.61 comments on average.
- **Messages Sent Per Day:** 22.56 messages on average.

These figures reveal the level of user engagement across platforms, with notable variation between users.

### 2. **Emotional Impact of Social Media Usage**

The analysis predicted users' emotions with an accuracy of 99.5%, categorizing emotions as **Happiness**, **Anger**, **Neutral**, **Anxiety**, **Boredom**, and **Sadness**.

#### Classification Report:

| Emotion    | Precision | Recall | F1-Score |
|------------|-----------|--------|----------|
| Happiness  | 1.00      | 1.00   | 1.00     |
| Anger      | 1.00      | 1.00   | 1.00     |
| Neutral    | 0.98      | 1.00   | 0.99     |
| Anxiety    | 1.00      | 0.97   | 0.99     |
| Boredom    | 1.00      | 1.00   | 1.00     |
| Sadness    | 1.00      | 1.00   | 1.00     |

The **overall accuracy** was 99.5%, indicating a highly precise model for identifying emotions based on social media behavior.

### 3. **Confusion Matrix**

The following confusion matrix illustrates how well the model identified emotions:

|              | Happiness | Anger | Neutral | Anxiety | Boredom | Sadness |
|--------------|-----------|-------|---------|---------|---------|---------|
| **Happiness** | 35        | 0     | 0       | 0       | 0       | 0       |
| **Anger**     | 0         | 29    | 0       | 0       | 0       | 0       |
| **Neutral**   | 0         | 0     | 42      | 0       | 0       | 0       |
| **Anxiety**   | 0         | 0     | 1       | 38      | 0       | 0       |
| **Boredom**   | 0         | 0     | 0       | 0       | 31      | 0       |
| **Sadness**   | 0         | 0     | 0       | 0       | 0       | 24      |

### 4. **Mental Health Implications**

The data suggest that the time spent on social media and the level of interaction with posts and messages can directly impact users' emotional states. **Anxiety** and **Boredom** are the emotions most frequently associated with higher levels of engagement.

### 5. **Opportunities for Mental Health Interventions**

Based on these findings, tools can be developed to monitor users' emotions in real-time and offer personalized interventions, such as mindfulness practices or redirection to positive content.

## Conclusion

This study shows that analyzing social media behaviors can provide valuable insights into users' emotional well-being. Based on these findings, we can work towards creating more mental health-conscious platforms for users.

