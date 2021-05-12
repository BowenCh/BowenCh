import pandas as pd
import sys

data = pd.read_csv(sys.stdin)

data['level_num'] = data['Level'].apply(lambda x: int(x[:-3]) )
data['Height'] = data['level_num'].apply(lambda x: (round((44300 * (1 - (float(x) / 1000) ** (1 /5.256)) * 3.28) / 25)) * 25)

#round((44300 * (1 - (100 / 1000) ** ( 1 /5.256)) * 3.2808399) / 25) * 25
data = data.drop(columns=['Level'])
data = data.drop(columns=['level_num'])
data = data.reindex(columns = ['Date','Time','Longitude','Latitude','Height','Field','Grid_Value'])

data.to_csv(sys.stdout,index=False)
