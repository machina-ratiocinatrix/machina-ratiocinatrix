# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from .config import Config


def machina(config:Config): # arg=None):
    print('Machina.')


if __name__ == '__main__':
    conf = Config()
    machina(config=conf)
