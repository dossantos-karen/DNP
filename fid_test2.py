#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 13:59:37 2022

@author: karensantos
"""

import wave
import struct
import numpy as np
import nmrglue as ng

#Original code from: https://github.com/mstrocchi/fid-to-wav/commit/f2114e4c114bbe62e7f19fa25ea4205b19eac0d0#

''' FOR TE 1D EXPERIMENTS'''
FILE_NAME = 'TE_afterDNP_slow_16s.wav'
FRAMERATE = 2000
AMPLITUDE = 32767 #(32767 for 16bits or 32700)
path_to_directory = '/Users/karensantos/Desktop/FID_tests'
data = []

dic,data = ng.bruker.read('/opt/topspin4.1.0/NMR/2021_09_27_Glutamine/4')
data = np.true_divide(data, np.max(np.abs(data)))


file_path = (path_to_directory + '/' + FILE_NAME)
file_wav = wave.open(file_path, "w")
number_of_channels = 1
sample_width = 2
number_of_frames = len(data)
compression_type = "NONE"
compression_name = "not compressed"
file_wav.setparams((number_of_channels,
                    sample_width,
                    FRAMERATE,
                    number_of_frames,
                    compression_type,
                    compression_name))
    
for value in data:
        file_wav.writeframes(struct.pack('i', int(value * AMPLITUDE)))
file_wav.close()

print("Done!")


''' FOR DDNP experiments - its only working with one spectra at a time '''

# # Constants - global settings
# FILE_NAME = 'DNP_full.wav'
# FRAMERATE = 32000 #to be in one second should be 32000, 8000 is 4 seconds, 4000 is 8s
# AMPLITUDE = 32767 #(32767 for 16bits or original 32700)
# path_to_directory = '/Users/karensantos/Desktop/FID_tests'
# data = []

# dic,data = ng.bruker.read('/opt/topspin4.1.0/NMR/2021_09_27_Glutamine/1/pdata/') # For 2D, use processed data
# # slice = 42 # chose 1D slice from 2D experiment (2rr)
# # data = np.true_divide(data[slice], np.max(np.abs(data[slice])))
# data = np.true_divide(data, np.max(np.abs(data)))


# # for i in range (0, len(data)):
#     # for value in data[i]:
# file_path = (path_to_directory + '/' + FILE_NAME)
# file_wav = wave.open(file_path, "w")
# number_of_channels = 1
# sample_width = 2
# number_of_frames = len(data)
# compression_type = "NONE"
# compression_name = "not compressed"
# file_wav.setparams((number_of_channels,
#                     sample_width,
#                     FRAMERATE,
#                     number_of_frames,
#                     compression_type,
#                     compression_name))

# # for value in data: #for slices
# #     file_wav.writeframes(struct.pack('i', int(value * AMPLITUDE)))
# # file_wav.close()

# # # for i in range (0, len(data)):
# for i in range (30, 90):
#     for value in data [i]:
#         file_wav.writeframes(struct.pack('i', int(value * AMPLITUDE)))
# file_wav.close()

# print("Done!")