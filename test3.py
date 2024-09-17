import requests
import json

# 1. Wikipedia API의 검색 엔드포인트 URL
WIKIPEDIA_API_URL = "https://en.wikipedia.org/w/api.php"

# 2. 검색할 쿼리와 파라미터 설정
params = {
    'action': 'query',               # 'query' 모듈을 사용하여 데이터 요청
    'list': 'search',               # 검색 목록을 가져옴
    'srsearch': 'fairy tales',      # 검색어 설정
    'format': 'json',               # 결과 형식은 JSON
    'srlimit': 100                  # 검색 결과 제한 (최대 100개)
}

# 3. API 요청 보내기
response = requests.get(WIKIPEDIA_API_URL, params=params)

# 4. 응답 JSON 데이터 파싱
data = response.json()

# 5. 검색 결과에서 제목 추출
titles = [item['title'] for item in data['query']['search']]

# 6. JSON 파일로 저장
with open('wikidipia_fairy_tales_title.json', 'w', encoding='utf-8') as file:
    json.dump(titles, file, ensure_ascii=False, indent=4)

print("동화 제목 목록이 'wikidipia_fairy_tales_title.json' 파일로 저장되었습니다.")
