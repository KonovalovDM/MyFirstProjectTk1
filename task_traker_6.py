import tkinter as tk
import os

# Пути к файлам для сохранения активных и выполненных задач
TASKS_FILE = "tasks.txt"
COMPLETED_TASKS_FILE = "completed_tasks.txt"

# Функция загрузки задач из файла
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            tasks = file.readlines()
            for task in tasks:
                task_listBox.insert(tk.END, task.strip())

    if os.path.exists(COMPLETED_TASKS_FILE):
        with open(COMPLETED_TASKS_FILE, "r", encoding="utf-8") as file:
            tasks = file.readlines()
            for task in tasks:
                completed_listBox.insert(tk.END, task.strip())

# Функция сохранения задач в файл
def save_tasks():
    tasks = task_listBox.get(0, tk.END)
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")

    completed_tasks = completed_listBox.get(0, tk.END)
    with open(COMPLETED_TASKS_FILE, "w", encoding="utf-8") as file:
        for task in completed_tasks:
            file.write(task + "\n")

# Функция добавления задачи в План, которая запускается по нажатию кнопки
def task_writing():
    task = entry.get()
    if task != '':
        task_listBox.insert(tk.END, task)
        entry.delete(0, tk.END)
        label.config(text=f'\nВнесите задачу в План\nЗадача записана, можно внести следующую\n')
        save_tasks()  # Сохраняем задачи после добавления новой

# Функция удаления задачи из Плана, которая запускается по нажатию кнопки
def task_deleting():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.delete(selected_task[0])
        label.config(text=f'\nВнесите задачу в План\nДанная задача удалена\n')
        save_tasks()  # Сохраняем задачи после удаления

# Функция маркировки задачи при выполнении, которая запускается по нажатию кнопки
def mark_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task = task_listBox.get(selected_task[0])
        completed_listBox.insert(tk.END, task)
        task_listBox.delete(selected_task[0])
        label.config(text=f'\nВнесите задачу в План\nДанная задача отмечена как выполненная\n')
        save_tasks()  # Сохраняем задачи после изменения

def on_entry_change(event):
    current_text = entry.get().upper()
    entry.delete(0, tk.END)
    entry.insert(0, current_text)

# Создаем главное окно приложения, задаём его размеры (ширина х высота) и заголовок
root = tk.Tk()
root.geometry('850x850')
root.title('Управление задачами "План задач"')
root.configure(background='#F0F0F5')

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

label = tk.Label(root, text='\nВнесите задачу в План', background='#E0E0E0', fg='#000000')
label.grid(row=0, column=0, columnspan=2, pady=10)

entry = tk.Entry(root, justify='center', bg='#FFFFFF')
entry.grid(row=1, column=0, columnspan=2, pady=10, sticky='ew')
entry.bind('<KeyRelease>', on_entry_change)

button = tk.Button(root, text='Нажать для записи задачи в План', command=task_writing, bg='#4CAF50', fg='#000000')
button.grid(row=2, column=0, columnspan=2, pady=10)

delete_button = tk.Button(root, text='Удалить задачу из Плана', command=task_deleting, bg='#4CAF50', fg='#333333')
delete_button.grid(row=3, column=0, columnspan=2, pady=10)

mark_button = tk.Button(root, text='Отметить задачу как выполненную', command=mark_task, bg='#4CAF50', fg='#333333')
mark_button.grid(row=4, column=0, columnspan=2, pady=10)

text1 = tk.Label(root, text='Список задач в Плане', justify='left', bg='#E0E0E0')
text1.grid(row=5, column=0, pady=10)

text2 = tk.Label(root, text='Выполненные задачи', justify='left', bg='#E0E0E0')
text2.grid(row=5, column=1, pady=10)

task_listBox = tk.Listbox(root, height=34, width=40, bg='#E0E0E0', fg='blue violet')
task_listBox.grid(row=6, column=0, pady=10, sticky='ew')

completed_listBox = tk.Listbox(root, height=34, width=40, bg='#E0E0E0', fg='blue violet')
completed_listBox.grid(row=6, column=1, pady=10, sticky='ew')

# Загрузка задач при запуске программы
load_tasks()

# Запускаем главный цикл обработки событий приложения
root.mainloop()
