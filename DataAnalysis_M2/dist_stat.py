import pandas
import matplotlib.pyplot as plt

## statistical analysis for trip length etc
pd1 = pandas.read_csv("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01_date_time.csv",
                      header=0,
                      names=['taxi_id', 'trip_start_timestamp', 'trip_end_timestamp', 'trip_seconds', 'trip_miles',
                              'pickup_community_area',
                             'dropoff_community_area', 'fare', 'tips', 'tolls', 'extras', 'trip_total', 'payment_type',
                             'company', 'pickup_latitude', 'pickup_longitude', 'dropoff_latitude', 'dropoff_longitude'])

##groupby_count3 = pd1.groupby(['trip_seconds']).avg()

mean_of_trip_seconds = pd1['trip_seconds'].mean()
min_fare = pd1['trip_seconds'].min()

max_fare = pd1['trip_seconds'].max()

##print('taxi_id \n'+ str(groupby_count1))

##print('payment_type \n'+ str(groupby_count2))

print("Trip Values" + " Min " + str(min_fare) + " Max " + str(max_fare) + "Mean " +str(mean_of_trip_seconds))

##taxi_num = pd1.groupby(['taxi_id'])['taxi_id'].count()

##
# print('taxi_num \n'+ str(taxi_num))

##Nominal -> payment type. Then for each payment type, calculate Mean, Median, Standard Deviation, Minimum, Maximum

pd4 = pandas.read_csv("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01_lengthClass.csv",
                      header=0,
                      names=['taxi_id', 'trip_start_timestamp', 'trip_end_timestamp', 'trip_seconds', 'trip_miles',
                              'pickup_community_area',
                             'dropoff_community_area', 'fare', 'tips', 'tolls', 'extras', 'trip_total', 'payment_type',
                             'company', 'pickup_latitude', 'pickup_longitude', 'dropoff_latitude', 'dropoff_longitude',
                             'trip_length_qual'])

grouped = pd4.groupby(['payment_type','trip_length_qual']).size()

grouped.columns = ['payment_type','trip_length_qual','count']
grouped = grouped.reset_index()
grouped.to_csv("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01_trip_length_qual_Payment_type.csv")

pd5 = pandas.read_csv("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01_trip_length_qual_Payment_type.csv",
                      header=0,
                      names=['payment_type','trip_length_qual','count'])
pdx = pandas.pivot_table(pd5,values='count',index='trip_length_qual',columns='payment_type')
pdx.to_csv("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01_trip_length_qual_Payment_type_1.csv")
pdx = pandas.read_csv("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01_trip_length_qual_Payment_type_1.csv",
                      header=0,
                      names=['trip_length_qual','Cash','Credit Card','Dispute','No Charge','Pcard','Prcard','Unknown'])
pdx.plot.bar(x='trip_length_qual',stacked=True)
plt.show()