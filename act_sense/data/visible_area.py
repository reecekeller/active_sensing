import os, sys
import numpy as np

from scripts.utils import info_map
from scripts.arena import Arena, Aperture

arena = Arena(length=60, width=60, height=50)
aperture = Aperture(arena_width=60, arena_height=50, arena_length=60, gap_width=10)
circleL = (arena.width/2 - aperture.gap_width, arena.width, arena.height/2)
circleR = (arena.width/2 + aperture.gap_width, arena.width, arena.height/2)


source = (20, 0, 25)

info_mat = info_map(arena, circleL, circleR, aperture, radius=5)


BASE_PATH = "/Users/reecekeller/Documents/Xaq/act_sense/act_sense/data/"
np.save(os.path.join(BASE_PATH, 'info_matrix.npy'), info_mat)
