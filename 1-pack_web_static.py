#!/usr/bin/python3
"""Generates a .tgz archive from the contents of
the web_static folder"""

import time
from fabric.api import local
from os.path import exists


def do_pack():
    """Adds all files in the folder web_static to the final archive"""
    timestamp = time.strftime("%Y%m%d%H%M%S")
    try:
        if not exists("versions"):
            local("mkdir -p versions")

        archive_path = "versions/web_static_{}.tgz".format(timestamp)
        local("tar -cvzf {} -C web_static/ .".format(archive_path))
        return archive_path

    except Exception as e:
        pass