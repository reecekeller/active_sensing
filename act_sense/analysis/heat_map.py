import numpy as np
import matplotlib.pyplot as plt
from scripts.utils import info_map
from scripts.arena import Arena, Aperture, Mouse, visualize_arena

BASE_PATH = "/Users/reecekeller/Documents/Xaq/act_sense/act_sense/data/"

info_map = np.load(BASE_PATH + 'info_matrix.npy')

arena = Arena(length=60, width=60, height=50)
aperture = Aperture(arena_width=60, arena_height=50, arena_length=60, gap_width=10)
mouse = Mouse(30, 0, 20)

plt.imshow(info_map)
plt.colorbar()
plt.show()
visualize_arena(arena, mouse, aperture)

