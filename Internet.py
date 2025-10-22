import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import mimetypes

USER_AGENT = "WETS/1.0 Python-requests"

def http_get(url, headers=None, params=None):
    hdrs = {"User-Agent": USER_AGENT}
    if headers:
        hdrs.update(headers)
    r = requests.get(url, headers=hdrs, params=params)
    r.raise_for_status()
    return r

def scrape_page(url):
    r = http_get(url)
    soup = BeautifulSoup(r.content, "lxml")
    title = soup.title.string.strip() if soup.title else ""
    for s in soup(["script","style","noscript"]):
        s.decompose()
    text = soup.get_text(separator="\n", strip=True)
    links = [urljoin(url, a.get("href")) for a in soup.find_all("a", href=True)]
    return {"url": url, "title": title, "text": text, "links": links}

def search_web_googlelike(query):
    # DuckDuckGo Instant Answer
    params = {"q": query, "format": "json", "no_redirect": 1, "no_html": 1, "skip_disambig": 1}
    url = "https://api.duckduckgo.com/"
    r = http_get(url, params=params)
    return r.json()

def download_file(url, dest_folder="downloads"):
    os.makedirs(dest_folder, exist_ok=True)
    r = http_get(url, headers={"User-Agent": USER_AGENT})
    filename = os.path.basename(url.split("?")[0]) or "download"
    if "." not in filename:
        ext = mimetypes.guess_extension(r.headers.get("content-type","").split(";")[0]) or ""
        filename += ext
    path = os.path.join(dest_folder, filename)
    with open(path, "wb") as f:
        f.write(r.content)
    return path

def fetch_json_api(url):
    r = http_get(url)
    try:
        return r.json()
    except:
        return {"status":"not_json","text": r.text}
  
