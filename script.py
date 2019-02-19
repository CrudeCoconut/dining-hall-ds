import pandas as pd
from imgD import ana
import os

df = pd.DataFrame([],columns = ['Location','Date','Time','People'])
df.to_csv('results.csv', mode='a', index = True, header = True)

while True:
    for img in os.listdir('images'):
        if img.endswith('.jpg'):
            fn, fext = os.path.splitext(img)
            if os.path.isfile("pImages\{}new.jpg".format(fn)) == False:
                loc = fn[0]
                sep = fn.find('T')
                date = fn[1:sep]
                time = fn[sep+1:]
                df = df.append({'Location': loc,'Date': date,'Time':time,'People': ana(fn)}, ignore_index=True)
    df.to_csv('results.csv', mode='a', index = False, header = False)
    df = pd.DataFrame([],columns = ['Location','Date','Time','People'])
