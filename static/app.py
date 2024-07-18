from flask import Flask, request, jsonify ,render_template
from app.scraper import scrape_kilimall, scrape_jiji, scrape_jumia
from app.routes import app

app = Flask(__name__)

@app.route('/')
def home():
    return  render_template('index.html')

 #"Welcome to the Price Tracking Website!"

@app.route('/scrape/<site>', methods=['GET' , 'POST'])
def scrape(site):
    item_name = request.args.get('item')
    if site == 'kilimall':
        data = scrape_kilimall(item_name)
    elif site == 'jiji':
        data = scrape_jiji(item_name)
    elif site == 'jumia':
        data = scrape_jumia(item_name)
    else:
        return jsonify({"error": "Invalid site"}), 400
    return jsonify(data)



if __name__ == '__main__':
    app.run(debug=True)
