import requests
from bs4 import BeautifulSoup
import json
from concurrent.futures import ThreadPoolExecutor

# 기본 페이지 URL 설정
base_url = 'https://fairytalez.com/user-tales/'

# 웹 크롤링 시 필요한 User-Agent 설정
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:110.0) Gecko/20100101 Firefox/110.0'
}

# 동화 페이지에서 제목과 본문을 추출하는 함수
def fetch_story(url):
    try:
        # 주어진 URL로 HTTP GET 요청을 보냅니다.
        response = requests.get(url, headers=headers)
        print(f"Fetching {url} - Status Code: {response.status_code}")  # 상태 코드 출력

        # 상태 코드가 200(성공)이면 아래 코드 실행
        if response.status_code == 200:
            # HTML 내용을 BeautifulSoup을 통해 파싱
            soup = BeautifulSoup(response.content, 'html.parser')

            # 제목을 담고 있는 <h1> 태그(class='title entry-title')를 찾습니다.
            title_elem = soup.find('h1', class_='title entry-title')
            title = title_elem.text.strip() if title_elem else "No Title Found"

            # 본문을 담고 있는 <section> 태그(class='entry user-tale')를 찾습니다.
            content_section = soup.find('section', class_='entry user-tale')
            if content_section:
                paragraphs = [elem.get_text(strip=True) for elem in content_section.find_all(['p', 'div']) if elem.get_text(strip=True)]
                content = "\n".join(paragraphs)
            else:
                content = "No content found."

            return {'title': title, 'content': content, 'url': url}
        else:
            return {'title': "Failed to fetch", 'content': "", 'url': url}
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return {'title': "Error occurred", 'content': "", 'url': url}

# 메인 함수: 동화 링크를 수집하고 각 링크의 데이터를 가져옵니다.
def main():
    try:
        # 기본 페이지에 GET 요청을 보냅니다.
        response = requests.get(base_url, headers=headers)
        print(f"Base page status code: {response.status_code}")  # 상태 코드 확인

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # <a> 태그에서 'https://fairytalez.com/user-tales/'로 시작하는 링크만 추출
            story_links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith('https://fairytalez.com/user-tales/')]

            # 추출된 링크 확인
            print(f"Collected {len(story_links)} story links.")
            
            if not story_links:
                print("No story links found.")
                return

            stories_data = []

            # 병렬로 크롤링 작업을 수행(max_workers=5)
            with ThreadPoolExecutor(max_workers=5) as executor:
                results = executor.map(fetch_story, story_links)

                for result in results:
                    stories_data.append(result)

            # 수집한 데이터를 JSON 파일로 저장
            with open('user_tales_data.json', 'w', encoding='utf-8') as f:
                json.dump(stories_data, f, ensure_ascii=False, indent=4)

            print("Data successfully saved to user_tales_data.json")
        else:
            print("Failed to fetch the base page.")

    except Exception as e:
        print(f"Error during main execution: {e}")

# 이 스크립트를 직접 실행할 때만 main 함수를 호출
if __name__ == "__main__":
    main()
