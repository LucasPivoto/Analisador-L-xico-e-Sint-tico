# 📡 Linguagem Sinalês — Analisador Léxico e Sintático

Este repositório contém a implementação completa do **Analisador Léxico** e do **Analisador Sintático** para a linguagem **Sinalês**, desenvolvida como projeto prático para a disciplina **ECOM06A - Compiladores** do curso de Engenharia de Computação da Universidade Federal de Itajubá (UNIFEI).

A característica central da linguagem Sinalês é a proposta de mimetizar visualmente o fluxo de dados e sinais eletrônicos. Para isso, ela restringe o uso de caracteres alfanuméricos exclusivamente para a nomeação de identificadores (variáveis) e constantes numéricas, substituindo todos os comandos tradicionais e estruturas de controle por uma interface puramente simbólica.

---

## 🛠️ Tecnologias e Ferramentas

O projeto foi construído utilizando as seguintes tecnologias:
* **Linguagem Base:** Python 3
* **Ferramenta de Parsing:** PLY (Python Lex-Yacc), responsável pela tokenização (Lex) e análise gramatical baseada no algoritmo LALR (Yacc).
* **Ambiente Alvo:** Desenvolvido e validado para execução no ecossistema Windows.

---

## 📋 Mapeamento de Sinais Principais

A tabela abaixo ilustra como algumas das estruturas de controle tradicionais foram convertidas para a sintaxe puramente simbólica do Sinalês:

| Estrutura / Comando | Símbolo Adotado | Nome do Token |
| :--- | :---: | :--- |
| Condicional (If / Else) | `??`  /  `!!` | `T_IF`  /  `T_ELSE` |
| Laço de Repetição (While) | `@@` | `T_WHILE` |
| Laço Contado (For) | `##` | `T_FOR` |
| Seleção Múltipla (Switch) | `?!` | `T_SWITCH` |
| Operador de Atribuição | `->` | `T_ATR` |
| Pausa na Execução (Delay) | `-.-` | `T_DELAY` |
| Interrupção Crítica (Fatal Error) | `!.!.!` | `T_FATERR` |
| Desvio de Fluxo (Jump/GoTo) | `~>` | `T_GOTO` |
| Permutação de Valores (Swap) | `<->` | `T_SWAP` |

---

## 🚀 Como Executar o Projeto (Windows)

### 1. Pré-requisitos
Certifique-se de ter o Python 3 instalado em sua máquina. Além disso, é necessário instalar a biblioteca PLY. Abra o seu Prompt de Comando (`cmd`) ou PowerShell e execute:
```bash
pip install ply
