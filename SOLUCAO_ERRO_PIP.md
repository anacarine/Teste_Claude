# Solução para Erro Errno 117 do pip

## Problema

Erro ao instalar bibliotecas Python:
```
ERROR: Could not install packages due to an OSError: [Errno 117] A estrutura necessita de limpeza
```

## Causa

O erro Errno 117 (EUCLEAN - "Structure needs cleaning") ocorre quando há corrupção em arquivos temporários do pip, geralmente em `/tmp/pip-*`.

## Solução Aplicada

1. **Limpeza do cache do pip** - Removidos 82 arquivos corrompidos
2. **Limpeza de diretórios temporários** - Removidos todos os diretórios `/tmp/pip-*`
3. **Atualização do pip** - Tentativa de atualizar para a versão mais recente

## Como Instalar Bibliotecas Agora

### Opção 1: Script Automático (Recomendada) ⭐
```bash
chmod +x install_with_fix.sh
./install_with_fix.sh netCDF4
```

Este script configura automaticamente todas as variáveis de ambiente e usa um diretório temporário fora de `/tmp`.

### Opção 2: Comandos Manuais (Solução Completa)
```bash
# 1. Criar e configurar diretório temporário
mkdir -p ~/pip_temp
export TMPDIR=~/pip_temp
export TEMP=~/pip_temp
export TMP=~/pip_temp
export PIP_BUILD=~/pip_temp/pip-build
export PIP_CACHE_DIR=~/pip_temp/pip-cache
mkdir -p "$PIP_BUILD" "$PIP_CACHE_DIR"

# 2. Limpar arquivos corrompidos
rm -rf /tmp/pip-*
pip cache purge

# 3. Instalar o pacote
pip install --no-cache-dir \
    --build "$PIP_BUILD" \
    --cache-dir "$PIP_CACHE_DIR" \
    netCDF4

# 4. Limpar após instalação
rm -rf ~/pip_temp
```

### Opção 3: Sem cache (Mais simples, pode não funcionar)
```bash
pip3 install --no-cache-dir nome-da-biblioteca
```

## Scripts Disponíveis

### `install_with_fix.sh` - Instalação com correções completas
```bash
./install_with_fix.sh nome-da-biblioteca
```

### `fix_pip_error.sh` - Apenas limpeza e correção
```bash
./fix_pip_error.sh
```

## Causa Raiz do Problema

O erro Errno 117 indica que há **corrupção no sistema de arquivos `/tmp`**. Possíveis causas:

1. Falha de energia durante escrita de arquivos
2. Problemas de hardware no disco
3. Sistema de arquivos não foi desmontado corretamente
4. Espaço em disco insuficiente em `/tmp`

## Prevenção Futura

Se o erro ocorrer novamente:

1. **Use sempre o script de instalação**: `./install_with_fix.sh nome-da-biblioteca`
2. **Verifique espaço em disco**: `df -h /tmp`
3. **Verifique integridade do sistema de arquivos** (requer root):
   ```bash
   # Verificar qual partição contém /tmp
   df /tmp

   # Verificar e reparar (exemplo com /dev/sda1, ajuste conforme necessário)
   sudo fsck -f /dev/sda1
   ```
4. **Configuração permanente**: Adicione ao `~/.bashrc` para usar sempre diretório alternativo:
   ```bash
   export TMPDIR=~/pip_temp
   mkdir -p $TMPDIR
   ```

## Solução para Ambientes Específicos

### Se estiver usando conda/anaconda:
```bash
# Desativa o ambiente conda
conda deactivate

# Instala com o script
./install_with_fix.sh netCDF4

# Reativa o ambiente
conda activate seu-ambiente
```
