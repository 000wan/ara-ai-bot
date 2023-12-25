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


def get_article(article_id: int, from_view: str = ""):
    """Get article by id"""
    query = f'?from_view={from_view}' if from_view else ''
    response = requests.get(f'{base_URL}/api/articles/{article_id}/{query}', headers=header, cookies=cookie)
    
    try: response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f'[ERROR] GET: {e}\n')
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
        print(f'[ERROR] POST: {e}\n')
        return None
    return response.json()

