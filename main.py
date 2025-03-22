from tkinter import *

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")  
        self.root.configure(bg="#1e1e1e")
        self.mem = 0
        self.f_num = 0  
        self.math = ""  
        
        self.e = Entry(root, width=25, borderwidth=5, font=("Arial", 14))
        self.e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
       
        self.mem_label = Label(root, text="Memory: 0", fg="white", bg="#1e1e1e", font=("Arial", 12))
        self.mem_label.grid(row=1, column=5, columnspan=4)
        
        self.button_create()
    
    def button_click(self, number):  
        current = self.e.get()
        self.e.delete(0, END)
        self.e.insert(0, str(current) + str(number))
    
    def button_clear(self):  
        self.e.delete(0, END)
   
    def button_equal(self):  
        second_number = self.e.get()
        self.e.delete(0, END)
        
        if self.math == "addition":
            self.e.insert(0, self.f_num + float(second_number))
        if self.math == "subtract":
            self.e.insert(0, self.f_num - float(second_number))
        if self.math == "multiply":
            self.e.insert(0, self.f_num * float(second_number))
        if self.math == "divide":
            
            if float(second_number) != 0:
                self.e.insert(0, self.f_num / float(second_number))
            else:
                self.e.insert(0, "Error")
    
    def button_operation(self, operation):  
        first_number = self.e.get()
        self.f_num = float(first_number)
        self.math = operation
        self.e.delete(0, END)
    
    def mem_clear(self):  
        self.mem = 0
        self.mem_label.config(text=f"Memory: {self.mem}")
    
    def mem_add(self):  
        current = self.e.get()
        if current:
            self.mem += float(current)
            self.mem_label.config(text=f"Memory: {self.mem}")
    
    def mem_subtract(self):  
        current = self.e.get()
        if current:
            self.mem -= float(current)
            self.mem_label.config(text=f"Memory: {self.mem}")
    
    def mem_store(self):  
        current = self.e.get()
        if current:
            self.mem = float(current)
            self.mem_label.config(text=f"Memory: {self.mem}")
            
    def mem_recall(self):  
        self.e.delete(0, END)
        self.e.insert(0, self.mem)
   
    def button_create(self):
        button_texts = [
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("X", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
            ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("+", 5, 3),
        ]
        
        
        operation_map = {"+": "addition", "-": "subtract", "X": "multiply", "/": "divide"}
        
        
        Button(self.root, text="C", padx=20, pady=10, font=("Arial", 12), 
               command=self.button_clear).grid(row=6, column=0, columnspan=4, padx=5, pady=5)
        
        for txt, r, c in button_texts:
            if txt.isdigit() or txt == ".":
                
                Button(self.root, text=txt, padx=20, pady=10, font=("Arial", 12), 
                       command=lambda t=txt: self.button_click(t)).grid(row=r, column=c, padx=5, pady=5)
            elif txt == "=":
                Button(self.root, text=txt, padx=20, pady=10, font=("Arial", 12), 
                       command=self.button_equal).grid(row=r, column=c, padx=5, pady=5)
            else:
                
                Button(self.root, text=txt, padx=20, pady=10, font=("Arial", 12), 
                       command=lambda op=operation_map[txt]: self.button_operation(op)).grid(row=r, column=c, padx=5, pady=5)
        
        # Memory Buttons
        memory_buttons = [
            ("MC", self.mem_clear, 1, 0),
            ("M+", self.mem_add, 1, 1),
            ("M-", self.mem_subtract, 1, 2),
            ("MS", self.mem_store, 1, 3),
            ("MR", self.mem_recall, 1, 4),
        ]
        
        for txt, cmd, r, c in memory_buttons:
            Button(self.root, text=txt, padx=15, pady=10, font=("Arial", 10), 
                   command=cmd).grid(row=r, column=c, padx=5, pady=5)

if __name__ == "__main__":
    root = Tk()
    calc = Calculator(root)
    root.mainloop()