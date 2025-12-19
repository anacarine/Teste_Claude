#!/bin/bash

echo "=== Solucionando Erro Errno 117 do pip ==="
echo ""

# Solução 1: Limpar cache do pip
echo "1. Limpando cache do pip..."
pip3 cache purge
echo "✓ Cache do pip limpo"
echo ""

# Solução 2: Limpar arquivos temporários antigos do pip
echo "2. Limpando diretórios temporários do pip..."
rm -rf /tmp/pip-*
echo "✓ Diretórios temporários limpos"
echo ""

# Solução 3: Atualizar pip
echo "3. Atualizando pip para a versão mais recente..."
pip3 install --upgrade pip
echo "✓ pip atualizado"
echo ""

echo "=== Soluções aplicadas com sucesso! ==="
echo ""
echo "Agora você pode tentar instalar sua biblioteca de 3 formas:"
echo ""
echo "OPÇÃO 1 (Recomendada): Instalar sem usar cache"
echo "  pip3 install --no-cache-dir <nome-da-biblioteca>"
echo ""
echo "OPÇÃO 2: Instalar usando diretório temporário alternativo"
echo "  TMPDIR=~/tmp pip3 install <nome-da-biblioteca>"
echo ""
echo "OPÇÃO 3: Instalar normalmente (após as limpezas)"
echo "  pip3 install <nome-da-biblioteca>"
echo ""
