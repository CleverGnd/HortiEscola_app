# gui.py
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label
from app.utils.authenticator import Authenticator

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(
    r"C:\Users\cleverG\Desktop\Alpha EdTech\Tkinter-Designer-master\build\assets\frame0"
)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("360x800")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=800,
    width=360,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)

canvas.place(x=0, y=0)
canvas.create_rectangle(0.0, 0.0, 360.0, 800.0, fill="#7BA42C", outline="")

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(185.0, 144.0, image=image_image_1)

canvas.create_text(
    46.0, 305.0, anchor="nw", text="Usuário:", fill="#FFFFFF", font=("Inter", 12 * -1)
)

canvas.create_text(
    46.0,
    585.0,
    anchor="nw",
    text="Ainda não possui cadastro?\n\n",
    fill="#FFFFFF",
    font=("Poppins Medium", 20 * -1),
)

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(180.0, 358.5, image=entry_image_1)
entry_1 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
entry_1.place(x=48.0, y=336.0, width=264.0, height=43.0)

canvas.create_text(
    46.0, 400.0, anchor="nw", text="Senha:", fill="#FFFFFF", font=("Inter", 12 * -1)
)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(180.0, 453.5, image=entry_image_2)
entry_2 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
entry_2.place(x=48.0, y=431.0, width=264.0, height=43.0)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
)
button_1.place(x=145.0, y=500.0, width=175.0, height=45.0)

message_label = Label(window, text="", font=("Inter", 12), bg="#FFFFFF")
message_label.place(x=48.0, y=550.0)


button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat",
)

authenticator = Authenticator("data/users.json")


def run_app():
    window.mainloop()


def login():
    username = entry_1.get()
    password = entry_2.get()
    if authenticator.authenticate(username, password):
        message_label.config(text="Usuário logado com sucesso!")
    else:
        message_label.config(text="Usuário ou senha inválidos!")


button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=login,
    relief="flat",
)
button_1.place(x=145.0, y=500.0, width=175.0, height=45.0)
