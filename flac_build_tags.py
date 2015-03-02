#! /usr/bin/env python3

import glob
import json

with open('info.json') as f:
    info = json.load(f)

flac_files = glob.glob('*.flac')
flac_files.sort()
print(flac_files)

if len(flac_files) == len(info['tracks']):
    for i in range(len(info['tracks'])):
        with open(flac_files[i].strip('.flac') + '.tag', 'w') as f:
            print('artist={}'.format(info['artist']), file=f)
            print('album={}'.format(info['album']), file=f)
            print('tracknumber={}/{}'.format(i+1, len(info['tracks'])), file=f)
            print('title={}'.format(info['tracks'][i]), file=f)
else:
    print('Error: Number of tracks.')
