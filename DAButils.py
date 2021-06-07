# Utility functions supporting population vector code for Quinn et al (NC 2021)
import numpy as np
import matplotlib.pyplot as plt  # plotting


def normalize_vector(v):
    nrm = np.sum(np.square(v))
    if nrm > 0:
        vnorm = v / np.sqrt(nrm)
    else:
        vnorm = v
    return vnorm


def drift_design_matrix(num_trials, drift_spacing=100, to_plot=False):
    xminus = 1-np.array(range(drift_spacing))/drift_spacing
    xplus = np.array(range(drift_spacing))/drift_spacing

    anchor_pnts = list(range(0, num_trials, drift_spacing))
    NW = len(anchor_pnts)-1

    Xoffset = np.zeros([num_trials, NW], dtype='float32')
    for nn in range(NW):
        #if nn < (NW-1):
        Xoffset[range(drift_spacing*nn, drift_spacing*(nn+1)),nn] = xminus
        if nn > 0:
            Xoffset[range(drift_spacing*(nn-1), drift_spacing*(nn)),nn] = xplus
    #Xoffset[win_spacing*(NW-1):,nn] = 1.0
    if to_plot:
        plt.imshow(Xoffset, aspect='auto')
        plt.show()
        
    return Xoffset, NW


def subplot_setup( num_rows, num_cols, row_height=2.0, full_width=False):
    fig, ax = plt.subplots(nrows=num_rows, ncols=num_cols)
    if full_width:
        fig.set_size_inches(15, row_height*num_rows)
    else:
        fig.set_size_inches(num_cols*2.5, row_height*num_rows) # 2.5 inches per figure
    fig.tight_layout()