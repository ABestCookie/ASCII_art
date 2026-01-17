@echo off
chcp 65001
REM 編譯 C++ 文件
C:\mingw64\bin\g++ -O2 -std=c++17 player.cpp -o player.exe

if %ERRORLEVEL% NEQ 0 (
    echo 編譯失敗！
    pause
    exit /b 1
)

echo 編譯成功！
pause
