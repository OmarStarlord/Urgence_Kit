import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def get_news():
    url = ('https://newsapi.org/v2/everything?'
           'q=Natural%20Disaster&'
           'from=2024-04-10&'
           'sortBy=popularity&'
           'apiKey=31b53b6c9b454900bbc790db174679ac')

    response = requests.get(url)

    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get('articles', [])
        return render_template('news.html', articles=articles)
    else:
        return 'Error fetching news data'

if __name__ == '__main__':
    app.run(debug=True)
