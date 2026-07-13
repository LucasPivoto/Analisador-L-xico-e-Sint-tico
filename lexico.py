# pyrefly: ignore [missing-import]
import ply.lex as lex
import sys

# Lista de nomes dos tokens
tokens = [
    'T_INT', 'T_FLOAT', 'T_CHAR',                                   # Tipos de Dados
    'T_LETRA', 'T_NUM',                                             # Identificadores e Literais
    'T_ATR',                                                        # Atribuição (->)
    'T_EQ', 'T_NEQ', 'T_GEQ', 'T_LEQ', 'T_GT', 'T_LT',              # Relacionais
    'T_AND', 'T_OR', 'T_NOT',                                       # Lógicos
    'T_FALSE', 'T_TRUE',                                            # Literais Lógicos
    'T_PLUS', 'T_MINUS', 'T_MUL', 'T_DIV', 'T_MOD', 'T_EXP',        # Aritméticos
    'T_LPAREN', 'T_RPAREN',                                         # Delimitadores ( )
    'T_LBRACE', 'T_RBRACE',                                         # Delimitadores { }
    'T_LBRACKET', 'T_RBRACKET',                                     # Delimitadores [ ]
    'T_SEMICOLON', 'T_DOT', 'T_COMMA', 'T_COLON',                   # Delimitadores ; . , :
    'T_IF', 'T_ELSE', 'T_FOR', 'T_WHILE', 'T_SWITCH', 'T_CASE',     # Reservadas Controle
    'T_VOID', 'T_NULL', 'T_BREAK', 'T_RETURN',                      # Reservadas Escopo
    'T_DEFINE', 'T_INCLUDE',                                        # Diretivas
    'T_CIN', 'T_COUT',                                              # I/O
    'T_FOREVER', 'T_DATETIME', 'T_MAIN',                            # Estruturas Especiais
    'T_SWAP', 'T_DELAY', 'T_RESTART', 'T_GOTO', 'T_FATERR'          # Comandos/Controle
]


# Expressões Regulares
t_T_ATR      = r'->'
t_T_EQ       = r'='
t_T_NEQ      = r'!='    
t_T_GEQ      = r'>='
t_T_LEQ      = r'<='
t_T_GT       = r'>'
t_T_LT       = r'<'
t_T_AND      = r'&&'
t_T_OR       = r'\|\|'
t_T_NOT      = r'~'
t_T_PLUS     = r'\+'
t_T_MINUS    = r'-'     
t_T_MUL      = r'\*'
t_T_DIV      = r'/'
t_T_MOD      = r'%'
t_T_EXP      = r'\&'
t_T_DOT      = r'\.'
t_T_COMMA    = r','
t_T_COLON    = r':'
t_T_LPAREN   = r'\('
t_T_RPAREN   = r'\)'
t_T_LBRACE   = r'\{'
t_T_RBRACE   = r'\}'
t_T_LBRACKET = r'\['
t_T_RBRACKET = r'\]'
t_T_SEMICOLON= r';'

# Expressões Regulares - Palavras Reservadas e Comandos Especiais
t_T_INT      = r'\$\!'
t_T_FLOAT    = r'\$\@'
t_T_FALSE    = r'\[-\]'
t_T_TRUE     = r'\[\+\]'
t_T_IF       = r'\?\?'
t_T_ELSE     = r'!!'
t_T_FOR      = r'\#\#'
t_T_WHILE    = r'\@\@'
t_T_SWITCH   = r'\?\!'
t_T_CASE     = r'\?\@'
t_T_VOID     = r'\$\(\)'
t_T_NULL     = r'\.\.\.'
t_T_BREAK    = r';\.;'
t_T_RETURN   = r'<<<'    
t_T_DEFINE   = r'\[\]'   
t_T_INCLUDE  = r',,'
t_T_CIN      = r'<<'     
t_T_COUT     = r'>>'
t_T_FOREVER  = r'\{\*\}'
t_T_DATETIME = r'\@\@\@'
t_T_MAIN     = r'\[!\]'
t_T_SWAP     = r'<->'
t_T_DELAY    = r'-\.-'
t_T_RESTART  = r'<_<'    
t_T_GOTO     = r'~>'
t_T_FATERR   = r'!\.!\.!'



# Regras com Lógica Adicional para Tokens Específicos

# Token para caractere
def t_T_CHAR(t):
    r'\$\#|S\#'
    return t


# Token para Números
def t_T_NUM(t):
    r'[+-]?[0-9]+(\.[0-9]+)?([eE][+-]?[0-9]+)?'
    return t


# Token para Identificadores
def t_T_LETRA(t):
    r'[a-zA-Z]+'
    return t


# Ignorar Comentários
def t_T_COMMENT(t):
    r'//.*'
    pass


# Ignorar espaços e tabulações
t_ignore = ' \t'


# Quebra de Linha - Contagem de linhas e erros
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Tratamento de Erros Léxicos
def t_error(t):
    print(f"Erro Léxico: Caractere inválido '{t.value[0]}' na linha {t.lineno}")
    t.lexer.skip(1)



# Inicializa o Lexer
lexer = lex.lex()