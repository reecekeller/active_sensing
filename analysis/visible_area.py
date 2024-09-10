from scripts.utils import *
from scripts.arena import *

arena = Arena(length=60, width=60, height=50)
aperture = Aperture(arena_width=60, arena_height=50, arena_length=60, gap_width=10)
circleL = (arena.width/2 - aperture.gap_width, arena.width, arena.height/2)
circleR = (arena.width/2 + aperture.gap_width, arena.width, arena.height/2)

info_mat = info_map(arena, circleL, circleR, aperture, radius=5)
np.save(info_mat)
print(info_mat)
