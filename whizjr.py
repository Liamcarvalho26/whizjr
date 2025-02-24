from transformers import pipeline
import random

# Load sentiment analysis model (specify model to avoid warning)
sentiment_model = pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

# Fallback: Hardcoded trend data
def fetch_trend_data(topic="AI"):
    return [
        f"{topic} is revolutionizing tech!",
        f"Concerns grow over {topic} ethics",
        f"New {topic} breakthrough announced",
        f"{topic} stocks dip slightly",
        f"Experts debate {topic} future"
    ]

# Analyze trend
def analyze_trend(posts):
    sentiments = [sentiment_model(post)[0] for post in posts]
    avg_score = sum(1 if s['label'] == 'POSITIVE' else -1 for s in sentiments) / len(sentiments)
    volume = random.randint(50, 200)  # Simulated volume
    return avg_score, volume

# Act: Make a recommendation
def recommend_action(avg_score, volume):
    if avg_score > 0 and volume > 100:
        return "Jump on this trend! It’s hot and positive."
    elif avg_score < 0:
        return "Avoid this—negative vibes dominate."
    else:
        return "Wait—this is cooling off or neutral."

# Run the agent
topic = "AI"
print(f"Monitoring trend: {topic}")
posts = fetch_trend_data(topic)
print("Sample posts collected:")
for i, post in enumerate(posts, 1):
    print(f"{i}. {post}")

avg_score, volume = analyze_trend(posts)
recommendation = recommend_action(avg_score, volume)
print(f"\nTrend Analysis - Sentiment Score: {avg_score:.2f}, Estimated Volume: {volume}")
print(f"Recommendation: {recommendation}")