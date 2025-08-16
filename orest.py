from customtkinter import *

class Orest():
    
    def __init__(self):

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

        add_button = CTkButton(sidebar_contents, text = "Add")
        add_button.pack(side = 'bottom')

        # Main frame ----------------------------------------------
        main = CTkFrame(root)
        main.pack(padx = (30, 30), pady = (30, 30), fill = 'both', expand = True)

        main.grid_columnconfigure(0, weight = 1)
        
        # Response box
        response = CTkTextbox(main, state = "disabled")
        response.grid(row = 0, sticky = "NSEW", pady = (0, 30))
        
        # Entry box
        entry = CTkFrame(main)
        entry.grid(row = 1, sticky = "NSEW")
        
        entry_box = CTkEntry(entry, height = 50, font = ('Times New Roman', 24))
        entry_box.grid(row = 0, column = 0, sticky = "NSEW", padx = (0, 10))
        
        entry_button = CTkButton(entry, text = "Enter")
        entry_button.grid(row = 0, column = 1, sticky = 'NSEW', padx = (10, 0))
        
        entry.grid_columnconfigure(0, weight = 15)
        entry.grid_columnconfigure(1, weight = 1)

        # Mainloop ----------------------------------------------

        root.mainloop()
        
        
def main():
    
    app = Orest()
    

if __name__ == "__main__":
    main()