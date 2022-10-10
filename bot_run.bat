@echo off

call %~dp0Bot_test\venv\Scripts\activate

cd %~dp0Bot_test

cd %CD%

set TOKEN=5607198410:AAF_NQnCDSOlVG-A2G-2yPpMg-DKvEVTwWM

python main.py

pause