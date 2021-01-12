import tensorflow as tf
# print("Tensorflow version",tf.__version__)
print(tf.test.is_built_with_cuda)
# print(tf.config.list_physical_devices(device_type=None))
# print(tf.config.list_physical_devices(device_type='GPU'))
# print(tf.math.reduce_sum(tf.random.normal([1,10])))