from setuptools import setup, find_packages
import py2exe

import os, platform, fnmatch
from glob import glob
def get_data():
  if platform.architecture()[0][:2] == "32":
   return [
   ("Microsoft.VC90.CRT", glob("windows_vc++/msvc32/Microsoft.VC90.CRT/*")),
   ("Microsoft.VC90.MFC", glob("windows_vc++/msvc32/Microsoft.VC90.MFC/*")),]
  elif platform.architecture()[0][:2] == "64":
   return [
   ("Microsoft.VC90.CRT", glob("windows_vc++/msvc64/Microsoft.VC90.CRT/*")),
   ("Microsoft.VC90.MFC", glob("windows_vc++/msvc64/Microsoft.VC90.MFC/*")),]

def get_espeak():
    answer = []
    tmp = []
    for root, dirs, files in os.walk("espeak-data"):
        for item in glob(os.path.join(root, "*")):
            if os.path.isfile(item):
                tmp.append(item)
        new = (root, tmp)
        tmp = []
        answer.append(new)
    answer.append(("", ["espeak.dll"]))
    return answer

setup(
    name = "Virtual Braille n'Speak emulator",
    author = "Tyler Spivey, Sukil Etxenike",
    author_email = "sukiletxe@yahoo.es",
    version = "1.0",
    console=['emu.py'],
    data_files = get_data() + get_espeak() + [("", ["../readme.html"])],
    packages = find_packages()
    options = {
        "py2exe":{
            "optimize": 2,
            "compressed": True,
        }
    }
)