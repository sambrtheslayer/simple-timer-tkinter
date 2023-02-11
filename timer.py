import time
import threading
import tkinter as tk
from tkinter import ttk

class Timer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("350x140")
        self.root.title("Параметры таймера")

        self.reset = False

        self.grid_layout_input_field = ttk.Frame(self.root)
        self.grid_layout_input_field.pack(pady=10)
        
        self.input_filed = ttk.Label(self.grid_layout_input_field, text="Введите количество минут: ", font=("Ubuntu", 12))
        self.input_filed.grid(row=0, column=0)

        self.input_filed = ttk.Entry(self.grid_layout_input_field)
        self.input_filed.grid(row=0, column=1)


        self.grid_layout_btn = ttk.Frame(self.root)
        self.grid_layout_btn.pack(pady=20)        

        self.start_btn = ttk.Button(self.grid_layout_btn, text="Запуск", command=self.start_timer_thread)
        self.start_btn.grid(row=1, column=0)

        self.stop_btn = ttk.Button(self.grid_layout_btn, text="Стоп", command=self.stop_clock)
        self.stop_btn.grid(row=1, column=1)

        self.reset_btn = ttk.Button(self.grid_layout_btn, text="Сброс", command=self.reset_clock)
        self.reset_btn.grid(row=1, column=2)


        self.top = tk.Toplevel()
        self.top.geometry("240x80")
        self.top.title("Таймер")
        self.top.attributes("-topmost", True)
        self.top.resizable(False, False)
        self.timer_label = ttk.Label(self.top, text="00:00", font=("Ubuntu", 46), foreground="#0F0")
        self.timer_label.pack()


        self.root.mainloop()

    def start_timer_thread(self):
        t = threading.Thread(target=self.start_timer)
        t.start()
        

    def start_timer(self):
        self.reset = False
        
        num_of_secs= int(self.input_filed.get()) * 60

        while not self.reset:
            if num_of_secs > 0:
                m, s = divmod(num_of_secs, 60)
                min_sec_format = '{:02d}:{:02d}'.format(m, s)
                print(min_sec_format)
                self.timer_label['foreground'] ="#0F0"
                self.timer_label['text'] = min_sec_format
                self.timer_label.update()
                time.sleep(1)
                num_of_secs -= 1
            else:
                m, s = 0, 0
                while not self.reset:
                    m, s = divmod(num_of_secs, 60)
                    min_sec_format = '{:02d}:{:02d}'.format(m, s)
                    print(min_sec_format)
                    self.timer_label['text'] = min_sec_format
                    self.timer_label['foreground'] ="#F00"
                    self.timer_label.update()
                    time.sleep(1)
                    num_of_secs += 1

    def reset_clock(self):
        self.reset = True
        self.timer_label['foreground'] ="#0F0"
        self.timer_label['text'] = "00:00"
    
    def stop_clock(self):
        self.reset = True

Timer()
