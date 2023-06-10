import os
import pickle

import time

from gesture import Gesture
from ai_controller import AIController


to_do_dir = "to_be_processed"
done_dir = "processed"
ai = AIController()


def read_gesture_pickle(filepath: str):
    with open(filepath, "rb") as file:
        gesture_from_pickle: Gesture = pickle.load(file)
    return gesture_from_pickle


def save_processed_gesture_pickle(filepath: str, processed_gesture: Gesture):
    with open(filepath.replace("to_be_processed", "processed"), "wb") as file:
        pickle.dump(processed_gesture, file)
    os.remove(filepath)


def analyze_by_ai(gesture_to_be_analyzed: Gesture):
    gesture_to_be_analyzed.is_correct = ai.is_gesture_correct(
        gesture_to_be_analyzed.expected_gesture, gesture_to_be_analyzed.gesture
    )
    return gesture_to_be_analyzed


def prepare_dirs():
    if not os.path.exists(to_do_dir):
        os.makedirs(to_do_dir)
    if not os.path.exists(done_dir):
        os.makedirs(done_dir)


def main():
    prepare_dirs()

    while True:
        file_list = os.listdir("to_be_processed")
        if file_list:
            time.sleep(2)
            current_gesture_file_path = f"to_be_processed/{file_list[0]}"
            current_gesture = read_gesture_pickle(current_gesture_file_path)
            current_gesture_result = analyze_by_ai(current_gesture)
            save_processed_gesture_pickle(
                current_gesture_file_path, current_gesture_result
            )
            print("Done:", current_gesture_file_path)


if __name__ == "__main__":
    main()
