from tkinter import *
import requests


def get_quote():
    request = requests.get("https://taylor-swift-api.sarbo.workers.dev/lyrics?shouldRandomizeLyrics=true&numberOfParagraphs=1")
    request.raise_for_status()
    lyrics = request.json()["lyrics"][0]
    canvas.itemconfig(quote_text, text=lyrics, font=("Arial", 15, "bold"), fill="black")

window = Tk()
window.title("Taylor Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Taylor once said...", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

taylor_img = PhotoImage(file="taylor_n.png")
taylor_button = Button(image=taylor_img,
                       highlightthickness=0,
                       command=get_quote,
                       borderwidth=0)

taylor_button.grid(row=1, column=0)



window.mainloop()