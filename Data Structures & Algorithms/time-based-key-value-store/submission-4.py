class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append((timestamp, value))
        else:
            self.store[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store or len(self.store[key]) == 0 or self.store[key][0][0] > timestamp:
            return ""
        return self.__search(key, timestamp)
        
    def __search(self, key: str, timestamp: int) -> str:
        array = self.store[key]
        left = 0
        right = len(array) - 1

        while left < right:
            mid = (left + right) // 2
            if array[mid][0] == timestamp:
                return array[mid][1]
            elif array[mid][0] > timestamp:
                right = mid - 1
            else:
                left = mid + 1
        
        # print("left after search", left)
        index = left - 1 if array[left][0] > timestamp else left
        return array[index][1]
