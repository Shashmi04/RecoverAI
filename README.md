RecoverAI – AI-Powered Payment Recovery System

RecoverAI is an AI-powered payment recovery system that uses Machine Learning to predict the probability of recovering failed payments and recommend the most suitable recovery action.

🚨 Problem

Businesses lose revenue because of failed payments caused by network errors, bank timeouts, card declines, technical errors, and checkout abandonment.

RecoverAI helps identify which failed payments are worth recovering and what action should be taken.

💡 Solution

RecoverAI provides:

Recovery Probability
Recovery Priority
Recommended Recovery Action
Estimated Recovery Value
🔄 Workflow

Transaction Data → Data Preprocessing → ML Models → Gradient Boosting → Recovery Probability → Recovery Priority → Recommended Action → Estimated Recovery Value → Flask API → Web Dashboard

🤖 Machine Learning

We compared:

Random Forest
Logistic Regression
Gradient Boosting
Best Model: Gradient Boosting
Accuracy: 64.68%
Precision: 66.24%
Recall: 71.23%
F1 Score: 68.65%
ROC-AUC: 0.6887
📊 Project Results
Total Transactions: 10,000
Recovery Opportunities: 2,689
Revenue at Risk: ₹3.32 Crore
Recovered Revenue: ₹1.80 Crore
Overall Recovery Rate: 54.33%
💳 Example

Input:
Amount: ₹23,123.58
Payment Method: UPI
Failure Reason: Bank Timeout

Output:
Recovery Probability: 59.01%
Priority: Medium
Recommended Action: Retry After Delay
Estimated Recovery Value: ₹13,645

🛠️ Technologies

Python, Pandas, NumPy, Scikit-learn, Gradient Boosting, Joblib, Flask, HTML, CSS, JavaScript

▶️ Run the Project

Install dependencies:

pip install -r requirements.txt

Run the application:

python -m api.app

Open in browser:

http://127.0.0.1:5000/
