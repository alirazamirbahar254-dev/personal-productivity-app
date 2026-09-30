
#customtkinter for UI intigretion 
import customtkinter as ctk
import warnings
from tkinter_icons import LucideIcon
warnings.filterwarnings("ignore", message="CTkButton Warning: Given image is not CTkImage")
app = ctk.CTk()
#window size
app.geometry("1200x700")
# window title
app.title("Personal Productivity")
# access to user can be adjest the window size
app.resizable(True, True)

# creating a sidebar
sidebar = ctk.CTkFrame(app, width=200,border_width=1,border_color="#8A8A8A")

# placeing and desplay to it 
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)

#slide baar buttons icon
dashboard_icon = LucideIcon("house", size=20,color="#1E1EE0")
tasks_icon = LucideIcon("check", size=20,color="#1E1EE0")
notes_icon = LucideIcon("notebook", size=20,color="#1E1EE0")
analytics_icon = LucideIcon("chart-no-axes-combined", size=20,color="#1E1EE0")
settings_icon = LucideIcon("settings", size=20,color="#1E1EE0")

#slide baar title
slidebar_name = ctk.CTkLabel(sidebar, text="Productivity",anchor="w",text_color="white",font=("Arial", 14, "bold"))
slidebar_name.pack(pady=(10, 5), padx=15, fill="x")

# sidebar buttons
dashboard_btn = ctk.CTkButton(sidebar, text="Dashboard",image=dashboard_icon,fg_color="transparent",anchor="w")
dashboard_btn.pack(pady="5", padx=15, fill="x")

task_btn = ctk.CTkButton(sidebar, text="Tasks", image=tasks_icon,fg_color="transparent",anchor="w")
task_btn.pack(pady="5", padx=15, fill="x")

notes_btn = ctk.CTkButton(sidebar, text="Notes",image=notes_icon,fg_color="transparent",anchor="w")
notes_btn.pack(pady="5", padx=15, fill="x")

analytics_btn = ctk.CTkButton(sidebar, text="Analytics",image=analytics_icon, fg_color="transparent",anchor="w")
analytics_btn.pack(pady="5", padx=15, fill="x")

settings_btn = ctk.CTkButton(sidebar, text="Settings",image=settings_icon,fg_color="transparent",anchor="w")
settings_btn.pack(pady="5", padx=15, fill="x")

main_content =ctk.CTkFrame(app)
main_content.pack(side="left", fill="both", expand=True)

header_frame =ctk.CTkFrame(main_content)
header_frame.pack(side="top",fill="x")

#Add a label to main window
dashboard_title = ctk.CTkLabel(header_frame, text ="Dashboard",font=("Arial", 24, "bold"))
dashboard_title.pack(anchor="w",padx=35, pady=(30, 0))

dashboard_description= ctk.CTkLabel(header_frame, text="Your productivity overview",font=("Arial", 14))
dashboard_description.pack(anchor="w",padx=35, pady=(0, 10))


# Keep the application running
app.mainloop()




