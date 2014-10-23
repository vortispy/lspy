#!/usr/bin/env python
# encoding: utf-8
import os
import stat
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
            filepath = os.path.join(path, filename)
            mode = os.lstat(filepath).st_mode
            access = convertAccess(mode)
            output += access + " " + filename + "\n"
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
