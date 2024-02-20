import tkinter as tk
import numpy as np

G = 6.6743e-11  # гравитационная постоянная

# Создание графического интерфейса
root = tk.Tk()
root.title("Вычисление радиальной скорости")
root.geometry("400x225")


# Функция для вычисления радиальной скорости
def calc_vrad():
    # Извлечение значений из полей ввода
    try:
        ms_val = float(ms_entry.get()) * 2e30
        p_val = float(p_entry.get()) * 86400
        mp_val = float(mp_entry.get()) * 1.89e27

        # Вычисление радиальной скорости
        a_val = ((G * ms_val) / (4 * np.pi ** 2) * p_val ** 2) ** (1 / 3)
        vrad_val = (2 * np.pi * a_val * mp_val) / (p_val * ms_val)

        # Вывод результата
        result_label.config(text=f"Радиальная скорость: {vrad_val:.2f} м/с", fg="green")
    except ValueError:
        # Вывод сообщения об ошибке, если введены некорректные значения
        result_label.config(text="Ошибка: введите корректные значения", fg="red")


# Создание полей ввода и меток для них
ms_label = tk.Label(root, text="Масса звезды (в массах Солнца):")
ms_label.pack()
ms_entry = tk.Entry(root)
ms_entry.pack()

p_label = tk.Label(root, text="Период орбиты экзопланеты (в днях):")
p_label.pack()
p_entry = tk.Entry(root)
p_entry.pack()

mp_label = tk.Label(root, text="Масса экзопланеты (в массах Юпитера):")
mp_label.pack()
mp_entry = tk.Entry(root)
mp_entry.pack()

calc_button = tk.Button(root, text="Рассчитать", command=calc_vrad, bg="#4CAF50", fg="white", font=("Arial", 12))
calc_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack()

root.mainloop()
