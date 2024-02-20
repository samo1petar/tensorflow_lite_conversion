import tensorflow as tf

# saved_model_dir = '/home/david/Projects/Retinus/dataset/models/2021-1-2_2-45-40/saved_model'
saved_model_dir = 'models/people'
output_model_file = 'models/people/people.tflite'

converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
converter.allow_custom_ops = True
# converter.optimizations = [tf.lite.Optimize.OPTIMIZE_FOR_SIZE]
converter.optimizations = []
tflite_model = converter.convert()
open(output_model_file, "wb").write(tflite_model)
