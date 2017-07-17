#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from collections import Counter


c = Counter()
with open('/root/python/access.log') as f:
    for line in f:
        c[line.split()[6]] += 1

print(c)
