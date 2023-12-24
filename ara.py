# load env
import os
from urllib import response
from dotenv import load_dotenv
load_dotenv()

base_URL = os.getenv("ARA_API_HOST")
api_session = os.getenv("ARA_API_SESSION")
# api_token = os.getenv("ARA_API_TOKEN")

# ARA API
import requests
import json

header = {
    # "x-csrftoken": api_token,
}
cookie = { "sessionid": api_session }


def get_article(article_id: int):
    """Get article by id"""
    response = requests.get(f'{base_URL}/api/articles/{article_id}', headers=header, cookies=cookie)
    
    try: response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f'[ERROR] GET: {e}')
        return None
    return response.json()


def post_comment(article_id: int, content: str):
    """Post comment to article"""
    data = {
        "parent_article": article_id,
        "content": content,
        "name_type": 1,
        "attachment": None,
    }
    response = requests.post(f'{base_URL}/api/comments/', headers=header, cookies=cookie, data=data)
    
    try: response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f'[ERROR] POST: {e}')
        return None
    return response.json()

