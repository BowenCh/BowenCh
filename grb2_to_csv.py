import pandas as pd
import gc
import numpy as np
import os
import subprocess
path = '/home/songlab/Documents/Kai/TIST2020/weather/rapfiles'
lst = os.listdir(path)

for c in lst:
    if c.endswith('.grb2'):
        name = c[:-4] + 'csv'
        print('processing %s' % c)
        command = 'wgrib2 ' + c + ' -csv ' + name
        #subprocess.call(command, shell=True)
        os.system(command)
        print('done file %s' % name)
        #os.system()