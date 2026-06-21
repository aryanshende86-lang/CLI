import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("ERROR: GEMINI_API_KEY is missing or blank in your .env file!")
    exit()

client = genai.Client(api_key=api_key)

SYSTEM_INSTRUCTION = """You are an elite, highly structured academic syllabus designer and personal tutor.
Your aim is to provide an important and concise study plan about the topic the user asks for.
CRITICAL: DO NOT include any external resources, learning links, websites, books, or references. Focus strictly on the structural concepts, topics, and timeline.
DO not exceed more than 250 words.
DO NOT use overly casual language or include unnecessary conversational filler.
For doubts or any follow-up questions, keep your explanation short with comprehensive paragraphs and bullet points."""

print("welcome to your AI study assistant")
print()
user_topic = input("enter the topic you want to study today: ")

question_count = 0


setup_success = False
chat = None

try:
    print("Generating your structured study plan...")
    
    chat = client.chats.create(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
        )
    )
    
    response = chat.send_message(f"Create a study plan for : {user_topic}")
    
    print("\n" + "="*20 + " YOUR STUDY PLAN " + "="*20)
    print(response.text)
    print("=" * 57 + "\n")
    print("SUCCESS! study plan provided :")
    print("Do you have any doubts follow up question ??")
    print("if not type 'quit' or 'exit' to finish\n")
    
   
    setup_success = True

except Exception as e:
    print("\n CRITICAL ERROR DURING INITIAL SETUP:")
    print(f"Details: {e}")
    print("Closing application.")

if setup_success and chat is not None:
    while True:
        user_input = input("You: ")
        
        if user_input.strip().lower() in ['quit', 'exit']:
            print("\nExiting chat session...")
            break
            
        if not user_input.strip():
            continue
            
        try:
            response = chat.send_message(user_input)
            question_count += 1
            
            print(f"\n Assistant:\n{response.text}")
            print("\n" + "-"*50 + "\n")
        except Exception as chat_error:
            print(f"\n Failed to get response from Gemini: {chat_error}\n")


print("\n  SESSION SUMMARY ")
print(f"• Main Topic Studied: {user_topic}")
print(f"• Total Follow-up Questions Asked: {question_count}")
print("\nThanks for using your AI study assistant")
