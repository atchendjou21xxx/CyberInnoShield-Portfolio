# AI Projects  

This section includes **Artificial Intelligence projects applied to cybersecurity**.  

## Example Projects  
- **AI Phishing Detector** → NLP model that identifies phishing emails.  
- **DeepFake Defense AI** → AI that detects deepfake videos.  
- **Password Strength Analyzer** → ML model evaluating password robustness.  

##  Demo: Simple Password Strength Analyzer  

```python
# password-analyzer-demo.py

def password_strength(pw):
    if len(pw) < 6:
        return "❌ Weak password"
    elif pw.isalpha() or pw.isdigit():
        return "⚠️ Medium password"
    else:
        return "✅ Strong password"

# Example
print(password_strength("12345"))
print(password_strength("CyberShield2025"))
