import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_or_create_vector_store():
    print("📦 Checking for existing vector store...")
    vector_stores = client.vector_stores.list().data

    existing_vs = next((vs for vs in vector_stores if vs.name == "OptiBot_Vector_Store"), None)

    if existing_vs:
        print(f"✅ Found existing vector store: {existing_vs.id}")
        return existing_vs

    print("➕ Creating new vector store...")
    new_vs = client.vector_stores.create(name="OptiBot_Vector_Store")
    print(f"✅ Created new vector store: {new_vs.id}")
    return new_vs

def upload_to_openai(filepaths, vector_store):
    if not filepaths:
        print("✅ No new or updated articles. Nothing to upload.")
        return

    print("📤 Uploading files to OpenAI vector store...")

    uploaded_count = 0
    for path in filepaths:
        with open(path, "rb") as f:
            client.vector_stores.file_batches.upload_and_poll(
                vector_store_id=vector_store.id,
                files=[f]
            )
        print(f"📤 Uploaded: {os.path.basename(path)}")
        uploaded_count += 1

    print(f"\n📦 Upload completed: {uploaded_count} files uploaded.")
