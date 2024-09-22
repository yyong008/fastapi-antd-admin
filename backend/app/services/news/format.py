def format_news_category(news_category):
    item = {
        "id": news_category.id,
        "name": news_category.name,
        "description": news_category.description,
        "userId": news_category.user_id,
    }
    return item

def format_news(news):
    item = {
        "id": news.id,
        "title": news.title,
        "content": news.content,
        "author": news.author,
        "source": news.source,
        "viewCount": news.viewCount,
        "publishedAt": news.publishedAt,
    }
    return item


def format_news_by_id(news):
    return {
        "id": news.id,
        "title": news.title,
        "content": news.content,
        "author": news.author,
        "source": news.source,
        "viewCount": news.viewCount,
        "publishedAt": news.publishedAt,
        "userId": news.user_id,
        "categoryId": news.news_id
    }
