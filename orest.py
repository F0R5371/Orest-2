import partner
from customtkinter import *

class Orest():
    
    def __init__(self):
        
        # PROPERTIES
        self.chats = 0
        self.max_chats = 10
        
        self.sections = dict()
        
        # SETUP
        self.setup()  
        
    def setup(self):
        
        # Root setup
        
        root = CTk()
        root.title("Orest")
        root.geometry("1000x500")
        
        # Navbar ----------------------------------------------
        
        navbar = CTkFrame(root, height = 30)
        navbar.pack(side = 'top', anchor = "w")
        
        nav_left = CTkFrame(navbar)
        nav_left.pack(fill = 'both')
        
        chat_button = CTkButton(
            nav_left, 
            text = "Chat", 
            corner_radius = 0,
            command = lambda : self.open_section("Chat")
        )
        chat_button.grid(row = 0, column = 0)
        
        file_button = CTkButton(
            nav_left, 
            text = "Vocab", 
            corner_radius = 0,
            command = lambda : self.open_section("Vocab")
        )
        file_button.grid(row = 0, column = 1)
        
        note_button = CTkButton(
            nav_left, 
            text = "Notes", 
            corner_radius = 0,
            command = lambda : self.open_section("Notes")
        )
        note_button.grid(row = 0, column = 2)
        
        dict_button = CTkButton(
            nav_left, 
            text = "Dictionary", 
            corner_radius = 0,
            command = lambda : self.open_section("Dictionary")
        )
        dict_button.grid(row = 0, column = 3)
        
        settings_button = CTkButton(
            nav_left, 
            text = "Settings", 
            corner_radius = 0,
            command = lambda : self.open_section("Settings")
        )
        settings_button.grid(row = 0, column = 4)


        # Sections ----------------------------------------------

        main = CTkFrame(root)
        main.pack(fill = 'both', expand = True)
        
        main.grid_columnconfigure(0, weight = 1)
        main.grid_rowconfigure(0, weight = 1)

        self.sections["Chat"] = Chat(self, main)
        self.sections["Vocab"] = Vocab(main) 
        
        for val in self.sections.values():
            val.grid(row = 0, column = 0, sticky = "NSEW")
        
        self.open_section("Chat")

        # Mainloop ----------------------------------------------

        root.mainloop()
        
    def add_chat(self, sidebar):
        
        if self.chats > 9:
            return
        self.chats += 1
        
        chat = CTkButton(sidebar, text = "Chat")
        chat.pack(side = 'top', pady = (10, 0))
        
    def add_chat_text(self, text, response_box):
        
        response_box.configure(state = "normal")
        response_box.insert("insert", text)
        response_box.configure(state = "disabled")
        
    def open_section(self, section):

        selected = self.sections[section]
        selected.tkraise()
        
    def get_section(self, section):
        
        return self.sections[section]
    
    def make_entry(self, entry_box, response):
        
        user_chat = "用戶：" + entry_box.get() + "\n\n"
        self.add_chat_text(user_chat, response)
        entry_box.delete(0, "end")
        
        self.get_section("Vocab").get_vocab()
        
        partner.respond(entry_box.get(), self, response)
        
        
class Chat(CTkFrame):
    
    def __init__(self, app, parent):
        
        CTkFrame.__init__(self, parent)
        
        # Sidebar frame ----------------------------------------------
        
        sidebar = CTkFrame(self)
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
        
        main = CTkFrame(self)
        main.pack(padx = (30, 30), pady = (30, 30), fill = 'both', expand = True)

        main.grid_columnconfigure(0, weight = 1)
        
        main.grid_rowconfigure(0, weight = 1)
        
        # Response box
        
        response = CTkTextbox(main, state = "disabled", font = ('Calibri', 18))
        response.grid(row = 0, sticky = "NSEW")
        
        # Entry box
        
        entry = CTkFrame(main)
        entry.grid(row = 1, sticky = "NSEW", pady = (30, 0))
        
        entry_box = CTkEntry(
            entry, 
            height = 50, 
            font = ('Calibri', 24), 
            placeholder_text = "Type sentence here..."
        )
        entry_box.grid(row = 0, column = 0, sticky = "NSEW", padx = (0, 10))
        
        entry_button = CTkButton(
            entry, 
            text = "Enter", 
            command = lambda : app.make_entry(entry_box, response)
        )
        entry_button.grid(row = 0, column = 1, sticky = 'NSEW', padx = (10, 0))
        
        entry.grid_columnconfigure(0, weight = 15)
        entry.grid_columnconfigure(1, weight = 1)
    
    
