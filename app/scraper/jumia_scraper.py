import requests
from bs4 import BeautifulSoup

def scrape_jumia(item_name):
    url = f'https://www.jumia.co.ke/catalog/?q={item_name}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    results = []
    for item in soup.select('.sku'):
        name = item.select_one('.name').text.strip()
        price = item.select_one('.price').text.strip()
        link = item.select_one('a.link')['href']
        
        results.append({
            'item_name': name,
            'website': 'Jumia',
            'price': price,
            'link': f'https://www.jumia.co.ke{link}'
        })
    
    return results
