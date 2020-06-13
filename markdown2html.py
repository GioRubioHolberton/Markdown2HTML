#!/usr/bin/python3
""" script that takes an argument 2 strings  """

if __name__=='__main__':
    import sys
    from os import path
    
    if len(sys.argv) < 2:
        sys.stderr.write('Usage: ./markdown2html.py README.md README.html\n')
        exit(1)
    if not path.exists(sys.argv[1]):
        sys.stderr.write("Missing " + sys.argv[1] + '\n')
        exit(1)
        exit(0)