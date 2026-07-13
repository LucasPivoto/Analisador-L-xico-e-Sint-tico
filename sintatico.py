# pyrefly: ignore [missing-import]
import ply.yacc as yacc
from lexico import tokens

# Sequência de Elementos do Programa
def p_programa(p):
    '''programa : lista_elementos'''
    p[0] = p[1]

def p_lista_elementos(p):
    '''lista_elementos : elemento
                       | lista_elementos elemento'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_elemento(p):
    '''elemento : estrutura_main
                | funcao
                | comando'''
    p[0] = p[1]

# Lista de Comandos
def p_lista_comandos(p):
    '''lista_comandos : comando
                      | lista_comandos comando'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

# Comandos Válidos 
def p_comando(p):
    '''comando : declaracao
               | atribuicao
               | comando_if
               | comando_while
               | comando_for
               | comando_switch
               | comando_cin
               | comando_cout
               | comando_chamar_funcao
               | comando_define
               | comando_include
               | comando_swap
               | comando_delay
               | comando_restart
               | comando_jump
               | comando_faterr
               | comando_break'''
    p[0] = p[1]

# Tipos de Dados
def p_tipo(p):
    '''tipo : T_INT
            | T_FLOAT
            | T_CHAR
            | T_VOID'''
    p[0] = p[1]

# Valores de Veracidade (Literais Lógicos)
def p_veracidade(p):
    '''veracidade : T_TRUE
                  | T_FALSE'''
    p[0] = p[1]

# Caracteres (Identificadores, Números, Horário)
def p_caracteres(p):
    '''caracteres : T_NUM
                  | T_LETRA
                  | T_DATETIME'''
    p[0] = p[1]

# Declaração de Variáveis
def p_declaracao(p):
    '''declaracao : tipo T_LETRA T_SEMICOLON
                  | tipo T_LETRA T_ATR expressao_saida T_SEMICOLON'''
    if len(p) == 4:
        p[0] = ('declaracao_pura', p[1], p[2])
    else:
        p[0] = ('declaracao_inicializada', p[1], p[2], p[4])

# Atribuição
def p_atribuicao(p):
    '''atribuicao : T_LETRA T_ATR termo_aritmetico T_SEMICOLON
                  | T_LETRA T_ATR op_aritmetica T_SEMICOLON'''
    p[0] = ('atribuicao', p[1], p[3])

# Expressões Aritméticas e Termos
def p_aritmetico(p):
    '''aritmetico : T_PLUS
                  | T_MINUS
                  | T_MUL
                  | T_DIV
                  | T_MOD
                  | T_EXP'''
    p[0] = p[1]

def p_termo_aritmetico(p):
    '''termo_aritmetico : caracteres
                        | chamar_funcao'''
    p[0] = p[1]

def p_op_aritmetica(p):
    '''op_aritmetica : termo_aritmetico aritmetico termo_aritmetico
                     | op_aritmetica aritmetico termo_aritmetico'''
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3])
    else:
        p[0] = (p[2], p[1], p[3])

# Estrutura de Retorno Opcional
def p_retorno(p):
    '''retorno : caracteres
               | veracidade'''
    p[0] = p[1]

def p_retorno_opt(p):
    '''retorno_opt : T_RETURN retorno T_SEMICOLON
                   | T_RETURN retorno
                   | empty'''
    if len(p) == 4:
        p[0] = p[2]
    elif len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = None

# Main
def p_estrutura_main(p):
    '''estrutura_main : T_MAIN T_LBRACE lista_comandos retorno_opt T_RBRACE'''
    p[0] = ('main', p[3], p[4])

# Funções e Parâmetros
def p_parametro(p):
    '''parametro : tipo T_LETRA'''
    p[0] = (p[1], p[2])

def p_lista_parametros(p):
    '''lista_parametros : parametro
                        | lista_parametros T_COMMA parametro'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_lista_parametros_opt(p):
    '''lista_parametros_opt : lista_parametros
                            | empty'''
    p[0] = p[1] if p[1] is not None else []

def p_funcao(p):
    '''funcao : tipo T_LETRA T_LPAREN lista_parametros_opt T_RPAREN T_LBRACE lista_comandos retorno_opt T_RBRACE'''
    p[0] = ('funcao', p[1], p[2], p[4], p[7], p[8])

# Chamada de Função
def p_lista_argumentos(p):
    '''lista_argumentos : caracteres
                        | veracidade
                        | lista_argumentos T_COMMA caracteres
                        | lista_argumentos T_COMMA veracidade'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_lista_argumentos_opt(p):
    '''lista_argumentos_opt : lista_argumentos
                            | empty'''
    p[0] = p[1] if p[1] is not None else []

def p_chamar_funcao(p):
    '''chamar_funcao : T_LETRA T_LPAREN lista_argumentos_opt T_RPAREN'''
    p[0] = ('chamar_funcao', p[1], p[3])

def p_comando_chamar_funcao(p):
    '''comando_chamar_funcao : chamar_funcao T_SEMICOLON'''
    p[0] = p[1]

# Condições Lógicas e Relacionais
def p_relacional(p):
    '''relacional : T_EQ
                  | T_NEQ
                  | T_GEQ
                  | T_LEQ
                  | T_GT
                  | T_LT'''
    p[0] = p[1]

def p_termo_relacional(p):
    '''termo_relacional : caracteres
                        | veracidade'''
    p[0] = p[1]

def p_op_relacional(p):
    '''op_relacional : termo_relacional relacional termo_relacional
                     | op_relacional relacional termo_relacional'''
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3])
    else:
        p[0] = (p[2], p[1], p[3])

