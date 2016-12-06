import subprocess

import os

from os3.fs.shortcuts import ls


DIRECTORY = os.environ['DIRECTORY']


args = ['stream2chromecast']

episode = ls(DIRECTORY).random()
if not episode.name.endswith('mp4'):
    args += ['-transcode']

subprocess.Popen(args + [episode.path])
