# encoding: utf-8
from urllib.parse import quote 
import sys, os
payload = open(sys.argv[1])
print('aqui esta o seu payload:')
print(quote(str(payload.read())))
