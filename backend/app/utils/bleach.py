import bleach

allowed_tags = ['a', 'b', 'strong', 'i', 'em', 'p', 'ul', 'ol', 'li', 'br']
allowed_attributes = {
    'a': ['href', 'title']
}

def clean_html(user_input_html):
    return bleach.clean(user_input_html, tags=allowed_tags, attributes=allowed_attributes)
