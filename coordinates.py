# This is a comment
import math
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import sys

def toCurve(p):
    if abs(p[1]) < 1e-3:
        return (0, p[0])
    else:
        k = 2*p[1]/(p[0]**2 + p[1]**2)
        s = math.asin(k*p[0])/k
        return (k, s)

if __name__ == '__main__':
    n = 10 if len(sys.argv) < 2 else int(sys.argv[1])
    p = np.random.uniform(low=-10, high=10, size=(2, n))
    q = np.apply_along_axis(toCurve, 0, p)


    fig = plt.figure(1)
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)

    ax1.plot(p[0,:], p[1,:], 'ko')
    ax1.set_title('Cartesian')
    ax1.set_xlabel('x (m)')
    ax1.set_ylabel('y (m)')

    ax2.plot(q[0,:], q[1,:], 'ko')
    ax2.set_title('Curved')
    ax2.set_xlabel('k (m-1)')
    ax2.set_ylabel('s (m)')

    tfig = fig.transFigure.inverted()
    tax1 = ax1.transData
    tax2 = ax2.transData

    for i in range(n):
        p_ax1 = tfig.transform(tax1.transform(p[:,i]))
        q_ax2 = tfig.transform(tax2.transform(q[0:,i]))

        line = Line2D((p_ax1[0], q_ax2[0]), (p_ax1[1], q_ax2[1]), transform=fig.transFigure)
        
        fig.lines.append(line)

    plt.show()
    

