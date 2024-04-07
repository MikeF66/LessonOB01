class Task():
  def __init__(self, name, date, done=False):
      self.name = name
      self.date = date
      self.done = done

class TaskManager():
  def __init__(self):
      self.tasks = []

  def add_task(self, name, date, done=False):
      self.tasks.append(Task(name, date, done))

  def mark_task_as_done(self, name):
      found = False
      for task in self.tasks:
          if task.name == name:
              task.done = True
              print("Задача:", name, "выполнена")
              found = True
              break
      if not found:
          print("Задачи:", name, "нет в вашем списке")

  def current_tasks(self):
      current_tasks = [task for task in self.tasks if not task.done]
      if current_tasks:
          print("Список текущих задач:")
          for task in current_tasks:
              print("Задача:", task.name, "Срок выполнения:", task.date)
      else:
          print("У вас нет текущих задач")

manager = TaskManager()
manager.add_task("Выполнить задание к уроку.", "07.04.2024")
manager.add_task("Сходить в магазин.", "07.04.2024")
manager.add_task("Позаниматься английским.", "07.04.2024")
manager.current_tasks()
print("")
manager.mark_task_as_done("Сходить в магазин.")
manager.current_tasks()
print("")
manager.mark_task_as_done("Выполнить задание к уроку.")
manager.current_tasks()
print("")
manager.mark_task_as_done("Позаниматься английским.")
manager.current_tasks()
