#!/bin/bash
# ============================================================
#  Provar la campanya ACA-UGT en local
#  Aixeca un servidor HTTP a http://localhost:8000
#  per provar la pàgina IGUAL que estarà desplegada,
#  evitant les restriccions de Chrome amb file://
# ============================================================
cd "$(dirname "$0")"

echo ""
echo "  Aixecant servidor local a http://localhost:8000"
echo ""
echo "  Obre el navegador a:"
echo "      http://localhost:8000/index.html?preview=1"
echo ""
echo "  Per aturar el servidor: prem Ctrl+C"
echo ""

if command -v python3 >/dev/null 2>&1; then
    python3 -m http.server 8000
elif command -v python >/dev/null 2>&1; then
    python -m http.server 8000
else
    echo ""
    echo "[!] Python no està instal·lat."
    echo "    Instal·la-ho o puja la carpeta a Netlify Drop:"
    echo "    https://app.netlify.com/drop"
    echo ""
    read -p "Prem una tecla per sortir... " -n1 -s
fi
