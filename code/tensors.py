import tensorflow as tf
import numpy as np

# This will be an int32 tensor by default; see "dtypes" below.
rank_0_tensor = tf.constant(4)
print("Rank 0 tensor: ", rank_0_tensor)

# Let's make this a float tensor.
rank_1_tensor = tf.constant([2.0, 3.0, 4.0])
print("Rank 1 tensor: ", rank_1_tensor)

# If you want to be specific, you can set the dtype (see below) at creation time
rank_2_tensor = tf.constant([[1, 2], 
                             [3, 4],
                             [5, 6]], dtype=tf.float16)
print("Rank 2 tensor: ", rank_2_tensor, "\n")

rank_3_tensor = tf.constant([
    [[0, 1, 2, 3, 4],
     [5, 6, 7, 8, 9]],
    [[10, 11, 12, 13, 14],
     [15, 16, 17, 18, 19]],
    [[20, 21, 22, 23, 24],
     [25, 26, 27, 28, 29]]])
print("Rank 3 tensor: ", rank_3_tensor, "\n")

a = tf.constant([[1, 2], [3, 4]])
b = tf.constant([[1, 1], [1, 1]]) # Could have also said `tf.ones([2,2], dtype=tf.int32)`

print(tf.add(a, b), "\n")
print(tf.multiply(a, b), "\n")
print(tf.matmul(a, b), "\n")