import hashlib

# BUF_SIZE is totally arbitrary, change for your app!
BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

md5 = hashlib.md5()
sha1 = hashlib.sha1()
sha256 = hashlib.sha256()

# filenames=("test.txt", "test1.txt")
filenames = ["test.docx", "test.jpg"]

for filename in filenames:
    with open(filename, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)
            sha1.update(data)
            sha256.update(data)
            print(f"--{filename}--")
            print("MD5: {0}".format(md5.hexdigest()))
            print("SHA1: {0}".format(sha1.hexdigest()))
            print("SHA256: {0}".format(sha256.hexdigest()))
