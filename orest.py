import partner
from customtkinter import *

class Orest():
    
    def __init__(self):
        
        # PROPERTIES
        self.chats = 0
        self.max_chats = 10
        
        self.chat_box = None
        
        # SETUP
        self.setup()  
        
    def setup(self):
        
        # Root setup
        root = CTk()
        root.title("Orest")
        root.geometry("1000x500")

        # Sidebar frame ----------------------------------------------
        sidebar = CTkFrame(root)
        sidebar.pack(side = 'left', fill = 'y')

        sidebar_contents = CTkFrame(sidebar)
        sidebar_contents.pack(padx = (10, 10), pady = (10, 10), fill = 'both', expand = True)

        toggle_button = CTkButton(sidebar_contents, text = "Toggle")
        toggle_button.pack(side = 'top')

        add_button = CTkButton(
            sidebar_contents, 
            text = "Add", 
            command = lambda : self.add_chat(sidebar_contents)
        )
        add_button.pack(side = 'bottom')

        # Main frame ----------------------------------------------
        main = CTkFrame(root)
        main.pack(padx = (30, 30), pady = (30, 30), fill = 'both', expand = True)

        main.grid_columnconfigure(0, weight = 1)
        
        main.grid_rowconfigure(0, weight = 1)
        
        # Response box
        response = CTkTextbox(main, state = "disabled")
        response.grid(row = 0, sticky = "NSEW")
        
        # Entry box
        entry = CTkFrame(main)
        entry.grid(row = 1, sticky = "NSEW", pady = (30, 0))
        
        entry_box = CTkEntry(
            entry, 
            height = 50, 
            font = ('Times New Roman', 24), 
            placeholder_text = "Type sentence here..."
        )
        entry_box.grid(row = 0, column = 0, sticky = "NSEW", padx = (0, 10))
        
        entry_button = CTkButton(
            entry, 
            text = "Enter", 
            command = lambda : partner.respond(entry_box.get(), self, response)
        )
        entry_button.grid(row = 0, column = 1, sticky = 'NSEW', padx = (10, 0))
        
        entry.grid_columnconfigure(0, weight = 15)
        entry.grid_columnconfigure(1, weight = 1)

        # Mainloop ----------------------------------------------

        root.mainloop()
        
    def add_chat(self, sidebar):
        
        if self.chats > 9:
            return
        self.chats += 1
        
        chat = CTkButton(sidebar, text = "Chat")
        chat.pack(side = 'top', pady = (10, 0))
        
    def add_chat_text(self, text, response_box):
        
        response_box.insert("insert", "eefefff")
        print(len(response_box.get("0.0", "end")))
        
        
def main():
    
    app = Orest()
    

if __name__ == "__main__":
    main()