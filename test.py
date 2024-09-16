from ultralytics import YOLO

model = YOLO('yolov9t.pt')

results = model("car.png")

print(results[0].boxes)