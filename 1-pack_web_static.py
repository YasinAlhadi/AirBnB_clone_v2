#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""

from datetime import datetime
from fabric.api import local


def do_pack():
    """generates a tgz archive"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static".format(date))
        file_name = "versions/web_static_{}.tgz".format(date)
        return file_name
    except Exception:
        return None
