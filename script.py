from imgD import ana
import os

outfile = open('results.txt','a')

for img in os.listdir('images'):
    if img.endswith('.jpg'):
        fn, fext = os.path.splitext(img)
        outfile.write(ana(fn) + '\n')   

outfile.close()
        #writing to text file has errors