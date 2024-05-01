from datetime import datetime, timedelta
import requests
import random
from django.shortcuts import render
from .models import Article

def home(request):
    # Define keywords for natural disasters
    keywords = ['earthquake', 'flood', 'hurricane', 'tornado', 'wildfire']
    
    # Join keywords with OR operator to form query string
    keyword_query = ' OR '.join(keywords)

    # Calculate the date two days before the current date
    two_days_ago = datetime.now() - timedelta(days=2)
    from_date = two_days_ago.strftime('%Y-%m-%d')

    # Construct URL for News API request
    url = ('https://newsapi.org/v2/everything?'
           f'q={keyword_query}&'
           f'from={from_date}&'
           'sortBy=popularity&'
           'apiKey=31b53b6c9b454900bbc790db174679ac')

    # Send request to News API
    response = requests.get(url)

    if response.status_code == 200:
        # Extract news articles from API response
        news_data = response.json().get('articles', [])
        
        # Iterate over each article and create Article objects
        for article_data in news_data:
            # Check if description exists before creating Article object
            description = article_data.get('description', '')
            if description:
                Article.objects.create(
                    title=article_data['title'],
                    description=description,
                    url=article_data['url']
                )

        # Get all articles from the database
        all_articles = list(Article.objects.all())
        
        # Select 5 random articles
        random_articles = random.sample(all_articles, min(5, len(all_articles)))

        # Render home.html template with random articles
        return render(request, 'news.html', {'articles': random_articles})
    else:
        # Render error.html template if API request fails
        return render(request, 'error.html')
