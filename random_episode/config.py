from yaml import load

from random_episode.exceptions import ConfigException
from random_episode.players import exec_player

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


class Config(dict):
    def __init__(self, file, **kwargs):
        super().__init__(**kwargs)
        self.file = file
        self.read()

    def read(self):
        self.update(load(open(self.file), Loader))
        self['playlists'] = self.get('playlists', {})
        self['players'] = self.get('players', {})
        if not 'chromecast' in self['players']:
            self['players']['chromecast'] = {'type': 'chromecast'}

    def get_playlist(self, playlist_name):
        if playlist_name is None:
            return
        if playlist_name not in self['playlists']:
            raise ValueError('{} is not a configured playlist.'.format(playlist_name))
        playlist = self['playlists'][playlist_name]
        if 'directories' not in playlist:
            raise ConfigException('You must specify a directories in the playlist {}'.format(playlist_name))
        return playlist

    def get_player(self, player_name):
        if player_name is None:
            return
        if player_name not in self['players']:
            raise ValueError('{} is not a configured player_name.'.format(player_name))
        return self['players'][player_name]

    def exec_player(self, path, player_name='native'):
        return exec_player(path, **self.get_player(player_name))
