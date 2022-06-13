from TimeFrame import TimeFrame

class TimeFrames:
    def __init__(self):
        self.timeframes = []

    def append_timeframes(self, timeframe: TimeFrame):
        self.timeframes.append(timeframe)

    def get_timeframes(self):
        return self.timeframes