class Vocab(CTkFrame):
    
    def __init__(self, parent):
        
        self.vocab_lists = list()
        
        self.setup(parent)
        
    def setup(self, parent):
        
        CTkFrame.__init__(self, parent)
        
        # Main frame ----------------------------------------------
        main = CTkFrame(self)
        main.pack(fill = 'both', expand = True, padx = (30, 30), pady = (30, 30))
        
        main.grid_columnconfigure(0, weight = 1)
        
        # Vocab table ----------------------------------------------
        table_contents = CTkFrame(main)
        table_contents.pack(fill = 'both', expand = True)
        
        table_contents.grid_rowconfigure(0, weight = 1)
        table_contents.grid_columnconfigure((0, 1, 2), weight = 1)
        
        table = CTkTextbox(table_contents, font = ('Calibri', 18))
        table.grid(row = 0, column = 0, sticky = "NSEW", padx = (0, 15))
        table.insert("0.0", "中文...")
        
        table1 = CTkTextbox(table_contents, font = ('Calibri', 18))
        table1.grid(row = 0, column = 1, sticky = "NSEW", padx = (15, 15))
        table1.insert("0.0", "Pinyin...")
        
        table2 = CTkTextbox(table_contents, font = ('Calibri', 18))
        table2.grid(row = 0, column = 2, sticky = "NSEW", padx = (15, 0))
        table2.insert("0.0", "English...")
        
        self.vocab_lists.append(table)
        self.vocab_lists.append(table1)
        self.vocab_lists.append(table2)
        
        # Next buttons ----------------------------------------------
        buttons = CTkFrame(main)
        buttons.pack(fill = 'x', pady = (30, 0))
        
        buttons.grid_columnconfigure((0, 2), weight = 1)
        buttons.grid_columnconfigure(1, weight = 15)
        
        button = CTkButton(buttons, text = "Import")
        button.grid(row = 0, column = 0, sticky = "w")
        
        title = CTkLabel(buttons, text = "")
        title.grid(row = 0, column = 1)
        
        button1 = CTkButton(buttons, text = "Save")
        button1.grid(row = 0, column = 2, sticky = "e")
        
    def get_vocab(self):
        
        vocab = ""
        
        labels = ["Chinese", "Pinyin", "English"]
        for i in range(len(self.vocab_lists)):
            
            vocab += f"{labels[i]}: "
            
            contents = self.vocab_lists[i].get(
                "0.0", 
                "end"
            ).replace(
                '\n', 
                ' '
            ).split(' ')
            
            contents = list(filter(lambda f : f != ' ' and f != '', contents))
            for word in contents:
                vocab += word + ", "
                
            vocab += "\n\n"

        return vocab
        
        
class Notes(CTkFrame):
    
    def __init__(self, parent):
        
        CTkFrame.__init__(self, parent)
    
    
class Dictionary(CTkFrame):
    
    def __init__(self, parent):
        
        CTkFrame.__init__(self, parent)
    
    
class Settings(CTkFrame):
    
    def __init__(self, parent):
        
        CTkFrame.__init__(self, parent)
        
        
def main():
    
    app = Orest()
    

if __name__ == "__main__":
    main()