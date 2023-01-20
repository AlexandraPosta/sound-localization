import pyroomacoustics as pra
import numpy as np
import matplotlib.pyplot as plt

corners = np.array([[0,0], [0,3], [3,3], [3,0]]).T  # [x,y]
room = pra.Room.from_corners(corners)

fig, ax = room.plot()
ax.set_xlim([-1, 6])
ax.set_ylim([-1, 4])
