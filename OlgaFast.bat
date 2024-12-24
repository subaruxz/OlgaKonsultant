@echo off
cd C:\OlgaV
start python app.py
timeout /t 5 /nobreak >nul
start http://127.0.0.1:5000 