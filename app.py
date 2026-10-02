
#customtkinter for UI intigretion 
import customtkinter as ctk
import warnings

#for charting we are using matplotlib
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#importing a icon library for icons in the sidebar and header
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
sidebar = ctk.CTkFrame(app, width=200,border_width=1,border_color="#8A8A8A",fg_color="transparent")
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
slidebar_name = ctk.CTkLabel(sidebar, text="Productivity",anchor="w",text_color="white",fg_color="transparent",font=("Arial", 14, "bold"))
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

main_content =ctk.CTkFrame(app,)
main_content.pack(side="left", fill="both", expand=True)

header_frame =ctk.CTkFrame(main_content,fg_color="transparent")
header_frame.pack(side="top",fill="x")


#Add a label to main window
dashboard_title = ctk.CTkLabel(header_frame, text ="Dashboard",font=("Arial", 24, "bold"))
dashboard_title.pack(anchor="w",padx=40, pady=(30, 0))

dashboard_description= ctk.CTkLabel(header_frame, text="Your productivity overview",font=("Arial", 14))
dashboard_description.pack(anchor="w",padx=42, pady=(0, 10))

#profile button 
profile_icon = LucideIcon("circle-user-round", size=38,color="#1E1EE0")
profile_btn= ctk.CTkButton(header_frame,text="",image=profile_icon,fg_color="transparent",corner_radius=50,width=30,height=30,font=("Arial", 15, "bold") )
profile_btn.place(relx=1.0, x=-27, y=40, anchor="ne")

#cards_container 
cards_container =ctk.CTkFrame(main_content,fg_color="transparent")
cards_container.pack(side="top",fill="both",padx=30,pady=5)

cards_container.grid_columnconfigure(0, weight=1)
cards_container.grid_columnconfigure(1, weight=1)

cards_container.grid_rowconfigure(0, weight=1)
cards_container.grid_rowconfigure(1, weight=1)

def create_card(title, number, row, column):
    
    Productivity_card=ctk.CTkFrame(cards_container,corner_radius=10,border_width=1,border_color="#1E1EE0",fg_color="#F8F9FC")
    Productivity_card.grid(row=row,column=column,padx=10,pady=10, sticky="nsew")

    Productivity_card_label = ctk.CTkLabel(Productivity_card,text=title,text_color="black",fg_color="#F8F9FC",border_width=0)
    Productivity_card_label.pack( padx=40,pady=(25, 3),anchor="w")

    Productivity_card_number = ctk.CTkLabel(Productivity_card,text=number,text_color="black",fg_color="#F8F9FC",border_width=0,font=("Arial", 24, "bold"))
    Productivity_card_number.pack(padx=40,pady=(0, 25),anchor="w")
    Productivity_card.grid_propagate(False)

create_card("Total Tasks", "24",0,0)
create_card("Completed", "16", 0, 1) 
create_card("Pending", "8", 1, 0)
create_card("Productivity", "67%", 1, 1)


# chart container
chart_container = ctk.CTkFrame(
    main_content,
    border_color="blue",
    border_width=1,
    height=300,
    width=1088,
    corner_radius=10
)

chart_container.pack(pady=10, padx=30, anchor="center")
chart_container.pack_propagate(False)   # container ka size fix

# Matplotlib chart
fig = Figure(dpi=100, layout="constrained")
ax = fig.add_subplot(1, 1, 1)

ax.set_facecolor("#F8F9FC")
fig.patch.set_facecolor("#FFFFFF")

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
productivity = [50, 70, 30, 80, 60, 40, 90]
bars = ax.bar(days, productivity, width=0.5, color="#1E1EE0",edgecolor="black", linewidth=1, alpha=0.8)
             
ax.bar_label(bars)

ax.set_xlabel("Days of the Week")
ax.set_ylabel("Productivity Score")
ax.set_title("Weekly Productivity Overview")

ax.grid(axis="y", alpha=0.2)
ax.set_axisbelow(True)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Chart: pack se, container ke size ke mutabiq
canvas = FigureCanvasTkAgg(fig, master=chart_container)
canvas.get_tk_widget().pack(fill="both", expand=True, padx=5, pady=5)
canvas.draw()

# Button: chart ke upar, top-right corner mein
calendar_icon = LucideIcon("calendar", size=20, color="#1E1EE0")
calendar = ctk.CTkButton(
    chart_container,
    image=calendar_icon,
    text="",
    width=32,
    height=32,
    corner_radius=6,
    fg_color="#FFFFFF",
    bg_color="#FFFFFF",        # <-- yeh kone theek karega
    hover_color="#E6E6FA",
    border_width=0
    
)

calendar.place(relx=0.0, rely=0.0, x=8, y=8, anchor="nw")
calendar.lift()

# Keep the application running
app.mainloop()

