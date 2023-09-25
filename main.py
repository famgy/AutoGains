import os

import win32gui
import tensorflow as tf

from keras.preprocessing.image import ImageDataGenerator
from keras.applications.xception import Xception, preprocess_input
from keras.layers import Dense, GlobalAveragePooling2D
from keras.models import Model, load_model
from keras.callbacks import ModelCheckpoint

import window_controller
from frame_grabber import FrameGrabber
from machine_learning.ml_toolbox import TrainContainer
from teammate_round_bot import round_auto

os.environ['KMP_DUPLICATE_LIB_OK'] = 'T'
current_dir = os.path.dirname(os.path.abspath(__file__))
images_path = os.path.join(current_dir, "images")


#
# def create_training_and_validation_sets(file_paths, validation_set_probability=0.1, seed=None):
#     if seed is None:
#         seed = generate_seed()
#
#     random.seed(seed)
#
#     if isinstance(file_paths, str):
#         file_paths = [file_paths]
#
#     clear_current_dataset()
#
#     for file_path in file_paths:
#         file_names = os.listdir(file_path)
#         random.shuffle(file_names)
#
#         os.makedirs(f"datasets/current/training/{file_path.split(os.sep)[-1]}".replace("/", os.sep))
#         os.makedirs(f"datasets/current/validation/{file_path.split(os.sep)[-1]}".replace("/", os.sep))
#
#         for file_name in file_names:
#             set_label = "training"
#
#             if random.random() <= validation_set_probability:
#                 set_label = "validation"
#
#             shutil.copyfile(
#                 f"{file_path}/{file_name}".replace("/", os.sep),
#                 f"datasets/current/{set_label}/{file_path.split(os.sep)[-1]}/{file_name}".replace("/", os.sep)
#             )
#
#     return seed
#
#
# def prepare_generators(self):
#     training_data_generator = ImageDataGenerator(preprocessing_function=preprocess_input)
#     validation_data_generator = ImageDataGenerator(preprocessing_function=preprocess_input)
#
#     self.training_generator = training_data_generator.flow_from_directory(
#         "datasets/current/training",
#         target_size=(self.input_shape[0], self.input_shape[1]),
#         batch_size=32
#     )
#
#     self.validation_generator = validation_data_generator.flow_from_directory(
#         "datasets/current/validation",
#         target_size=(self.input_shape[0], self.input_shape[1]),
#         batch_size=32
#     )
#
# def train(self, epochs=3, autosave=False, validate=True):
#     if validate and (self.training_generator is None or self.validation_generator is None):
#         self.prepare_generators()
#
#     base_model = Xception(
#         weights="imagenet",
#         include_top=False,
#         input_shape=self.input_shape
#     )
#
#     output = base_model.output
#     output = GlobalAveragePooling2D()(output)
#     output = Dense(1024, activation='relu')(output)
#
#     predictions = Dense(len(self.training_generator.class_indices), activation='softmax')(output)
#     self.classifier = Model(inputs=base_model.input, outputs=predictions)
#
#     for layer in base_model.layers:
#         layer.trainable = False
#
#     self.classifier.compile(
#         optimizer="rmsprop",
#         loss="categorical_crossentropy",
#         metrics=["accuracy"]
#     )
#
#     callbacks = []
#
#     if autosave:
#         callbacks.append(ModelCheckpoint(
#             "datasets/context_classifier_{epoch:02d}-{val_loss:.2f}.model",
#             monitor='val_loss',
#             verbose=0,
#             save_best_only=False,
#             save_weights_only=False,
#             mode='auto',
#             period=1
#         ))
#
#     self.classifier.fit_generator(
#         self.training_generator,
#         samples_per_epoch=self.training_sample_count,
#         nb_epoch=epochs,
#         validation_data=self.validation_generator,
#         nb_val_samples=self.validation_sample_count,
#         class_weight="auto",
#         callbacks=callbacks
#     )


def setup_base():
    os.makedirs(os.path.join(os.getcwd(), "datasets/collect_frames_for_context"), exist_ok=True)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')

    setup_base()

    # window_controller.get_window_titles()

    # window_id = window_controller.locate_window("AOSP on blueline")
    # window_controller.bring_window_to_top(window_id)
    # window_controller.focus_window(window_id)
    # window_geometry = window_controller.get_window_geometry(window_id)

    # screen capture
    # frame_grabber = FrameGrabber(window_id, window_geometry)
    # frame_grabber.start()

    # collect frames
    # frame_grabber.collect_frames_for_context("login_role")
    # frame_grabber.collect_frames_for_context("region_luoyang")
    # frame_grabber.collect_frames_for_context("role_attributes")
    # frame_grabber.collect_frames_for_context("role_inventory")


    # train
    train_container = TrainContainer()
    # train_container.train_context()

    # frame_path = os.path.join(images_path, "region_luoyang.png")
    # frame_path = os.path.join(images_path, "role_attributes.png")
    # frame_path = os.path.join(images_path, "login_role.png")
    frame_path = os.path.join(images_path, "role_inventory.png")

    train_container.predict_context(frame_path)

    # round_auto()


    # hello = tf.constant("Hello, Tensorflow!")
    # sess = tf.Session()



