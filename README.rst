
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
