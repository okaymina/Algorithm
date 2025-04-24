import requests
from bs4 import BeautifulSoup
import json
import random
import os

def get_solved_problems():
    if not os.path.exists("solved_problems.json"):
        return []
    with open("solved_problems.json", "r", encoding="utf-8") as f:
        return json.load(f)

def get_programmers_lv0_problems():
    url = "https://school.programmers.co.kr/learn/challenges?order=recent&levels=0"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    problems = []

    cards = soup.select(".challenge-card")
    for card in cards:
        title_tag = card.select_one(".challenge-card__title")
        if not title_tag:
            continue
        title = title_tag.get_text(strip=True)
        link = "https://school.programmers.co.kr" + card.get("href")
        problems.append({"title": title, "url": link})

    return problems

def recommend_unsolved_problem():
    all_problems = get_programmers_lv0_problems()
    solved = get_solved_problems()

    unsolved = [p for p in all_problems if p['title'] not in solved]

    if not unsolved:
        return "모든 문제를 다 푼 것 같아요! 🎉"

    pick = random.choice(unsolved)
    return f"오늘의 추천 문제 👉 [{pick['title']}]({pick['url']})"

# 테스트 실행
if __name__ == "__main__":
    print(recommend_unsolved_problem())
