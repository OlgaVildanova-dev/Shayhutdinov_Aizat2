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
        self.date_entry = ttk.# Expense Tracker — пошаговая инструкция по созданию

В этом руководстве подробно описан процесс создания приложения для учёта личных расходов с графическим интерфейсом на Python. Программа будет поддерживать фильтрацию, подсчёт суммы за период, сохранение данных в JSON, валидацию ввода и работу с Git.

## 1. Установка зависимостей

Для реализации GUI используем библиотеку `tkinter`, для работы с датами — `datetime`, для JSON — стандартную библиотеку, для фильтрации — `pandas`.
