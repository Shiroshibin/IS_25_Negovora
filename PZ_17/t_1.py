"""
Вариант 21

В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
приближенный к оригиналу (см. таблицу 1).
"""


import tkinter as tk
from tkinter import ttk

def on_submit():
    print("Data submitted")
    root.quit()

def on_cancel():
    print("Input cancelled")
    root.quit()

root = tk.Tk()
root.resizable(False, False)


title = tk.Label(root, text="Форма регистрации пользователя", font=("Arial", 14))
title.grid(row=0, column=0, columnspan=2, pady=10)


tk.Label(root, text="Ваше имя:").grid(row=1, column=0, sticky=tk.W, pady=(10, 0))
name_entry = tk.Entry(root, background="lightgrey")
name_entry.grid(row=1, column=1, pady=(10, 0))


tk.Label(root, text="Пароль:").grid(row=2, column=0, sticky=tk.W, pady=(10, 0))
password_entry = tk.Entry(root, show="*", background="lightgrey")
password_entry.grid(row=2, column=1, pady=(10, 0))


tk.Label(root, text="Возраст:").grid(row=3, column=0, sticky=tk.W, pady=(10, 0))
age_entry = tk.Entry(root, background="lightgrey")
age_entry.grid(row=3, column=1, pady=(10, 0))


tk.Label(root, text="Пол:").grid(row=4, column=0, sticky=tk.W, pady=(10, 0))
gender_frame = tk.Frame(root)
gender_var = tk.StringVar()
tk.Radiobutton(gender_frame, text="Мужской", variable=gender_var, value="Мужской").pack(side=tk.LEFT)
tk.Radiobutton(gender_frame, text="Женский", variable=gender_var, value="Женский").pack(side=tk.LEFT)
gender_frame.grid(row=4, column=1, pady=(10, 0))


tk.Label(root, text="Ваши увлечения:").grid(row=5, column=0, sticky=tk.W, pady=(10, 0))
hobbies_frame = tk.Frame(root)
music_var = tk.BooleanVar()
video_var = tk.BooleanVar()
drawing_var = tk.BooleanVar()
tk.Checkbutton(hobbies_frame, text="Музыка", variable=music_var).pack(side=tk.LEFT)
tk.Checkbutton(hobbies_frame, text="Видео", variable=video_var).pack(side=tk.LEFT)
tk.Checkbutton(hobbies_frame, text="Рисование", variable=drawing_var).pack(side=tk.LEFT)
hobbies_frame.grid(row=5, column=1, pady=(10, 0))


tk.Label(root, text="Ваша страна:").grid(row=6, column=0, sticky=tk.W, pady=(10, 0))
country_combo = ttk.Combobox(root)
country_combo['values'] = ("Country 1", "Country 2", "Country 3")
country_combo.grid(row=6, column=1, pady=(10, 0))


tk.Label(root, text="Ваш город:").grid(row=7, column=0, sticky=tk.W, pady=(10, 0))
city_combo = ttk.Combobox(root)
city_combo['values'] = ("City 1", "City 2", "City 3")
city_combo.grid(row=7, column=1, pady=(10, 0))


tk.Label(root, text="Кратко о себе:").grid(row=8, column=0, sticky=tk.W+tk.N, pady=(10, 0))
about_text = tk.Text(root, height=4, width=30, background="lightgrey")
about_text.grid(row=8, column=1, pady=(15, 0))


tk.Label(root, text="Решите пример, запишите результат в поле ниже:").grid(row=9, column=0, columnspan=2, sticky=tk.W, pady=(10, 0))
example_entry = tk.Entry(root, background="lightgrey")
example_entry.grid(row=10, column=0, columnspan=2, pady=(10, 0))


button_frame = tk.Frame(root)
cancel_button = tk.Button(button_frame, text="Отменить ввод", command=on_cancel)
submit_button = tk.Button(button_frame, text="Данные подтверждаю", command=on_submit)
cancel_button.pack(side=tk.LEFT, padx=5)
submit_button.pack(side=tk.LEFT, padx=5)
button_frame.grid(row=11, column=0, columnspan=2, pady=10)

root.mainloop()