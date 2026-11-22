import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

from analyzer import get_leetcode_data, analyze_performance
from recommender import recommend_problems, generate_practice_plan, detect_weak_topics

st.set_page_config(
    page_title="LeetCode AI Analyzer",
    page_icon="🚀",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.title("📊 Dashboard")
    st.write("LeetCode AI Performance Analyzer")
    st.write("Analyze coding skills and contest performance.")


# Styling
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b, #020617);
    color: #ffffff;
}

/* Main heading */
h1 {
    text-align: center;
    color: #38bdf8 !important;
    font-size: 50px;
}

/* Section headings */
h2, h3 {
    color: #ffffff !important;
}

/* Metric labels: Total, Easy, Medium, Hard */
[data-testid="stMetricLabel"],
[data-testid="stMetricLabel"] p,
[data-testid="stMetricLabel"] div {
    color: #CBD5E1 !important;
    opacity: 1 !important;
}

/* Metric values: 159, 107, 49, 3 */
[data-testid="stMetricValue"],
[data-testid="stMetricValue"] div {
    color: #FFFFFF !important;
    opacity: 1 !important;
}

/* Metric delta text */
[data-testid="stMetricDelta"] {
    color: #CBD5E1 !important;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #3b82f6, #06b6d4);
    color: white !important;
    border-radius: 10px;
    height: 3em;
    width: 200px;
    font-size: 18px;
}

/* Input labels */
.stTextInput label {
    color: #FFFFFF !important;
}

/* General text */
.stMarkdown p,
.stMarkdown li {
    color: #E2E8F0;
}

</style>
""", unsafe_allow_html=True)

# Session state fix
if "analyzed" not in st.session_state:
    st.session_state.analyzed = False

if st.button("Analyze Profile"):
    st.session_state.analyzed = True

if st.session_state.analyzed:

    with st.spinner("Analyzing profile..."):

        data = get_leetcode_data(username)

        if data is None:
            st.error("User not found or profile private")
            st.stop()

        stats = analyze_performance(data)

        if stats is None:
            st.error("Unable to analyze profile data")
            st.stop()

        total = stats["total"]
        easy = stats["easy"]
        medium = stats["medium"]
        hard = stats["hard"]

        rating = stats["rating"]
        ranking = stats["ranking"]
        contests = stats["contests"]

        score = easy*1 + medium*3 + hard*5

        if score < 100:
            level = "Beginner 🟢"
        elif score < 300:
            level = "Intermediate 🟡"
        else:
            level = "Advanced 🔴"

        st.success("Profile analyzed successfully!")

        st.markdown("---")

        # Coding Statistics
        st.subheader("📊 Coding Statistics")

        col1,col2,col3,col4 = st.columns(4)

        col1.metric("Total",total)
        col2.metric("Easy",easy)
        col3.metric("Medium",medium)
        col4.metric("Hard",hard)

        # Contest Performance
        st.subheader("🏆 Contest Performance")

        col5,col6,col7 = st.columns(3)

        col5.metric("Contest Rating", int(rating))
        col6.metric("Global Ranking", ranking)
        col7.metric("Contests Attended", contests)

        # Skill Score
        st.subheader("🏆 Skill Score")

        col8,col9 = st.columns(2)

        col8.metric("Score",score)
        col9.metric("Level",level)

        # Skill Progress
        st.subheader("📈 Skill Progress")

        progress = min(score/300,1.0)
        st.progress(progress)

        # Weekly Coding Target
        st.subheader("🎯 Weekly Coding Target")

        if score < 100:
            st.info("Solve 20 Easy problems this week")

        elif score < 300:
            st.info("Solve 15 Medium + 5 Easy problems")

        else:
            st.success("Solve 10 Hard + 10 Medium problems")

        # Coding Consistency
        st.subheader("🔥 Coding Consistency")

        if total < 50:
            st.write("Begin building daily coding habit (3 problems/day).")

        elif total < 200:
            st.write("Good consistency! Try solving 4–5 problems/day.")

        else:
            st.success("Excellent consistency. Maintain 5+ problems/day.")

        # AI Feedback
        st.subheader("🤖 AI Feedback")

        if easy < 30:
            st.info("Focus on solving more Easy problems to build fundamentals.")

        elif medium < 50:
            st.info("You have good basics. Start solving more Medium problems.")

        elif hard < 20:
            st.info("Try solving Hard problems to become advanced.")

        else:
            st.success("Excellent performance!")

        # Difficulty Chart
        st.subheader("📊 Difficulty Breakdown")

        labels = ["Easy","Medium","Hard"]
        values = [easy,medium,hard]

        fig,ax = plt.subplots()
        ax.pie(values,labels=labels,autopct="%1.1f%%")
        ax.axis("equal")

        st.pyplot(fig)

        # Radar Chart
        st.subheader("🧠 Skill Radar")

        labels = ['Easy','Medium','Hard','Problem Solving','Consistency']

        values = [
        easy,
        medium,
        hard,
        (easy+medium+hard)/3,
        (min(easy,50)+min(medium,50))/2
        ]

        angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)

        values = np.concatenate((values,[values[0]]))
        angles = np.concatenate((angles,[angles[0]]))

        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)

        ax.plot(angles, values)
        ax.fill(angles, values, alpha=0.25)

        ax.set_thetagrids(angles[:-1]*180/np.pi, labels)

        st.pyplot(fig)

        # Recommended Problems
        st.subheader("🧠 Recommended Problems")

        problems = recommend_problems(stats)

        for p in problems:
            st.markdown(f"✅ [{p['title']}]({p['link']})")

        # Practice Plan
        st.subheader("📅 5-Day Practice Plan")

        plan = generate_practice_plan()

        for day,tasks in plan.items():

            st.write(day)

            for t in tasks:
                st.markdown(f"- [{t['title']}]({t['link']})")

        # Weak Topics
        st.subheader("⚠️ Weak Topics")

        weak_topics = detect_weak_topics()

        for topic in weak_topics:
            st.warning(f"Practice more problems in **{topic}**")

        # Topic Difficulty Predictor
        st.subheader("🧠 Topic Difficulty Predictor")

        topic = st.text_input("Enter a topic (Array, DP, Graph, Tree)")

        if topic:

            if topic.lower() in ["array","string"]:
                st.success("Recommended Difficulty: Easy → Medium")

            elif topic.lower() in ["dp","dynamic programming","graph"]:
                st.warning("Recommended Difficulty: Medium → Hard")

            elif topic.lower() in ["tree","binary tree"]:
                st.info("Recommended Difficulty: Medium")

            else:
                st.write("Practice mixed difficulty problems.")

        # Professional completion message
        st.markdown("---")
        st.success("✅ Profile Analysis Completed")
        st.caption("LeetCode performance insights generated successfully.")
