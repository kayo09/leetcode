from typing import List
import heapq
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        actual_tasks = tasks[0]
        self.heap = []
        self.task_details = {}
        self.is_active = {}
        self.user_tasks = {}

        for task_data in actual_tasks:
            userId, taskId, priority = task_data
            heapq.heappush(self.heap, (-priority, -taskId))
            self.task_details[taskId] = [userId, priority]
            self.is_active = True
            if userId not in self.user_tasks:
                self.user_tasks[userId] = set()
            self.user_tasks[userId].add(taskId)


    def add(self, userId: int, taskId: int, priority: int) -> None:
       pass

    def edit(self, taskId: int, newPriority: int) -> None:
       pass

    def rmv(self, taskId: int) -> None:
       pass

    def execTop(self) -> int:
       pass

obj = TaskManager([[[1, 101, 10], [2, 102, 20], [3, 103, 15]]])
# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
