import lmstudio as lms

def respond(text, app, box):
    
    #model = lms.llm('deepseek/deepseek-r1-0528-qwen3-8b')
    #chat = lms.Chat(text)
    #result = model.respond(chat)
    
    app.add_chat_text("result", box)