import tkinter as tk
from tkinter import ttk

def main(number=""):
    """
    Чтение трехзначного числа справа налево
    """
    try:
        if len(number) != 3:
            return "На ввод принимается только 3 символа"
    except:
        return "На ввод принимается только 3 символа"

    try:
        int(number)
    except:
        return "Вы ввели не целое число, попробуйте снова"

    number_list = list(number)[::-1]
    answer = "".join(number_list)
    
    return answer

def on_submit():
    number = number_entry.get()
    result = main(number)
    result_label.config(text=result)

def on_clear():
    number_entry.delete(0, tk.END)
    result_label.config(text="")

root = tk.Tk()
root.resizable(False, False)
root.title("Перевернуть число")


frame = tk.Frame(root, padx=10, pady=10)
frame.grid(row=0, column=0, padx=10, pady=10)


number_label = tk.Label(frame, text="Введите трехзначное число:")
number_label.grid(row=0, column=0, pady=(0, 5), sticky=tk.W)


number_entry = tk.Entry(frame, width=15)
number_entry.grid(row=1, column=0, pady=(0, 10))


result_label = tk.Label(frame, text="", font=("Arial", 12), fg="orange")
result_label.grid(row=2, column=0, pady=(0, 10))


buttons_frame = tk.Frame(frame)
buttons_frame.grid(row=3, column=0, pady=(0, 10))


submit_button = tk.Button(buttons_frame, text="Преобразовать", command=on_submit)
submit_button.pack(side=tk.LEFT, padx=5)


clear_button = tk.Button(buttons_frame, text="Очистить", command=on_clear)
clear_button.pack(side=tk.LEFT, padx=5)


root.mainloop()