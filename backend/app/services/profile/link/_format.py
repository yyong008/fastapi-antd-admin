
def format_category(category):
    """
    格式化 profile link category
    """
    item = {
        "id": category.id,
        "name": category.name,
        "description": category.description,
    }
    return item

def format_link(link):
    """
    格式化 profile link
    """
    item = {
        "id": link.id,
        "name": link.name,
        "url": link.url,
        "description": link.description,
        "created_at": link.created_at,
        "updated_at": link.updated_at,
    }
    return item
