from crawl_bot import Crawl_bot
from run import *
from file_manage import *
from queue import Queue
import threading
from get_domains import *

GET_DOMAIN = get_domain_name(BASE_URL)
data_crawled = FOLDER_NAME + '/crawled.txt'
data_in_queue = FOLDER_NAME + '/queue.txt'
thread_count =10
queue = Queue()

Crawl_bot(FOLDER_NAME, BASE_URL, GET_DOMAIN)

def do_job():                     # Get the job done
    while True:
        url = queue.get()
        Crawl_bot.crawl_page(threading.current_thread().name, url)
        queue.task_done()

def queue_jobs():                 # Define each queued link as a new job
    for url_link in convert_to_set(data_in_queue):
        queue.put(url_link)
    queue.join()
    initiate_bot()

def get_links_to_queue():          # Also used to create threads to work
    for _ in range(thread_count):
        thread = threading.Thread(target=do_job)
        thread.daemon = True
        thread.start()

def initiate_bot():               # Does the crawling job
    links_in_queue = convert_to_set(data_in_queue)
    if len(links_in_queue) > 0:
        print(str(len(links_in_queue)) + ' queued links')
        queue_jobs()

get_links_to_queue()
initiate_bot()

# 2, 4, 5