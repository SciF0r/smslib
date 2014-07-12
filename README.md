smslib
======

A library to handle SMS-related data: SMS PDU, SMPP PDU, User Data Headers (UDH), GSM alphabets, ...

Intention
---------

For a job I had to write an application which handles both, SMS PDU and SMPP
PDU - which also involved User Data Headers, fiddling with the GSM alphabets,
and so on. Fortunately, there are two libraries for this purpose:

* [smpplib](https://github.com/SciF0r/python-smpplib)
* [smspdu](https://github.com/SciF0r/smspdu)

Both work quite well, but are incomplete. Additionally, smpplib has not unit
tests. My intention is to learn from the insights I gained while using both
libraries and to write a new library which unites both and is complete.

Resources
---------

* [SMPP specification](http://www.nowsms.com/discus/messages/1/SMPP_v3_4_Issue1_2-24857.pdf)
* [SMS specification](http://www.etsi.org/deliver/etsi_gts/03/0340/05.03.00_60/gsmts_0340v050300p.pdf)

The Plan
--------

I think that the following steps should be done (in this order):

1. Declare the required classes to describe SMPP and SMPP PDU
2. Design an architecture which allows generic generation of PDU
3. Based on this, design the rest of the software
4. ...

Everything shall be unit tested.
