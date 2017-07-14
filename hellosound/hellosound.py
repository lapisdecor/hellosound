#!/usr/bin/env python3

# This was made to test a simple sound on pulseaudio in a snap

import subprocess

def playme():
    """ Play a sound from freedesktop.org """
    soundfile = "/usr/share/sounds/freedesktop/stereo/phone-incoming-call.oga"

    subprocess.Popen(["paplay", soundfile])
