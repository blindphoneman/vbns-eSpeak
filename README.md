# vbns-eSpeak

## Introduction
This is a braille N'Speak emulator, which works with MS-DOS screen readers. It was originally created by [Tyler Spivey](https://www.allinaccess.com), and modified by Sukil Etxenike. [Here is the original version](http://batsupport.com/unsupported/dosbox/vbns.zip).

## Variants
There are two versions of this project:
* This one which, as the original version, uses eSpeak as output.
* And [one which can interact with many Windows screen readers and SAPI](https://github.com/sukiletxe/vbns-ao2).

## Modifications until first commit
* Added the option to select by voice name rather than selecting the default English voice, allowing selection of variants.
* Used argparse instead of sys.argv[n], to include help in the commands.
* Added Habla mode (currently, for unknown reasons, it doesn't work, so don't use it).

## Requirements
You will need Com0Com for the emulator to work properly:
* [Download for Windows XP](http://sourceforge.net/projects/com0com/files/com0com/3.0.0.0/com0com-3.0.0.0-i386-and-x64-unsigned.zip/download)
* [Download for Windows 7 and newer (x64)](http://code.google.com/p/powersdr-iq/downloads/detail?name=setup_com0com_W7_x64_signed.exe&can=2&q=)
* [download for Windows 7 and newer (x86)](http://code.google.com/p/powersdr-iq/downloads/detail?name=setup_com0com_W7_x86_signed.exe&can=2&q=)

To run the emulator, simply specify the portname and the voice in the command line. For example:

emu com8 -v en-us+m3

Will use the COM8 port (the default in ASAP for talking Dosbox), And the US English voice, with the Male 3 variant. Note that you also can  omit the variant name.

### To run from source and compile
You will need:
* Python (I use version 2.7.10).
* Pyserial

You will need py2exe to make a compiled executable.

