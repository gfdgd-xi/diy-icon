#!/usr/bin/env python3
import os
import sys
for i in sys.argv:
    os.system(f"convert '{i}' -resize 48x48 '{i}'")
