# import urllib.request as urllib2
# import gzip
# from io import StringIO,BytesIO
# import zlib

# def gzip(data):
#     print(data)
#     buf=BytesIO(data)
#     f = gzip.GzipFile(fileobj=buf)
#     print(f.read())


# b = b'\x01\x02\x03'
# gzip(b)


import gzip

f_in = open("data.txt", "rb") #打开文件

f_out = gzip.open("data.txt.gz", "wb")#创建压缩文件对象

f_out.writelines(f_in)

f_out.close()

f_in.close()
