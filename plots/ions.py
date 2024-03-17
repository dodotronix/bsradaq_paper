import sys, os
import matplotlib

import numpy as np
import matplotlib.pyplot as plt

matplotlib.use("pdf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False})

dir_path = os.path.dirname(sys.argv[1])

agm_new = np.loadtxt(os.path.join(dir_path, 'timber_data/vfc_abort_gap_raw_data_spill.txt'), 
               encoding='ASCII')

agm_current = np.loadtxt(os.path.join(dir_path, 'timber_data/abort_gap_raw_data_spill.txt'), 
               encoding='ASCII')

fig, ax = plt.subplots()
plt.plot(agm_current, '--', markersize=2, color=(0, 0.3, 0.3), linewidth=0.8)
plt.plot(agm_new, '-o', markersize=2, color=(0, 0.3, 0.7), linewidth=0.8)

ax.tick_params(axis='both', direction='in', labelcolor='k',
               labelsize='small', width=0.6, which='both',
               top=True, right=True)

plt.xticks(np.arange(0, 64, 9))

legend = ax.legend(['Current AGM', 'New AGM'], 
         loc='upper left', shadow=False, frameon=True, borderpad=0.5,
         framealpha=1, facecolor='white', fancybox=False, edgecolor=(0, 0, 0))

frame = legend.get_frame()
frame.set_linewidth(0.5)

plt.ylabel('Amplitude [-]')
plt.xlabel('4xBunch sums [-]')
plt.xlim([0, 63])
plt.grid(color=(0.7, 0.7, 0.7), linestyle='--', linewidth=0.6)

# # # NOTE USER HAVE TO PASS A PATH IN THE ARGUMENTS TO MAKE THE SCRIPT WORK
# plt.show()

plt.savefig(sys.argv[1])
