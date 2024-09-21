def format_news_category(news_category):
    item = {
        "id": news_category.id,
        "name": news_category.name,
        "description": news_category.description,
        "userId": news_category.user_id,
    }
    return item
