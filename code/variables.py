import tensorflow as tf

var = tf.Variable([0.0, 0.0, 0.0])
var.assign([1, 2, 3])
var.assign_add([2, 3, 4])

print(var)



