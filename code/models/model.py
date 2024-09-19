from ultralytics import YOLO
import yaml


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

    def detect(self, image_path):
        results = self.model(image_path, conf=self.conf, data=self.data)
        detected_items = self.get_list_of_detected_items(results)
        return detected_items
    