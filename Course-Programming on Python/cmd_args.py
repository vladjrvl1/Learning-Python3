import os
import sys
print(*sys.argv[1:])
if 'sos' in sys.argv:
    os.chdir(r'C:\Users')