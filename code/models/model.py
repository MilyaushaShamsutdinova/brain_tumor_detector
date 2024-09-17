from ultralytics import YOLO
import os
import yaml
from typing import List
import torch
import time


class BrainTumorDetector:
    def __init__(self, model_path, data_path, confidence=0.5):
        self.model = YOLO(model_path).to('cpu')
        self.data = self.load_data(data_path)
        self.conf = confidence

    def load_data(self, data_path):
        with open(data_path, 'r') as file:
            return yaml.safe_load(file)
        
    def get_list_of_detected_items(self, results):
        detected_items = set()
        for result in results:
            for box in result.boxes:
                detected_items.add(result.names[box.cls.item()])
        return 'Tumor' if list(detected_items) else 'No tumor'

    def detect(self, image_path) -> List[str]:
        results = self.model(image_path, conf=self.conf, data=self.data)
        detected_items = self.get_list_of_detected_items(results)
        return detected_items


def main():
    model_path = 'models\model_0.pt'
    data_path = 'code\datasets\Brain-tumor-Detection-1\data.yaml'
    conf = 0.5
    
    # image_path = r'code\datasets\Brain-tumor-Detection-1\test\images\3_jpg.rf.24e34e13cf2b7e3a657c2a1d04baf721.jpg'
    image_path = r'data\brain.jpg'

    model = BrainTumorDetector(model_path, data_path)
    result = model.detect(image_path)
    print(result)

if __name__ == "__main__":
    main()
    