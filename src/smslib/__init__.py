#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# vim: autoindent expandtab tabstop=4 sw=4 sts=4 filetype=python

"""Implement (parts of) SMPP v3.4 and SMS PDU handling

While SMPP is not limited to SMS, it is the most common use case. This library
intends to provide an easy way to handle SMS and forward them between SMPP and
GSM. Also, some common helper classes are implemented, such as handling of
7-bit encoded text and semi-byte encoded phone numbers.
"""
