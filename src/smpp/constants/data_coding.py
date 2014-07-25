#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# vim: autoindent expandtab tabstop=4 sw=4 sts=4 filetype=python

"""data_coding schemes according to chapter 5.2.19"""

# TODO: Clarify difference between OCTET_1 and OCTET_2

# Values not defined here are reserved
DEFAULT      = (0x00, 'SMSC Default Alphabet')
IA5          = (0x01, 'IA5 (CCITT T.50)/ASCII (ANSI X3.4)')
OCTET_1      = (0x02, 'Octet unspecified (8-bit binary)')
LATIN_1      = (0x03, 'Latin 1 (ISO-8859-1)')
OCTET_2      = (0x04, 'Octet unspecified (8-bit binary)')
JIS          = (0x05, 'JIS (X 0208-1990)')
CYRILLIC     = (0x06, 'Cyrillic (ISO-8859-5)')
LATIN_HEBREW = (0x07, 'Latin/Hebrew (ISO-8859-8)')
UCS2         = (0x08, 'UCS2 (ISO/IEC-10646)')
PICTOGRAM    = (0x09, 'Pictogram Encoding')
MUSIC_CODES  = (0x0A, 'ISO-2022-JP (Music Codes)')
KANJI_JIS    = (0x0D, 'Extended Kanji JIS(X 0212-1990)')
KS_C         = (0x0E, 'KS C 5601')

# Did not implement these values:
# - 1 1 0 0 x x x x GSM MWI control - see [GSM 03.38]
# - 1 1 0 1 x x x x GSM MWI control - see [GSM 03.38]
# - 1 1 1 1 x x x x GSM message class control - see [GSM 03.38]
