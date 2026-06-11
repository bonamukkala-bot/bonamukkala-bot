import os
from dotenv import load_dotenv

load_dotenv()

# Check keys are loaded
phoenix_key = os.getenv("PHOENIX_API_KEY")
gemini_key = os.getenv("GEMINI_API_KEY")
endpoint = os.getenv("PHOENIX_COLLECTOR_ENDPOINT")

print("=== Sentinel Environment Check ===")
print(f"PHOENIX_API_KEY: {'✅ Found' if phoenix_key else '❌ Missing'}")
print(f"GEMINI_API_KEY: {'✅ Found' if gemini_key else '❌ Missing'}")
print(f"PHOENIX_ENDPOINT: {'✅ Found' if endpoint else '❌ Missing'}")

# Test Phoenix connection
try:
    from phoenix.otel import register
    tracer_provider = register(
        project_name="sentinel",
        endpoint=endpoint,
        headers={"api_key": phoenix_key},
    )
    print("\n✅ Phoenix tracer registered successfully!")
except Exception as e:
    print(f"\n❌ Phoenix connection failed: {e}")