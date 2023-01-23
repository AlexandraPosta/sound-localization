import pyroomacoustics as pra
import numpy as np
from matplotlib.figure import Figure
from scipy.io import wavfile
import base64
from io import BytesIO

def getroom():
    # specify signal source
    fs, signal = wavfile.read("C:\\Users\\Alex\\source\\repos\\Data\\Sound\\arctic_a0010.wav")

    # generate 2D room
    corners = np.array([[0,0], [0,3.], [3.,3.], [3.,0]]).T  # [x,y]
    room = pra.Room.from_corners(corners, fs=fs, max_order=3)
    room.extrude(3.)

    # add sound source to room
    room.add_source([2.5,2.5,2.5], signal=signal)

    # add microphone
    mic_loc = [1.5, 1.5, 1.5]
    room.add_microphone(mic_loc)

    fig = Figure()
    ax = fig.subplots()
    ax.plot([1, 2])

    fig, ax = room.plot()
    ax.set_xlim([0, 4])
    ax.set_ylim([0, 4])
    ax.set_zlim([0, 4])

    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    encoded = base64.b64encode(buf.getvalue()).decode('utf-8')

    # Embed the result in the html output.
    html = '<img src=\'data:image/png;base64,{}\'>'.format(encoded)

    return html