import subprocess
import re
import json
from datetime import datetime, timedelta

def extract_programmers_problems_from_commits(days=30):
    since = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
    result = subprocess.run(
        ['git', 'log', '--since=' + since, '--pretty=format:%s'],
        stdout=subprocess.PIPE,
        text=True
    )

    messages = result.stdout.split('\n')
    solved = []

    pattern = re.compile(r'프로그래머스.*- (.+)')

    for msg in messages:
        match = pattern.search(msg)
        if match:
            solved.append(match.group(1))

    return list(set(solved))  # 중복 제거

# 테스트
if __name__ == "__main__":
    problems = extract_programmers_problems_from_commits()
    print("✅ 푼 문제 리스트:")
    print(json.dumps(problems, ensure_ascii=False, indent=2))

# 푼 문제 리스트 저장
with open("solved_problems.json", "w", encoding="utf-8") as f:
    json.dump(problems, f, ensure_ascii=False, indent=2)
