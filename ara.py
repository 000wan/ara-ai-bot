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


def get_article(article_id: int, **kwargs):
    """Get article by id"""
    query = query_builder(**kwargs)
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


# Formatting functions
def format_article(article) -> str:
    """Format article to string"""
    import html2text

    title = article['title']
    content = html2text.html2text(article['content'])
    if article['parent_topic']:
        title = f'[{article["parent_topic"]["ko_name"]}] {title}'
    comments = format_comments(article['comments'], "    -")

    res = f'''
    게시판: {article['parent_board']['ko_name']}
    제목: {title}
    작성자: {article['created_by']['profile']['nickname']}

    본문: {content}

    댓글 {article['comment_count']}개:\n'''
    res += comments

    return res

def format_comments(comments, prefix: str) -> str:
    """Format comments to string"""
    comments = filter(lambda comment: not comment['is_hidden'], comments)
    res = ""
    for comment in comments:
        res += f'{prefix} {comment["created_by"]["profile"]["nickname"]}: {comment["content"]}\n'
        if "comments" in comment.keys():
            res += format_comments(comment["comments"], "  " + prefix)
    return res


# Helper functions
def query_builder(**kwargs) -> str:
    """Build query string for GET requests"""
    if not kwargs: return ''
    return '?' + '&'.join(f'{key}={value}' for key, value in kwargs.items())

def is_already_commented(article) -> bool:
    """Check if article is already commented by myself"""
    return any(comment['is_mine'] and not comment['is_hidden']
        for comment in article['comments'])
