import subprocess

CHROMECAST_CMD = 'stream2chromecast'
COMMON_PLAYERS = ['xdg-open', 'bomi', 'vlc', 'smplayer', 'totem', 'mpv', 'mplayer']


def execute(args):
    p = subprocess.Popen(args)
    p.communicate()


def chromecast(path, cmd=None):
    cmd = cmd or CHROMECAST_CMD
    args = [cmd]
    if not path.endswith('mp4'):
        args += ['-transcode']
    execute(args + [path])


def native(path, cmd=None):
    if cmd is None:
        cmds = COMMON_PLAYERS
    else:
        cmds = [cmd]
    for cmd in cmds:
        try:
            execute([cmd] + [path])
        except OSError:
            pass
        else:
            return


def exec_player(path, type='native', cmd=None):
    return globals()[type](path, cmd)
