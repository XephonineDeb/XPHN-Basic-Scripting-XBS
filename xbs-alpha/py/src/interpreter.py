from lexer import *
from parser import *
from exec import *
if __name__ == '__main__': 

    lexer = BasicLexer() 

    parser = BasicParser() 


    env = {} 

      

    while True: 

          

        try: 

            text = input('>>>') 

          

        except EOFError: 

            break

          

        if text: 

            tree = parser.parse(lexer.tokenize(text)) 

            BasicExecute(tree, env)