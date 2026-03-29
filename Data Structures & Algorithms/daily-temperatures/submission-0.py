class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for t in temperatures]

        for idx, temp in enumerate(temperatures):
            while len(stack) != 0 and temp > temperatures[stack[-1]]:
                r_idx = stack.pop()
                res[r_idx] = idx - r_idx
            
            stack.append(idx)
        
        
        return res


        