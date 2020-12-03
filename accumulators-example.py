from pyspark import SparkConf, SparkContext
from pyspark.shell import sc

accum = sc.accumulator(0)
print(accum)

sc.parallelize([1, 2, 3, 4]).foreach(lambda x: accum.add(x))

print(accum.value)

# excetion

# driver readonly
# every executer write add, add, add...
# total result return to driver