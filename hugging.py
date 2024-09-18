import os
from transformers import AutoTokenizer, AutoModelForCausalLM

# Hugging Face API를 사용해 LLaMA 3.18b 모델을 불러와 텍스트 생성 함수
def run(prompt):
    print("모델 로딩 중...")
    tokenizer = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3.1-8B")  # LLaMA 3.18b 모델
    model = AutoModelForCausalLM.from_pretrained("meta-llama/Meta-Llama-3.1-8B")  # LLaMA 3.18b 모델
    
    # 입력된 프롬프트가 최대 길이인 1024 토큰을 넘지 않도록 자름
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

    print("모델에서 응답 생성 중...")
    outputs = model.generate(**inputs, max_new_tokens=100)  # 최대 100개의 새 토큰 생성

    print("응답 디코딩 중...")
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return response

# 파일 경로 설정 및 텍스트 읽기 (UTF-8 인코딩 지정)
current_dir = os.path.dirname(os.path.abspath(__file__))  # 현재 파일의 디렉토리 경로
text_dir = os.path.join(current_dir)
file_path = os.path.join(text_dir, "test.json")

# 텍스트 파일에서 내용을 읽어옴
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# 사용자에게 프롬프트 입력을 받음
user_prompt = input("Prompt를 입력하세요: ")

# 사용자 입력 프롬프트와 텍스트 파일의 내용을 결합하여 최종 프롬프트 생성
combined_prompt = f"{user_prompt}: {text}"

# 결합된 프롬프트를 LLaMA 모델에 전달하여 응답 생성
response = run(combined_prompt)

# 응답을 파일로 저장할 경로 설정 (UTF-8 인코딩 지정)
output_file_path = os.path.join(text_dir, "response.txt")

# 생성된 응답을 텍스트 파일로 저장
with open(output_file_path, "w", encoding="utf-8") as output_file:
    output_file.write(response)  # 응답 텍스트 저장

print(f"응답이 '{output_file_path}' 파일에 저장되었습니다.")
