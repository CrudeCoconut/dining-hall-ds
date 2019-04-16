import os
import argparse
import time
import pandas as pd
from multiprocessing import Process
import people_counter as p
import dining_hall_cams as cams

if __name__ == '__main__':
    c_api = "https://api.ucsb.edu/dining/cams/v1/stream/carrillo?ucsb-api-key="
    d_api = "https://api.ucsb.edu/dining/cams/v1/stream/de-la-guerra?ucsb-api-key="
    o_api = "https://api.ucsb.edu/dining/cams/v1/stream/ortega?ucsb-api-key="

    c,d,o = 0, 0, 0

    for vid in os.listdir('videos'):
        if vid[0] == "c":
            c=c+1
        if vid[0] == "d":
            d=d+1
        if vid[0] == "o":
            o=o+1
    x,y,z = c,d,o

    p1 = Process(target=p.record,args=(cams.dining_halls[0],c_api,"output/carillo_sample{}.avi".format(c),30))
    p2 = Process(target = p.record,args=(cams.dining_halls[1],d_api,"output/dlg_sample{}.avi".format(d),30))
    p3 = Process(target = p.record,args=(cams.dining_halls[2],o_api,"output/ortega_sample{}.avi".format(o),30))

    df = pd.DataFrame([],columns = ['Location','Date','People'])
    
    if os.path.isfile("results.csv") == False:
        df.to_csv('results.csv', mode='a', index = True, header = True)
    else:
        df.to_csv('results.csv', mode='a', index = True, header = False)
     
    while True:
        while x == c and y == d and z == o:
            if cams.dining_hall_open(cams.dining_halls[0]) == True and p1.is_alive() == False:
                p1.start()
            if cams.dining_hall_open(cams.dining_halls[1]) == True and p2.is_alive() == False:
                p2.start()
            if cams.dining_hall_open(cams.dining_halls[2]) == True and p3.is_alive() == False:  
                p3.start()
        
            if cams.dining_hall_open(cams.dining_halls[0]) == False and p1.is_alive == True: 
                    p1.terminate()
                    x = x + 1
            if cams.dining_hall_open(cams.dining_halls[1]) == False and p2.is_alive == True: 
                    p2.terminate()
                    y = y +1
            if cams.dining_hall_open(cams.dining_halls[2]) == False and p3.is_alive == True: 
                    p3.terminate()
                    z = z + 1
        if x>c:
            c = x
            p1 = Process(target=p.record,args=(cams.dining_halls[0],c_api,"output/carillo_sample{}.avi".format(c)))
        if y>d:
            d = y
            p2 = Process(target = p.record,args=(cams.dining_halls[1],d_api,"output/dlg_sample{}.avi".format(d)))
        if z >o:
            o = z
            p3 = Process(target = p.record,args=(cams.dining_halls[2],o_api,"output/ortega_sample{}.avi".format(o)))
        print(c,d,o)


        