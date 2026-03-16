def recommend_problems(stats):

    easy = stats["easy"]
    medium = stats["medium"]
    hard = stats["hard"]

    problems = []

    # Beginner recommendations
    if easy < 30:
        problems.append({
            "title":"Two Sum",
            "link":"https://leetcode.com/problems/two-sum/"
        })

        problems.append({
            "title":"Valid Parentheses",
            "link":"https://leetcode.com/problems/valid-parentheses/"
        })

    # Intermediate recommendations
    if medium < 40:
        problems.append({
            "title":"Longest Substring Without Repeating Characters",
            "link":"https://leetcode.com/problems/longest-substring-without-repeating-characters/"
        })

        problems.append({
            "title":"3Sum",
            "link":"https://leetcode.com/problems/3sum/"
        })

    # Advanced recommendations
    if hard < 15:
        problems.append({
            "title":"Trapping Rain Water",
            "link":"https://leetcode.com/problems/trapping-rain-water/"
        })

        problems.append({
            "title":"Median of Two Sorted Arrays",
            "link":"https://leetcode.com/problems/median-of-two-sorted-arrays/"
        })

    return problems


def generate_practice_plan():

    plan = {
        "Day 1":[
            {"title":"Two Sum","link":"https://leetcode.com/problems/two-sum/"},
            {"title":"Best Time to Buy and Sell Stock","link":"https://leetcode.com/problems/best-time-to-buy-and-sell-stock/"}
        ],

        "Day 2":[
            {"title":"Valid Parentheses","link":"https://leetcode.com/problems/valid-parentheses/"},
            {"title":"Merge Two Sorted Lists","link":"https://leetcode.com/problems/merge-two-sorted-lists/"}
        ],

        "Day 3":[
            {"title":"3Sum","link":"https://leetcode.com/problems/3sum/"},
            {"title":"Container With Most Water","link":"https://leetcode.com/problems/container-with-most-water/"}
        ],

        "Day 4":[
            {"title":"Longest Palindromic Substring","link":"https://leetcode.com/problems/longest-palindromic-substring/"},
            {"title":"Binary Tree Level Order Traversal","link":"https://leetcode.com/problems/binary-tree-level-order-traversal/"}
        ],

        "Day 5":[
            {"title":"Trapping Rain Water","link":"https://leetcode.com/problems/trapping-rain-water/"},
            {"title":"Word Ladder","link":"https://leetcode.com/problems/word-ladder/"}
        ]
    }

    return plan


def detect_weak_topics():

    topics = [
        "Dynamic Programming",
        "Graphs",
        "Binary Trees",
        "Greedy Algorithms",
        "Backtracking"
    ]

    return topics