import random
import pandas

## might as well prune the dataset

pd1 = pandas.read_csv("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01.csv",
                        header=0,
                        names=['taxi_id','trip_start_timestamp','trip_end_timestamp','trip_seconds','trip_miles','pickup_census_tract','dropoff_census_tract','pickup_community_area','dropoff_community_area','fare','tips','tolls','extras','trip_total','payment_type','company','pickup_latitude','pickup_longitude','dropoff_latitude','dropoff_longitude'])


##fW = open("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01.csv", "w")

##for i in pd1.index:
##    if(pd1['trip_seconds'][i] == 0):
##        print(i,pd1['trip_seconds'][i],pd1['taxi_id'][i])

pd1 = pd1[pd1['trip_seconds'] != 0]
pd1 = pd1[pd1['trip_miles'] > 1]
pd1 = pd1[pd1['trip_seconds'] <= 3600]
pd1 = pd1[pd1['trip_miles'] <= 50]
pd1 = pd1[pd1['fare'] <= 100]

pd1.drop(['pickup_census_tract','dropoff_census_tract'],axis=1, inplace = True)

pd1.to_csv("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01.csv")

file1 = open("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01.csv", "r")

linecount = 0
for line in file1:
  linecount += 1
##  print(line.strip())

print(linecount)
