# main.py
import threading
import time
import atexit

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

def exit_handler():
    print(f'Terminated with {success_count} success(es) and {fail_count} failure(s), out of {success_count + fail_count} total.')


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
    atexit.register(exit_handler)

    article_id = 7212
    is_waiting = False

    threads = []
    while True:
        # article = ara.get_article(article_id, from_view="board", override_hidden="true")
        article = ara.get_article(article_id, from_view="all", override_hidden="true")
        
        if not is_waiting:
            # multithreading
            thread = threading.Thread(target=worker, args=(article,))
            threads.append(thread)
            thread.start()
        
        if article['side_articles']['after']:
            is_waiting = False
            article_id = int(article['side_articles']['after']['id'])
        else:
            if not is_waiting:
                print(f'* Waiting for a new article...')
                is_waiting = True
            time.sleep(10)
    
    # for thread in threads:
    #     thread.join()
