import cv2
print(cv2.__version__)

class VisionSensor:
    def __init__(self, model_path="sensors/yolo_model.onnx"):
        self.model_path = model_path
        self.capture = cv2.VideoCapture(0)

    def classify_scene(self):
        ret, frame = self.capture.read()
        if not ret:
            return "No camera input"
        # Stub for model-based scene detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        avg_brightness = gray.mean()
        return "Indoor" if avg_brightness < 100 else "Outdoor"

    def classify_surroundings(self):
        scene = self.classify_scene()
        print(f"[VisionSensor] Surroundings classified as: {scene}")
        return scene

    def release(self):
        self.capture.release()
