
# Libraries

import json
import argparse
import sys
import os

# Banner Step

GREEN = "\033[1;32m"
BOLD = '\033[1m'

banner = """\u001b[34m

           ____ ____  _____ ______   __
          / ___|  _ \| ____|  _ \ \ / /
         | |  _| |_) |  _| | |_) \ V /
         | |_| |  _ <| |___|  __/ | |
          \____|_| \_\_____|_|    |_| v1.0
                                     \u001b[0m

                \u001b[36m *- coded by RAMON\u001b[0m
            """

# Parse Step

parser = argparse.ArgumentParser(description='grepy program v1.0')

parser.add_argument('-w', type=str, help='Wordlist (format JSON)')
parser.add_argument('-l', type=str, help='List of URLs (format txt)')


args = parser.parse_args()

# greppy function 


def greppy(w, l):
    vetor = []

    with open(l) as arquivo:
        conteudo1 = arquivo.readlines()

    with open(w) as obj:
        lista_js = json.load(obj)


    for linha1 in conteudo1:
        linha1 = linha1.strip()

        for linha2 in lista_js['patterns']:
    	    if linha2 in linha1:
	           if linha1 not in vetor:
                    vetor.append(linha1)

    with open('results.txt', 'a') as fo:
        for item in vetor:
            fo.write(item+'\n')

# Main function

try:
    if len(sys.argv)<2:
        print(banner)
        print(BOLD + 'Use -h or --help option to usage of grepy')


    else:
        print(banner)
        greppy(args.w, args.l)
        ext = args.w.replace(".json", "")
        os.system('mv results.txt ' + ext +'-results.txt')
        print(BOLD +"The results were stored in the TXT file")

except (KeyboardInterrupt, EOFError):
    print(BOLD + 'ABORTING...')
