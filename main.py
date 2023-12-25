# main.py
if __name__ == "__main__":
    import ara
    import ai

    article_id = 5526

    success_count = 0
    fail_count = 0
    while True:
        article = ara.get_article(article_id, from_view="board", override_hidden="true")
        res = ai.write_comment(article)
        success_count += res
        fail_count += not res

        try:
            article_id = int(article['side_articles']['after']['id'])
        except:
            break

    print(f'Terminated with {success_count} success(es) and {fail_count} failure(s), out of {success_count + fail_count} total.')
