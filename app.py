import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

from analyzer import get_leetcode_data, analyze_performance
from recommender import (
    recommend_problems,
    generate_practice_plan,
    detect_weak_topics
)

st.set_page_config(
    page_title="LeetCode AI Analyzer",
    page_icon="🚀",
    layout="wide"
)


# Custom CSS for the dashboard
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b, #020617);
    color: #ffffff;
}

h1 {
    text-align: center;
    color: #38bdf8 !important;
    font-size: 42px !important;
}

h2, h3 {
    color: #ffffff !important;
}

[data-testid="stMetricLabel"],
[data-testid="stMetricLabel"] p {
    color: #cbd5e1 !important;
    opacity: 1 !important;
}

[data-testid="stMetricValue"],
[data-testid="stMetricValue"] div {
    color: #ffffff !important;
    opacity: 1 !important;
}

.stButton > button {
    background: linear-gradient(90deg, #3b82f6, #06b6d4);
    color: white !important;
    border: none;
    border-radius: 10px;
    height: 3em;
    width: 200px;
    font-size: 16px;
}

.stTextInput label {
    color: #ffffff !important;
}

.stTextInput input {
    color: #ffffff !important;
}

[data-testid="stSidebar"] {
    background-color: #242631;
}

[data-testid="stSidebar"] * {
    color: #ffffff;
}
</style>
""", unsafe_allow_html=True)


# Sidebar
with st.sidebar:
    st.title("📊 Dashboard")
    st.write("LeetCode AI Performance Analyzer")
    st.write("Analyze coding skills and contest performance.")


# Main page
st.markdown(
    "<h1>🚀 AI LeetCode Performance Analyzer</h1>",
    unsafe_allow_html=True
)

username = st.text_input("Enter your LeetCode Username")


# Store analysis results between Streamlit reruns
if "stats" not in st.session_state:
    st.session_state.stats = None

if "analyzed_username" not in st.session_state:
    st.session_state.analyzed_username = ""


# Fetch and process the profile when the button is clicked
if st.button("Analyze Profile"):
    if not username.strip():
        st.session_state.stats = None
        st.warning("Please enter your LeetCode username.")

    else:
        with st.spinner("Analyzing profile..."):
            data = get_leetcode_data(username.strip())

            if data is None:
                st.session_state.stats = None
                st.error("User not found or profile is private.")

            else:
                stats = analyze_performance(data)

                if stats is None:
                    st.session_state.stats = None
                    st.error("Unable to analyze profile data.")

                else:
                    st.session_state.stats = stats
                    st.session_state.analyzed_username = username.strip()


# Display the dashboard after a successful analysis
if st.session_state.stats is not None:

    stats = st.session_state.stats

    total = stats["total"]
    easy = stats["easy"]
    medium = stats["medium"]
    hard = stats["hard"]

    rating = stats["rating"]
    ranking = stats["ranking"]
    contests = stats["contests"]

    # Calculate the skill score
    score = easy + (medium * 3) + (hard * 5)

    if score < 100:
        level = "Beginner 🟢"
    elif score < 300:
        level = "Intermediate 🟡"
    else:
        level = "Advanced 🔴"

    st.success(
        f"Profile analyzed successfully! Username: "
        f"{st.session_state.analyzed_username}"
    )

    st.markdown("---")

    # Coding statistics
    st.subheader("📊 Coding Statistics")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total", total)
    col2.metric("Easy", easy)
    col3.metric("Medium", medium)
    col4.metric("Hard", hard)

    # Contest performance
    st.subheader("🏆 Contest Performance")

    col5, col6, col7 = st.columns(3)

    col5.metric("Contest Rating", int(rating))
    col6.metric("Global Ranking", ranking)
    col7.metric("Contests Attended", contests)

    # Skill score
    st.subheader("🏆 Skill Score")

    col8, col9 = st.columns(2)

    col8.metric("Score", score)
    col9.metric("Level", level)

    # Progress towards the next skill level
    st.subheader("📈 Skill Progress")

    progress = min(score / 300, 1.0)
    st.progress(progress)

    # Weekly practice target
    st.subheader("🎯 Weekly Coding Target")

    if score < 100:
        st.info("Solve 20 Easy problems this week.")
    elif score < 300:
        st.info("Solve 15 Medium + 5 Easy problems.")
    else:
        st.success("Solve 10 Hard + 10 Medium problems.")

    # Coding consistency
    st.subheader("🔥 Coding Consistency")

    if total < 50:
        st.write("Begin building a daily coding habit (3 problems/day).")
    elif total < 200:
        st.write("Good consistency! Try solving 4–5 problems/day.")
    else:
        st.success("Excellent consistency. Maintain 5+ problems/day.")

    # Performance feedback
    st.subheader("🤖 AI Feedback")

    if easy < 30:
        st.info("Focus on solving more Easy problems to build fundamentals.")
    elif medium < 50:
        st.info("You have good basics. Start solving more Medium problems.")
    elif hard < 20:
        st.info("Try solving Hard problems to improve your skills.")
    else:
        st.success("Excellent performance!")

    # Problem difficulty distribution
    st.subheader("📊 Difficulty Breakdown")

    labels = ["Easy", "Medium", "Hard"]
    values = [easy, medium, hard]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct="%1.1f%%")
    ax.axis("equal")

    st.pyplot(fig)
    plt.close(fig)

    # Visualize the user's problem-solving distribution
    st.subheader("🧠 Skill Radar")

    radar_labels = [
        "Easy",
        "Medium",
        "Hard",
        "Problem Solving",
        "Consistency"
    ]

    radar_values = [
        easy,
        medium,
        hard,
        (easy + medium + hard) / 3,
        (min(easy, 50) + min(medium, 50)) / 2
    ]

    angles = np.linspace(
        0, 2 * np.pi, len(radar_labels), endpoint=False
    )

    radar_values = np.concatenate((radar_values, [radar_values[0]]))
    angles = np.concatenate((angles, [angles[0]]))

    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)

    ax.plot(angles, radar_values)
    ax.fill(angles, radar_values, alpha=0.25)
    ax.set_thetagrids(angles[:-1] * 180 / np.pi, radar_labels)

    st.pyplot(fig)
    plt.close(fig)

    # Suggested problems based on profile statistics
    st.subheader("🧠 Recommended Problems")

    problems = recommend_problems(stats)

    for problem in problems:
        st.markdown(
            f"✅ [{problem['title']}]({problem['link']})"
        )

    # Five-day practice schedule
    st.subheader("📅 5-Day Practice Plan")

    plan = generate_practice_plan()

    for day, tasks in plan.items():
        st.write(f"**{day}**")

        for task in tasks:
            st.markdown(
                f"- [{task['title']}]({task['link']})"
            )

    # Topics suggested for additional practice
    st.subheader("⚠️ Weak Topics")

    weak_topics = detect_weak_topics()

    for topic in weak_topics:
        st.warning(f"Practice more problems in **{topic}**")

    # Topic-based difficulty suggestions
    st.subheader("🧠 Topic Difficulty Predictor")

    topic = st.text_input(
        "Enter a topic (Array, DP, Graph, Tree)",
        key="topic_input"
    )

    if topic:
        selected_topic = topic.strip().lower()

        if selected_topic in ["array", "string"]:
            st.success("Recommended Difficulty: Easy → Medium")

        elif selected_topic in ["dp", "dynamic programming", "graph"]:
            st.warning("Recommended Difficulty: Medium → Hard")

        elif selected_topic in ["tree", "binary tree"]:
            st.info("Recommended Difficulty: Medium")

        else:
            st.write("Practice mixed difficulty problems.")

    st.markdown("---")
    st.success("✅ Profile Analysis Completed")
