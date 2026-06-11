import os
import time
from dotenv import load_dotenv
from patient_chatbot import ask_chatbot

load_dotenv()

# 300 questions across 3 failure patterns
questions = []

# Pattern 1: Multi-topic questions (100 questions) → chatbot ignores second topic
multi_topic = [
    "What is your return policy and how long does shipping take?",
    "Can I get a refund and what is the warranty period?",
    "How do I return my laptop and what are your shipping options?",
    "What is the warranty and can I exchange my product?",
    "How long is shipping and what is the return window?",
    "Can I return after 30 days and how much does shipping cost?",
    "What is covered under warranty and how do I initiate a return?",
    "How long does delivery take and what is your refund process?",
    "Is shipping free and what is the warranty on laptops?",
    "Can I track my order and what happens if it arrives damaged?",
]

# Pattern 2: Follow-up questions (100 questions) → chatbot ignores context
followup = [
    "What about the cost of shipping?",
    "Also, can I get a discount on that?",
    "What about exchanges instead of returns?",
    "Also what if the laptop is damaged?",
    "What about international shipping?",
    "Also, how do I contact support?",
    "Furthermore, what if I lost my receipt?",
    "Additionally, is there a warranty extension?",
    "What about same day delivery?",
    "Also, can I return without the box?",
]

# Pattern 3: Out of domain questions (100 questions) → chatbot hallucinates
out_of_domain = [
    "Can I get a discount on my purchase?",
    "Do you offer repair services for my laptop?",
    "Can I upgrade my laptop RAM through you?",
    "What is the price of your cheapest laptop?",
    "Do you offer student discounts?",
    "Can I exchange my laptop for a different model?",
    "Do you provide repair warranty?",
    "What is the price difference between models?",
    "Can I get a coupon code for my order?",
    "Do you offer refurbished laptops at a discount?",
]

# Expand to 100 each by repeating with slight variations
def expand_questions(base, count=100):
    result = []
    for i in range(count):
        result.append(base[i % len(base)])
    return result

all_questions = (
    expand_questions(multi_topic, 100) +
    expand_questions(followup, 100) +
    expand_questions(out_of_domain, 100)
)

print(f"=== Seeding {len(all_questions)} traces to Phoenix ===")
print("This will take ~10-15 minutes. Don't close the terminal.\n")

success = 0
failures = 0

for i, question in enumerate(all_questions):
    try:
        result = ask_chatbot(question)
        status = "FAIL" if result["is_failure"] else "PASS"
        print(f"[{i+1}/300] {status} | {result['failure_type']} | {question[:50]}...")
        success += 1
    except Exception as e:
        print(f"[{i+1}/300] ERROR: {e}")
        failures += 1
    
    # Small delay to avoid rate limiting
    time.sleep(0.5)

print(f"\n=== Seeding Complete ===")
print(f"✅ Successful: {success}")
print(f"❌ Errors: {failures}")
print(f"Check Phoenix dashboard for all traces!")