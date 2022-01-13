import numpy as np
import os
import matplotlib.pyplot as plt
from pathlib import Path

def processNGAfile(filepath, scalefactor=None):
    try:
        if not scalefactor:
            scalefactor = 1.0
        with open(filepath,'r') as f:
            content = f.readlines()
        counter = 0
        desc, row4Val, acc_data = "","",[]
        for x in content:
            if counter == 1:
                desc = x
            elif counter == 3:
                row4Val = x
                if row4Val[0][0] == 'N':
                    val = row4Val.split()
                    npts = float(val[(val.index('NPTS='))+1].rstrip(','))
                    dt = float(val[(val.index('DT='))+1])
                else:
                    val = row4Val.split()
                    npts = float(val[0])
                    dt = float(val[1])
            elif counter > 3:
                data = str(x).split()
                for value in data:
                    a = float(value) * scalefactor
                    acc_data.append(a)
                inp_acc = np.asarray(acc_data)
                time = []
                for i in range (0,len(acc_data)):
                    t = i * dt
                    time.append(t)
            counter = counter + 1
        return desc, npts, dt, time, inp_acc
    except IOError:
        print("processMotion FAILED!: File is not in the directory")

def main():
    directory = Path(__file__).parent.absolute()
    seismic_folder = os.path.join(directory, 'Earthquake_Data')
    files = os.listdir(seismic_folder)
    for file in files:
        filename = os.path.join(seismic_folder, file)
        desc, npts, dt, time, inp_acc = processNGAfile(filename)
        plt.plot(time, inp_acc, 'b-', linewidth=0.5)
    plt.show()

if __name__ == '__main__':
    main()