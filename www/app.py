# -*- coding: utf-8 -*-
 
__author__ = 'Alex Zhang'

'''
async web application
'''

import logging; logging.basicConfig(level=logging.INFO)

import asynico, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
	return web.Response(body=b'<h1>Awesome')