class TimeMap:
    def __init__(self):
        self.dict = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = []
        self.dict[key].append([timestamp, value])
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""
            
        curr = self.dict[key]
        if timestamp < curr[0][0]:
            return ""
            
        low = 0
        high = len(curr) - 1
        
        while low <= high:
            mid = (low + high) // 2
            if curr[mid][0] <= timestamp:
                low = mid + 1
            else:
                high = mid - 1
                
        if high < 0:
            return ""
            
        return curr[high][1]