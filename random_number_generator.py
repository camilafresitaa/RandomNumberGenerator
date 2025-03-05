import tkinter as tk
from random import choice

# Colors
light_pink = "#ffdae9"
dark_pink = "#e6679b"
medium_pink = "#f5aac3"

class RandomNumber():
    def __init__(self, window):
        self.numbers_list = []
        self.window = window
        self.createwidgets()

    def createwidgets(self):
        # Frame 1
        self.frame1 = tk.Frame(self.window, bg="white", width=650, height=650)
        self.frame1.pack(fill="both", padx=40, pady=40, expand=True)

        # Label title
        self.title = tk.Label(self.frame1, font=("Open Sans", 60), text="RANDOM NUMBER\nGENERATOR", fg="black", bg="white", height=2, width=20, anchor="center", relief="flat")
        self.title.pack(side="top", pady=(40,0), expand=True)

        # Text generated number
        self.text_number = tk.Label(self.frame1, text="", font=("Open Sans", 230, "bold"), fg=dark_pink, bg="white", height=1, width=10, relief="flat", anchor="center")
        self.text_number.pack(pady=(5,5), expand=True)

        # Label text
        self.text = tk.Label(self.frame1, font=("Open Sans", 20), text="Please enter a positive number greater than 0", fg="black", bg="white", height=1, width=50, anchor="center", relief="flat")
        self.text.pack(pady=(20, 20), expand=True)

        # Entry number
        self.entry = tk.Entry(self.frame1, bg=light_pink, fg="black", font=("Open Sans", 20), relief="flat", width=5, highlightthickness=0, highlightcolor=light_pink)
        self.entry.pack(pady=(0,40), expand=True)
        self.entry.focus()
        self.entry.bind("<Return>", self.save_number)

        # Buttons frame
        self.frame_buttons = tk.Frame(self.frame1, bg="white", height=2)

        # Button yes
        self.button_yes = self.create_button("Yes", self.generate_number)

        # Button no
        self.button_no = self.create_button("No", self.start_again)

        # Button restart
        self.button_restart = self.create_button("Press here to restart!", self.restart)
        self.button_restart.config(width=15, height=2)

    def create_button(self, text, command):
        return tk.Button(self.frame_buttons, text=text, font=("Open Sans", 15), width=5, height=2,
                        foreground="black",
                        background=light_pink,
                        bd=0,
                        activebackground=medium_pink,
                        highlightbackground=light_pink,
                        highlightthickness=0,
                        command=command)
    

    def save_number(self, event):
        try:
            limit = int(self.entry.get())
            if limit > 0:
                self.entry.delete(0, tk.END)
                self.entry.pack_forget()

                self.numbers_list = list(range(1, limit+1))

                generated_number = choice(self.numbers_list)
                self.numbers_list.remove(generated_number)

                self.text_number.config(text=generated_number)
                self.text.config(text="Do you want another number?")

                self.button_yes.config(state="normal", background=light_pink, activebackground=medium_pink)
                self.button_no.config(state="normal", background=light_pink, activebackground=medium_pink)

                self.frame_buttons.pack(pady=(0,40))

                self.button_yes.pack(side="left", padx=10, expand=True)
                self.button_no.pack(side="left", padx=10, expand=True)

                self.button_yes.update_idletasks()
                self.button_no.update_idletasks()

            else:
                self.text.config(text="Invalid input! Please enter a positive number.")
                self.entry.delete(0, tk.END)

        except:
            self.text.config(text="Invalid input! Please enter a positive number.")
            self.entry.delete(0, tk.END)

    def generate_number(self):
        if self.numbers_list:
            generated_number = choice(self.numbers_list)
            self.numbers_list.remove(generated_number)
            self.text_number.config(text=generated_number)
        else:
            self.text.config(text="All numbers have been generated.")
            self.button_restart.config(state="normal", background=light_pink, activebackground=medium_pink)
            self.button_yes.pack_forget()
            self.button_no.pack_forget()
            self.button_restart.pack(expand=True)
            self.button_restart.update_idletasks()

    def restart(self):
        self.numbers_list = []
        self.entry.pack(pady=(0,40))
        self.entry.focus()
        self.entry.delete(0, tk.END)
        self.text.config(text="Please enter a positive number greater than 0.")
        self.text_number.config(text="")
        self.frame_buttons.pack_forget()
        self.button_restart.pack_forget()
        self.button_yes.pack_forget()
        self.button_no.pack_forget()

    def start_again(self):
        self.text.config(text="Do you want to start again?")
        self.button_restart.config(state="normal", background=light_pink, activebackground=medium_pink)
        self.button_yes.pack_forget()
        self.button_no.pack_forget()
        self.button_restart.pack(expand=True)
        self.button_restart.update_idletasks()

# Window configuration
window = tk.Tk()
window.title("Random number generator :)")
window.geometry("700x700")
window.configure(bg=light_pink)

app = RandomNumber(window)

window.mainloop()


