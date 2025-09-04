# 🌿 Medicinal Plants Detection with YOLOv8

A deep learning project for accurately identifying medicinal plants using the YOLOv8 object detection model. This tool aims to bridge the gap between traditional botanical knowledge and modern technology.

---

## 📌 Table of Contents
- [Project Overview](#-project-overview)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [Installation and Setup](#-installation-and-setup)
- [Usage](#-usage)
- [Model Performance](#-model-performance)
- [Project Roadmap](#-project-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 📖 Project Overview

For centuries, medicinal plants have been a cornerstone of natural remedies and traditional medicine. However, accurately identifying different species can be challenging for non-experts, and even botanists can benefit from technological assistance.

This project introduces an intelligent system powered by **YOLOv8** to **detect and classify medicinal plants**. The model is trained on a custom dataset and is capable of identifying the specified plant species with high precision. This serves as a foundational step towards building accessible tools for researchers, enthusiasts, and practitioners in the field of herbal medicine.

---

## 🎯 Key Features

- **High-Accuracy Detection:** Leverages the state-of-the-art YOLOv8 model for fast and precise plant identification.
- **Custom-Trained Model:** Trained on a dedicated dataset of medicinal plants to ensure specialized performance.
- **Reduces Human Error:** Provides a reliable second opinion to minimize misidentification of plants.
- **Scalable Foundation:** Designed as a base for future development, including a **web or mobile application**.
- **Continuously Improving:** The dataset is actively being expanded to include more plant species.

---

## 🛠️ Tech Stack

- **Python**
- **PyTorch**
- **Ultralytics YOLOv8**
- **OpenCV**
- **NumPy**
- **Matplotlib**

---

## ⚙️ Installation and Setup

Follow these steps to get the project up and running on your local machine.

### 1️⃣ Clone the Repository
```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name
```

### 2️⃣ Create a Virtual Environment (Recommended)
It's best practice to create a virtual environment to manage dependencies.
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
Install all the required libraries from the `requirements.txt` file.
```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Once the installation is complete, you can run the pre-trained model to perform inference.

### Run the Model on Test Images
Execute the following command to run the detection script. This will load the trained weights and process the test images.
```bash
python "Trained model/yolov8n-medicinal-plants/Model implementation.py"
```
The script will save the output images with bounding boxes drawn around the detected medicinal plants.

---

## 📊 Model Performance

The model was trained on a custom dataset and evaluated using standard object detection metrics.

**Note:** Please update the following metrics with your final results.

### 🔹 Core Metrics
* **mAP50-95:** `~X.XX`
* **Precision:** `~X.XX`
* **Recall:** `~X.XX`

---

### 🖼️ Training Process Samples

* **Training Batches:** A glimpse into the data fed to the model during training.  
    `train_batch0.jpg`, `train_batch1.jpg`, `train_batch2.jpg`

* **Dataset Labels:** An example of how the ground truth labels are structured.  
    `labels.jpg`

---

### 🧪 Validation Results Samples

* **Validation Batch with Ground Truth Labels:** `val_batch0_labels.jpg`, `val_batch1_labels.jpg`, `val_batch2_labels.jpg`

* **Validation Batch with Model Predictions:** `val_batch0_pred.jpg`, `val_batch1_pred.jpg`, `val_batch2_pred.jpg`

---

### 📈 Performance Evaluation Charts

* **Confusion Matrix:** Visualizes the classification performance of the model.  
    `confusion_matrix.png`  
    `confusion_matrix_normalized.png`

* **Precision-Recall Curve:** Shows the trade-off between precision and recall for different thresholds.  
    `BoxPR_curve.png`

* **Key Metric Curves:** - F1 Score Curve: `BoxF1_curve.png`
    - Precision Curve: `BoxP_curve.png`
    - Recall Curve: `BoxR_curve.png`

* **Overall Training Results:** A summary of all metrics across training epochs.  
    `results.png`

---

## 🚀 Project Roadmap

This project is in active development. Future plans include:
- [ ] **Expand Dataset:** Add new species of medicinal plants to the dataset.
- [ ] **Advanced Data Augmentation:** Implement more sophisticated augmentation techniques to improve model robustness.
- [ ] **Model Enhancement:** Experiment with larger YOLOv8 architectures (e.g., YOLOv8m, YOLOv8l) for better accuracy.
- [ ] **Web/Mobile Application:** Develop a user-friendly web or mobile app for real-world use.
- [ ] **Live Camera Detection:** Integrate real-time detection using a device's camera.

---

## 🤝 Contributing

Contributions are welcome! This is an open-source project, and I am looking for collaborators passionate about:

* Deep Learning and Computer Vision
* Web and Mobile App Development
* Dataset Curation and Annotation

If you are interested in contributing, please feel free to open an issue, submit a pull request, or contact me directly.

---

## 📜 License

This project is licensed under the **Business Source License 1.1 (BUSL-1.1)**.

🔒 **Terms of Use:**
* You are free to use this project for **educational, research, and testing purposes**.
* Any **commercial or personal production use** is strictly prohibited without prior written permission from the developer.
* Integrating this project into a final product or application requires a formal license.

The full license text is available in the `LICENSE` file.

---

## 📩 Contact

Feel free to reach out if you have any questions, suggestions, or collaboration inquiries.

**Emad Reza** 💬 Telegram & Other Messengers: **[@EmadReza870](https://t.me/EmadReza870)**

---
