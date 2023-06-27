from tkinter import *
from tkinter import ttk
from googletrans import Translator

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
    "Латинский": "la"
}

def translate():
    selected_language = comboTwo.get()
    if selected_language in languages:
        text = input_text.get("1.0", END)
        translation = translator.translate(text, dest=languages[selected_language])
        output_text.delete("1.0", END)
        output_text.insert("1.0", translation.text)

root = Tk()
root.geometry("500x350")
root.title("Переводчик")
root.resizable(width=False, height=False)
root.config(bg="black")

header_frame = Frame(root, bg="black")
header_frame.pack(fill=X)
header_frame.grid_columnconfigure(0, weight=1)
header_frame.grid_columnconfigure(1, weight=1)
header_frame.grid_columnconfigure(2, weight=1)

comboOne = ttk.Combobox(header_frame, values=list(languages.keys()), state="readonly")
comboOne.current(0)
comboOne.grid(row=0, column=0)

label = Label(header_frame, fg="white", bg="black", font="Arial 17 bold", text="->")
label.grid(row=0, column=1)

comboTwo = ttk.Combobox(header_frame, values=list(languages.keys()), state="readonly")
comboTwo.current(1)
comboTwo.grid(row=0, column=2)

input_text = Text(root, width=35, height=5, font="Arial 12 bold")
input_text.pack(pady=20)

translate_button = Button(root, width=45, text="Перевести", command=translate)
translate_button.pack()

output_text = Text(root, width=35, height=5, font="Arial 12 bold")
output_text.pack(pady=20)

root.mainloop()
