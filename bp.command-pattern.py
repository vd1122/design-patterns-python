#!/usr/bin/env python

"""
Behavioural Pattern --> Command Pattern

A command is wrapped as object and passed to invoker object.
Invoker object looks for the appropriate object which can handle this command and
passes the command to the corresponding object which executes the command.
"""
import os
import shutil
from pathlib import Path
from os.path import lexists

class MoveFileCommand:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def do(self):
        self.move_file(self.src, self.dest)

    def undo(self):
        self.move_file(self.dest, self.src)

    def move_file(self, src, dest):
        shutil.move(src, dest)


def main():
    src_file = "file1"
    dest_file = "file2"

    Path(src_file).touch()

    assert (lexists(src_file))
    assert (not lexists(dest_file))

    action_move_file = MoveFileCommand(src_file, dest_file)

    action_move_file.do()
    assert (not lexists(src_file))
    assert (lexists(dest_file))

    action_move_file.undo()
    assert (lexists(src_file))
    assert (not lexists(dest_file))

    os.unlink(src_file)
    assert (not lexists(src_file))

if __name__ == "__main__":
    main()
