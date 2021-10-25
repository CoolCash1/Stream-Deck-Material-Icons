@ECHO OFF

echo PYTHON AND FFMPEG ARE REQUIRED TO BUILD THE ICONPACK. Please download and install these before continuing
pause

cd /D "%~dp0"

echo Creating Virtural Enviroment...
python -m venv .

echo Downloading Required Packages...

python -m pip install -r builder/requirements.txt

echo Bulding...

python builder/build.py