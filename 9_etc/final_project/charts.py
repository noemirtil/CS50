#!/usr/bin/env python

import json
import requests
import sys

import billboard

# from albums import discography


def get_charts(y):
    charts = billboard.ChartData("pop-songs", year=y)
    return charts
