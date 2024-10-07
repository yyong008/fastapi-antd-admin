def format_tools_storage(storage):
    item = {
        "id": storage.id,
        "createdAt": storage.createdAt,
        "updatedAt": storage.updatedAt,
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
