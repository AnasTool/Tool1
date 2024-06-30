import os, sys
os.system("git pull")
try:
    __import__("decode_enc").anas()
except Exception as e:
    exit(str(e))