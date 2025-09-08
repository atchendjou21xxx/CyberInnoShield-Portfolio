# stress-detector-demo.py
# Simple demo for Emotional Cybersecurity (CyberInnoShield INT™)

from textblob import TextBlob

# Demo texts
texts = [
    "I feel very nervous about this suspicious email.",
    "This looks safe, I think it is fine.",
    "I'm stressed and confused because my account was locked."
]

print("=== Stress Detector Demo ===")
for t in texts:
    analysis = TextBlob(t)
    polarity = analysis.sentiment.polarity  # -1 (negatif) → +1 (positif)
    
    if polarity < -0.1:
        print(f"[ALERT] Stress/Anxiety detected: \"{t}\"")
    else:
        print(f"[OK] Neutral/Safe: \"{t}\"")
