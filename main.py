import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime
import pandas as pd

DATA_FILE = "expenses.json"

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("800x500")

        self.create_widgets()
        self.load_data()
        self.update_table()

    def create_widgets(self):
        # Поля ввода
        ttk.Label(self.root, text="Сумма:").grid(row=0, column=0, padx=10, pady=5)
        self.amount_entry = ttk.Entry(self.root)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Категория:").grid(row=1, column=0, padx=10, pady=5)
        self.category_entry = ttk.Entry(self.root)
        self.category_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Дата (ГГГГ-ММ-ДД):").grid(row=2, column=0, padx=10, pady=5)
        self.date_entry = ttk.Entry(self.root)
        self.date_entry.grid(row=2, column=1, padx=10, pady=5)

        # Кнопка добавления
        ttk.Button(self.root, text="Добавить расход", command=self.add_expense).grid(row=3, column=0, columnspan=2, pady=10)

        # Фильтры
        ttk.Label(self.root, text="Фильтр по категории:").grid(row=4, column=0, padx=10)
        self.filter_category = ttk.Entry(self.root)
        self.filter_category.grid(row=4, column=1, padx=10)

        ttk.Label(self.root, text="Фильтр по дате (ГГГГ-ММ-ДД):").grid(row=5, column=0, padx=10)
        self.filter_date = ttk.Entry(self.root)
        self.filter_date.grid(row=5, column=1, padx=10)

        ttk.Button(self.root, text="Применить фильтр", command=self.apply_filter).grid(row=6, column=0, columnspan=2, pady=5)

        # Таблица расходов
        self.tree = ttk.Treeview(self.root, columns=("amount", "category", "date"), show='headings')
        self.tree.heading("amount", text="Сумма")
        self.tree.heading("category", text="Категория")
        self.tree.heading("date", text="Дата")
        self.tree.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Подсчёт суммы за период
        ttk.Label(self.root, text="Сумма за период:").grid(row=8, column=0, padx=10)
        self.sum_label = ttk.Label(self.root, text="0")
        self.sum_label.grid(row=8, column=1, padx=10)

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                self.expenses = json.load(f)
        else:
            self.expenses = []

    def save_data(self):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(self.expenses, f, ensure_ascii=False, indent=2)

    def add_expense(self):
        amount = self.amount_entry.get()
        category = self.category_entry.get()
        date = self.date_entry.get()

        # Валидация суммы
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Сумма должна быть положительной")
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректную сумму (положительное число)")
            return

        # Валидация даты
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Ошибка", "Дата должна быть в формате ГГГГ-ММ-ДД")
            return

        self.expenses.append({"amount": amount, "category": category, "date": date})
        self.save_data()
        self.update_table()

    def update_table(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        for exp in self.expenses:
            self.tree.insert("", "end", values=(exp["amount"], exp["category"], exp["date"]))

    def apply_filter(self):
        cat_filter = self.filter_category.get()
        date_filter = self.filter_date.get()

        filtered = self.expenses

        if cat_filter:
            filtered = [e for e in filtered if e["category"].lower() == cat_filter.lower()]

        if date_filter:
            try:
                datetime.strptime(date_filter, "%Y-%m-%d")
                filtered = [e for e in filtered if e["date"] == date_filter]
            except ValueError:
                messagebox.showerror("Ошибка", "Дата фильтра должна быть в формате ГГГГ-ММ-ДД")
                return

        # Очистка и заполнение таблицы отфильтрованными данными
        for i in self.tree.get_children():
            self.tree.delete(i)

        for exp in filtered:
            self.tree.insert("", "end", values=(exp["amount"], exp["category"], exp["date"]))

    def calculate_sum_for_period(self):
        # Пример: можно добавить поля для выбора периода и кнопку подсчёта суммы.
        # Для простоты считаем сумму по всем расходам.
        total = sum(e["amount"] for e in self.expenses)
        self.sum_label.config(text=f"{total:.2f} ₽")


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    app.calculate_sum_for_period()
    root.mainloop()
