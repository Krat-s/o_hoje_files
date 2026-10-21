@echo off
chcp 65001 >nul
set PYTHONIOENCODING=utf-8
title Word Converter
rem Usa a pasta onde este .bat esta (o word_converter.py deve estar junto)
cd /d "%~dp0"

if not exist "word_converter.py" (
    echo.
    echo [ERRO] word_converter.py nao encontrado nesta pasta:
    echo %~dp0
    echo Coloque o .bat e o word_converter.py juntos na mesma pasta.
    echo.
    pause
    exit /b 1
)

rem --- Localiza o Python (prefere o launcher "py") ---
set "PY="
where py >nul 2>nul && set "PY=py -3"
if not defined PY (
    where python >nul 2>nul && set "PY=python"
)
if not defined PY (
    echo.
    echo [ERRO] Python nao encontrado.
    echo Instale em https://www.python.org/downloads/
    echo IMPORTANTE: marque a opcao "Add python.exe to PATH" no instalador.
    echo.
    pause
    exit /b 1
)

rem --- Primeira execucao: cria ambiente isolado e instala dependencias ---
if not exist ".venv\Scripts\python.exe" (
    echo Preparando o ambiente pela primeira vez, aguarde...
    %PY% -m venv .venv
    if errorlevel 1 (
        echo [ERRO] Nao foi possivel criar o ambiente Python.
        pause
        exit /b 1
    )
    ".venv\Scripts\python.exe" -m pip install --quiet --disable-pip-version-check watchdog
    if errorlevel 1 (
        echo [ERRO] Falha ao instalar dependencias. Verifique a conexao com a internet.
        rmdir /s /q ".venv"
        pause
        exit /b 1
    )
    echo Ambiente pronto.
    echo.
)

rem --- Se o script estiver configurado com MOTOR = "word", garante o pywin32 ---
findstr /r /c:"^MOTOR = .word" "word_converter.py" >nul 2>nul
if not errorlevel 1 (
    ".venv\Scripts\python.exe" -c "import win32com.client" >nul 2>nul
    if errorlevel 1 (
        echo Instalando suporte ao Word, aguarde...
        ".venv\Scripts\python.exe" -m pip install --quiet --disable-pip-version-check pywin32
        if errorlevel 1 (
            echo [ERRO] Falha ao instalar o pywin32. Verifique a conexao com a internet.
            pause
            exit /b 1
        )
    )
)

rem --- Executa o conversor ---
".venv\Scripts\python.exe" word_converter.py

echo.
echo O conversor foi encerrado.
pause
