import os

from keras.applications.xception import Xception
from keras.layers import Dense, GlobalAveragePooling2D
from keras.models import Model
from keras.callbacks import ModelCheckpoint


class CNNXceptionContextClassifier:

    def __init__(self, training_generator, validation_generator, input_shape=None):
        super().__init__()
        self.classifier = None
        self.input_shape = input_shape

        self.training_generator = None
        self.validation_generator = None

    def train(self, epochs=3, autosave=False, validate=True):
        print('start train')

        if validate and (self.training_generator is None or self.validation_generator is None):
            self.prepare_generators()

        base_model = Xception(
            weights="imagenet",
            include_top=False,
            input_shape=self.input_shape
        )

        output = base_model.output
        output = GlobalAveragePooling2D()(output)
        output = Dense(1024, activation='relu')(output)

        predictions = Dense(len(self.training_generator.class_indices), activation='softmax')(output)
        self.classifier = Model(inputs=base_model.input, outputs=predictions)

        for layer in base_model.layers:
            layer.trainable = False

        self.classifier.compile(
            optimizer="rmsprop",
            loss="categorical_crossentropy",
            metrics=["accuracy"]
        )

        callbacks = []
        if autosave:
            callbacks.append(ModelCheckpoint(
                "datasets/context_classifier_{epoch:02d}-{val_loss:.2f}.model",
                monitor='val_loss',
                verbose=0,
                save_best_only=False,
                save_weights_only=False,
                mode='auto',
                period=1
            ))

        training_sample_count = self.training_sample_count()
        validation_sample_count = self.validation_sample_count()
        self.classifier.fit(
            x=self.training_generator,
            steps_per_epoch=training_sample_count,
            epochs=epochs,
            validation_data=self.validation_generator,
            validation_steps=validation_sample_count,
            class_weight=None,
            callbacks=callbacks
        )

        return self.classifier

    def training_sample_count(self):
        sample_count = 0

        for root, dirs, files in os.walk("datasets/current/training"):
            sample_count += len(files)

        return sample_count

    def validation_sample_count(self):
        sample_count = 0

        for root, dirs, files in os.walk("datasets/current/validation"):
            sample_count += len(files)

        return sample_count
