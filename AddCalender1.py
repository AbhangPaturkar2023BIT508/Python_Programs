class MyCalendar:
    def __init__(self):
        self.calender = []        

    def book(self, start: int, end: int) -> bool:
        for slot in self.calender:
            if start < slot[1] and end > slot[0]:
                return False
        self.calender.append([start, end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)