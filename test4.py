import requests
import json

# Wikisource API URL
WIKISOURCE_API_URL = "https://en.wikisource.org/w/api.php"

# API 요청 파라미터
params = {
    'action': 'query',
    'titles': 'Alice\'s Adventures in Wonderland',
    'prop': 'revisions',
    'rvprop': 'content',
    'format': 'json'
}

# API 요청
response = requests.get(WIKISOURCE_API_URL, params=params)

# JSON 응답 데이터 파싱
data = response.json()

# 데이터 예시
print(json.dumps(data, indent=4, ensure_ascii=False))