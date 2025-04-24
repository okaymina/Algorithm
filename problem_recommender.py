import requests
from bs4 import BeautifulSoup
import json
import random
import os
import unicodedata

# 문자열 정규화 함수
def normalize(text):
    return unicodedata.normalize("NFC", text).strip()

# 푼 문제 리스트 불러오기
def get_solved_problems():
    if not os.path.exists("solved_problems.json"):
        return []
    with open("solved_problems.json", "r", encoding="utf-8") as f:
        return json.load(f)

# 프로그래머스 Lv.0 문제 크롤링
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
        link = "https://school.programmers.co
