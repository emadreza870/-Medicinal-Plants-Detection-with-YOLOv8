from ultralytics import YOLO
import cv2

# مسیر صحیح فایل مدل آموزش‌دیده
model_path = "E:/python/yolov8n-medicinal-plants/weights/best.pt"

# بارگذاری مدل
model = YOLO(model_path)

# مسیر تصویر برای تست
image_path = "E:/python/yolov8n-medicinal-plants/2.jpg"

# خواندن تصویر با OpenCV
image = cv2.imread(image_path)

# اجرای تشخیص اشیا روی تصویر
results = model(image)

# رسم جعبه‌ها و برچسب‌ها روی تصویر
for r in results:
    boxes = r.boxes
    for box in boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = box.conf[0]
        cls = int(box.cls[0])
        label = model.names[cls] if cls in model.names else str(cls)
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(image, f'{label} {conf:.2f}', (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

# نمایش نتیجه
cv2.imshow("Detections", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
