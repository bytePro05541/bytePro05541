import pandas

pd1 = pandas.read_csv("/Users/ritambhara/Documents/chicago_taxi_trips_2016_01_date_time_count.csv",
                      header=0,
                      names=['trip_start_timestamp','count'])

print(str(pd1.describe(include="all")))

print('Max  '+ str(pd1['count'].max()))
print('Min  '+ str(pd1['count'].min()))
print('Median   '+ str(pd1['count'].median()))
print('Mean '+ str(pd1['count'].mean()))
print('quantile '+ str(pd1['count'].quantile()))
print('standard deviation '+ str(pd1['count'].std()))
print('variance '+ str(pd1['count'].var()))
print('Skew '+ str(pd1['count'].skew()))