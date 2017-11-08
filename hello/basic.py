import tensorflow as tf

zero_tsr = tf.zeros([2, 3])
one_tsr = tf.ones([3, 4])
filled_tsr = tf.fill([3, 5], 12)
constant_tsr = tf.constant([1, 2, 4])

# Similar shape

zeros_sim = tf.zeros_like(filled_tsr)

# Sequence tensor

linear_tsr = tf.linspace(start=0.0, stop=1.0, num=3, name='linspace')
integer_seq_tsr = tf.range(start=6, limit=16, delta=3)
randunif_tsr = tf.random_uniform([2, 3], minval=0, maxval=1)
randnorm_tsr = tf.random_normal([3, 4], mean=0.0, stddev=1.0)

sess = tf.Session()
result = sess.run(randnorm_tsr)
print result
    