from imgD import ana
import os

outfile = open('results.txt','a')

for img in os.listdir('images'):
    if img.endswith('.jpg'):
        fn, fext = os.path.splitext(img)
        loc = fn[0]
        sep = fn.find('T')
        date = fn[1:sep]
        time = fn[sep+1:]
        outfile.write( loc + ',' + date + ',' + time + '\n' + ana(fn) + '\n')   

outfile.close()
