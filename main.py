import sys
from lexico import lexer
from sintatico import parser

# Mapeamento dos tokens
DICIONARIO_TOKENS = {
    'T_INT': 'tipo inteiro',
    'T_FLOAT': 'tipo real (float)',
    'T_CHAR': 'tipo caractere',
    'T_LETRA': 'identificador',
    'T_NUM': 'número/literal numérico',
    'T_ATR': 'atribuição (->)',
    'T_EQ': 'operador relacional de igualdade (=)',
    'T_NEQ': 'operador relacional de diferença (!=)',
    'T_GEQ': 'operador relacional maior ou igual (>=)',
    'T_LEQ': 'operador relacional menor ou igual (<=)',
    'T_GT': 'operador relacional maior (>)',
    'T_LT': 'operador relacional menor (<)',
    'T_AND': 'operador lógico e (&&)',
    'T_OR': 'operador lógico ou (||)',
    'T_NOT': 'operador lógico não (~)',
    'T_FALSE': 'literal lógico falso ([-])',
    'T_TRUE': 'literal lógico verdadeiro ([+])',
    'T_PLUS': 'operador aritmético de soma (+)',
    'T_MINUS': 'operador aritmético de subtração (-)',
    'T_MUL': 'operador aritmético de multiplicação (*)',
    'T_DIV': 'operador aritmético de divisão (/)',
    'T_MOD': 'operador aritmético de módulo (%)',
    'T_EXP': 'operador aritmético de exponenciação (&)',
    'T_SEMICOLON': 'terminador ponto e vírgula (;)',
    'T_DOT': 'delimitador ponto (.)',
    'T_COMMA': 'delimitador vírgula (,)',
    'T_COLON': 'delimitador dois pontos (:)',
    'T_LPAREN': 'abre parênteses (()',
    'T_RPAREN': 'fecha parênteses ())',
    'T_LBRACE': 'abre chaves ({)',
    'T_RBRACE': 'fecha chaves (})',
    'T_LBRACKET': 'abre colchetes ([)',
    'T_RBRACKET': 'fecha colchetes (])',
    'T_IF': 'comando condicional (if: ??)',
    'T_ELSE': 'comando condicional (else: !!)',
    'T_FOR': 'comando de repetição (for: ##)',
    'T_WHILE': 'comando de repetição (while: @@)',
    'T_SWITCH': 'comando de seleção múltipla (switch: ?!)',
    'T_CASE': 'caso de seleção (case: ?@)',
    'T_VOID': 'tipo de retorno vazio (void: $())',
    'T_NULL': 'literal nulo (null: ...)',
    'T_BREAK': 'interrupção de loop (break: ;.; ou ;:;)',
    'T_RETURN': 'retorno de função (return: <<<)',
    'T_DEFINE': 'diretiva de pré-processamento (define: [])',
    'T_INCLUDE': 'diretiva de importação (include: ,,)',
    'T_CIN': 'leitura de dados (cin: <<)',
    'T_COUT': 'exibição de dados (cout: >>)',
    'T_FOREVER': 'loop infinito (forever: {*})',
    'T_DATETIME': 'obtenção de data/hora (getDateTime: @@@)',
    'T_MAIN': 'ponto de entrada do programa (main: [!])',
    'T_SWAP': 'comando de troca (swap: <->)',
    'T_DELAY': 'comando de atraso (delay: -.-)',
    'T_RESTART': 'comando de reinício (restart: <_<)',
    'T_GOTO': 'comando de desvio (goto: ~>)',
    'T_FATERR': 'erro fatal (fatal error: !.!.!)'
}

def compilar_sinales(caminho_arquivo_fonte):
    try:
        # Leitura do código
        with open(caminho_arquivo_fonte, 'r', encoding='utf-8') as arquivo:
            codigo_fonte = arquivo.read()
        
        print(f"--- Iniciando Análise do Arquivo: {caminho_arquivo_fonte} ---")
        
        # Executa a Análise Léxica e gera o arquivo de reconhecimento de tokens
        lexer.input(codigo_fonte)
        tokens_reconhecidos = []
        
        # Clona o lexer para consumir os tokens sem afetar o parser
        while True:
            tok = lexer.token()
            if not tok:
                break
            descricao = DICIONARIO_TOKENS.get(tok.type, tok.type)
            tokens_reconhecidos.append(f"{tok.value} -> {descricao}")
        
        # Grava os tokens no arquivo de saída
        caminho_saida_tokens = "reconhecimento_tokens.txt"
        with open(caminho_saida_tokens, 'w', encoding='utf-8') as arq_tokens:
            arq_tokens.write("\n".join(tokens_reconhecidos) + "\n")
        
        print(f"[LÉXICO] Arquivo '{caminho_saida_tokens}' gerado com sucesso!")
        
        # Reinicia o lexer para a análise sintática
        lexer.lineno = 1
        
        # Executa a Análise Sintática
        resultado_ast = parser.parse(codigo_fonte, lexer=lexer)
        
        if resultado_ast is not None:
            print("\n[SUCESSO SINTÁTICO] O código é sintaticamente válido!")
            print("Árvore de Sintaxe Gerada (AST):")
            print(resultado_ast)
            return True
        else:
            print("\n[FALHA] Não foi possível estruturar a árvore sintática devido a erros.")
            return False

    except FileNotFoundError:
        print(f"[ERRO] O arquivo '{caminho_arquivo_fonte}' não foi encontrado.")
        return False
    except Exception as e:
        print(f"[ERRO] Ocorreu um problema na compilação: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    # Testa compilando o arquivo padrão se fornecido
    alvo = sys.argv[1] if len(sys.argv) > 1 else "exemplo_repeticao.sinal.txt"
    compilar_sinales(alvo)