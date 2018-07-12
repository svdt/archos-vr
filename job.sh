#!/bin/bash
python2.7 stream.py | mplayer -cache 2048 -fps 25 -nosound -vc ffmjpeg -
