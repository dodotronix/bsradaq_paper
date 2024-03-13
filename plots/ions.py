import sys, os
import matplotlib

import numpy as np
import matplotlib.pyplot as plt


# matplotlib.use("pgf")
# matplotlib.rcParams.update({
#     "pgf.texsystem": "pdflatex",
#     'font.family': 'serif',
#     'text.usetex': True,
#     'pgf.rcfonts': False})

# dir_path = os.path.dirname(sys.argv[1])
# a = np.loadtxt(os.path.join(dir_path, 'data/filter/indata.txt'), 
#                encoding='ASCII', dtype='int', skiprows=1)
# b = np.loadtxt(os.path.join(dir_path, 'data/filter/file_filter.txt'), 
#                encoding='ASCII', dtype='int', skiprows=1)

# def fixed_to_float(num, N, Q):
#     binary_num = np.binary_repr(num, N)
#     s_int = binary_num[0:Q]
#     s_frac = binary_num[Q:]

#     # resolve the integer part
#     tmp = -1 if(s_int[0] != '0') else int(s_int, 2)
#     if((Q > 1) and (s_int[0])):
#         tmp = -1*(2**(Q-1)) + int(s_int[1:],2)
#     s_int = tmp

#     # resolve fractional part
#     s_frac = int(s_frac,2)/(2**(N-Q))
#     return s_int + s_frac

# def align_array(array, multiples):
#     tmp = (len(array)%multiples)
#     if(not tmp): return array
#     else: return array[:-tmp]

# def data_aligner(data):
#     #  make each line 64 nums long
#     d = align_array(data, 64)
#     arr = np.array(d, dtype=int)
#     # reshape the data to matrix with
#     # 64 columns and N rows and then
#     # read data column by column
#     arr = np.reshape(arr, (-1, 64))
#     return arr

# # N = number of digits
# # Q = number of digits befor floating point
# def convert_array(np_array, N, Q):
#     c = lambda n:fixed_to_float(n, N, Q)
#     convert = np.vectorize(c)
#     return convert(np_array)


# # NOTE this takes numpy array as
# # an argument the beta and alpha
# def smoothing_formula(data, alph):
#     beta = 1 - alph
#     tmp = np.copy(data)
#     # add zero on the first place
#     tmp = np.insert(tmp, 0, 0) 
#     for i in range(len(tmp)-1):
#         x = tmp[i+1]
#         y_prev = tmp[i]
#         tmp[i+1] = beta*y_prev + alph*x
#     return tmp[1:] # cut 0 element

# # this function takes serial data split them into 2^N rows, 
# # it adds extends the array to have size in muliples of 2
# # then process the data and retun the 64 words long vector
# def exponential_smoothing(data, alph):
#     tmp = np.copy(data);
#     for i in range(64):
#         # print(tmp[:, i])
#         tmp[:, i] = smoothing_formula(data[:, i], alph)
#         # print(tmp[:, i])
#         # print(i)
#     return tmp


# raw = a[:, 0].astype(np.int32)
# raw = data_aligner(raw)
# raw_conv = convert_array(raw, 32, 1)
# print(raw_conv[0])
# print(raw[0])

# processed = exponential_smoothing(raw, 0.008)
# processed_conv = convert_array(processed, 32, 1)
# print(processed_conv[0])

# flt = b[:,0]
# flt = data_aligner(flt)
# flt_conv = convert_array(flt, 32, 1)

# # NOTE if you set different alpha factor in the SV you have
# # to change the factor either here to get the same results

# fig, ax = plt.subplots()
# plt.plot(raw_conv[0], '-o', markersize=2, color=(0, 0.3, 0.7), linewidth=0.8)
# plt.plot(processed_conv[-1], '--', markersize=2, color=(0, 0.3, 0.3), linewidth=0.8)
# plt.plot(flt_conv[-1], 'd', markersize=2, color=(1, 0, 0), linewidth=0.8)

# ax.tick_params(axis='both', direction='in', labelcolor='k',
#                labelsize='small', width=0.6, which='both',
#                top=True, right=True)

# legend = ax.legend(['Input Data', 'Python Simulation', 'SV Verification'], 
#          loc='upper right', shadow=False, frameon=True, borderpad=0.5,
#          framealpha=1, facecolor='white', fancybox=False, edgecolor=(0, 0, 0))

# frame = legend.get_frame()
# frame.set_linewidth(0.5)

# plt.ylabel('Amplitude [-]')
# plt.xlabel('Filters [-]')
# plt.xlim([0, 64])
# plt.grid(color=(0.7, 0.7, 0.7), linestyle='--', linewidth=0.6)

# # NOTE USER HAVE TO PASS A PATH IN THE ARGUMENTS TO MAKE THE SCRIPT WORK
# plt.savefig(sys.argv[1])
