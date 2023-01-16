import requests
import warnings
from furl import furl
from bs4 import BeautifulSoup
from tldextract import extract
from urllib.parse import urljoin

warnings.filterwarnings("ignore")
crawled_urls = set()
user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
headers = {"User-Agent": user_agent}

def remove_fragment(url:str) -> str:
	"""
	Remove the fragment from the URL
		
		:param url: URL
		
		:return: URL without fragment
	"""
	
	if "#" in url:
		return url.split("#")[0]
	
	return url

def crawl_urls(base_url:str, main_domain:str, visited:set, max_depth, depth=1) -> set:
	"""
	Crawl the URLs of the website
		
		:param base_url: Base URL
		:param path: Path of the URL
		:param main_domain: Main domain of the website (e.g. example.com)
		:param visited: Visited URLs set, to avoid duplicate crawling
		:param max_depth: Maximum depth of the crawling
		:param depth: Current depth of the crawling
		
		:return: Set of Crawled URLs
	"""

	if depth <= max_depth:

		try:

			session_object = requests.Session()

			if base_url.startswith("http"):
				req = session_object.get(base_url, headers=headers, timeout=1)
			else:
				pass

			if req.status_code == 200:

				# Parse the HTML content
				soup = BeautifulSoup(req.text, "lxml")

				# Get all the links of the page
				for link in soup.find_all(["base", "link", "a", "area"]):

					href = link.get("href")
					
					if href:
					
						href = remove_fragment(href)

						# check if the URL is already visited or not
						if href not in visited and "/img/" not in href:

							visited.add(href)

							# handle absolute urls
							if href.startswith("http") and main_domain == extract(furl(href).host).registered_domain:
								if href.endswith("/"):
									href = href[0:-1]
								crawl_urls(href, main_domain, visited, max_depth, depth + 1)
								print(href)
								crawled_urls.add(href)

							# handle relative urls, such as "/about"
							elif href.startswith("/") and len(href) > 1 and not href.startswith("//"):
								url = urljoin(base_url, href)
								crawl_urls(url, main_domain, visited, max_depth, depth + 1)
								print(url)
								crawled_urls.add(url)

							# handle relative urls without "/", excluding cases such as "file://", "android-app://", "ios-app://", etc.
							elif not href.startswith("http") and href[0].isalpha() and not href.startswith("//") and not href.split("//")[0][-1]==":":
								url = urljoin(base_url, href)
								crawl_urls(url, main_domain, visited, max_depth, depth + 1)
								print(url)
								crawled_urls.add(url)

							# handle // urls, such as "//www.example.com"
							elif href.startswith("//") and main_domain == extract(furl(href).host).registered_domain:
								url = "https:" + href
								crawl_urls(url, main_domain, visited, max_depth, depth + 1)
								print(url)
								crawled_urls.add(url)

		except Exception:
			pass

	return crawled_urls