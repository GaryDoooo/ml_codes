#
# Copyright 2017 Garry Du
#

"""Implements the Keras model."""

import keras
from keras import layers, models
from keras.backend import relu, sigmoid


def model_create(learning_rate):

    model = models.Sequential()
    for units in hidden_units:
        model.add(layers.Dense(units=units,
                               input_dim=input_dim,
                               activation=relu))
        input_dim = units

    # Add a dense final layer with sigmoid function
    model.add(layers.Dense(labels_dim, activation=sigmoid))
    compile_model(model, learning_rate)
    return model


def compile_model(model, learning_rate):
    model.compile(loss='categorical_crossentropy',
                  optimizer=keras.optimizers.SGD(lr=learning_rate),
                  metrics=['accuracy'])
    return model

#  def to_savedmodel(model, export_path):
    #  """Convert the Keras HDF5 model into TensorFlow SavedModel."""
#
    #  builder = saved_model_builder.SavedModelBuilder(export_path)
#
    #  signature = predict_signature_def(inputs={'input': model.inputs[0]},
    #  outputs={'income': model.outputs[0]})
#
    #  with K.get_session() as sess:
    #  builder.add_meta_graph_and_variables(
    #  sess=sess,
    #  tags=[tag_constants.SERVING],
    #  signature_def_map={
    #  signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY: signature}
    #  )
    #  builder.save()
