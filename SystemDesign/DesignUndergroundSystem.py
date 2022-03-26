class UndergroundSystem:

    def __init__(self):
        #have two hashtables
        #1 key=(customerid):tuple=(timestart,startstation)
        self.i = defaultdict(tuple)
        #2 using startstation and endstation as our key we could calculate how much time it took
        #(start,end):(timeend-timestart)
        self.o = defaultdict(list)#list of all the times it took
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        #tuple: id = timestart and stationname = starstation
        #id gets updated everytime the customer checks in
        self.i[id]=(t, stationName)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        starttime,startStation = self.i[id]
        total = t-starttime
        self.o[(startStation,stationName)].append(total)#append the total time it took for our output
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        #return sum of everything in self.o[] for the two stations,divide by the length
        return sum(self.o[startStation,endStation])/len(self.o[startStation,endStation])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
