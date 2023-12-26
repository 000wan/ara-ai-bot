# main.py
import threading

success_count = 0
fail_count = 0
def worker(article):
    import ai
    global success_count
    global fail_count

    res = ai.write_comment(article)
    success_count += res
    fail_count += not res
    return


if __name__ == "__main__":
    print('''
 █████╗ ██████╗  █████╗      █████╗ ██╗    ██████╗  ██████╗ ████████╗
██╔══██╗██╔══██╗██╔══██╗    ██╔══██╗██║    ██╔══██╗██╔═══██╗╚══██╔══╝
███████║██████╔╝███████║    ███████║██║    ██████╔╝██║   ██║   ██║   
██╔══██║██╔══██╗██╔══██║    ██╔══██║██║    ██╔══██╗██║   ██║   ██║   
██║  ██║██║  ██║██║  ██║    ██║  ██║██║    ██████╔╝╚██████╔╝   ██║   
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝    ╚═════╝  ╚═════╝    ╚═╝   
    \n''')

    import ara

    article_id = 7199

    threads = []
    while True:
        # article = ara.get_article(article_id, from_view="board", override_hidden="true")
        article = ara.get_article(article_id, from_view="all", override_hidden="true")
        
        # multithreading
        thread = threading.Thread(target=worker, args=(article,))
        threads.append(thread)
        thread.start()

        if article['side_articles']['after']:
            article_id = int(article['side_articles']['after']['id'])
        else:
            break
    
    for thread in threads:
        thread.join()
    print(f'Terminated with {success_count} success(es) and {fail_count} failure(s), out of {success_count + fail_count} total.')
