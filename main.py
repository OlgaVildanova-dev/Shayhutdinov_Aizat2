import tkinter as tk
from tkinter import ttk, messagebox
import json
import re

class WeatherDiaryApp:
    def __init__(self, root):
        self.root = root
        self.records = []
        # ... создание виджетов, привязка методов к кнопкам

    def add_record(self):
        date = self.date_entry.get()
        temp = self.temp_entry.get()
        desc = self.desc_entry.get()
        precip = self.precip_var.get()
        # Валидация ввода
        if not self.validate_input(date, temp, desc):
            return
        self.records.append({
            "date": date,
            "temperature": float(temp),
            "description": desc,
            "precipitation": precip == 1
        })
        self.update_list()

    def validate_input(self, date, temp, desc):
        if not re.match(r"\d{2}.\d{2}.\d{4}", date):
            messagebox.showerror("Ошибка", "Неверный формат даты (ДД.ММ.ГГГГ)")
            return False
        try:
            float(temp)
        except ValueError:
            messagebox.showerror("Ошибка", "Температура должна быть числом")
            return False
        if not desc:
            messagebox.showerror("Ошибка", "Описание не может быть пустым")
            return False
        return True

    def save_to_json(self):
        with open("data/records.json", "w") as f:
            json.dump(self.records, f, ensure_ascii=False, indent=4)

    def load_from_json(self):
        try:
            with open("data/records.json", "r") as f:
                self.records = json.load(f)
                self.update_list()
        except FileNotFoundError:
            messagebox.showinfo("Информация", "Файл данных не найден")

    # ... методы фильтрации, обновления списка и т.д.
