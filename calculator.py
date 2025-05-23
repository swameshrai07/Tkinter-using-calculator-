import tkinter as tk
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.expression = ""
        self.input_text = tk.StringVar()

        self._create_widgets()

    def _create_widgets(self):
    
        input_frame = tk.Frame(self.root)
        input_frame.pack(expand=True, fill="both")

        input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, bd=10, insertwidth=2, width=14,
                               borderwidth=4, relief="ridge", justify='right')
        input_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15)

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack()

        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('C', '0', '=', '+')
        ]

        for i, row in enumerate(buttons):
            for j, button_text in enumerate(row):
                tk.Button(button_frame, text=button_text, padx=20, pady=20, font=('arial', 14, 'bold'),
                          command=lambda txt=button_text: self._on_button_click(txt)).grid(row=i, column=j)

    def _on_button_click(self,char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "Error"
        else:
            self.expression += str(char)

        self.input_text.set(self.expression)



if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
