#! /usr/bin/env python3

import os
import glob
import json
import csv

if os.path.isfile('info.json'):
    with open('info.json') as f:
        info = json.load(f)

if os.path.isfile('info.csv'):
    with open('info.csv', newline='') as f:
        info = []
        for row in csv.reader(f, delimiter=',', quotechar='"'):
            info.append(row)

flac_files = glob.glob('*.flac')
flac_files.sort()
print(flac_files)

if type(info) == dict:
    if len(flac_files) == len(info['tracks']):
        for i in range(len(info['tracks'])):
            with open(flac_files[i].split('.flac')[0] + '.tag', 'w') as f:
                print('artist={}'.format(info['artist']), file=f)
                print('album={}'.format(info['album']), file=f)
                print('tracknumber={}/{}'.format(i+1, len(info['tracks'])), file=f)
                print('title={}'.format(info['tracks'][i]), file=f)
    else:
        print('Error: Number of tracks.')
elif type(info) == list:
    if len(flac_files) == len(info):
        i = 1
        for track in zip(flac_files, info):
            with open(track[0].split('.flac')[0] + '.tag', 'w') as f:
                print('artist={}'.format(track[1][0]), file=f)
                print('title={}'.format(track[1][1]), file=f)
                print('tracknumber={}/{}'.format(i, len(info)), file=f)
            i += 1
    else:
        print('Error: Number of tracks.')
