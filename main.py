from task_manager import TaskManager

if __name__ == "__main__":
    manager = TaskManager()

    while True:
        print("\n1. Registrar nueva tarea")
        print("2. Listar todas las tareas (orden de agregado)")
        print("3. Listar todas las tareas (orden de prioridad)")
        print("4. Buscar tarea por ID o por nombre")
        print("5. Editar nombre y descripción de una tarea por ID")
        print("6. Eliminar tarea por ID")
        print("7. Exportar tareas a un archivo")
        print("8. Salir")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            manager.register_task()
        elif choice == "2":
            print("Todas las tareas (orden de agregado):")
            for task in reversed(manager.get_tasks_by_order_added()):
                print(task)
        elif choice == "3":
            print("Todas las tareas (orden de prioridad):")
            for task in manager.get_all_tasks():
                print(task)
        elif choice == "4":
            search_term = input("Ingrese el ID o nombre de la tarea a buscar: ")
            results = manager.search_task(search_term)
            if results:
                print("Resultado de la búsqueda:")
                for task in results:
                    print(task)
            else:
                print("No se encontraron tareas con ese ID o nombre.")
        elif choice == "5":
            id = int(input("Ingrese el ID de la tarea a editar: "))
            new_name = input("Ingrese el nuevo nombre de la tarea: ")
            new_description = input("Ingrese la nueva descripción de la tarea: ")
            manager.edit_task(id, new_name, new_description)
            print("Tarea editada con éxito.")
        elif choice == "6":
            id = int(input("Ingrese el ID de la tarea a eliminar: "))
            manager.remove_task(id)
            print("Tarea eliminada con éxito.")
        elif choice == "7":
            file_path = input("Ingrese la ruta del archivo para exportar las tareas: ")
            manager.export_tasks(file_path)
            print("Tareas exportadas con éxito.")

        elif choice == "8":
            break
        else:
            print("Opción no válida. Por favor, seleccione nuevamente.")
