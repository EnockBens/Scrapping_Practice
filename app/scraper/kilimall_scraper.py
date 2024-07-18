import requests
from bs4 import BeautifulSoup

def scrape_kilimall(item):
    url = f"https://www.kilimall.co.ke/new/commoditysearch?c=0&k={item}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return []
    
    
    print(response.text)  
    
    soup = BeautifulSoup(response.text, 'html.parser')
    items = []
    
    for product in soup.find_all('div', class_='product-info'):
        item_name = product.find('a', class_='product-title').text.strip()
        price = product.find('span', class_='price').text.strip()
        link = product.find('a', class_='product-title')['href']
        
        items.append({
            'item_name': item_name,
            'website': 'Kilimall',
            'price': price,
            'link': link
        })
    
    print(f"Parsed items: {items}")  
    return items
