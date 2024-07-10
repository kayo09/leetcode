class Solution:
    def minOperations(self, logs: list[str]) -> int:
        stack = []
        for log in logs:
            if log == "../":
                if stack:
                    stack.pop()
            elif log != "./":
                stack.append(log)

        return len(stack)
        
solution=Solution()
logs=["d1/","../","../","../"]

results=solution.minOperations(logs)
print(results)
