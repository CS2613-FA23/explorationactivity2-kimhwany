import os
from tkinter import *
from tkinter import messagebox
import speech_recognition as sr
from gtts import gTTS

def text_to_speech():
    text = text_entry.get("1.0", "end-1c")
    if len(text) <= 1:
        messagebox.showerror(message="Please enter text before converting to speech")
        return

    language = "en"  # Default language 
    speech = gTTS(text=text, lang=language, slow=False)
    speech.save("text.mp3")
    os.system("mpg123 text.mp3")

def list_microphones():
    mic_names = sr.Microphone().list_microphone_names()
    if not mic_names:
        messagebox.showinfo(message="No microphones found. Please ensure a microphone is connected.")
        return

    # Create a new window to display microphone names
    mic_window = Toplevel(window)
    mic_window.title("List of Microphones")

    # Calculate center coordinates of the main window
    window_x = window.winfo_rootx() + window.winfo_width() // 2
    window_y = window.winfo_rooty() + window.winfo_height() // 2

    # Set the size and position of the microphone window
    mic_window_width = 300
    mic_window_height = 200
    mic_window_x = window_x - mic_window_width // 2
    mic_window_y = window_y - mic_window_height // 2

    mic_window.geometry(f"{mic_window_width}x{mic_window_height}+{mic_window_x}+{mic_window_y}")

    # Create a listbox to display microphone names with some padding
    mic_listbox = Listbox(mic_window, selectmode=SINGLE, width=40, height=10)
    mic_listbox.pack(padx=10, pady=10)

    # Insert microphone names into the listbox
    for mic_name in mic_names:
        mic_listbox.insert(END, mic_name)


def speech_to_text():
    recorder = sr.Recognizer()

    try:
        timeout = int(duration_entry.get())
    except ValueError:
        messagebox.showerror(message="Enter a valid duration")
        return

    messagebox.showinfo(message="Please speak into the microphone and wait after finishing the recording")
    with sr.Microphone() as mic:
        recorder.adjust_for_ambient_noise(mic)
        try:
            audio_input = recorder.listen(mic, timeout=timeout)
            text_output = recorder.recognize_google(audio_input)

            messagebox.showinfo(message="Speech recognition successful. You said:\n" + text_output)
        except sr.UnknownValueError:
            messagebox.showinfo(message="Speech recognition could not understand the audio")
        except sr.RequestError as e:
            messagebox.showinfo(message=f"Error: Could not request results from Google Speech Recognition service. {e}")

# Create the main window
window = Tk()

# Calculate the center coordinates of the screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = 500
window_height = 300

window_x = (screen_width - window_width) // 2
window_y = (screen_height - window_height) // 2

# Set the size and position of the main window
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.resizable(0, 0)
window.title("Talk2Text & Text2Talk")
window.geometry("500x300")

# Create and place the UI elements
Label(window, text="Text:", font=('Arial', 16, 'bold')).place(x=10, y=20)
text_entry = Text(window, width=50, height=5)
text_entry.place(x=90, y=20)

Label(window, text="Duration:", font=('Arial', 16, 'bold')).place(x=10, y=140)
duration_entry = Entry(window, width=38)
duration_entry.place(x=90, y=140)

button1 = Button(window, text='List Available Microphones', bg='Turquoise', fg='Black', command=list_microphones)
button1.place(x=90, y=190)

button2 = Button(window, text='Text to Speech', bg='Turquoise', fg='Black', command=text_to_speech)
button2.place(x=90, y=220)

button3 = Button(window, text='Speech to Text', bg='Turquoise', fg='Black', command=speech_to_text)
button3.place(x=90, y=250)

window.mainloop()
