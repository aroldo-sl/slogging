#!/usr/bin/env python3
# @file: sloggers.py
# @date: 2023-03-29T23:25:42
# @author: Aroldo Souza-Leite
# @description: 
"""
inline documentation of this module (99:.\*.py)
"""
import os, sys, logging, random, string
fmt = "%(levelname)s:%(name)s:%(module)s.%(funcName)s:%(lineno)s\n%(message)s"

#
class SLogFormatter(logging.Formatter):
        "A log formatter for SLogHandler"
        def __init__(self, fmt = fmt):
            super().__init__(fmt = fmt)

#
class SLogHandler(logging.StreamHandler):
        "Simple logging handler."
        def __init__(self, stream = sys.stderr, level = logging.DEBUG, fmt = fmt):
            super().__init__(stream = stream)
            self.setLevel(level)
            self.setFormatter(SLogFormatter())

#
def get_slog(level = logging.DEBUG, handler = None, fmt = fmt):
    "Make a simple logger"
    if handler is None:
        handler = SLogHandler(fmt = fmt)
    handler.setLevel(level)
    random_string = "".join(random.sample(string.ascii_letters, 4))
    log_name  = __name__ + "-" + random_string
    slog = logging.getLogger(log_name)
    slog.addHandler(handler)
    slog.setLevel(level)
    return slog












