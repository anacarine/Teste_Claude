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

### Opção 1: Sem cache (Recomendada)
```bash
pip3 install --no-cache-dir nome-da-biblioteca
```

Esta opção evita usar o cache do pip, prevenindo o erro.

### Opção 2: Diretório temporário alternativo
```bash
# Criar diretório temporário no home
mkdir -p ~/tmp

# Instalar usando o novo diretório
TMPDIR=~/tmp pip3 install nome-da-biblioteca
```

### Opção 3: Instalação normal
```bash
pip3 install nome-da-biblioteca
```

Após as limpezas, a instalação normal pode funcionar.

## Script Automatizado

Um script `fix_pip_error.sh` foi criado para aplicar todas as correções automaticamente:

```bash
./fix_pip_error.sh
```

## Prevenção Futura

Se o erro ocorrer novamente:

1. Execute o script de correção: `./fix_pip_error.sh`
2. Use sempre `--no-cache-dir` ao instalar: `pip3 install --no-cache-dir <biblioteca>`
3. Se o problema persistir, pode indicar problemas no sistema de arquivos - execute `fsck` na partição afetada
