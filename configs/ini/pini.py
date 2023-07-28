#!/usr/bin/env python3

# https://docs.python.org/3/library/configparser.html

import configparser


config = configparser.ConfigParser()
config['DEFAULT'] = {'ServerAliveInterval': 45,
                     'Compression': 'yes',
                     'CompressionLevel': 9}

u = 'user'
config['forge.exmaple'] = {}
config['forge.exmaple'][u] = 'foo'

config['topsecret.server.example'] = {}
topsecret = config['topsecret.server.example']
topsecret['Port'] = '50022'
topsecret['ForwardX11'] = 'no'

config['DEFAULT']['ForwardX11'] = 'yes'


with open('example.ini', 'w') as f:
    config.write(f)
