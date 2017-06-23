import sys

try:
   package_name = sys.argv[1]
   module = __import__( package_name, fromlist=[''])
   print(module.__version__)
except:
   print("v0.0.0")

