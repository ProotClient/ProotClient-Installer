@echo off
title ProotClient Installer Compiler
color 06
echo Please confirm that you want to start compiling.
echo.
echo.
echo.
pause
cls

color 07
title Compiling ProotClient Installer...
pip install requests
pip install pyinstaller
pyinstaller --clean -y -n "ProotClient-Installer" --onefile --icon "installer_icon.png" main.pyw
del ProotClient-Installer.spec

cls
title ProotClient Installer Compiler
color 0A
echo Compiling Complete.
echo.
echo The .exe file is found in the "dist" folder.
echo.
echo.
echo.
pause
