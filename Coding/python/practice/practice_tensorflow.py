import tensorflow
a = tensorflow.constant("Hello world")
b = tensorflow.Session()
print(b.run(a))
