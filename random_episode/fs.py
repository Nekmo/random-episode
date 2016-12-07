import random

from os3.fs.shortcuts import ls


def get_episodes(directories):
    all_episodes = []
    for directory in directories:
        all_episodes += list(ls(directory))
    return all_episodes


def get_random_episode(directories):
    return random.choice(get_episodes(directories))
