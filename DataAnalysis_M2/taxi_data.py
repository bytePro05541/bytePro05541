import pandas
import numpy as np
import matplotlib.pyplot as plt
def histogram_intersection(a, b):
    v = np.minimum(a, b).sum().round(decimals=1)
    return v

pd1 = pandas.read_csv("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01.csv",
                        header=0,
                        names=['taxi_id','trip_start_timestamp','trip_end_timestamp','trip_seconds','trip_miles','pickup_community_area','dropoff_community_area','fare','tips','tolls','extras','trip_total','payment_type','company','pickup_latitude','pickup_longitude','dropoff_latitude','dropoff_longitude'])

pdtable= pandas.pivot_table(data=pd1,
                            index=['taxi_id'],
                            values=['trip_seconds', 'trip_miles','trip_total'],
                            aggfunc = {'trip_seconds':np.sum,
                                       'trip_miles':np.sum,
                                       'trip_total':np.sum})

pdtable.to_csv("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01_taxi_id_stat.csv")

pdtable = pandas.read_csv("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01_taxi_id_stat.csv",
                               header=0,
                               names=[ 'trip_miles'])

pdtable.plot.box()
plt.show()

#pdx = pdtable.corr(method=histogram_intersection)
#pdx= pdx.to_csv("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01_taxi_id_stat_cov.csv",)