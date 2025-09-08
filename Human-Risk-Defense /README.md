
# 📂 Human-Risk-Defense / README.md

```markdown
# Human Risk Defense  

This section is dedicated to **reducing the human factor in cybersecurity risks**.  

## Example Projects  
- **Phishing Awareness Simulator** → Training tool for employees.  
- **Account Recovery Workflow** → Steps to recover hacked accounts.  
- **Security Awareness Programs** → Protocols to reduce human error.  

##  Demo: Simple Phishing Email Checker  

```python
# phishing-checker-demo.py

def is_phishing(email_text):
    suspicious_keywords = ["urgent", "click here", "reset password", "bank account"]
    for word in suspicious_keywords:
        if word in email_text.lower():
            return "⚠️ Potential phishing detected"
    return "✅ Safe email"

# Example
print(is_phishing("Urgent! Reset your password now"))
print(is_phishing("Meeting at 10am, bring your laptop"))
