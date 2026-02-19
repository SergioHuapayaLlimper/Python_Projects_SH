import os
from tkinter import Tk, Text, Button, END, Label
from datetime import datetime
from gtts import gTTS

#Sergio Rodrigo Huapaya Llimper

#Función para guardar el texto en un .txt con la fecha y hora de guardado
def save_text():
    text = text_area.get('1.0', END)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"text_{timestamp}.txt"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
    status_label.config(text=f'Texto guardado como {filename}')

#Función para convertir el .txt en .mp3 y ser reproducido
def text_to_voice():
    files = [f for f in os.listdir() if f.startswith("text_") and f.endswith(".txt")]
    if not files:
        status_label.config(text="No hay archivos de texto guardados")
        return
    latest_txt = max(files, key=os.path.getmtime)
    with open(latest_txt, 'r', encoding='utf-8') as file:
        text = file.read()
    mp3_filename = latest_txt.replace(".txt", ".mp3")
    speech = gTTS(text=text, lang='es', slow=False)
    speech.save(mp3_filename)
    os.system(f'start {mp3_filename}')
    status_label.config(text=f'Reproduciento texto de {mp3_filename}')

#Creación de ventana principal
root = Tk()
root.title('Texto a Voz')

text_area = Text(root, height=10, width=50)
text_area.pack()

save_button = Button(root, text='Guardar Texto', command=save_text)
save_button.pack()

play_button = Button(root, text='Reproducir Texto', command=text_to_voice)
play_button.pack()

status_label = Label(root, text="" , fg="green")
status_label.pack()

root.mainloop()
