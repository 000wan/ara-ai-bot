def test_comment(article_id):
    import ara
    import ai

    article = ara.get_article(article_id, from_view="board", override_hidden="true")
    print(ara.format_article(article))
    res = ai.generate_comment(article)
    print("\n- Generated Comment: " + res)

# test.py
if __name__ == "__main__":
    import sys
    try:
        article_id = int(sys.argv[1])
    except IndexError:
        print('Usage: python test.py <article_id>')
        print('[ERROR] Too few arguments.')
        exit(1)
    except ValueError:
        print('Usage: python test.py <article_id>')
        print('[ERROR] article_id must be an integer.')
        exit(1)
    
    test_comment(article_id)
