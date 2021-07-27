import matplotlib.pyplot as plt
import csv
import pandas

## graphing
pd1 = pandas.read_csv("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01_lengthClass_type.csv",
                        header=0,
                        names=['trip_length_qual', 'Count'])
#
#pd1 = pandas.read_csv("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01_date_time_count.csv",
#                      header=0,
#                      names=['trip_start_timestamp','count'])

#Paymentscape = pandas.read_csv("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01_taxi_id_Paymentscape_CC.csv",
#                               header=0,
#                               names=['trip_total'])

pd1.plot.hist(x='trip_length_qual', y='Count')
#ax1= pd1.plot.scatter(x='trip_seconds', y='trip_miles')
#pd1.plot.bar(x='trip_seconds', y='trip_miles')
plt.show()
