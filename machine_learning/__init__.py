import os
import random
import shutil


def create_training_and_validation_sets(file_paths, validation_set_probability=0.1):
    random.seed("AutoGains")

    clear_current_dataset()

    for file_path in file_paths:
        file_names = os.listdir(file_path)
        random.shuffle(file_names)

        os.makedirs(f"datasets/current/training/{file_path.split(os.sep)[-1]}".replace("/", os.sep))
        os.makedirs(f"datasets/current/validation/{file_path.split(os.sep)[-1]}".replace("/", os.sep))

        for file_name in file_names:
            set_label = "training"

            if random.random() <= validation_set_probability:
                set_label = "validation"

            shutil.copyfile(
                f"{file_path}/{file_name}".replace("/", os.sep),
                f"datasets/current/{set_label}/{file_path.split(os.sep)[-1]}/{file_name}".replace("/", os.sep)
            )


def clear_current_dataset():
    try:
        shutil.rmtree("datasets/current".replace("/", os.sep))
    except FileNotFoundError:
        pass

    os.mkdir("datasets/current".replace("/", os.sep))