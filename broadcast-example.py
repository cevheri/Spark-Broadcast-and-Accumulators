from pyspark.shell import sc

txt_file= sc.textFile("README.md")

print(*txt_file.collect()[0])

s = txt_file.collect()
print(type(s))

broadcastVar = sc.broadcast(s)

print( broadcastVar.value)
# [1, 2, 3]

# driver write small data(user list)
# executer readonly

