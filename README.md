# Price Tracker

A web application to track prices of items across multiple online shopping platforms like Kilimall, Jiji, and Jumia.

## Features

- Search for products by name.
- Scrape and compare prices from Kilimall, Jiji, and Jumia.
- Display the results in a user-friendly interface.

## Project Structure

price-tracker/
├── app/
│ ├── init.py
│ ├── app.py
│ ├── routes.py
│ ├── scraper/
│ │ ├── init.py
│ │ ├── jiji_scraper.py
│ │ ├── jumia_scraper.py
│ │ ├── kilimall_scraper.py
├── price-tracker-env/
├── static/
│ ├── css/
│ │ └── styles.css
├── templates/
│ ├── index.html
├── .gitignore
├── requirements.txt
├── prices.db
└── README.md

markdown
Copy code

## Prerequisites

- Python 3.x
- `pip` (Python package installer)
- `virtualenv` (to create a virtual environment)

## Setup

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/price-tracker.git
cd price-tracker
Create and activate a virtual environment:
bash
Copy code
python -m venv price-tracker-env
source price-tracker-env/bin/activate   # On Windows: price-tracker-env\Scripts\activate
Install the dependencies:
bash
Copy code
pip install -r requirements.txt
Initialize the database:
The database will be automatically initialized when you run the application for the first time.

Run the Application
Start the Flask application:
bash
Copy code
python app.py
Open your web browser and go to:
arduino
Copy code
http://127.0.0.1:5000
Usage
Enter the item name you want to search for in the input field.
Click the "Search" button.
The application will scrape prices from Kilimall, Jiji, and Jumia and display the results.
Scrapers
The scraping logic for each website is implemented in separate modules:

Kilimall: app/scraper/kilimall_scraper.py
Jiji: app/scraper/jiji_scraper.py
Jumia: app/scraper/jumia_scraper.py
Each scraper module contains a function that takes an item name as input and returns a list of dictionaries containing the item details.

Contributing
Contributions are welcome! Please fork this repository and submit a pull request for any changes or improvements.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
If you have any questions or suggestions, please feel free to reach out to me at [your-email@example.com].

arduino
Copy code

Replace the placeholder content (e.g., `https://github.com/yourusername/price-tracker.git`, `[your-email@example.com]`) with the actual information for your project. This `README.md` file provides a comprehensive overview of your project, its structure, setup instructions, and usage details.
