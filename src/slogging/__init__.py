#!/usr/bin/env python3
# @file: __init__.py
# @date: 2023-03-29T23:24:04
# @author: Aroldo Souza-Leite
# @description: slogging
"""
slogging
"""
from pkg_resources import get_distribution, DistributionNotFound
__version__ = "0.0"
try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    pass  # package is not installed
# exporting:
from .sloggers import get_slog




