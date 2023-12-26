# load env
import os
from dotenv import load_dotenv
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Google AI API
import google.generativeai as genai
genai.configure(api_key=GOOGLE_API_KEY)

from PIL import Image
import requests
from io import BytesIO

def generate_comment(article) -> str:
    instruction = "다음 게시물에 적절한 댓글을 작성하세요. 당신은 KAIST 교내 커뮤니티 Ara의 사용자입니다. 인터넷 예절을 지키되 자연스러운 댓글을 작성하세요. 닉네임을 제외하고 오직 댓글 내용만을 작성하세요."
    
    content = ara.format_article(article)
    prompt = f'''{instruction}

    {content}
    - 나의 댓글: '''

    # print(prompt)
    
    # Use Gemini Pro Vision if there are attachments
    attachments = list(filter(lambda attachment: attachment['mimetype'].startswith('image'), article['attachments']))
    if attachments:
        model = genai.GenerativeModel('gemini-pro-vision')
        images = []
        for attachment in attachments:
            response = requests.get(attachment['file'])
            images.append(Image.open(BytesIO(response.content)))
        #     images[-1].show()
        # print(images)

        parameters = genai.types.GenerationConfig(
            candidate_count=1,
            temperature=0.4,
            top_p=0.9,
            top_k=40,
        )
        response = model.generate_content([prompt] + images, generation_config=parameters)
    else:
        model = genai.GenerativeModel('gemini-pro')
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
        print(f'[ERROR] AI: {e}\n')
        print(response.prompt_feedback)
        return None

import ara
def write_comment(article) -> bool:
    if article is None:
        print('[ERROR] Article not found.\n')
        return False
    
    id = int(article['id'])
    if ara.is_already_commented(article):
        print(f'* Already commented on article {id}.')
        return False
    print(f'* Commenting on article {id}...')

    try:
        comment = generate_comment(article)
        res = ara.post_comment(id, comment)
    except Exception as e:
        print(f'[ERROR] AI: {e}\n')
        return False
    
    if res:
        print(f'- Successfully commented on {id}: {comment}\n')
        return True
    else: return False
