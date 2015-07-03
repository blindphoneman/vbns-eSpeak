# vbns-eSpeak
This is a braille N'Speak emulator, which works with MS-DOS screen readers. It was originally created by [Tyler Spivey](https://www.allinaccess.com), and modified by Sukil Etxenike. [Here is the original version](http://batsupport.com/unsupported/dosbox/vbns.zip).

## Modifications
* Added the option to select by voice name rather than by language, allowing selection of variants.
* Used argparse instead of sys.argv[n], to include help in the commands.
* Added Habla mode.

## Requirements
You will need Com0Com for the emulator to work properly:
* [Download for Windows XP](http://sourceforge.net/projects/com0com/files/com0com/3.0.0.0/com0com-3.0.0.0-i386-and-x64-unsigned.zip/download)
* [Download for Windows 7 and newer (x64)](http://code.google.com/p/powersdr-iq/downloads/detail?name=setup_com0com_W7_x64_signed.exe&can=2&q=)
* [download for Windows 7 and newer (x86](http://code.google.com/p/powersdr-iq/downloads/detail?name=setup_com0com_W7_x86_signed.exe&can=2&q=)

### To run from source and compile
You will need:
* Python (I use version 2.7.10).
* Pyserial

You will need py2exe to make a compiled executable.

## Usage
Simply specify the portname and the voice in the command line. For example:
emu com8 en-us+m3
In addition, if you specify --habla, a mode will be executed where everything received by the emulator will be spoken after 300 milliseconds, instead of waiting for a carriage return. This was made to make a Spanish screen reader called Habla, but for unknown reasons, it failed.
