# sismapse
Sistema de Mapeamento de Projetos Sociais nas Escolas

## 🚀 Configuração do Projeto

### Instalação
```bash
cd server
pip install -r requirements.txt
```

### Migrações de Banco de Dados

Este projeto usa **Alembic** para gerenciar migrações de banco de dados. Para mais detalhes, consulte [ALEMBIC_SETUP.md](ALEMBIC_SETUP.md).

#### Comandos Rápidos:

**Criar uma migração:**
```bash
cd server
alembic revision --autogenerate -m "descrição da mudança"
```

**Aplicar migrações:**
```bash
alembic upgrade head
```

**Reverter última migração:**
```bash
alembic downgrade -1
```

**Ver status atual:**
```bash
alembic current
```

#### Script Helper:
Você também pode usar o script utilitário:
```bash
python alembic_helper.py create "minha nova migração"
python alembic_helper.py upgrade
python alembic_helper.py current
```

### Executar o Servidor
```bash
cd server
uvicorn main:app --reload
```
