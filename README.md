# 🚀 AI-Powered LeetCode Performance Analyzer

An interactive analytics dashboard that analyzes a user's LeetCode coding performance and provides personalized recommendations for improving problem-solving skills.

This project fetches data from the LeetCode profile and generates insights such as solved problem statistics, contest performance, skill level, and recommended problems to practice.

---

## 📊 Features

* 🔍 **LeetCode Profile Analysis**
  Analyze total solved problems including Easy, Medium, and Hard difficulty.

* 🏆 **Contest Performance Tracker**
  View contest rating, global ranking, and number of contests attended.

* 📈 **Skill Score System**
  Calculates a skill score based on solved problems to determine coding level.

* 📊 **Difficulty Distribution Chart**
  Visual representation of Easy, Medium, and Hard problems solved.

* 🧠 **Skill Radar Chart**
  Displays coding strengths and areas that need improvement.

* 🤖 **AI Feedback System**
  Provides recommendations on what difficulty problems to focus on.

* 🧩 **Dynamic Problem Recommendations**
  Suggests problems to practice based on the user’s current performance.

* 📅 **5-Day Coding Practice Plan**
  Generates a structured practice schedule.

* ⚠️ **Weak Topic Detector**
  Identifies topics that need more practice.

* 🎯 **Weekly Coding Target Generator**
  Suggests weekly problem-solving goals.

* 🔥 **Coding Consistency Tracker**
  Encourages daily coding habits based on total solved problems.

* 🧠 **Topic Difficulty Predictor**
  Predicts recommended problem difficulty based on selected coding topics.

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Matplotlib**
* **NumPy**
* **LeetCode GraphQL API**

---

## 📂 Project Structure

leetcode-analyzer
│
├── app.py                # Main Streamlit dashboard
├── analyzer.py           # Fetches and analyzes LeetCode profile data
├── recommender.py        # Problem recommendation system
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation

---

## ⚙️ Installation

1. Clone the repository

```
git clone https://github.com/your-username/leetcode-analyzer.git
```

2. Navigate to the project folder

```
cd leetcode-analyzer
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Run the application

```
streamlit run app.py
```

---

## 💡 How It Works

1. Enter your LeetCode username.
2. The system fetches profile data using the LeetCode API.
3. Performance statistics are analyzed.
4. The dashboard displays:

   * Problem solving statistics
   * Contest performance
   * Skill level
   * AI feedback
   * Recommended problems
   * Practice plans

---

## 🎯 Future Improvements

* Compare two LeetCode users' performance
* Add topic-based problem recommendations
* Implement machine learning for smarter recommendations
* Track daily coding streaks

---

## 👩‍💻 Author

Muskan Sahu

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
