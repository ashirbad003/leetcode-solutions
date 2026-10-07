from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0
        
        visited = {s}
        queue = deque([s])
        result = []
        found = False
        
        while queue:
            current = queue.popleft()
            
            if is_valid(current):
                result.append(current)
                found = True
            
            if found:
                continue
            
            for i in range(len(current)):
                if current[i] not in '()':
                    continue
                next_str = current[:i] + current[i + 1:]
                if next_str not in visited:
                    visited.add(next_str)
                    queue.append(next_str)
        
        return result