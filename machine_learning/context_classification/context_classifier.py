import os
import random
import numpy as np
import skimage.io

from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.applications.xception import preprocess_input
from machine_learning.context_classification.context_classifiers.cnn_xception_context_classifier import \
    CNNXceptionContextClassifier


class ContextClassifier:
    def __init__(self, context_paths):
        self.training_generator = None
        self.validation_generator = None

        context_path = random.choice(context_paths)
        frame_path = None

        for root, directories, files in os.walk(context_path):
            for file in files:
                if file.endswith(".png"):
                    frame_path = f"{context_path}/{file}"
                    break

            if frame_path is not None:
                break
        frame = skimage.io.imread(frame_path)

        self.input_shape = frame.shape
        self.class_labels = None
        self.prepare_generators()

    def executable_train(self, model_path="datasets/context_classifier.model"):
        # train datasets
        context_classifier = CNNXceptionContextClassifier(self.input_shape, self.training_generator, self.validation_generator)
        context_classifier.train()

        # save datasets
        if context_classifier.classifier is not None:
            context_classifier.classifier.save(model_path)
            print("Success! Model was saved to " + model_path)

    def executable_predict(self, input_frame, model_path="datasets/context_classifier.model"):
        classifier = load_model(model_path)

        # 调用 normalize 函数来标准化图像
        normalized_frame = self.normalize(input_frame)

        # 使用模型进行预测
        predictions = classifier.predict(np.expand_dims(normalized_frame, axis=0))

        # 获取预测结果
        class_indices = np.argmax(predictions, axis=1)
        predicted_class_index = class_indices[0]

        # 获取类别标签
        predicted_label = self.class_labels[predicted_class_index]

        # 获取预测的类别概率分数
        predicted_score = predictions[0][predicted_class_index]

        print("Predicted Class Index:", predicted_class_index)
        print("Predicted Class Label:", predicted_label)
        print("Predicted Class Score:", predicted_score)

    def prepare_generators(self):
        training_data_generator = ImageDataGenerator(preprocessing_function=preprocess_input)
        validation_data_generator = ImageDataGenerator(preprocessing_function=preprocess_input)

        self.training_generator = training_data_generator.flow_from_directory(
            "datasets/current/training",
            target_size=(self.input_shape[0], self.input_shape[1]),
            batch_size=32
        )

        self.validation_generator = validation_data_generator.flow_from_directory(
            "datasets/current/validation",
            target_size=(self.input_shape[0], self.input_shape[1]),
            batch_size=32
        )

        self.class_labels = {v: k for k, v in self.training_generator.class_indices.items()}

    def normalize(self, data, target_min=0, target_max=1):
        # 计算数据的均值和标准差
        data_mean = np.mean(data)
        data_std = np.std(data)

        # 将数据标准化到均值为0，标准差为1的分布
        normalized_data = (data - data_mean) / data_std

        # 将标准化后的数据映射到目标范围
        min_value = np.min(normalized_data)
        max_value = np.max(normalized_data)
        normalized_data = (normalized_data - min_value) / (max_value - min_value) * (
                    target_max - target_min) + target_min

        return normalized_data
