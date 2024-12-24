@echo off
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python не найден. Загружаем и устанавливаем Python...
    
    :: Скачиваем Python (укажите путь к установщику)
    set "PYTHON_INSTALLER=https://www.python.org/ftp/python/3.9.7/python-3.9.7.exe"
    
    :: Загружаем установщик
    powershell -Command "(New-Object System.Net.WebClient).DownloadFile('%PYTHON_INSTALLER%', 'python_installer.exe')"
    
    :: Запускаем установку Python
    start /wait python_installer.exe /quiet InstallAllUsers=1 PrependPath=1
    
    :: Удаляем установочный файл
    del python_installer.exe
    
    echo Python установлен. Пожалуйста, перезапустите батник.
    pause
    exit /b
)
cd C:\OlgaV
python -m pip install --upgrade pip
pip install -r requirements.txt
start python app.py
timeout /t 5 /nobreak >nul
start http://127.0.0.1:5000 