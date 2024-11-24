import numpy as np
import matplotlib.pyplot as plt

for i in range(1,4):
    with open("signals/signal0"+str(i)+".dat") as f:
        a=np.array((f.read().split("\n")), dtype=np.float64)
    b=np.arange(len(a))
    print(a)
    fig, ax = plt.subplots()
    ax.plot(b, a)
    ax.grid()
    plt.savefig("graph_old/for_signal0"+str(i)+".jpg")
    plt.close()
    c=np.zeros((len(a)))
    for g in range(0,10):
        c[g]=a[0:(g+1)].mean()
    for g in range(10,len(a)):
        c[g] = a[(g-9):(g+1)].mean()
    fig, ax = plt.subplots()
    ax.plot(b, c)
    ax.grid()
    plt.savefig("graph_new/for_signal0" + str(i) + ".jpg")
    plt.close()
    #print(a)