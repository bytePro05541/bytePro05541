import csv
import pandas

pandas.set_option("display.precision", 3)
pandas.set_option("display.expand_frame_repr", False)
pandas.set_option("display.max_rows", 25)

pd1 = pandas.read_csv("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01.csv",
                        header=0,
                        names=['taxi_id','trip_start_timestamp','trip_end_timestamp','trip_seconds','trip_miles','pickup_community_area','dropoff_community_area','fare','tips','tolls','extras','trip_total','payment_type','company','pickup_latitude','pickup_longitude','dropoff_latitude','dropoff_longitude'])

groupby_count1 = pd1.groupby(['taxi_id']).count()

groupby_count2 = pd1.groupby(['payment_type']).count()

## create multiple datasets

pd1.groupby(['taxi_id'])['taxi_id'].count().to_csv("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01_taxi_id.csv")

pd1.groupby(['taxi_id','payment_type'])['payment_type'].count().to_csv("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01_taxi_id_Payment_type.csv")

pd1['trip_start_timestamp'] = pandas.to_datetime(pd1['trip_start_timestamp']).dt.date
pd1.to_csv("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01_date_time.csv",date_format='%Y-%m-%d')

pd2 = pandas.read_csv("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01_date_time.csv",
                      header=0,
                      names=['taxi_id', 'trip_start_timestamp', 'trip_end_timestamp', 'trip_seconds', 'trip_miles',
                              'pickup_community_area',
                             'dropoff_community_area', 'fare', 'tips', 'tolls', 'extras', 'trip_total', 'payment_type',
                             'company', 'pickup_latitude', 'pickup_longitude', 'dropoff_latitude', 'dropoff_longitude'])

pd2.groupby(['trip_start_timestamp'])['trip_start_timestamp'].count().to_csv("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01_date_time_count.csv")

pd2.groupby(['taxi_id']).agg({'trip_seconds':'sum','trip_miles':'sum'}).reset_index().to_csv("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01_bytaxi.csv")

pd3 = pandas.read_csv("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01_bytaxi.csv",
                      header=0,
                      names=['taxi_id', 'trip_seconds', 'trip_miles'])
## create two tables, one for length of trips
trip_length_qual = []

for trip in  pd2['trip_seconds']:
    if trip<900:
        trip_length_qual.append('Short')
    elif 600 < trip < 2000:
        trip_length_qual.append('Med')
    else:
        trip_length_qual.append('Long')

pd2['trip_length_qual'] = trip_length_qual
pd2.to_csv("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01_lengthClass.csv")
pd3['trip_mins'] = pd3['trip_seconds'] / 60
pd3.round(2)['Average'] = pd3['trip_miles']/pd3['trip_mins']
pd3.to_csv("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01_bytaxi.csv")

pd4 = pandas.read_csv("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01_lengthClass.csv",
                      header=0,
                      names=['taxi_id', 'trip_seconds', 'trip_miles','trip_length_qual'])
pd4.groupby(['trip_length_qual'])['trip_length_qual'].count().to_csv("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01_lengthClass_type.csv")
