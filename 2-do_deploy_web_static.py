#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers"""
from fabric import Group, env
from os.path import exists

env.hosts = ["100.25.102.191", "100.26.161.26"]
env.user = "ubuntu"
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """Deploy web files to server"""
    if not exists(archive_path):
        return False
    with Group(*env.hosts,
                     user=env.user,
                     connect_kwargs={"key_filename": env.key_filename})as conn:
        # Upload archive
        conn.put(archive_path, '/tmp/')

        timestamp = archive_path.split('.')[0][-14:]
        conn.sudo('mkdir -p /data/web_static/releases/web_static_{}/'
                  .format(timestamp))

        # Uncompress archive, delete archive, Move files into Host
        # web_static then remove the src web_static dir
        conn.sudo('tar -vxzf /tmp/web_static_{}.tgz -C \
                  /data/web_static/releases/web_static_{}/'
                  .format(timestamp, timestamp))
        conn.sudo('rm /tmp/web_static_{}.tgz'.format(timestamp))
        conn.sudo('mv /data/web_static/releases/web_static_{}/web_static/* \
                  /data/web_static/releases/web_static_{}/'
                  .format(timestamp, timestamp))
        conn.sudo('rm -rf \
                  /data/web_static/releases/web_static_{}/web_static'
                  .format(timestamp))

        # Delete pre-existing sym link and re-establish
        conn.sudo('rm -rf /data/web_static/current')
        conn.sudo('ln -s /data/web_static/releases/web_static_{}/ \
                  /data/web_static/current'.format(timestamp))
