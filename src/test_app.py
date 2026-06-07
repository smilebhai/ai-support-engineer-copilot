from dotenv import load_dotenv

load_dotenv()

from app import support_copilot

result = support_copilot(
    {
        "issue": "Users started receiving 401 errors after rotating API keys."
    }
)

print(result)