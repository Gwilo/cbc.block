from __future__ import division
from .common import *
import numpy

#####
# Adapted from SciPy (BSD license)
# Copyright (C) 2009, Pauli Virtanen <pav@iki.fi>
#####

def lgmres(B, A, x, b, tolerance, maxiter, progress, relativeconv=False,
           inner_m=30, outer_k=3, outer_v=None, store_outer_Av=True, callback=None):
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear Emily.")
    print("Happy Birthday to you!")
