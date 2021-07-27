import pandas
import numpy as np
import matplotlib.pyplot as plt

## statistical analysis for payment type
pd1 = pandas.read_csv("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01_date_time.csv",
                      header=0,
                      names=['taxi_id', 'trip_start_timestamp', 'trip_end_timestamp', 'trip_seconds', 'trip_miles',
                              'pickup_community_area',
                             'dropoff_community_area', 'fare', 'tips', 'tolls', 'extras', 'trip_total', 'payment_type',
                             'company', 'pickup_latitude', 'pickup_longitude', 'dropoff_latitude', 'dropoff_longitude'])

pd1.groupby(['payment_type'])['payment_type'].count().to_csv("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01_payment_type.csv")

pd1=pandas.read_csv("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01_payment_type.csv",
                      header=0,
                      names=['payment_type','count'])
pd1.plot.bar()
plt.show()
##
Paymentscape = pd1[['fare', 'tips', 'tolls', 'extras', 'trip_total', 'payment_type']]
Paymentscape.reset_index()
Paymentscape.to_csv("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01_taxi_id_Paymentscape.csv")
##pd1.to_csv("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01_taxi_id_Paymentscape.csv")

Paymentscape = pandas.read_csv("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01_taxi_id_Paymentscape.csv",
                               header=0,
                               names=['trip_total', 'payment_type'])

pdtable= pandas.pivot_table(data=Paymentscape,
                            index=['payment_type'], aggfunc = {'trip_total':[np.mean, min, max, count]})

pdtable.to_csv("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01_taxi_id_Paymentscape_pivot.csv")
#Paymentscape = Paymentscape[Paymentscape['payment_type'] == 'Cash']
#Paymentscape.to_csv("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01_taxi_id_Paymentscape_Cash.csv")

