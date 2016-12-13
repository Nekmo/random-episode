
.. image:: https://raw.githubusercontent.com/Nekmo/random-episode/master/random-episode.png
    :width: 100%

|

.. image:: https://img.shields.io/pypi/v/random-episode.svg?style=flat-square
  :target: https://pypi.org/project/random-episode/
  :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/pyversions/random-episode.svg?style=flat-square
  :target: https://pypi.org/project/random-episode/
  :alt: Python versions

.. image:: https://img.shields.io/codeclimate/github/Nekmo/random-episode.svg?style=flat-square
  :target: https://codeclimate.com/github/Nekmo/random-episode
  :alt: Code Climate

.. image:: https://img.shields.io/requires/github/Nekmo/random-episode.svg?style=flat-square
     :target: https://requires.io/github/Nekmo/random-episode/requirements/?branch=master
     :alt: Requirements Status



Play Random Episode
###################
Play a random chapter of your favorite series, like *The Simpsons*, *Futurama*, *Friends*...

With this program you can:

- Define **multiple directories** as a source.
- Optional support for **subdirectories**.
- Use **patterns** to filter files.
- Choose a **video player**, or let it choose one automatically.
- Native support for **chromecast**.

How to use it
=============

By default, it plays a video of the current directory with the default player.

.. code-block:: bash

    # Use current directory
    $ random-player

The syntax is:

.. code-block:: bash

    $ random-player[ --config <config_path>][ <player>[ <playlist>]]


The available parameters are:

* ``<config_path>``: by default it is ``random-episode.yml``.
* ``<player>``: by default it is ``native`` (default video player). ``chromecast`` is also available.
You can define others in the configuration.
* ``<playlist>``: you must define the playlists in the configuration.


Configuration
=============
Using a configuration file you can define playlists and players. An example:

.. code-block:: yaml

    # random-episode.yml
    # ------------------

    playlists:
        groening:  # playlist name
            directories:  # Multiple directories
              - '/path/to/simpsons/'
              - '/path/to/futurama/'
            recursive: true  # Optional
            patterns:  # Optional
              - '*.mkv'  # file pattern
              - '*.mp4'
              - '*.avi'
        simpsons-t1:  # playlist name
            directories: '/path/to/simpsons/The Simpsons/'
            patterns: 'The Simpsons 1x*'
    players:
        bedroom-chromecast:  # player name
            type: chromecast  # chromecast or native
            # Chromecast name. Useful if you have more than one
            name: bedroom
        vlc:  # player name
            # default type: native
            cmd: vlc  # command to execute


The options are:

* **playlists**:
    * **directories**: required. A list or just one.
    * **recursive**: optional. ``true`` or ``false``. Search for episodes recursively into subdirectories,
    * **patterns**: optional. A list or just one. Check the file names.
* **players**: by default chromecast (with type chromecast) and native (with type native).
    * **type**: optional. By default native.
    * **cmd**: Command to execute in native type.


Install
=======
If you have ``pip`` installed, you can install it with:

.. code:: bash

    sudo pip install random-episode


Amazon Dash
===========
It's easy to use Random Episode with your Amazon Dash. You just need to install::

    $ pip install amazon-dash

Then configure in Amazon Dash:

.. code:: yaml

    # amazon-dash.yml
    # ---------------

    44:65:0D:48:FA:88:
      name: Pompadour
      user: nekmo
      cmd: random-episode chromecast simpsons


License
=======
This project is under the MIT license.

*The Simpsons*, *The simpsons logo image* and *Futurama* are owned by 20th Century Fox Television.
*Friends* is owned by Warner Bros. Television.
