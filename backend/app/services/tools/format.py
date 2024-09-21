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
