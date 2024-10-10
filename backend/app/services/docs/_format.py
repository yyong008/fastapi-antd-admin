def format_changelog(changelog):
    """
    格式化更新
    """
    item = {
        "id": changelog.id,
        "userId": changelog.userId,
        "publish_name": changelog.publish_name,
        "publish_version": changelog.publish_version,
        "type": changelog.type,
        "content": changelog.content,
        "url": changelog.url,
        "created_at": changelog.created_at,
        "updated_at": changelog.updated_at,
    }
    return item

def format_feedback(feedback):
    """格式化反馈"""
    item = {
        "id": feedback.id,
        "userId": feedback.userId,
        "content": feedback.content,
        "url": feedback.url,
        "created_at": feedback.created_at,
        "updated_at": feedback.updated_at,
    }
    return item
