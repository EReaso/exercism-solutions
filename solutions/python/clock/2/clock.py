class Clock:
    @property
    def hour(self) -> int:
        return self._hour
    
    @hour.setter
    def hour(self, value: int):
        self._hour = value % 24

    @property
    def minute(self) -> int:
        return self._minute
    
    @minute.setter
    def minute(self, value: int):
        self._minute = value % 60
        self.hour += value // 60
    
    def __init__(self, hour: int, minute: int):
        self.hour, self.minute = hour, minute

    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        return f"{str(self.hour).zfill(2)}:{str(self.minute).zfill(2)}"

    def __eq__(self, other):
        if not isinstance(other, Clock): return False
        return (self.hour, self.minute) == (other.hour, other.minute)

    def __add__(self, minutes: int):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes: int):
        return self.__add__(-minutes)
