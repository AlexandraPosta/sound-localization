# Visualization
import numpy as np
from matplotlib.figure import Figure

# Environment and sound
import pyroomacoustics as pra
from scipy.io import wavfile

# Server
import http.server
import socketserver
from urllib.parse import parse_qs, urlparse
import base64
from io import BytesIO