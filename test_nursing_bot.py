# test_nursing_bot.py
from nursing_bot import nursing_bot

context = {}
while True:
    user_input = input("You: ")
    reply = nursing_bot(user_input, context)
    print("Bot:", reply)
    if context.get("step") == -1:
        break
