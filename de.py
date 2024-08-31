import scipy.io.wavfile as wav
import numpy as np

# Загружаем аудиофайл
filename = '404.wav'  # Замените на имя вашего файла
fs, data = wav.read(filename)
wav.write("reversed_audio.wav", fs, data.astype(np.int16))

# Проверка характеристик файла
print(f"Частота дискретизации: {fs} Гц")
print(f"Тип данных: {data.dtype}")

# Преобразование в список (если нужно)
data_list = data.tolist()

# Вывод первых 10 элементов списка для проверки
print(data_list[:10])
print(len(data_list))
for i in range(0, len(data_list), 8000):
    try:
        new_data = np.array(data_list[i-20000:i+20000])
        if len(new_data) == 40000:
            print(i//8000)
            data_reversed = np.flip(new_data)
            wav.write(str(i//8000)+".wav", 8000, new_data.astype(np.int16))
    except IndexError:
        pass