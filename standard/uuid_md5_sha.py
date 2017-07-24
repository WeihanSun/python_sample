# coding=utf-8

# hash : md5 sha1
# uuid

import hashlib
import uuid

print(hashlib.md5('python-izn'.encode('utf-8')).hexdigest())
print(hashlib.md5('python-izm'.encode('utf-8')).hexdigest())
print(hashlib.sha1('python-izn'.encode('utf-8')).hexdigest())
print(hashlib.sha1('python-izm'.encode('utf-8')).hexdigest())

print(uuid.uuid4())
