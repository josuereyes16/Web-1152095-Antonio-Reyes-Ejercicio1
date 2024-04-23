from datetime import datetime
from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, id):
        self.tasks = [task for task in self.tasks if task.id != id]

    def get_task_by_id(self, id):
        for task in self.tasks:
            if task.id == id:
                return task
        return None
    
    def get_tasks_by_order_added(self):
        return self.tasks[:]
    
    def get_all_tasks(self):
        return sorted(self.tasks, key=lambda x: (x.priority, x.created_at))

    def register_task(self):
        id = len(self.tasks) + 1
        name = input("Nombre de la tarea: ")
        description = input("Descripción de la tarea: ")
        while True:
            try:
                priority = int(input("Prioridad de la tarea (1: alta, 2: media, 3: baja): "))
                if priority not in [1, 2, 3]:
                    raise ValueError
                break
            except ValueError:
                print("Por favor, ingrese una prioridad válida (1, 2 o 3).")

        created_at = datetime.now()
        task = Task(id, name, description, priority, created_at)
        self.add_task(task)
        print("Tarea registrada con éxito.")

    def search_task(self, search_term):
        results = []
        for task in self.tasks:
            if str(task.id) == search_term or task.name.lower() == search_term.lower():
                results.append(task)
        return results    

    def edit_task(self, id, new_name, new_description):
        for task in self.tasks:
            if task.id == id:
                task.name = new_name
                task.description = new_description
                break

    def export_tasks(self, file_path):
        with open(file_path, 'w') as file:
            for task in self.tasks:
                file.write(f"ID: {task.id}, Name: {task.name}, Description: {task.description}, Priority: {task.priority}, Created at: {task.created_at}\n")