import os
import pickle

import time

from gesture import Gesture
from ai_controller import AIController
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler


TO_BE_PROCESSED_DIR = "to_be_processed"
PROCESSED_DIR = "processed"
ai = AIController()


class Event(LoggingEventHandler):
    def dispatch(self, event):
        process_gesture()


def process_gesture():
    file_list = os.listdir(TO_BE_PROCESSED_DIR)
    if file_list:
        time.sleep(1)
        current_gesture_file_path = os.path.join(TO_BE_PROCESSED_DIR, file_list[0])
        current_gesture = read_gesture_pickle(current_gesture_file_path)
        current_gesture_result = analyze_by_ai(current_gesture)
        save_processed_gesture_pickle(current_gesture_file_path, current_gesture_result)
        print("Done:", current_gesture_file_path)


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
    if not os.path.exists(TO_BE_PROCESSED_DIR):
        os.makedirs(TO_BE_PROCESSED_DIR)
    if not os.path.exists(PROCESSED_DIR):
        os.makedirs(PROCESSED_DIR)


def main():
    prepare_dirs()

    event_handler = Event()
    observer = Observer()
    observer.schedule(event_handler, TO_BE_PROCESSED_DIR, recursive=False)
    observer.start()

    process_gesture()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()
