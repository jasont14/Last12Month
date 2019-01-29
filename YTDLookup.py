import os as fo


class YTD:
        def __init__(self,start_year,end_year):
                self.sy = start_year
                self.ey = end_year               
                self.mPairs = []
        

        def setDatePairs(self):
                ptrYr = self.sy
                while ptrYr < self.ey + 1:
                        ptrMth = 1
                        while ptrMth < 13:
                                loopmth = 1
                                while loopmth < ptrMth + 1:
                                        last12mo = ptrYr * 100 + loopmth
                                        self.mPairs.append(YTD(ptrYr * 100 + ptrMth,last12mo))
                                        loopmth += 1
                                ptrMth += 1
                        ptrYr += 1                
                

aa = YTD(2010,2030)
aa.setDatePairs()
bb = aa.mPairs

with open("/home/jasont14/20yrs.csv", "w") as f:
        for b in bb:
                
                f.write("{},{} {}".format(b.sy,b.ey,"\n"))