#!/usr/bin/python
import math
import sys, os
import matplotlib

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# matplotlib.use("pgf")
# matplotlib.rcParams.update({
    # "pgf.texsystem": "pdflatex",
    # 'font.family': 'serif',
    # 'text.usetex': True,
    # 'pgf.rcfonts': False})

dir_path = os.path.dirname(sys.argv[1])
a = np.loadtxt(os.path.join(dir_path, 'timber_data/vfc_abort_gap_raw_data_spill.txt'), 
               encoding='ASCII')

data = np.tile(a, (8, 1))

X = np.arange(data.shape[1])
Y = np.arange(data.shape[0])
X, Y = np.meshgrid(X, Y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.tick_params(axis='y',which='major',length=data.shape[0], width=1, labelsize=12)

# ax.set_yticks([0, len(Y)-1, 1])
# ax.set_xticks([0, len(X)-1, 1])

surf = ax.plot_wireframe(X, Y, data, rstride=1, cstride=0,
                   cmap='Oranges', edgecolor=None, linewidth=2, antialiased=True)

plt.xticks(np.arange(0, 64, 9))
plt.yticks(np.arange(0, 8, 1))

ax.set_ylabel('Time [s]')
ax.set_xlabel('Filters output [-]')
ax.set_zlabel('Normalized Amplitude')

ax.view_init(38, -148)
# plt.show()

# # NOTE USER HAVE TO PASS A PATH IN THE ARGUMENTS TO MAKE THE SCRIPT WORK

file_name = sys.argv[1].split('.')[0]
plt.savefig(f"{file_name}.svg", transparent=True)
