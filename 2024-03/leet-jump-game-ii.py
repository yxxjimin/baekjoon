"""
문제 : https://leetcode.com/problems/jump-game-ii/
날짜 : 24/03/29

- BFS와 유사한 아이디어
    - `curr_end`에 도달하면 depth 갱신
- curr_end: k번째 점프에서 가장 멀리 갈 수 있는 지점
- next_end: (k+1)번째 점프에서 가장 멀리 갈 수 있는 지점
"""

class Solution:
    def jump(self, nums: list[int]) -> int:
        ans = 0
        curr_end, next_end = 0, 0

        for i in range(len(nums) - 1):
            next_end = max(next_end, i + nums[i])

            if i == curr_end:
                ans += 1
                curr_end = next_end
            
        return ans
