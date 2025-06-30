# 📚 Sistema de Notas

Um sistema simples e intuitivo para gerenciamento de notas de alunos, desenvolvido em Python com interface gráfica Tkinter e banco de dados SQLite.

## 🚀 Funcionalidades

- ✅ **Adicionar Notas**: Cadastre notas de alunos por disciplina
- 📝 **Atualizar Notas**: Modifique notas existentes facilmente
- 🗑️ **Deletar Registros**: Remova registros com confirmação de segurança
- 👀 **Visualizar Dados**: Interface em tabela organizada e responsiva
- 🔍 **Seleção Intuitiva**: Clique nos registros para editar automaticamente
- 💾 **Persistência**: Dados salvos em banco SQLite local

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Tkinter** - Interface gráfica nativa
- **SQLite3** - Banco de dados local
- **ttk** - Widgets modernos do Tkinter

## 📋 Pré-requisitos

- Python 3.6 ou superior
- Tkinter (já incluído na maioria das instalações Python)

## 🔧 Instalação e Execução

1. **Clone ou baixe o projeto**:

   ```bash
   git clone <url-do-repositorio>
   cd sistema_permissoes
   ```

2. **Execute a aplicação**:

   ```bash
   python app.py
   ```

3. **Primeira execução**:

   - O banco de dados `notas.db` será criado automaticamente
   - A tabela `notas` será inicializada

## 💻 Como Usar

### Adicionando uma Nova Nota

1. Preencha os campos:

   - **Nome do Aluno**: Nome completo do estudante
   - **Disciplina**: Matéria ou disciplina
   - **Nota**: Valor numérico entre 0 e 10

2. Clique em **"Adicionar Nota"**
3. A nota aparecerá na tabela automaticamente

### Atualizando uma Nota

1. Clique no registro desejado na tabela
2. Os campos serão preenchidos automaticamente
3. Modifique apenas o campo **"Nota"**
4. Clique em **"Atualizar Nota"**

### Deletando um Registro

1. Selecione o registro na tabela
2. Clique em **"Deletar Nota"**
3. Confirme a exclusão na caixa de diálogo

### Limpando os Campos

- Use o botão **"Limpar Campos"** para resetar o formulário

## 🗂️ Estrutura do Banco de Dados

```sql
CREATE TABLE notas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    disciplina TEXT NOT NULL,
    nota REAL NOT NULL
);
```

## 📁 Estrutura do Projeto

```text
sistema_permissoes/
├── app.py              # Aplicação principal
├── README.md           # Este arquivo
└── notas.db           # Banco de dados (criado automaticamente)
```

## 🎨 Interface

A aplicação possui uma interface moderna com:

- **Formulário de entrada** organizado em seções
- **Botões estilizados** com cores e hover effects
- **Tabela responsiva** com scrollbar automática
- **Validação de dados** em tempo real
- **Mensagens informativas** para feedback do usuário

## ⚙️ Funcionalidades Técnicas

### Validações Implementadas

- ✅ Campos obrigatórios (nome e disciplina)
- ✅ Validação numérica de notas
- ✅ Intervalo válido de notas (0-10)
- ✅ Confirmação antes de deletar

### Tratamento de Erros

- 🛡️ Conexões seguras com o banco
- 🛡️ Tratamento de exceções SQLite
- 🛡️ Mensagens de erro amigáveis
- 🛡️ Rollback automático em falhas

## 🐛 Resolução de Problemas

### Erro: "No module named 'tkinter'"

```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# CentOS/RHEL
sudo yum install tkinter
```

### Erro de Permissão no Banco

- Verifique se o diretório tem permissão de escrita
- Execute como administrador se necessário

### Interface não Aparece

- Verifique se há um servidor X rodando (Linux)
- Certifique-se de que não está executando via SSH sem X11

## 📈 Possíveis Melhorias Futuras

- 🔐 Sistema de autenticação de usuários
- 📊 Relatórios e estatísticas
- 📤 Exportação para CSV/Excel
- 🔍 Sistema de busca e filtros
- 🎯 Cálculo automático de médias
- 🌐 Interface web com Flask/Django
- 📱 Versão mobile responsiva

## 👨‍💻 Desenvolvimento

### Executando em Modo Debug

```python
# Adicione no final do app.py para logs detalhados
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Estrutura do Código

- **Seção 1**: Configurações do banco de dados
- **Seção 2**: Funções CRUD (backend)
- **Seção 3**: Interface gráfica (frontend)
- **Seção 4**: Execução principal

## 📄 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer um fork do projeto
2. Criar uma branch para sua feature
3. Fazer commit das mudanças
4. Abrir um Pull Request

## 📞 Suporte

Para dúvidas, sugestões ou problemas:

- Abra uma issue no repositório
- Entre em contato através do email

---

Desenvolvido com ❤️ em Python

Sistema de Notas v1.0 - Gerenciamento acadêmico simplificado
