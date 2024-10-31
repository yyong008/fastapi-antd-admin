import json

def yield_string(chat_id, content, role):
    data = {"id": chat_id, "content": content, "role": role}
    stream_response_data = f"data: {json.dumps(data)}\n\n"
    return stream_response_data
