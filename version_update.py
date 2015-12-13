#!/usr/bin/env python
# -*- coding: utf-8 -*-

from milkcocoa import __version__ as version
from milkcocoa import __build_version__ as build_version

from sh import git


def create_tag(v, bv):
    if not isinstance(v, str):
        v = str(v)
    if not isinstance(bv, str):
        bv = str(bv)

    tag_version = v + '-' + bv
    git('tag', '-a', tag_version)
    return tag_version


def upload_tag(tag_version):
    git('push', 'origin', tag_version)


def update_build_version(build_version_old):
    build_version_old += 1
    return build_version_old


def get_build_version():
    number_version = build_version
    if isinstance(number_version, str):
        number_version = int(number_version)
    return number_version


def get_version():
    return version


def save_build_version(old_build_version, build_version):
    old_build_version = '__build_version__ = "' + str(old_build_version) + '"'
    build_version = '__build_version__ = "' + str(build_version) + '"'

    with open('milkcocoa/__init__.py', 'r+') as init_file:
        lines = init_file.readlines()
        lines = [line.replace(old_build_version, build_version) for line in lines]
        init_file.seek(0)  # Rewrite everything
        init_file.writelines(lines)


if __name__ == '__main__':
    old_bv = get_build_version()
    bv = update_build_version(old_bv)
    save_build_version(old_bv, bv)

    v = get_version()

    tag_version = create_tag(v, bv)
    upload_tag(tag_version)
