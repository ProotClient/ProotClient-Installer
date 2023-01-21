@echo off
title Compiling ProotClient Installer...

Rem Failsafe if PyInstaller is not installed yet.
pip install pyinstaller

pyinstaller --clean -y -n "ProotClient-Installer" --onefile --icon "installer_icon.png" main.pyw

cls
color 0A
echo Compiling Complete.
echo.
echo The .exe file is found in the "dist" folder.
echo.
echo.
echo.
pause