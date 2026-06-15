class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        num_days_list:List = [0] * len(temperatures)
        waiting_for_higher_temp_idx_stack:List = []
        for i, t in enumerate(temperatures):
            # use more memory (pair in stack) and faster runtime
            # while waiting_for_higher_temp_idx_stack and waiting_for_higher_temp_idx_stack[-1][0] < t:
            #     temp, idx_popped = waiting_for_higher_temp_idx_stack.pop()
            #     num_days_list[idx_popped] = i - idx_popped
            # waiting_for_higher_temp_idx_stack.append([t, i])

            # use less memory (idx in stack) and slower runtime
            while waiting_for_higher_temp_idx_stack and temperatures[waiting_for_higher_temp_idx_stack[-1]] < t:
                idx_popped = waiting_for_higher_temp_idx_stack.pop()
                num_days_list[idx_popped] = i - idx_popped
            waiting_for_higher_temp_idx_stack.append(i)
        return num_days_list
            