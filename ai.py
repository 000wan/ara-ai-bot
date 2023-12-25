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
    instruction = "다음 게시물에 적절한 댓글을 작성하세요. 당신은 KAIST 교내 커뮤니티 Ara의 사용자입니다. 인터넷 예절을 지키되 자연스러운 댓글을 작성하세요."
    
    prompt = f'''{instruction}

    게시물: {article}

    댓글 내용: '''

    parameters = genai.types.GenerationConfig(
        candidate_count=1,
        temperature=0.9,
        top_p=0.9,
        top_k=40,
    )

    return model.generate_content(prompt, generation_config=parameters).text

def write_comment(article) -> bool:
    if article is None:
        print('[ERROR] Article not found.')
        return False

    import ara
    id = article['id']
    print(f'* Commenting on article {id}...')

    comment = generate_comment(article)
    res = ara.post_comment(id, comment)
    if res:
        print(f'- Successfully commented: {comment}\n')
        return True
    else: return False