@echo off
REM ============================================================
REM  Provar la campanya ACA-UGT en local
REM  Aixeca un servidor HTTP a http://localhost:8000
REM  per provar la pagina IGUAL que estara desplegada,
REM  evitant les restriccions de Chrome amb file://
REM ============================================================
echo.
echo  Aixecant servidor local a http://localhost:8000
echo.
echo  Obre el navegador a:
echo      http://localhost:8000/index.html?preview=1
echo.
echo  Per aturar el servidor: tanca aquesta finestra o prem Ctrl+C
echo.

REM Python 3 first (standard install)
where python >nul 2>nul
if %errorlevel%==0 (
    python -m http.server 8000
    goto :eof
)

REM Python via py launcher (Windows)
where py >nul 2>nul
if %errorlevel%==0 (
    py -3 -m http.server 8000
    goto :eof
)

echo.
echo [!] No es pot trobar Python al sistema.
echo     Instal-la a https://www.python.org/downloads/
echo     o puja la carpeta directament a Netlify Drop:
echo     https://app.netlify.com/drop
echo.
pause
