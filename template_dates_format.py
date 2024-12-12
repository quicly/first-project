import os
import re
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

TEMPLATES_DIR = r"C:\Vaults\Daily\Templates"

def update_dates_in_file(file_path):
    today = datetime.now().strftime('%Y-%m-%d')
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    pattern = r'\[\[\d{4}-\d{2}-\d{2}\|\d{4}-\d{2}-\d{2}\]\]'
    new_date = f'[[{today}|{today}]]'
    new_content = re.sub(pattern, new_date, content)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)
    return True

def process_directory():
    files_processed = 0
    files_updated = 0
    
    for filename in os.listdir(TEMPLATES_DIR):
        if filename.endswith('.md'):
            files_processed += 1
            file_path = os.path.join(TEMPLATES_DIR, filename)
            if update_dates_in_file(file_path):
                files_updated += 1
    
    messagebox.showinfo(
        "Обработка завершена",
        f"Обработано файлов: {files_processed}\n"
        f"Обновлено файлов: {files_updated}"
    )

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    process_directory()