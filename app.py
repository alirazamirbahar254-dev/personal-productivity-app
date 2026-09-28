
#customtkinter for UI intigretion 
import customtkinter as ctk
app = ctk.CTk()
#window size
app.geometry("1200x700")
# window title
app.title("Personal Productivity")
# access to user can be adjest the window size
app.resizable(True, True)
labels = ctk.CTkLabel(app, text = "Hello world")
labels.pack()











































# Keep the application running
app.mainloop()


