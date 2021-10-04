import os

print(os.getcwd())
for k, v in sorted(os.environ.items()):
    print(k+':', v)
print('\n')
# list elements in path environment variable
[print(item) for item in os.environ['PATH'].split(';')]
