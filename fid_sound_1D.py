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

#Based on code from: https://github.com/mstrocchi/fid-to-wav/commit/f2114e4c114bbe62e7f19fa25ea4205b19eac0d0#

''' FOR TE 1D EXPERIMENTS'''
FILE_NAME = 'TE_Proton_exp_slow_16s_waterpressat.wav'
FRAMERATE = 2000 #it changes the rate, 2000 is 16s, 8000 is 4s, 32000 is 1s. 
AMPLITUDE = 32767 #(32767 for 16bits or 32700)
path_to_directory = '/Users/karensantos/Desktop/FID_tests' #Where to save?
data = []

dic,data = ng.bruker.read('/opt/topspin4.1.0/NMR/2021_09_27_Glutamine/4') #Where is the data? 
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
