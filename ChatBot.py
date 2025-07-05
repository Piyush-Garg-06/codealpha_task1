
# This is the solution according to given instructions:


def chat_bot():
    print("Welcome to the basic chatbot! (Type 'bye' to exit)")
    
    while(True):
        print("You :", end="")
        user_input = input("").lower()
            
        if(user_input == "hello"):
            print("Bot: Hi!")

        elif(user_input == "how are you"):
            print("Bot: I'm fine thanks!")

        elif(user_input == "bye"):
            print("Bot: Good Bye!")
            break

        else:
            print("Bot: Sorry, I don't understand you input")


chat_bot()
        



#Modified solution according to me:

# import random

# responses = {
#     "hello": ["Hi there!", "Hello!", "Greetings!", "Hey!"],
#     "how are you?": ["I'm doing well, thank you.", "I'm fine, and you?", "All good here!"],
#     "what is your name?": ["I'm a chatbot.", "You can call me ChatBot.", "I don't have a name, but I'm here to help!"],
#     "what can you do?": ["I can chat with you!", "Right now, I can respond to basic questions."],
#     "thank you": ["You're welcome!", "No problem!", "Glad to help!"],
#     "thanks": ["You're welcome!", "Anytime!", "Happy to help!"],
#     "who created you?": ["I was created by a developer.", "A human coded me into existence!"],
#     "good morning": ["Good morning!", "Morning! Have a great day ahead!"],
#     "good night": ["Good night!", "Sweet dreams!", "Rest well!"],
#     "what is your favorite color?": ["I like all colors equally!", "I don't have eyes, but I hear blue is nice."]
# }

# while(True):
#     user_input = input("You : ").lower()

#     if(user_input == "bye"):
#         print("Bot : Good bye!")
#         break

#     if(user_input in responses):
#         bot_reply = random.choice(responses[user_input])
#         print("Bot :", bot_reply)

#     else:
#         print("Bot : Sorry, I don't understand your input")