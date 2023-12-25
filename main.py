# main.py
if __name__ == "__main__":
    import ara
    import ai

    article_id = 5552

    success_count = 0
    fail_count = 0
    while article_id:
        article = ara.get_article(article_id, from_view="board")
        res = ai.write_comment(article)
        success_count += res
        fail_count += not res

        try:
            article_id = article['side_articles']['after']['id']
        except:
            article_id = None
            break

    print(f'Terminated with {success_count} success(es) and {fail_count} failure(s).')