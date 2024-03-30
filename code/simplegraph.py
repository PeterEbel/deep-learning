import tensorflow as tf

a = tf.constant(5) 
b = tf.constant(2)
c = tf.constant(3)

d = tf.multiply(a, b) 
e = tf.add(c, b) 
f = tf.subtract(d, e) 

# print(f) # tf.Tensor(5, shape=(), dtype=int32
print("Result Graph 1: {}".format(f)) # 5

a = tf.constant(4)
b = tf.constant(5)
c = tf.multiply(b, a)
d = tf.add(b, a)
e = tf.subtract(c, d)
f = tf.add(c, d)
g = tf.divide(e, f)

print("Result Graph 2: {}".format(g))

a = tf.constant(3)
b = tf.constant(30)
c = tf.multiply(a, b)
d = tf.sin(c)
e = tf.divide(b, d)

print("Result Graph 3: {}".format(e))


