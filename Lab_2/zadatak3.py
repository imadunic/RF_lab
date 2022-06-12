import hashlib
import glob

BUF_SIZE = 1024

filenames = glob.glob("Dokaz/*")

evidence= "c15e32d27635f248c1c8b66bb012850e5b342119"

for filename in filenames:
    with open(filename, 'rb') as f:
        sha1_hash = hashlib.sha1()
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha1_hash.update(data)

        print(filename, sha1_hash.hexdigest())
        if sha1_hash.hexdigest() == evidence :
                print(f"Trazeni dokument je {filename}")
                break