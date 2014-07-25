#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# vim: autoindent expandtab tabstop=4 sw=4 sts=4 filetype=python

"""Constants for SMPP"""

import enum


class data_coding(enum.Enum):
    """data_coding according to chapter 5.2.19"""
    # SMSC Default Alphabet
    DEFAULT       = 0b00000000
    # IA5 (CCITT T.50)/ASCII (ANSI X3.4)
    IA5           = 0b00000001
    # Octet unspecified (8-bit binary)
    OCTET_1       = 0b00000010
    # Latin 1 (ISO-8859-1)
    LATIN_1       = 0b00000011
    # Octet unspecified (8-bit binary)
    OCTET_2       = 0b00000100
    # JIS (X 0208-1990)
    JIS           = 0b00000101
    # Cyrillic (ISO-8859-5)
    CYRILLIC      = 0b00000110
    # Latin/Hebrew (ISO-8859-8)
    LATIN_HEBREW  = 0b00000111
    # UCS2 (ISO/IEC-10646)
    UCS2          = 0b00001000
    # Pictogram Encoding
    PICTOGRAM     = 0b00001001
    # ISO-2022-JP (Music Codes)
    MUSIC         = 0b00001010
    # Extended Kanji JIS(X 0212-1990)
    EXT_KANJI_JIS = 0b00001101
    # KS C 5601
    KSC_C         = 0b00001110
    # Not implemented:
    # - 1 1 0 0 x x x x GSM MWI control - see [GSM 03.38]
    # - 1 1 0 1 x x x x GSM MWI control - see [GSM 03.38]
    # - 1 1 1 1 x x x x GSM message class control - see [GSM 03.38]
    # All other values are reserved


class esm_class(object):
    """esm_class according to chapter 5.2.12

    The esm_class field consists of three parts:
    - Mode
    - Type
    - Feature
    The signification of Mode and Type depends on the direction the PDU is
    sent. Thank you balu on stackoverflow.com for the help.
    See http://stackoverflow.com/questions/24957795/
    """
    BITMASK_MODE    = 0b00000011
    BITMASK_TYPE    = 0b00111100
    BITMASK_FEATURE = 0b11000000

    class Modes(enum.Enum):
        """Messaging Mode (bits 1-0)

        Depends on the direction (ESME<->SMSC)
        """
        pass

    class Types(enum.Enum):
        """Message Type (bits 5-2)

        Depends on the direction (ESME<->SMSC)
        """
        pass

    class Features(enum.Enum):
        """GSM Network specific features (bits 7-6)"""
        # No specific features selected
        NONE                = 0b00
        # UDHI (UDH Indicator, only relevant for MT short messages)
        UDHI                = 0b01
        # Set Reply Path (only relevant for GSM network)
        REPLY_PATH          = 0b10
        # Set UDHI and Reply Path (only relevant for GSM network)
        UDHI_AND_REPLY_PATH = 0b11

    def __init__(self, mode, type_, feature):
        self.mode    = mode
        self.type    = type_
        self.feature = feature

    def __bytes__(self):
        """Use this to write an instance of esm_class to a file-like object or
        stream, e.g..: mysocket.send(bytes(my_esm_class_obj))
        """
        return ((self.feature << 6) | (self.type << 2) | self.mode).to_bytes(
            1,
            byteorder='big'
        )

    @classmethod
    def parse(cls, filelike):
        """Use this to parse incoming data from a file-like object and create
        an instance of esm_class accordingly, e.g:
        my_esm_class_obj = esm_class.parse(stream)
        """
        data = filelike.read(1)
        mode = int.from_bytes((data & cls.BITMASK_MODE))
        type_ = int.from_bytes((data & cls.BITMASK_TYPE) >> 2)
        feature = int.from_bytes((data & cls.BITMASK_TYPE) >> 6)
        return cls(type_, mode, feature)


class esm_class_outgoing(esm_class):
    """For submit_sm, submit_multi and data_sm (ESME->SMSC)"""
    class Modes(esm_class.Modes):
        """Messaging Mode (bits 1-0)"""
        # Default SMSC Mode (e.g. Store and Forward)
        DEFAULT           = 0b00
        # Datagram mode
        DATAGRAM          = 0b01
        # Forward (i.e. Transaction) mode
        FORWARD           = 0b10
        # Store and Forward mode
        STORE_AND_FORWARD = 0b11

    class Types(esm_class.Types):
        """Message Type (bits 5-2)"""
        # Default message Type (i.e. normal message)
        DEFAULT           = 0b0000
        # Short Message contains ESME Delivery Acknowledgement
        ESME_DELIVERY_ACK = 0b0010
        # Short Message contains ESME Manual/User Acknowledgement
        ESME_USER_ACK     = 0b0100
        # All other values are reserved


class esm_class_incoming(esm_class):
    """For deliver_sm and data_sm (SMSC->ESME)"""
    class Modes(esm_class.Modes):
        """Messaging Mode (bits 1-0)

        Not applicable - ignore bits 0 and 1
        """
        pass

    class Types(esm_class.Types):
        """Message Type (bits 5-2)"""
        # Default message Type (i.e. normal message)
        DEFAULT              = 0b0000
        # Short Message contains SMSC Delivery Receipt
        SME_DELIVERY_RECEIPT = 0b0001
        # Short Message contains SME Delivery Acknowledgement
        SME_DELIVERY_ACK     = 0b0010
        # Short Message contains SME Manual/User Acknowledgment
        SME_USER_ACK         = 0b0100
        # Short Message contains Conversation Abort (Korean CDMA)
        CONVERSATION_ABORT   = 0b0110
        # Short Message contains Intermediate Delivery Notification
        INTERMEDIATE         = 0b1000
        # All other values are reserved


class NPI(enum.Enum):
    """Numeric Plan Indicators (NPI) according to chapter 5.2.6"""
    UNKNOWN       = 0b00000000
    # ISDN (E163/E164)
    ISDN          = 0b00000001
    # Data (X.121)
    DATA          = 0b00000011
    # Telex (F.69)
    TELEX         = 0b00000100
    # Land Mobile (E.212)
    LAND_MOBILE   = 0b00000110
    NATIONAL      = 0b00001000
    PRIVATE       = 0b00001001
    ERMES         = 0b00001010
    # Internet (IP)
    INTERNET      = 0b00001110
    # WAP Client Id (to be defined by WAP Forum)
    WAP_CLIENT_ID = 0b00010010
    # All other values are reserved


class TON(enum.Enum):
    """Type of Number (TON) according to chapter 5.2.5"""
    UNKNOWN           = 0b00000000
    INTERNATIONAL     = 0b00000001
    NATIONAL          = 0b00000010
    NETWORK_SPECIFIC  = 0b00000011
    SUBSCRIBER_NUMBER = 0b00000100
    ALPHANUMERIC      = 0b00000101
    ABBREVIATED       = 0b00000110
    # All other values are reserved
