#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 14:40:35 2013

@author: Ronald L. Sprouse (ronald@berkeley.edu)
"""
# This is an implementation of the Klatt synthesizer suitable for running
# in batch mode.

import os, sys
import scipy.io.wavfile
import klsyn.klatt_wrap
import klsyn.klpfile
import klsyn.xlsfile

Usage = 'klattsyn paramfile ... [paramfileN]'

if __name__ == '__main__':
    ''' Run the Klatt synthesizer, produce output .wav and write out complete .klp parameter file.'''
    try:
        sys.argv[1] != None
    except:
        raise Exception('Usage: {:s}'.format(Usage))

    for pfile in sys.argv[1:]:
        fname, fext = os.path.splitext(pfile)
        synth = klsyn.klatt_wrap.synthesizer()
        if fext == '.xls':
            (params, comments) = klsyn.xlsfile.read(pfile)
        else:
            (params, comments) = klsyn.klpfile.read(pfile)
        synth.set_params(params)
        (d,rate) = synth.synthesize()
        scipy.io.wavfile.write(fname + '.wav', rate, d)
        if fext == '.xls':
            #klsyn.xlsfile.write(fname + '.wav.xls', synth=synth, comments=comments)
            sys.stderr.write("XLS output not implemented.\n")
        else:
            klsyn.klpfile.write(fname + '.wav.klp', synth=synth, comments=comments)
