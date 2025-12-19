#!/bin/bash

# Script para instalar pacotes Python evitando o erro Errno 117
# Uso: ./install_with_fix.sh nome-do-pacote

if [ -z "$1" ]; then
    echo "Uso: ./install_with_fix.sh nome-do-pacote"
    echo "Exemplo: ./install_with_fix.sh netCDF4"
    exit 1
fi

PACKAGE_NAME="$1"

echo "=== Instalando $PACKAGE_NAME com correções para Errno 117 ==="
echo ""

# Criar diretório temporário alternativo
echo "1. Criando diretório temporário alternativo..."
CUSTOM_TMP="$HOME/pip_temp"
mkdir -p "$CUSTOM_TMP"
chmod 777 "$CUSTOM_TMP"
echo "✓ Diretório $CUSTOM_TMP criado"
echo ""

# Limpar arquivos temporários antigos do pip
echo "2. Limpando arquivos temporários corrompidos em /tmp..."
sudo rm -rf /tmp/pip-* 2>/dev/null || rm -rf /tmp/pip-* 2>/dev/null
echo "✓ Arquivos temporários limpos"
echo ""

# Limpar cache do pip novamente
echo "3. Limpando cache do pip..."
pip cache purge
echo "✓ Cache limpo"
echo ""

# Configurar variáveis de ambiente
echo "4. Configurando variáveis de ambiente..."
export TMPDIR="$CUSTOM_TMP"
export TEMP="$CUSTOM_TMP"
export TMP="$CUSTOM_TMP"
export PIP_BUILD="$CUSTOM_TMP/pip-build"
export PIP_CACHE_DIR="$CUSTOM_TMP/pip-cache"

mkdir -p "$PIP_BUILD" "$PIP_CACHE_DIR"
echo "✓ Variáveis configuradas:"
echo "  TMPDIR=$TMPDIR"
echo "  PIP_BUILD=$PIP_BUILD"
echo "  PIP_CACHE_DIR=$PIP_CACHE_DIR"
echo ""

# Instalar o pacote
echo "5. Instalando $PACKAGE_NAME..."
echo ""
pip install --no-cache-dir \
    --build "$PIP_BUILD" \
    --cache-dir "$PIP_CACHE_DIR" \
    "$PACKAGE_NAME"

EXIT_CODE=$?

echo ""
if [ $EXIT_CODE -eq 0 ]; then
    echo "✓ $PACKAGE_NAME instalado com sucesso!"
    echo ""
    echo "Limpando diretórios temporários..."
    rm -rf "$CUSTOM_TMP"
    echo "✓ Limpeza concluída"
else
    echo "✗ Erro ao instalar $PACKAGE_NAME (código de saída: $EXIT_CODE)"
    echo ""
    echo "Se o erro persistir, pode haver corrupção no sistema de arquivos."
    echo "Execute como root: fsck -f /dev/sda1 (ajuste o dispositivo conforme necessário)"
fi

exit $EXIT_CODE
