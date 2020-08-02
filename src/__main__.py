#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import gui

app = gui.Application(sys.argv)

main_window = gui.MainWindow()
main_window.showMaximized()

RetCode = app.exec_()
sys.exit(RetCode)
