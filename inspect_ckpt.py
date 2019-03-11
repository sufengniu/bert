from tensorflow.python import pywrap_tensorflow
import os

model_dir = "/scratch4/sniu/lm/uncased_L-12_H-768_A-12"
checkpoint_path = os.path.join(model_dir, "bert_model.ckpt")
reader = pywrap_tensorflow.NewCheckpointReader(checkpoint_path)
var_to_shape_map = reader.get_variable_to_shape_map()

for key in var_to_shape_map:
    print("tensor_name: ", key)
    # print(reader.get_tensor(key)) # Remove this is you want to print only variable names