import requests
from bs4 import BeautifulSoup

def scrape_jiji(item_name):
    url = f'https://www.jiji.co.ke/search?query={item_name}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    results = []
    for item in soup.select('.b-list-advert__item'):
        name = item.select_one('.b-list-advert__item-title').text.strip()
        price = item.select_one('.b-list-advert__item-price').text.strip()
        link = item.select_one('.b-list-advert__item-title a')['href']
        
        results.append({
            'item_name': name,
            'website': 'Jiji',
            'price': price,
            'link': link
        })
    
    return results
