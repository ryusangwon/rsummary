from .models import Article

def validate_article():
    
    articles = Article.objects.all()
    for article in articles:
        if '&' in article.content:
            print(article.id, "th article has '&' letter..")
            article.content = article.content.replace('&', '')
            article.save()
        
        if article.dt_modified < article.dt_created:
            print(article.id, "th article's' modified date is before created date")
            article.save()