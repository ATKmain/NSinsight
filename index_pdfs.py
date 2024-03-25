
from dotenv import load_dotenv
load_dotenv('/path/to/your/.env')

from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)

# Load environment variables from .env file
load_dotenv('.env')

folder_path = "data"  # Change this to your PDF folder path
PERSIST_DIR = "./storage"

# load the documents and create the index
documents = SimpleDirectoryReader(folder_path).load_data()
index = VectorStoreIndex.from_documents(documents)
# store it for later
index.storage_context.persist(persist_dir=PERSIST_DIR)
