# load env
import os
from dotenv import load_dotenv
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Google AI API
import google.generativeai as genai
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def generate_comment(article) -> str:
    instruction = "다음 게시물에 적절한 댓글을 작성하세요. 당신은 KAIST 교내 커뮤니티 Ara의 사용자입니다. 인터넷 예절을 지키되 자연스러운 댓글을 작성하세요. 닉네임을 제외하고 오직 댓글 내용만을 작성하세요."
    
    prompt = f'''{instruction}

  게시물: {article}

  댓글 내용: '''

    # print(prompt)

    parameters = genai.types.GenerationConfig(
        candidate_count=1,
        temperature=0.9,
        top_p=0.9,
        top_k=40,
    )

    response = model.generate_content(prompt, generation_config=parameters)
    try:
        return response.text
    except Exception as e:
        print(f'[ERROR] AI: {e}')
        print(response.prompt_feedback)
        return None

import ara
def write_comment(article) -> bool:
    if article is None:
        print('[ERROR] Article not found.\n')
        return False
    
    id = int(article['id'])
    if ara.is_already_commented(article):
        print(f'* Already commented on article {id}.\n')
        return False
    print(f'* Commenting on article {id}...')

    comment = generate_comment(ara.format_article(article))
    res = ara.post_comment(id, comment)
    if res:
        print(f'- Successfully commented on {id}: {comment}\n')
        return True
    else: return False
