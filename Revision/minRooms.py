from heapq import *

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        self.end < other.end

def minMeetingRoom(intervals):
    intervals.sort(key=lambda x : x.start)

    rooms = 0
    minHeap = []

    for interval in intervals:
        # remove all the meetings that have ended
        while len(minHeap) > 0 and interval.start >= minHeap[0].end:
            # remove
            heappop(minHeap)

        heappush(minHeap, interval)

        rooms = max(rooms, len(minHeap))

    return rooms
