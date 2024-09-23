import numpy as np
import matplotlib.pyplot as plt
from scripts.utils import info_map
from scripts.arena import Arena, Aperture, Mouse, visualize_arena
from tqdm import tqdm
import os

BASE_PATH = "/Users/reecekeller/Documents/Xaq/act_sense/act_sense/data/"


arena_length = 60
arena_width = 60
arena = Arena(length=arena_length, width=60, height=50)

aperture = Aperture(arena_width=arena_width, arena_height=50, arena_length=arena_length, gap_width=5)
circleL = (arena.width/2 - 10, arena.width, arena.height/2)
circleR = (arena.width/2 + 10, arena.width, arena.height/2)
info_mat = info_map(arena, circleL, circleR, aperture, radius=5)
np.save(os.path.join(BASE_PATH, 'info_matrix_5.npy'), info_mat)

aperture = Aperture(arena_width=arena_width, arena_height=50, arena_length=arena_length, gap_width=6)
circleL = (arena.width/2 - 10, arena.width, arena.height/2)
circleR = (arena.width/2 + 10, arena.width, arena.height/2)
info_mat = info_map(arena, circleL, circleR, aperture, radius=5)
np.save(os.path.join(BASE_PATH, 'info_matrix_6.npy'), info_mat)

aperture = Aperture(arena_width=arena_width, arena_height=50, arena_length=arena_length, gap_width=7)
circleL = (arena.width/2 - 10, arena.width, arena.height/2)
circleR = (arena.width/2 + 10, arena.width, arena.height/2)
info_mat = info_map(arena, circleL, circleR, aperture, radius=5)
np.save(os.path.join(BASE_PATH, 'info_matrix_7.npy'), info_mat)

aperture = Aperture(arena_width=arena_width, arena_height=50, arena_length=arena_length, gap_width=8)
circleL = (arena.width/2 - 10, arena.width, arena.height/2)
circleR = (arena.width/2 + 10, arena.width, arena.height/2)
info_mat = info_map(arena, circleL, circleR, aperture, radius=5)
np.save(os.path.join(BASE_PATH, 'info_matrix_8.npy'), info_mat)

aperture = Aperture(arena_width=arena_width, arena_height=50, arena_length=arena_length, gap_width=9)
circleL = (arena.width/2 - 10, arena.width, arena.height/2)
circleR = (arena.width/2 + 10, arena.width, arena.height/2)
info_mat = info_map(arena, circleL, circleR, aperture, radius=5)
np.save(os.path.join(BASE_PATH, 'info_matrix_9.npy'), info_mat)

aperture = Aperture(arena_width=arena_width, arena_height=50, arena_length=arena_length, gap_width=10)
circleL = (arena.width/2 - 10, arena.width, arena.height/2)
circleR = (arena.width/2 + 10, arena.width, arena.height/2)
info_mat = info_map(arena, circleL, circleR, aperture, radius=5)
np.save(os.path.join(BASE_PATH, 'info_matrix_10.npy'), info_mat)

aperture = Aperture(arena_width=60, arena_height=50, arena_length=60, gap_width=11)
circleL = (arena.width/2 - 10, arena.width, arena.height/2)
circleR = (arena.width/2 + 10, arena.width, arena.height/2)
info_mat = info_map(arena, circleL, circleR, aperture, radius=5)
np.save(os.path.join(BASE_PATH, 'info_matrix_11.npy'), info_mat)

aperture = Aperture(arena_width=60, arena_height=50, arena_length=60, gap_width=12)
circleL = (arena.width/2 - 10, arena.width, arena.height/2)
circleR = (arena.width/2 + 10, arena.width, arena.height/2)
info_mat = info_map(arena, circleL, circleR, aperture, radius=5)
np.save(os.path.join(BASE_PATH, 'info_matrix_12.npy'), info_mat)

aperture = Aperture(arena_width=60, arena_height=50, arena_length=60, gap_width=13)
circleL = (arena.width/2 - 10, arena.width, arena.height/2)
circleR = (arena.width/2 + 10, arena.width, arena.height/2)
info_mat = info_map(arena, circleL, circleR, aperture, radius=5)
np.save(os.path.join(BASE_PATH, 'info_matrix_13.npy'), info_mat)

aperture = Aperture(arena_width=60, arena_height=50, arena_length=60, gap_width=14)
circleL = (arena.width/2 - 10, arena.width, arena.height/2)
circleR = (arena.width/2 + 10, arena.width, arena.height/2)
info_mat = info_map(arena, circleL, circleR, aperture, radius=5)
np.save(os.path.join(BASE_PATH, 'info_matrix_14.npy'), info_mat)

aperture = Aperture(arena_width=60, arena_height=50, arena_length=60, gap_width=15)
circleL = (arena.width/2 - 10, arena.width, arena.height/2)
circleR = (arena.width/2 + 10, arena.width, arena.height/2)
info_mat = info_map(arena, circleL, circleR, aperture, radius=5)
np.save(os.path.join(BASE_PATH, 'info_matrix_15.npy'), info_mat)

