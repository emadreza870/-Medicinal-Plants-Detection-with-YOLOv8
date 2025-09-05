# 🌿 Medicinal Plants Detection with YOLOv8

A deep learning project for accurately identifying medicinal plants using the YOLOv8 object detection model. This README presents images in a clean, graphical layout using simple HTML so they appear side-by-side on GitHub.

---

## 📌 Table of Contents
- [Project Overview](#-project-overview)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [Installation and Setup](#-installation-and-setup)
- [Usage](#-usage)
- [Model Performance](#-model-performance)
- [Gallery (Graphical)](#gallery-graphical)
- [Project Roadmap](#-project-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 📖 Project Overview

This project uses **YOLOv8** to detect and classify medicinal plants from images. The model was trained on a custom dataset and outputs visual results saved under the repository folder `Trained model/yolov8n-medicinal-plants/`.

---

## 🎯 Key Features

- Fast object detection with YOLOv8
- Custom dataset focused on medicinal plants
- Visual outputs (predictions / labels / confusion matrix / curves)

---

## 🛠️ Tech Stack

- Python, PyTorch, Ultralytics YOLOv8
- OpenCV, NumPy, Matplotlib

---

## ⚙️ Installation and Setup

```bash
git clone https://github.com/emadreza870/Medicinal-Plants-Detection-with-YOLOv8.git
cd Medicinal-Plants-Detection-with-YOLOv8
```

Create and activate a virtual environment, then install requirements:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
```

---

## 🚀 Usage

Run the provided inference/visualization script:

```bash
python "Trained model/yolov8n-medicinal-plants/Model implementation.py"
```

Outputs (images and charts) will be saved into `Trained model/yolov8n-medicinal-plants/`.

---

## 📊 Model Performance

### 🔹 Core Metrics
* **mAP50-95:** `~X.XX`  
* **Precision:** `~X.XX`  
* **Recall:** `~X.XX`  

> Replace these placeholders with final numbers from `results.png` / YOLOv8 log.

---

## Gallery (Graphical)

Below images are arranged in rows (3 per row). You can adjust the `width` percentage to change sizing.

### Training batches
<p align="center">
  <img src="https://github.com/emadreza870/Medicinal-Plants-Detection-with-YOLOv8/blob/main/Trained%20model/yolov8n-medicinal-plants/train_batch0.jpg" width="32%" alt="train_batch0">
  <img src="https://github.com/emadreza870/Medicinal-Plants-Detection-with-YOLOv8/blob/main/Trained%20model/yolov8n-medicinal-plants/train_batch1.jpg" width="32%" alt="train_batch1">
  <img src="https://github.com/emadreza870/Medicinal-Plants-Detection-with-YOLOv8/blob/main/Trained%20model/yolov8n-medicinal-plants/train_batch2.jpg" width="32%" alt="train_batch2">
</p>

*Caption: Training images shown during batch sampling.*

### Validation - Ground Truths
<p align="center">
  <img src="https://github.com/emadreza870/Medicinal-Plants-Detection-with-YOLOv8/blob/main/Trained%20model/yolov8n-medicinal-plants/val_batch0_labels.jpg" width="32%" alt="val_batch0_labels">
  <img src="https://github.com/emadreza870/Medicinal-Plants-Detection-with-YOLOv8/blob/main/Trained%20model/yolov8n-medicinal-plants/val_batch1_labels.jpg" width="32%" alt="val_batch1_labels">
  <img src="https://github.com/emadreza870/Medicinal-Plants-Detection-with-YOLOv8/blob/main/Trained%20model/yolov8n-medicinal-plants/val_batch2_labels.jpg" width="32%" alt="val_batch2_labels">
</p>

### Validation - Predictions
<p align="center">
  <img src="https://github.com/emadreza870/Medicinal-Plants-Detection-with-YOLOv8/blob/main/Trained%20model/yolov8n-medicinal-plants/val_batch0_pred.jpg" width="32%" alt="val_batch0_pred">
  <img src="https://github.com/emadreza870/Medicinal-Plants-Detection-with-YOLOv8/blob/main/Trained%20model/yolov8n-medicinal-plants/val_batch1_pred.jpg" width="32%" alt="val_batch1_pred">
  <img src="https://github.com/emadreza870/Medicinal-Plants-Detection-with-YOLOv8/blob/main/Trained%20model/yolov8n-medicinal-plants/val_batch2_pred.jpg" width="32%" alt="val_batch2_pred">
</p>

### Charts & Metrics
<p align="center">
  <img src="https://github.com/emadreza870/Medicinal-Plants-Detection-with-YOLOv8/blob/main/Trained%20model/yolov8n-medicinal-plants/confusion_matrix.png" width="32%" alt="confusion_matrix">
  <img src="https://github.com/emadreza870/Medicinal-Plants-Detection-with-YOLOv8/blob/main/Trained%20model/yolov8n-medicinal-plants/BoxPR_curve.png" width="32%" alt="BoxPR_curve">
  <img src="https://github.com/emadreza870/Medicinal-Plants-Detection-with-YOLOv8/blob/main/Trained%20model/yolov8n-medicinal-plants/results.png" width="32%" alt="results">
</p>

---

## 🚀 Project Roadmap

- [ ] Expand dataset with more species
- [ ] Test larger YOLOv8 variants
- [ ] Add live camera demo and mobile app

---

## 🤝 Contributing

Contributions welcome. Open issues or PRs for dataset, models, or UI.

---

## 📜 License

Business Source License 1.1 (BUSL-1.1). See `LICENSE` file.

---

## 📩 Contact

**Emad Reza** — Telegram: [@EmadReza870](https://t.me/EmadReza870)
