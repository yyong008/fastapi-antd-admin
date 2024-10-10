def format_tools_storage(storage):
    """
    格式化存储信息
    """
    item = {
        "id": storage.id,
        "created_at": storage.created_at,
        "updated_at": storage.updated_at,
        "name": storage.name,
        "user_id": storage.user_id,
        "file_name": storage.file_name,
        "ext_name": storage.ext_name,
        "size": storage.size,
        "path": storage.path,
        "type": storage.type,
    }
    return item


def format_tools_mail(mail):
    """
    格式化邮件信息
    """
    item = {
        "id": mail.id,
        "name": mail.name,
        "title": mail.title,
        "host": mail.host,
        "port": mail.port,
        "user": mail.user,
        "pass": mail.pass_,
        "from": mail.from_,
        "to": mail.to_,
        "subject": mail.subject,
        "content": mail.content,
    }
    return item
