import os
import tkinter as tk
import threading
import pyaudio
import numpy as np
import scipy.io.wavfile as wav

CHUNK = 1000
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 8000

p = pyaudio.PyAudio()


def start_thread_1():
    print("Поток 1 запущен")
    name = len(os.listdir(os.fsencode("404")))
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    frames = []
    num_samples = 40000
    while len(frames) * CHUNK < num_samples:
        data = stream.read(CHUNK)
        frames.append(data)

    # Объединяем все фрагменты в один массив NumPy
    np_array = np.frombuffer(b''.join(frames), dtype=np.int16)
    stream.stop_stream()
    stream.close()
    np_array = np_array.astype(np.int16)
    wav.write("404/NEW" + str(name) + ".wav", 8000, np_array)
    print("Поток 1 закрыт")


def start_thread_2():
    print("Поток 2 запущен")
    name = len(os.listdir(os.fsencode("noth")))
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    frames = []
    num_samples = 40000
    while len(frames) * CHUNK < num_samples:
        data = stream.read(CHUNK)
        frames.append(data)

    # Объединяем все фрагменты в один массив NumPy
    np_array = np.frombuffer(b''.join(frames), dtype=np.int16)
    stream.stop_stream()
    stream.close()
    np_array = np_array.astype(np.int16)
    wav.write("noth/NEW" + str(name) + ".wav", 8000, np_array)
    print("Поток 2 закрыт")


def start_thread_3():
    print("Запущена модель")
    os.system('''"C:\\Users\i5 6400\AppData\Local\Programs\Python\Python38\python.exe" main.py''')


def create_gui():
    root = tk.Tk()
    root.title("Мое окно")
    root.geometry("600x470")  # Устанавливаем размер окна

    button1 = tk.Button(root, text="404", command=lambda: threading.Thread(target=start_thread_1).start(),
                        height=5)
    button1.pack(fill=tk.X)  # Растягиваем по горизонтали, отступы

    button2 = tk.Button(root, text="Шум", command=lambda: threading.Thread(target=start_thread_2).start(),
                        height=5)
    button2.pack(fill=tk.X)
    button3 = tk.Button(root, text="Запуск модели", command=lambda: threading.Thread(target=start_thread_3).start(),
                        height=5)
    button3.pack(fill=tk.X)
    root.mainloop()
    p.terminate()


if __name__ == "__main__":
    create_gui()
