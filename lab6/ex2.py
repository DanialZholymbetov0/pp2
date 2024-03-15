import os
path = os.getcwd()
if not os.path.exists(path):
    print("Path does not exist.")
if os.access(path, os.R_OK):
    print("readable.")
else:
    print("not readable.")
if os.access(path, os.W_OK):
    print("writable.")
else:
    print("not writable.")
if os.access(path, os.X_OK):
    print("executable.")
else:
    print("not executable.")