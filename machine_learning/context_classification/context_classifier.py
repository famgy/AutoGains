import os

class ContextClassifier:
    def __init__(self, ):
        self.classifier = None

    def executable_train(self):
        context_paths = list()

        for root, directories, files in os.walk("datasets/collect_frames_for_context".replace("/", os.sep)):
            if root != "datasets/collect_frames_for_context".replace("/", os.sep):
                break

            for directory in directories:
                context_paths.append(f"datasets/collect_frames_for_context/{directory}".replace("/", os.sep))

        if not len(context_paths):
            raise "No Context Frames found in 'datasets/collect_frames_for_datasets'..."

        serpent.datasets.create_training_and_validation_sets(context_paths)
