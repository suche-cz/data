"""
pomocí re extrahování dat z 
https://www.csfd.cz/zebricky/filmy/nejlepsi/
"""

import requests, re
# python -m pip install requests

base_url = 'https://www.csfd.cz/zebricky/filmy/nejlepsi/'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 OPR/110.0.0.0'

article_pattern = r'<span class="film-title-user">(.*?)</span>.*?<a.*?>(.*?)</a>.*?<span class="info">(\(\d{4}\))</span>'
article_pattern += r'.*?<p class="film-origins-genres"><span class="info">(.*?)</span>'
article_pattern += r'.*?<p class="film-creators">(.*?)</p>'
article_pattern += r'.*?<p class="film-creators">(.*?)</p>'


article_regex = re.compile(article_pattern, re.DOTALL)

# document.querySelectorAll('article[id][class="article article-poster-60"]')


def gen_film_data(url):
    response = requests.get(url, headers={'User-Agent': user_agent})
    data = article_regex.findall(response.text)

    for poradi, nazev, rok, zanr, rezie, herci in data:
        yield {
            'poradi': poradi.strip(),
            'nazev': nazev.strip(),
            'rok': rok.strip(),
            'zanr': zanr,
            'rezie': rezie,
            'herci': herci,
        }

for item in gen_film_data(base_url):
    print(item)
