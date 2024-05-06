from datetime import datetime, timedelta
import requests
import random
from django.shortcuts import render, redirect
from .models import Article


def home(request):
    user_id = request.session.get('user_id')
    if not user_id:
        
        return redirect('users:login')
    
    keywords = ['earthquake', 'flood', 'hurricane', 'tornado', 'wildfire']
    keyword_query = ' OR '.join(keywords)
    
    two_days_ago = datetime.now() - timedelta(days=2)
    from_date = two_days_ago.strftime('%Y-%m-%d')

    url = ('https://newsapi.org/v2/everything?'
           f'q={keyword_query}&'
           f'from={from_date}&'
           'sortBy=popularity&'
           'apiKey=31b53b6c9b454900bbc790db174679ac')

    response = requests.get(url)

    if response.status_code == 200:
        news_data = response.json().get('articles', [])
        natural_disaster_articles = []

        for article_data in news_data:
            title = article_data.get('title', '').lower()
            

            if any(keyword in title for keyword in keywords):
                natural_disaster_articles.append(article_data)

        for article_data in natural_disaster_articles:
            description = article_data.get('description', '')
            if description:
                Article.objects.create(
                    title=article_data['title'],
                    description=description,
                    url=article_data['url']
                )

        all_articles = list(Article.objects.all())
        random_articles = random.sample(all_articles, min(5, len(all_articles)))

        return render(request, 'news.html', {'articles': random_articles})
    else:
        return render(request, 'error.html')
