import os

from random_episode.config import Config
from random_episode.fs import get_random_episode
from random_episode.players import exec_player


class RandomEpisode(object):
    def __init__(self, config_path, playlist_name=None, player='native'):
        self.config = Config(config_path)
        self.playlist = self.config.get_playlist(playlist_name)
        self.player = player

    def get_directories(self):
        if self.playlist is None:
            return [os.getcwd()]
        return self.playlist['directories']

    def get_random_episode(self):
        return get_random_episode(self.get_directories())

    def play_episode(self, episode):
        exec_player(episode.path)

    def play_random(self):
        episode = self.get_random_episode()
        self.play_episode(episode)
