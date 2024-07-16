# settings.py

import pymongo

# MongoDB client connection
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Database name
db = client["lm_chat_db"]

# Ensure MongoDB collections exist on server start
def ensure_collections_exist():
    # Ensure conversation collection and indexes exist
    if 'conversation' not in db.list_collection_names():
        db.create_collection('conversation')
        db.conversation.create_index([('user', pymongo.ASCENDING)])

    # Ensure message collection and indexes exist
    if 'message' not in db.list_collection_names():
        db.create_collection('message')
        db.message.create_index([('conversation_id', pymongo.ASCENDING)])

# Call the function to ensure collections exist
ensure_collections_exist()
