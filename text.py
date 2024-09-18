from transformers import pipeline

# 감정 분석 및 구분을 위한 모델 로딩
nlp = pipeline("text-classification")

def split_text(text):
    # 간단한 기준으로 서론, 본론, 결론을 구분 (이 방법은 예시로 실제 구현에서는 더 정교한 로직이 필요)
    # 예를 들어, '서론', '본론', '결론'이라는 단어를 기준으로 나누기
    sections = text.split('\n\n')  # 예시로 두 개의 줄바꿈 기준
    return {
        "introduction": sections[0],
        "body": sections[1],
        "conclusion": sections[2] if len(sections) > 2 else ""
    }

text = """
2090, Year of Confiscated Minds by Cice Rivera
Harmful bacteria has destroyed the world as we know it. The year is 2090. India is a deserted place ruled by confiscated minds. Once glorious, the Taj Mahal is now iced over.

Stable private detective, Lady Sallina Gibul is humanity’s only hope. Sallina finds the courage to start a secret revolutionary organization called The New Federation. The fight is jeopardised when Sallina is tricked by sinister police officer, Sir Gregyn McCallim, and injures her hand.

Armed with oxygen tanks and diligence, The New Federation try their best to save mankind, but can they defeat ruthless confiscated minds and restore the Taj Mahal to its former glory?
"""

sections = split_text(text)
print("Introduction:", sections["introduction"])
print("Body:", sections["body"])
print("Conclusion:", sections["conclusion"])