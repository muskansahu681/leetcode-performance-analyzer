import requests

def get_leetcode_data(username):

    url = "https://leetcode.com/graphql"

    query = """
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            submitStats {
                acSubmissionNum {
                    difficulty
                    count
                }
            }
        }
        userContestRanking(username: $username) {
            rating
            globalRanking
            attendedContestsCount
            topPercentage
        }
    }
    """

    variables = {"username": username}

    response = requests.post(url, json={"query": query, "variables": variables})
    data = response.json()

    if data["data"]["matchedUser"] is None:
        return None

    return data


def analyze_performance(data):

    stats = data["data"]["matchedUser"]["submitStats"]["acSubmissionNum"]

    contest = data["data"]["userContestRanking"]

    result = {
        "total": stats[0]["count"],
        "easy": stats[1]["count"],
        "medium": stats[2]["count"],
        "hard": stats[3]["count"],
        "rating": contest["rating"] if contest else 0,
        "ranking": contest["globalRanking"] if contest else 0,
        "contests": contest["attendedContestsCount"] if contest else 0
    }

    return result