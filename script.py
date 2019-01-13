from imgD import ana
import os

outfile = open('results.txt','a')

for img in os.listdir('images'):
    if img.endswith('.jpg'):
        fn, fext = os.path.splitext(img)
        loc = fn[0]
        time = f[1:]
        outfile.write(ana(fn) + loc + ',' + time + '\n')   

outfile.close()
