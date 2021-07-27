import random

f = open("/Users/ritambhara/Downloads/chicago_taxi_trips_2016_01.csv", "r")

fW = open("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01.csv", "w")

for i in range(500000):
  line = f.readline()
  fW.writelines(line)

fW.close()

file1 = open("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01.csv", "r")

linecount = 0
for line in file1:
  linecount += 1

print(linecount)
