from app.utils.bleach import clean_html


def format_news_category(news_category):
    """
    格式化新闻分类
    """
    item = {
        "id": news_category.id,
        "name": news_category.name,
        "description": news_category.description,
        "userId": news_category.user_id,
        "created_at": news_category.created_at,
        "updated_at": news_category.updated_at
    }
    return item

def format_news(news):
    """
    格式化新闻
    """
    item = {
        "id": news.id,
        "title": news.title,
        "content": news.content,
        "author": news.author,
        "source": news.source,
        "view_count": news.view_count,
        "published_at": news.published_at,
        "category_id": news.news_id, # TODO: 修改为 category_id in db
        "created_at": news.created_at,
        "updated_at": news.updated_at
    }
    return item


def format_news_by_id(news):
    """
    通过 id 格式化新闻
    """
    return {
        "id": news.id,
        "title": news.title,
        "content": news.content,
        "author": news.author,
        "source": news.source,
        "view_count": news.view_count,
        "published_at": news.published_at,
        "userId": news.user_id,
        "categoryId": news.news_id,
        "created_at": news.created_at,
        "updated_at": news.updated_at
    }

def format_news_from_old_news(current_user_id, news):
    """
    格式化旧新闻
    """
    older_news = news
    news['content'] = clean_html(news['content'])
    news["news_id"] = older_news["categoryId"]
    news["user_id"] = current_user_id
    news["view_count"] = 0
    del news["categoryId"]
    return news
