import argparse
parser = argparse.ArgumentParser(prog = "Braille'n Speak Emulator")
parser.add_argument("port",  help = "Specifies the COM port to which the emulator connects.")
parser.add_argument( "-v", "--voice", default = "en", help = "Specifies the Espeak voice that the emulator will use. This should be given in language[-dialect]+[variant] format, (e. g.: en, en-us, en+max, en-us+max).")
parser.add_argument("--habla", action = 'store_true', default=False, help = "If specified, makes the emulator compatible with Habla")
args = parser.parse_args()
