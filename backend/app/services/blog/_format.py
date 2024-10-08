def format_blog_category(blog_category):
    """格式化博客分类"""
    item = {
        "id": blog_category.id,
        "name": blog_category.name,
        "description": blog_category.description,
    }
    return item


def format_blog(blog):
    """格式化博客"""
    item = {
        "id": blog.id,
        "title": blog.title,
        "content": blog.content,
        "author": blog.author,
        "source": blog.source,
        "viewCount": blog.viewCount,
        "publishedAt": blog.publishedAt,
        "categoryId": blog.category_id,
        "tagId":blog.tag_id
    }
    return item


def format_blog_tag(blog_tag):
    """格式化博客标签"""
    item = {
        "id": blog_tag.id,
        "name": blog_tag.name,
        "description": blog_tag.description,
    }
    return item
