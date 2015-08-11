pushd ..\src
python setup.py py2exe
rd /s /q build
ren dist vbns-espeak
7z a vbns-espeak-v1.0.zip vbns-espeak\ -r -tzip
rd /s /q vbns-espeak
popd
