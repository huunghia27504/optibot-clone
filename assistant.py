from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_assistant(vector_store_id):
    print("🤖 Creating assistant...")
    assistant = client.beta.assistants.create(
        name="OptiBot",
        instructions=(
            "You are OptiBot, the customer-support bot for OptiSigns.com.\n"
            "• Tone: helpful, factual, concise.\n"
            "• Only answer using the uploaded docs.\n"
            "• Max 5 bullet points; else link to the doc.\n"
            "• Cite up to 3 'Article URL:' lines per reply."
        ),
        tools=[{"type": "file_search"}],
        model="gpt-4o",
        tool_resources={"file_search": {"vector_store_ids": [vector_store_id]}}
    )
    print(f"✅ Assistant created: {assistant.id}")
    return assistant
