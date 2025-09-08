
# 📂 Emotional-Cybersecurity / README.md

```markdown
# Emotional Cybersecurity  

This section focuses on **human risk defense and emotional cybersecurity (NJAWA™)**.  

## Example Projects  
- **Stress Detector AI** → Detecting stress and emotional manipulation.  
- **NJAWA™ Emotional Shield** → Framework protecting humans before machines.  
- **Digital Burnout Prevention** → Tools to reduce cognitive overload.  

##  Demo: Stress Detector  

```python
# stress-detector-demo.py
from textblob import TextBlob

def stress_detector(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity < -0.3:
        return "⚠️ High Stress"
    elif polarity < 0.3:
        return "😐 Medium Stress"
    else:
        return "✅ Low Stress"

print(stress_detector("I feel nervous about this email."))
print(stress_detector("Everything looks fine and safe.
