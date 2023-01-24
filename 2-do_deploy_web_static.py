#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['35.153.193.218', '100.27.0.214']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        unpack = archive_path.split("/")[1]
        no_ext = unpack.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(unpack, path, no_ext))
        run('rm /tmp/{}'.format(unpack))
        run('mv {}{}/web_static/* {}{}/'.format(path, no_ext, path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{} /data/web_static/current'.format(path, no_ext))
        return True
    except Exception:
        return False