def p_logico(p):
    '''logico : T_AND
              | T_OR'''
    p[0] = p[1]

def p_condicao(p):
    '''condicao : op_relacional
                | T_NOT condicao
                | op_relacional logico condicao
                | T_LPAREN condicao T_RPAREN'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = ('not', p[2])
    elif len(p) == 4:
        if p[1] == '(':
            p[0] = p[2]
        else:
            p[0] = (p[2], p[1], p[3])

# Comando Condicional (If/Else)
def p_comando_if(p):
    '''comando_if : T_IF T_LPAREN condicao T_RPAREN T_LBRACE lista_comandos T_RBRACE
                  | T_IF T_LPAREN condicao T_RPAREN T_LBRACE lista_comandos T_RBRACE T_ELSE T_LBRACE lista_comandos T_RBRACE'''
    if len(p) == 8:
        p[0] = ('if', p[3], p[6])
    else:
        p[0] = ('if_else', p[3], p[6], p[10])

# Repetição (While / Forever)
def p_comando_while(p):
    '''comando_while : T_WHILE T_LPAREN condicao T_RPAREN T_LBRACE lista_comandos T_RBRACE
                     | T_FOREVER T_LBRACE lista_comandos T_RBRACE'''
    if len(p) == 8:
        p[0] = ('while', p[3], p[6])
    else:
        p[0] = ('forever', p[3])

# Repetição (For)
def p_atribuicao_for(p):
    '''atribuicao_for : T_LETRA T_ATR termo_aritmetico
                      | T_LETRA T_ATR op_aritmetica'''
    p[0] = ('atribuicao', p[1], p[3])

def p_comando_for(p):
    '''comando_for : T_FOR T_LPAREN atribuicao_for T_SEMICOLON condicao T_SEMICOLON op_aritmetica T_RPAREN T_LBRACE lista_comandos T_RBRACE
                   | T_FOR T_LPAREN atribuicao_for T_SEMICOLON condicao T_SEMICOLON termo_aritmetico T_RPAREN T_LBRACE lista_comandos T_RBRACE'''
    p[0] = ('for', p[3], p[5], p[7], p[10])

# Switch / Case
def p_caso(p):
    '''caso : T_CASE caracteres T_COLON lista_comandos T_BREAK T_SEMICOLON
            | T_CASE caracteres T_COLON lista_comandos T_BREAK'''
    p[0] = ('caso', p[2], p[4])

def p_lista_casos(p):
    '''lista_casos : caso
                   | lista_casos caso'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_comando_switch(p):
    '''comando_switch : T_SWITCH T_LPAREN T_LETRA T_RPAREN T_LBRACE lista_casos T_RBRACE'''
    p[0] = ('switch', p[3], p[6])

# Entrada e Saída
def p_comando_cin(p):
    '''comando_cin : T_CIN T_LETRA T_SEMICOLON
                   | T_CIN T_LPAREN T_LETRA T_RPAREN T_SEMICOLON'''
    if len(p) == 4:
        p[0] = ('cin', p[2])
    else:
        p[0] = ('cin', p[3])

def p_expressao_saida(p):
    '''expressao_saida : termo_aritmetico
                       | op_aritmetica
                       | veracidade'''
    p[0] = p[1]

def p_comando_cout(p):
    '''comando_cout : T_COUT expressao_saida T_SEMICOLON
                    | T_COUT T_LPAREN expressao_saida T_RPAREN T_SEMICOLON'''
    if len(p) == 4:
        p[0] = ('cout', p[2])
    else:
        p[0] = ('cout', p[3])

# Comandos Especiais
def p_comando_define(p):
    '''comando_define : T_DEFINE T_LETRA caracteres
                      | T_DEFINE T_LETRA caracteres T_SEMICOLON'''
    p[0] = ('define', p[2], p[3])

def p_comando_include(p):
    '''comando_include : T_INCLUDE caracteres
                       | T_INCLUDE caracteres T_SEMICOLON'''
    p[0] = ('include', p[2])

def p_comando_swap(p):
    '''comando_swap : T_LETRA T_SWAP T_LETRA T_SEMICOLON
                    | T_LETRA T_SWAP T_LETRA'''
    p[0] = ('swap', p[1], p[3])

def p_comando_delay(p):
    '''comando_delay : T_DELAY T_LPAREN T_NUM T_RPAREN T_SEMICOLON
                     | T_DELAY T_LPAREN T_NUM T_RPAREN'''
    p[0] = ('delay', p[3])

def p_comando_restart(p):
    '''comando_restart : T_RESTART T_SEMICOLON
                       | T_RESTART'''
    p[0] = ('restart',)

def p_comando_jump(p):
    '''comando_jump : T_GOTO T_NUM T_SEMICOLON
                    | T_GOTO T_NUM'''
    p[0] = ('goto', p[2])

def p_comando_faterr(p):
    '''comando_faterr : T_FATERR T_SEMICOLON
                      | T_FATERR'''
    p[0] = ('fatal_error',)

def p_comando_break(p):
    '''comando_break : T_BREAK T_SEMICOLON
                     | T_BREAK'''
    p[0] = ('break',)

def p_empty(p):
    '''empty :'''
    pass

# Tratamento de Erros Sintáticos
def p_error(p):
    if p:
        print(f"Erro Sintático: Token inesperado '{p.value}' na linha {p.lineno}")
    else:
        print("Erro Sintático: Fim de arquivo inesperado (EOF)")

parser = yacc.yacc()