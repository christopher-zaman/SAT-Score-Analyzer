import csv

class School:
    Name = ""
    SCount = 0
    Reading = 0 
    Math = 0 
    Writing = 0 
    
    def Score(self):
        return self.Reading + self.Math + self.Writing
    
    def Print(self):
        print(self.Name)
        
f = open("SAT_Results.csv")
rows = csv.reader(f)

next(rows)

schools = []

for row in rows:
    if row[4] == "s":
        continue
    
    s = School()
    s.Name = row[1]
    s.SCount = int(row[2])
    s.Reading = int(row[3])
    s.Math = int(row[4])
    s.Writing = int(row[5])
    schools.append(s)
    
sMax = max(schools, key = lambda x: x.Score())
sMax.Print()

sMin = min(schools, key = lambda x: x.Score())
sMin.Print()

def FindAvg(schools, botRange, topRange):
    ls = filter(lambda x: x.SCount > botRange and x.SCount <= topRange, schools)
    scores = list(map(lambda x: x.Score(), ls))
    avg = sum(scores) / len(scores)
    print("Average: " + str(avg))

FindAvg(schools, 0, 100)
FindAvg(schools, 100, 200)
FindAvg(schools, 200, 500)
FindAvg(schools, 500, 1000)
FindAvg(schools, 1000, 10000)



























