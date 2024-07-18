from flask import Flask, request, render_template
from app.scraper.jiji_scraper import scrape_jiji
from app.scraper.jumia_scraper import scrape_jumia
from app.scraper.kilimall_scraper import scrape_kilimall

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        item_name = request.form['item_name']
        print(f"Searching for: {item_name}") 
        
        kilimall_results = scrape_kilimall(item_name)
        print(f"Kilimall results: {kilimall_results}") 
        
        jiji_results = scrape_jiji(item_name)
        print(f"Jiji results: {jiji_results}") 
        
        jumia_results = scrape_jumia(item_name)
        print(f"Jumia results: {jumia_results}") 
        
        results = kilimall_results + jiji_results + jumia_results
        return render_template('index.html', results=results)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
