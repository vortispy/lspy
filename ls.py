#!/usr/bin/env python
# encoding: utf-8
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("path", default=".", nargs="?")
parser.add_argument("-a", "--all", action="store_true")
parser.add_argument("-l", "--list", action="store_true")
args = parser.parse_args()

def ls():
    path = args.path
    listdir = os.listdir(path)
    listdir.sort()
    for filename in listdir:
        if args.all:
            print filename,
        elif not filename.startswith("."):
            print filename,
        elif args.list:
            filepath = os.path.join(path, filename)
            mode = os.stat(filepath).st_mode
            access = convertAccess(mode)
            print access + " " + filename


def convertAccess(mode):
    access = ["-"] * 10

    S_IFDIR = 004000

    S_IRUSR = 00400
    S_IWUSR = 00200
    S_IXUSR = 00100
    
    S_IRGRP = 00040
    S_IWGRP = 00020
    S_IXGRP = 00010

    S_IROTH = 00004
    S_IWOTH = 00002
    S_IXOTH = 00001

    if S_IFDIR & mode:
        access[0] = "d"
    if S_IRUSR & mode:
        access[1] = "r"
    if S_IWUSR & mode:
        access[2] = "w"
    if S_IXUSR & mode:
        access[3] = "x"
    if S_IRGRP & mode:
        access[4] = "r"
    if S_IWGRP & mode:
        access[5] = "w"
    if S_IXGRP & mode:
        access[6] = "x"
    if S_IROTH & mode:
        access[7] = "r"
    if S_IWOTH & mode:
        access[8] = "w"
    if S_IXOTH & mode:
        access[9] = "x"

    return "".join(access)

if __name__ == '__main__':
    ls()
