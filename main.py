from tkinter import *
from tkinter import ttk
from googletrans import Translator


def translate():
    for language, suffix in languages.items():
        if comboTwo.get() == language:
            text = t_input.get("1.0", END)
            print(text)
            translation = translator.translate(text, dest=suffix)
            t_output.delete("1.0", END)
            t_output.insert("1.0", translation.text)


root = Tk()
root.geometry("500x350")
root.title("Переводчик")
root.resizable(width=False, height=False)
root["bg"] = "black"

translator = Translator()
languages = {
    "Русский": "ru",
    "Английский": "en",
    "Французский": "fr",
    "Испанский": "es",
    "Немецкий": "de",
    "Итальянский": "it",
    "Португальский": "pt",
    "Японский": "ja",
    "Китайский (упрощенный)": "zh-CN",
    "Китайский (традиционный)": "zh-TW",
    "Корейский": "ko",
    "Арабский": "ar",
    "Турецкий": "tr",
    "Голландский": "nl",
    "Польский": "pl",
    "Шведский": "sv",
    "Датский": "da",
    "Норвежский": "no",
    "Финский": "fi",
    "Украинский": "uk",
    "Чешский": "cs",
    "Греческий": "el",
    "Иврит": "he",
    "Венгерский": "hu",
    "Румынский": "ro",
    "Хорватский": "hr",
    "Болгарский": "bg",
    "Словацкий": "sk",
    "Словенский": "sl",
    "Латинский": "la",
}


header_frame = Frame(root, bg="black")
header_frame.pack(fill=X)
header_frame.grid_columnconfigure(0, weight=1)
header_frame.grid_columnconfigure(1, weight=1)
header_frame.grid_columnconfigure(2, weight=1)

comboOne = ttk.Combobox(
    header_frame, values=[lang for lang in languages], state="readonly"
)
comboOne.current(0)
comboOne.grid(row=0, column=0)

label = Label(header_frame, fg="white", bg="black", font="Arial 17 bold", text="->")
label.grid(row=0, column=1)

comboTwo = ttk.Combobox(
    header_frame, values=[lang for lang in languages], state="readonly"
)
comboTwo.current(1)
comboTwo.grid(row=0, column=2)

t_input = Text(root, width=35, height=5, font="Arial 12 bold")
t_input.pack(pady=20)

btn = Button(root, width=45, text="Перевести", command=translate)
btn.pack()

t_output = Text(root, width=35, height=5, font="Arial 12 bold")
t_output.pack(pady=20)

root.mainloop()
