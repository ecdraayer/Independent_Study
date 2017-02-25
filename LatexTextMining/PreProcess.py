import magic
import os, sys
import shutil

files = os.listdir(sys.argv[1])
dest = os.path.dirname(os.path.abspath(__file__))
print dest
for filename in files:
  blob = open(os.path.join(sys.argv[1], filename)).read()
  m = magic.Magic(mime_encoding=True)
  encoding = m.from_buffer(blob)
  if encoding != 'us-ascii':
    shutil.move(os.path.join(sys.argv[1], filename), dest)
    print filename, " - ", encoding