import os
from dotenv import load_dotenv
from phoenix.client import Client

load_dotenv()

phoenix = Client(
    base_url="https://app.phoenix.arize.com/s/bonamukkalacharan",
    api_key=os.getenv("PHOENIX_API_KEY")
)

spans = phoenix.spans.get_spans_dataframe(
    project_identifier="patient-chatbot",
)

print("Total spans:", len(spans))
print("\nColumn names:")
print("\nChecking input values:")
for i, (_, span) in enumerate(spans.iterrows()):
    val = span.get("attributes.input.value", "")
    print(f"  Row {i}: type={type(val).__name__}, len={len(str(val))}, val={str(val)[:80]}")
    if i >= 4:
        break