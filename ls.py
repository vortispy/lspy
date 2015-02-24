#!/usr/bin/env python
# encoding: utf-8
import os
import stat
import pwd
import grp
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("path", default=".", nargs="?")
parser.add_argument("-a", "--all", action="store_true")
parser.add_argument("-l", "--list", action="store_true")
args = parser.parse_args()

def ls():
    path = args.path
    if args.all:
        listdir = os.listdir(path)
    else:
        listdir = [f for f in os.listdir(path) if not f.startswith(".")]
    listdir.sort()
    output = ""
    for filename in listdir:
        if args.list:
            filepath = os.path.join(filename)
            file_stat = os.lstat(filepath)
            mode = file_stat.st_mode
            filepath += "/" if stat.S_ISDIR(mode) else ""
            nlink = file_stat.st_nlink
            username = pwd.getpwuid(file_stat.st_uid).pw_name
            group = grp.getgrgid(file_stat.st_gid).gr_name
            fsize = file_stat.st_size
            access = convertAccess(mode)
            ctime = time.strftime("%b %d %H:%M", time.localtime(file_stat.st_ctime))
            output += "%s %d %s %s %d %s %s\n" % (access, nlink, username, group, fsize, ctime, filepath)
        else:
            output += filename + " "
    print output


def convertAccess(mode):
    access = ["-"] * 10

    if stat.S_ISDIR(mode):
        access[0] = "d"
    elif stat.S_ISLNK(mode):
        access[0] = "l"
    if stat.S_IRUSR & mode:
        access[1] = "r"
    if stat.S_IWUSR & mode:
        access[2] = "w"
    if stat.S_IXUSR & mode:
        access[3] = "x"
    if stat.S_IRGRP & mode:
        access[4] = "r"
    if stat.S_IWGRP & mode:
        access[5] = "w"
    if stat.S_IXGRP & mode:
        access[6] = "x"
    if stat.S_IROTH & mode:
        access[7] = "r"
    if stat.S_IWOTH & mode:
        access[8] = "w"
    if stat.S_IXOTH & mode:
        access[9] = "x"

    return "".join(access)

if __name__ == '__main__':
    ls()
