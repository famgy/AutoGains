import os

from machine_learning import create_training_and_validation_sets
from machine_learning.context_classification.context_classifier import ContextClassifier


class TrainContainer:
    def __init__(self):
        self.context_paths = list()

        for root, directories, files in os.walk("datasets/collect_frames_for_context".replace("/", os.sep)):
            if root != "datasets/collect_frames_for_context".replace("/", os.sep):
                break

            for directory in directories:
                self.context_paths.append(f"datasets/collect_frames_for_context/{directory}".replace("/", os.sep))

        if not len(self.context_paths):
            raise "No Context Frames found in 'datasets/collect_frames_for_datasets'..."

        create_training_and_validation_sets(self.context_paths)

    def train_context(self):
        print('Start train_object')

        contextClassifier = ContextClassifier(self.context_paths)
        contextClassifier.executable_train()

    def predict_context(self, frame_path):
        print('Start predict_context')

        contextClassifier = ContextClassifier(self.context_paths)
        contextClassifier.executable_predict(frame_path)

    def train_object(self):
        print('Start train_object')

    def predict_object(self):
        print('Start train_object')


