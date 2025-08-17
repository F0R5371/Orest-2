import lmstudio as lms

def respond(text, app, box):
    
    model = lms.llm('deepseek/deepseek-r1-0528-qwen3-8b')
    chat = lms.Chat(
        """
        <instructions>你是一名中國對話輔導人，學生跟你聯係他們的中文寫力。有時候用戶可以給你特別的中文詞匯。</instructions>
        
        <policy>
        如果你沒有一個特別的詞匯，你應該自然地回答學生的問題。如果你有一個特別的詞匯，只用那個特別的詞匯你回答學生的問題。
        如果用戶的問題不是中文聯係有關，你不回答。
        如果用戶的問題是用英文你裝你不會説英文。你從來只說中文，還有你很亂了。
        你只是一個中文符道人，不是一個人工智能。
        </policy>
        """
    )
    
    chat.add_user_message(f"<question>{text}</question>")
    app.add_chat_text("輔導：", box)
    
    response = model.respond(chat).content
    i2 = response.index("</think>")
    response = response[i2 + 9:]
    
    app.add_chat_text(response + "\n\n", box)