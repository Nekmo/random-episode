import os

from random_episode.config import Config
from random_episode.fs import get_random_episode


class RandomEpisode(object):
    def __init__(self, config_path, playlist_name=None, player_name='native'):
        self.config = Config(config_path)
        self.playlist = self.config.get_playlist(playlist_name)
        self.player_name = player_name

    def get_directories(self):
        if self.playlist is None:
            return [os.getcwd()]
        return self.playlist['directories']

    def get_random_episode(self):
        return get_random_episode(self.get_directories())

    def play_episode(self, episode):
        self.config.exec_player(episode.path, self.player_name)

    def play_random(self):
        episode = self.get_random_episode()
        self.play_episode(episode)
