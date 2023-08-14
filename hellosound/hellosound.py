#!/usr/bin/env python3

# This was made to test a simple sound on pulseaudio in a snap

import subprocess
import os
import sys
from pkg_resources import resource_filename
import subprocess

soundfile = resource_filename(__name__, 'sounds/' + 'ring.oga')

def playme():
    """ Play a sound from freedesktop.org """

    subprocess.Popen(["paplay", soundfile])
