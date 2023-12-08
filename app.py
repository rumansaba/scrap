from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    youtube_data = scrape_youtube()
    amazon_data = scrape_amazon()
    return render_template('index.html', youtube_data=youtube_data, amazon_data=amazon_data)

def scrape_youtube():
    # Implement YouTube scraping logic here
    # Example: Extracting video titles
    youtube_url = 'https://www.youtube.com/'
    response = requests.get(youtube_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    video_titles = [title.text for title in soup.select('h3')]
    return video_titles

def scrape_amazon():
    # Implement Amazon scraping logic here
    # Example: Extracting product names
    amazon_url = 'https://www.amazon.com/'
    response = requests.get(amazon_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    product_names = [name.text for name in soup.select('.s-title-instructions')]
    return product_names


if __name__ == '__main__':
    app.run(host="0.0.0.0", )
