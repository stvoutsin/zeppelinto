#!/usr/bin/python
from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("yarn-client")
sc = SparkContext(conf = conf)

import random
from pyspark import SparkContext
def inside(p):
    x, y = random.random(), random.random()
    return x*x + y*y < 1
NUM_SAMPLES = 1000000
count = sc.parallelize(range(0, NUM_SAMPLES)) \
             .filter(inside).count()

print("Pi is roughly %f" % (4.0 * count / NUM_SAMPLES))
