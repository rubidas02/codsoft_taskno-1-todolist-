class toDoList:
    def __init__(self):
        self.tasks=[]
    def addtask(self,task):
    
            self.tasks.append(task)
            print("Task added successfully")
        
    def deletetask(self,index):
        if index>0 and index<=len(self.tasks):
            self.tasks.pop(index-1)
            print(f"Task number {index} was deleted successfully")
        else:
            print("Invalid index")
    def displaytask(self):
        print("Tasks remaining:\n")
        for i,task in enumerate(self.tasks):
            
            print(f"{i+1}. {task}")
    def updatetask(self,update,index):
        if index>0 and index<=len(self.tasks):
            self.tasks[index-1]=update
            print(f"Task number {index} is updated successfully")
    def clearall(self):
        self.tasks.clear()
        print("All tasks cleared successfully")



obj=toDoList()
while(1):
    print("\n\nWELCOME TO YOUR TASK MANAGER!\n")
    print("SELECT WHAT YOU WANT TO DO\n")
    print("1. TO add new task press 1: ")
    print("2. TO delete a task press 2: ")
    print("3. TO update a task press 3: ")
    print("4. TO show all task press 4: ")
    print("5. TO clear all task press 5: ")
    select1=int(input("Enter choice: "))
    if select1==1:
        print("ADD TASK")
        task=input("Enter task: ")
        if task:
            obj.addtask(task)
            continue
        else:
            print("Invalid entry")
        
        continue
    elif select1==2:
        print("DELETE TASK")
        obj.displaytask()
        index=int(input("Enter task index to delete: "))
        obj.deletetask(index)
        continue
    elif select1==3:
        print("UPDATE TASK")
        obj.displaytask()
        index=int(input("Enter task index to update: "))
        update=input("Enter task: ")
        if update:
            obj.updatetask(update,index)
            continue
        else:
            print("Invalid update")
            continue
    elif select1==4:
        obj.displaytask()
        continue
    elif select1==5:
        obj.clearall()
    else:
        print("Invalid entry")
        continue


