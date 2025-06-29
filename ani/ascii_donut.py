import numpy as np
import os
import time

A = 0
B = 0
while True:
    z = np.zeros(1760)
    b = [' '] * 1760
    for j in np.arange(0, 6.28, 0.07):
        for i in np.arange(0, 6.28, 0.02):
            c = np.sin(i)
            d = np.cos(j)
            e = np.sin(A)
            f = np.sin(j)
            g = np.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = np.cos(i)
            m = np.cos(B)
            n = np.sin(B)
            t = c * h * g - f * e
            x = int(40 + 30 * D * (l * h * m - t * n))
            y = int(12 + 15 * D * (l * h * n + t * m))
            o = x + 80 * y
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
            if 0 <= y < 22 and 0 <= x < 80 and D > z[o]:
                z[o] = D
                b[o] = ".,-~:;=!*#$@"[N if N > 0 else 0]
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\x1b[H', end='')
    for k in range(1760):
        print(b[k], end='' if (k + 1) % 80 else '\n')
    A += 0.04
    B += 0.02
    time.sleep(0.01)