import requests
from bs4 import BeautifulSoup
import datetime
import gevent.monkey


def get_cat_links(url):
    req = requests.get(url)
    src = req.text

    soup = BeautifulSoup(src, 'lxml')

    links = soup.find("div", id="tags").find_all("a")

    links_list = []
    for item in links:
        link = f'{url}{item.get("href")}'
        links_list.append(link)

    return links_list


gevent.monkey.patch_all()


def get_pages(url):
    req = requests.get(url)
    src = req.text

    soup = BeautifulSoup(src, 'lxml')
    title = soup.find('title').text

    with open(f'{title}.html', 'w', encoding='utf-8') as f:
        f.write(src)

    print(f'{title} is done')


def main():
    domain = 'http://127.0.0.1:8000'
    links = get_cat_links(domain)
    pages = [gevent.spawn(get_pages, u) for u in links]
    gevent.wait(pages)


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main()
    end_time = datetime.datetime.now() - start_time
    print('=' * 20)
    print(f'All Done in {end_time}')
