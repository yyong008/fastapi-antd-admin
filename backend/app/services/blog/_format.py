def format_blog_category(blog_category):
    """格式化博客分类"""
    item = {
        "id": blog_category.id,
        "name": blog_category.name,
        "description": blog_category.description,
        "created_at": blog_category.created_at,
        "updated_at": blog_category.updated_at,
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
        "view_count": blog.view_count,
        "published_at": blog.published_at,
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
        "created_at": blog_tag.created_at,
        "updated_at": blog_tag.updated_at,
    }
    return item
