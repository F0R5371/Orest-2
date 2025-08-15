from customtkinter import *

class Orest():
    
    def __init__(self):

        self.setup()
        
    def setup(self):
        
        root = CTk()
        root.title("Orest")
        root.geometry("1500x900")
        
        # Response box
        response = CTkTextbox(root)
        response.pack(padx = (30, 30), pady = (30, 30), fill = 'both')
        
        # Entry box
        entry = CTkFrame(root)
        entry.pack(padx = (30, 30), pady = (30, 30), fill = 'both')
        
        entry_box = CTkEntry(entry)
        entry_box.grid(row = 0, column = 0, sticky = "NSEW", padx = (0, 10))
        
        entry_button = CTkButton(entry, text = "Enter")
        entry_button.grid(row = 0, column = 1, sticky = 'NSEW', padx = (10, 0))
        
        entry.grid_columnconfigure(0, weight = 15)
        entry.grid_columnconfigure(1, weight = 1)

        root.mainloop()
        
        
def main():
    
    app = Orest()
    

if __name__ == "__main__":
    main()