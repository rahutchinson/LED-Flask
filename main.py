from Lexer import *
from Tokenizer import *
from LED_GameParser import *
from LED_GameCompiler_js import *



FILENAME = "TicTacToe"

"""
def compile_LED_to_JS(LED_code_string):
    helper_js_string = open_file_as_string("/home/rahutchinson/mysite/helpers.js")

    LED_code = preprocess_codeblocks(LED_code_string)
    lexed_LED = lex(LED_code)
    preprocessed_defs_LED = preprocess_definitions(lexed_LED)
    tokenized_LED = tokenize(preprocessed_defs_LED)
    pared_LED = parse(tokenized_LED)
    compiled_LED_to_js = comp_func(pared_LED)
    compiled_LED_with_helpers = compiled_LED_to_js + helper_js_string

    return compiled_LED_with_helpers
"""

def compile_LED_to_JS(LED_code_string):
    helper_js_string = open_file_as_string("/home/rahutchinson/LED-Flask/helpers.js")


    LED_code = preprocess_codeblocks(LED_code_string)
    lexed_LED = lex(LED_code)
    preprocessed_defs_LED = preprocess_definitions(lexed_LED)
    tokenized_LED = tokenize(preprocessed_defs_LED)
    print(tokenized_LED)

    pared_LED = parse(tokenized_LED)

    compiled_LED_to_js = comp_func(pared_LED)
    compiled_LED_with_helpers = compiled_LED_to_js + helper_js_string


    return compiled_LED_with_helpers

def LED_to_EASEL_game(LED_code):


    compiled_LED_to_js = compile_LED_to_JS(LED_code)


    HTML_file = open("LED_Game/HTML_file.html", "w+")
    for i in HTML_code: HTML_file.write(i)
    HTML_file.close()

    return (HTML_code)