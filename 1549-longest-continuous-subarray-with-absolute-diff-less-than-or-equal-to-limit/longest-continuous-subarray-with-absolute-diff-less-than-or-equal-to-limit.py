class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        max_len = 0
        left = 0
        min_queue = deque()
        max_queue = deque()
        
        for right in range(n):
            while min_queue and nums[min_queue[-1]] >= nums[right]:
                min_queue.pop()
            min_queue.append(right)
  
            while max_queue and nums[max_queue[-1]] <= nums[right]:
                max_queue.pop()
            max_queue.append(right)
        
            while nums[max_queue[0]] - nums[min_queue[0]] > limit:
                left += 1
                if min_queue[0] < left:
                    min_queue.popleft()
                if max_queue[0] < left:
                    max_queue.popleft()
            
            max_len = max(max_len, right - left + 1)
        
        return max_len
