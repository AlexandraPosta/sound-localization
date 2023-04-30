import pyroomacoustics as pra
import numpy as np

from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt, patches

from scipy.io import wavfile
import base64
from io import BytesIO

aroom = None
microphones = None
sound_source_loc = None
fs = 16000
c = 343 # speed of sound
nfft = 256  # FFT size
freq_range = [300, 3500]
base = 1.
height = 10.
true_col = [0, 0, 0]
distance = 2.5 # meters
sound_files = ".\\data\\arctic_a0015.wav"


def add_microphone_room(mic_loc):
    aroom.add_microphone_array(mic_loc)


def getroom(room, sound_loc, mic):
    # Generate room
    global aroom
    room_dim = np.r_[float(room[0]), float(room[1]), 2.]
    fs, signal = wavfile.read(sound_files)
    aroom = pra.ShoeBox(room_dim, fs=fs, max_order=0)
    aroom.add_source([float(sound_loc[0]), float(sound_loc[1]), 1.], signal=signal)

    global sound_source_loc
    sound_source_loc = sound_loc

    # Add microphone
    global microphones
    microphones = np.c_[[float(mic[0][0]), float(mic[0][1]), 1.], [float(mic[1][0]), float(mic[1][1]), 1.]]
    aroom.add_microphone_array(microphones)

    # Run the simulation
    aroom.simulate()

    fig = plt.figure()
    ax = fig.subplots()
    fig, ax = aroom.plot()
    ax.set_xlim([0, float(room[0])])
    ax.set_ylim([0, float(room[1])])
    ax.set_zlim([0, 2.]) 

    html = encode(fig)
    return html


def runModel(model):
    spatial_resp = None
    X = pra.transform.stft.analysis(aroom.mic_array.signals.T, nfft, nfft // 2)
    X = X.transpose([2, 1, 0])

    # Construct the new DOA object and perform localization on the frames in X
    doa = pra.doa.algorithms[model](microphones, fs, nfft, c=c, num_src=1)
    doa.locate_sources(X, freq_range=freq_range)
    spatial_resp = doa.grid.values  
    min_val = spatial_resp.min()
    max_val = spatial_resp.max()
    spatial_resp = (spatial_resp - min_val) / (max_val - min_val)

    # Vizualize
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='polar')

    phi_plt = doa.grid.azimuth
    c_phi_plt = np.r_[phi_plt, phi_plt[0]]
    c_dirty_img = np.r_[spatial_resp, spatial_resp[0]]
    
    ax.plot(c_phi_plt, base + height * c_dirty_img, linewidth=3,alpha=0.55, linestyle='-', label="spectrum")
    plt.title(model)
    ax.set_xticks(np.linspace(0, 2 * np.pi, num=24, endpoint=False))
    ax.set_yticks(np.linspace(0, 0, 0))
    ax.xaxis.grid(visible=True, color=[0.3, 0.3, 0.3], linestyle=':')
    ax.set_ylim([0, 1.05*(base + height)])

    html = encode(fig)
    return html


def pathFinder(room_dim=np.r_[float(5), float(5), 2.], sound_loc=[4, 4]):
    plt.rcParams["figure.figsize"] = [8, 8]
    plt.rcParams["figure.autolayout"] = True
    fig, _ = plt.subplots()
    ax = plt.gca()

    sound = patches.Circle((4, 4), radius=0.05, edgecolor='green', facecolor='none', linewidth=2)
    ax.add_patch(patches.Rectangle((.1, .1), 5, 5, edgecolor='black', facecolor='none', linewidth=2))
    ax.add_patch(sound)

    centre_mic = [(microphones[0][0]-microphones[1][0])/2, (microphones[0][1]-microphones[1][1])/2]
    found = False

    while found:
        # Generate room
        fs, signal = wavfile.read(sound_files)
        room = pra.ShoeBox(room_dim, fs=fs, max_order=0)
        room.add_source([float(sound_loc[0]), float(sound_loc[1]), 1.], signal=signal)

        microphones = np.c_[[2.5-0.1, 0.5, 0], [2.5+0.1, 0.5, 0]]
        room.add_microphone_array(microphones)

        room.simulate()

        X = pra.transform.stft.analysis(room.mic_array.signals.T, nfft, nfft // 2)
        X = X.transpose([2, 1, 0])

        # Construct the new DOA object and perform localization on the frames in X
        doa = pra.doa.algorithms['MUSIC'](microphones, fs, nfft, c=c, num_src=1)
        doa.locate_sources(X, freq_range=freq_range)
        pred = doa.azimuth_recon[0] 
        if pred > np.pi:
            pred = (2 * np.pi - pred) * 180 / np.pi
        else:
            pred =  pred * 180 / np.pi
        pred = round(pred)

    
        if centre_mic == sound_source_loc:
            found = True
        else:
            centre_mic
            


    # Vizualize
    plt.title("Path planner")
    ax.set_xlim([0, 5.2])
    ax.set_ylim([0, 5.2])

    html = encode(fig)
    return html


def encode(figure):
    # Save it to a temporary buffer.
    buf = BytesIO()
    figure.savefig(buf, format="png")
    encoded = base64.b64encode(buf.getvalue()).decode('utf-8')

    # Embed the result in the html output.
    image = '<img src=\'data:image/png;base64,{}\'>'.format(encoded)
    return image