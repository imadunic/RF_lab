import magic
import glob


filenames = glob.glob("Dokazi/*")
for filename in filenames:
    print(filename, magic.from_buffer(open(filename, "rb").read(2048)))