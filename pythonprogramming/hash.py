import hashlib

md5hash = hashlib.md5()

md5hash.update('This is a simple Hash ')
print md5hash.hexdigest()
