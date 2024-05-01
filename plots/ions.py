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

agm_current_norm = agm_current/max(agm_current)
agm_new_norm = agm_new/max(agm_new)

# error calculation
agm_error = (agm_new_norm - agm_current_norm)*100

fig, ax = plt.subplots()
plt.plot(agm_current_norm, '-x', markersize=4, color=(0.878, 0.106, 0.141), linewidth=0.8)
plt.plot(agm_new_norm, '-o', markersize=2, color=(0, 0.3, 0.7), linewidth=0.8)

ax.tick_params(axis='both', direction='in', labelcolor='k',
               labelsize='small', width=0.6, which='both',
               top=True, right=True)

plt.xticks(np.arange(0, 64, 9))


plt.ylabel('Amplitude [-]')
plt.xlabel('4xBunch sums [-]')
plt.xlim([0, 63])
plt.grid(color=(0.7, 0.7, 0.7), linestyle='--', linewidth=0.6)

ax2 = ax.twinx() 
ax2.plot(agm_error, '-o', markersize=5, color=(0.961, 0.761, 0.067), linewidth=0.8)  

ax2.tick_params(axis='both', direction='in', labelcolor='k',
               labelsize='small', width=0.6, which='both',
               top=True, right=True)

ax2.set_ylabel('deviation [%]')
ax2.set_yticks(np.linspace(-8, 6, 8))
ax2.set_ylim([-6.71, 4.51])

legend = fig.legend(['Current AGM', 'New AGM', 'Deviation'], 
         loc='upper left', shadow=False, frameon=True, borderpad=0.5,
         framealpha=1, facecolor='white', fancybox=False, edgecolor=(0, 0, 0),
                    bbox_to_anchor=(0,1), bbox_transform=ax.transAxes)

frame = legend.get_frame()
frame.set_linewidth(0.5)

# # # NOTE USER HAVE TO PASS A PATH IN THE ARGUMENTS TO MAKE THE SCRIPT WORK
# plt.show()

plt.savefig(sys.argv[1])

file_name = sys.argv[1].split('.')[0]
plt.savefig(f"{file_name}.svg", transparent=True)
