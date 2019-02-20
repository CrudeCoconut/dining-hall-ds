import pandas as pd
from imgD import ana
import os

df = pd.DataFrame([],columns = ['Location','Date','Time','People'])
if os.path.isfile("results.csv") == False:
    df.to_csv('results.csv', mode='a', index = True, header = True)
else:
    df.to_csv('results.csv', mode='a', index = True, header = False)

while True:
    for img in os.listdir('images'):
        if img.endswith('.jpg'):
            fn, fext = os.path.splitext(img)
            if os.path.isfile("pImages\{}new.jpg".format(fn)) == False:
                loc = fn[0]
                sep = fn.find('T')
                date = fn[1:sep]
                time = fn[sep+1:]
                print("I think there are ",ana(fn)," people in this frame of ",loc," at time ",time)
                df = df.append({'Location': loc,'Date': date,'Time':time,'People': ana(fn)}, ignore_index=True)
    df.to_csv('results.csv', mode='a', index = True, header = False)
    df = pd.DataFrame([],columns = ['Location','Date','Time','People'])