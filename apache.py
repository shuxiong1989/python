#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: apahce.py

from __future__ import print_function

ips = []

with open('/root/python/access.log') as f:
    for line in f:
        ips.append(line.split()[0])

#print(len(ips))
#print(set(ips))
print("PV is {0}".format(len(ips)))
print("UV is {0}".format(set(ips)))
