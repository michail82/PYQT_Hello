#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication


class Application(QApplication):

    def __init__(self, argv):
        super().__init__(argv)
