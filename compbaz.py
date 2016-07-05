import h5py
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    import argparse
    import matplotlib.pyplot as plt

    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help="input filename")
    args = parser.parse_args()

    f = h5py.File(args.filename)

    plt.figure()
    for i in range(1000):
        plt.plot(f['c1'][i], color='red')
    plt.title('channel 1')

    for i in range(1000):
        plt.plot(f['c2'][i], color='blue')

    plt.show()
