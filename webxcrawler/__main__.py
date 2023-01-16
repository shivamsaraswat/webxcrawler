import crawler
import argparse
import threading
from furl import furl
from typing import Tuple
from termcolor import colored
from tldextract import extract

def logo():
    print(colored("""
██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗██████╗  █████╗ ██╗    ██╗██╗     ███████╗██████╗ 
██║    ██║██╔════╝██╔══██╗╚██╗██╔╝██╔════╝██╔══██╗██╔══██╗██║    ██║██║     ██╔════╝██╔══██╗
██║ █╗ ██║█████╗  ██████╔╝ ╚███╔╝ ██║     ██████╔╝███████║██║ █╗ ██║██║     █████╗  ██████╔╝
██║███╗██║██╔══╝  ██╔══██╗ ██╔██╗ ██║     ██╔══██╗██╔══██║██║███╗██║██║     ██╔══╝  ██╔══██╗
╚███╔███╔╝███████╗██████╔╝██╔╝ ██╗╚██████╗██║  ██║██║  ██║╚███╔███╔╝███████╗███████╗██║  ██║
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝  ╚═╝"""))
    print(colored('					   Coded with Love by Shivam Saraswat (@cybersapien)\n', 'green', attrs=['bold']))

def parse_arguments() -> Tuple[str, int, int, str]:
    parser = argparse.ArgumentParser(prog='python3 webxcrawler', description ="WebXCrawler is a fast static crawler to crawl a website and get all the links.", epilog="Example: python3 webxcrawler -u https://toscrape.com -d 2 -t 10 -o /tmp/toscrape")
    parser.add_argument("-u", "--url", type=str, required=True, help="URL to crawl")
    parser.add_argument("-d", "--depth", type=int, metavar='int', default=2, help="maximum depth to crawl (default 2)")
    parser.add_argument("-t", "--threads", type=int, metavar='int', default=2, help="number of threads to use (default 2)")
    parser.add_argument("-o", "--output", type=argparse.FileType('w'), metavar='file_path', action='store', dest='output', help="file to write output to")

    args = parser.parse_args()
    url = args.url
    max_depth = args.depth
    num_of_threads = args.threads
    output_file = args.output

    return url, max_depth, num_of_threads, output_file

if __name__ == '__main__':

    logo() # Print the logo

    # Parse the arguments
    url, max_depth, num_of_threads, output_file = parse_arguments()

    # Get the main domain of the URL, e.g. https://www.google.com/ -> google.com
    main_domain = extract(furl(url).host).registered_domain

    # initialize variables
    crawled_urls = set()
    visited = set()
    visited.add(url)

    # threading
    threads = list()
    for num in range(num_of_threads):
        t = threading.Thread(target=crawler.crawl_urls, args=(url, main_domain, visited, max_depth))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # Get the crawled URLs and sort them
    crawled_urls = sorted(crawler.crawled_urls)

    for url in crawled_urls:

        # Write to file if output file is specified
        if output_file:
            with open(output_file.name, 'a') as file:
                file.write(f"{url}\n")

    print(f"\nTotal Crawled URLs: {len(crawled_urls)}")