import pandas as pd
import sys

#file = pd.read_csv(sys.stdin, names = ['time_start','time_end','field','level','longitude','latitude','grid_value'])
#file1 = file[file.latitude > 24.10]
#file1.to_csv(sys.stdout,index = False)

data = pd.read_csv(sys.stdin)
data = data[data.Link_Technology == '1090 ES']
data = data[(data.Latitude > 24) & (data.Latitude < 31) & (data.Longitude < -77) & (data.Longitude > -90)]
data = data.dropna(subset=['Pressure_Altitude'])
data = data.drop(columns=['Track_Heading_b', 'True_Magnetic_b', 'Track_Heading', 'True_Magnetic', 'Target_Status'])
data.to_csv(sys.stdout,index=False)
