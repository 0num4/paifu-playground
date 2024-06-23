import helloworld_pb2

a = helloworld_pb2.Person()
a.name = "Alice"
a.id = 123
a.email = "aaa@test.com"

# 追加もできる
# a.maaas.add()

pbserializedStr = a.SerializeToString()
print(pbserializedStr)

# dd = helloworld_pb2.Person().ParseFromString(pbserializedStr)
# print(dd.name)
