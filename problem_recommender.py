import requests
from bs4 import BeautifulSoup
import json
import random
import unicodedata
import time

def normalize(text):
    return unicodedata.normalize("NFC", text).strip()

def get_solved_problems():
    try:
        with open("/mnt/data/solved_problems.json", "r", encoding="utf-8") as f:
            return [normalize(title) for title in json.load(f)]
    except FileNotFoundError:
        return []

def get_programmers_lv0_problems(pages=7):
    base_url = "https://school.programmers.co.kr"
    problems = []

    for page in range(1, pages + 1):
        url = f"{base_url}/learn/challenges/training?order=acceptance_desc&page={page}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        cards = soup.select("div.css-1n6g4vv a")

        for card in cards:
            title_tag = card.select_one("span")
            if not title_tag:
                continue
            title = title_tag.get_text(strip=True)
            link = base_url + card.get("href")
            problems.append({"title": title, "url": link})

        time.sleep(0.5)

    return problems

def recommend_unsolved_problem():
    all_problems = get_programmers_lv0_problems()
    solved = get_solved_problems()
    unsolved = [p for p in all_problems if normalize(p['title']) not in solved]

    print(f"🔍 총 문제 수: {len(all_problems)}")
    print(f"✅ 푼 문제 수: {len(solved)}")
    print(f"❓ 추천 가능한 미풀이 수: {len(unsolved)}")

    if not unsolved:
        return "모든 문제를 다 푼 것 같아요! 🎉"

    pick = random.choice(unsolved)
    return f"오늘의 추천 문제 👉 [{pick['title']}]({pick['url']})"

recommend_unsolved_problem()
