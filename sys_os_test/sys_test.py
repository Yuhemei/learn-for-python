import sys
for item in sys.argv:
    print(item)
print("#"*20)
print("sys.argv:",sys.argv)
print("#"*20)
for item in sys.path:
    print(item)
sys.exit(0)