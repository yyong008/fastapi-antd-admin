
def format_category(category):
    item = {
        "id": category.id,
        "name": category.name,
        "description": category.description,
    }
    return item

def format_link(link):
    item = {
        "id": link.id,
        "name": link.name,
        "url": link.url,
    }
    return item