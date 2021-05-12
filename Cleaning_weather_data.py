#Cleaning weather data
#1. add name of column
#2. change date and time format
#3. only keep data with level like (n mb) format 
import pandas as pd
import sys

data = pd.read_csv(sys.stdin, names = ['Time_Start','Time_End','Field','Level','Longitude','Latitude','Grid_Value'])
data['Date'] = data['Time_Start'].apply(lambda x: x[0:4] + x[5:7] + x[8:10])
data['Time'] = data['Time_Start'].apply(lambda x: x[11:13] + x[14:16] + x[17:19])
data = data.drop(columns=['Time_Start'])
data = data.drop(columns=['Time_End'])
data = data.reindex(columns = ['Date','Time','Field','Level','Longitude','Latitude','Grid_Value'])
keep_level =['100 mb','125 mb', '150 mb', '175 mb', '200 mb', '225 mb', '250 mb',
             '275 mb', '300 mb', '325 mb', '350 mb', '375 mb', '400 mb',
             '425 mb', '450 mb', '475 mb', '500 mb', '525 mb', '550 mb',
             '575 mb', '600 mb', '625 mb', '650 mb', '675 mb', '700 mb',
             '725 mb', '750 mb', '775 mb', '800 mb', '825 mb', '850 mb',
             '875 mb', '900 mb', '925 mb', '950 mb', '975 mb', '1000 mb']
data = data[data['Level'].isin(keep_level)]
data.to_csv(sys.stdout,index=False)
