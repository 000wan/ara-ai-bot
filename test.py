def test_comment(article_id):
    import ara
    import ai

    article = ara.get_article(article_id, from_view="board", override_hidden="true")
    res = ai.generate_comment(article)
    print("    " + res)

# test.py
if __name__ == "__main__":
    test_comment(5563)
