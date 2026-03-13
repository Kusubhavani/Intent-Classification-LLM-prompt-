from classifier import classify_intent
from router import route_and_respond
from logger import log_route

def main():
    print("🤖 LLM Router Ready! (Type 'quit' to exit)")
    
    while True:
        message = input("\nUser: ")
        
        if message.lower() in ['quit', 'exit', 'q']:
            print("Goodbye! 👋")
            break
            
        if not message.strip():
            continue
            
        intent_data = classify_intent(message)
        intent = intent_data["intent"]
        confidence = intent_data["confidence"]
        
        print(f"\n🎯 Intent: {intent} ({confidence:.2f})")
        
        response = route_and_respond(message, intent_data)
        log_route(intent, confidence, message, response)
        
        print(f"\n💬 Response:\n{response}")

if __name__ == "__main__":
    main()