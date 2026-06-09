# 🧠 Brain Tumor Detection using CNN

A state-of-the-art deep learning application that uses Convolutional Neural Networks (CNN) to detect and classify brain tumors from MRI scans. This project provides an intuitive web interface built with Streamlit for real-time brain tumor prediction.

## 🎯 Project Overview

This project implements a sophisticated CNN model trained on brain MRI images to classify different types of brain conditions with high accuracy. The application can distinguish between:

- **Glioma Tumor** - A type of tumor that occurs in the brain and spinal cord
- **Meningioma Tumor** - A tumor that arises from the meninges
- **No Tumor** - Healthy brain scans

## ✨ Key Features

- **High Accuracy**: Achieves 94% accuracy in brain tumor classification
- **Real-time Prediction**: Upload MRI images and get instant results
- **User-friendly Interface**: Clean, intuitive Streamlit web application
- **Multiple Tumor Types**: Classifies 4 different categories including healthy brains
- **Confidence Scores**: Provides prediction confidence for each classification
- **Image Preprocessing**: Automatic image resizing and normalization
- **Responsive Design**: Works seamlessly across different devices

## 🛠️ Technologies Used

- **Deep Learning Framework**: TensorFlow 2.x / Keras
- **Web Interface**: Streamlit
- **Image Processing**: OpenCV, PIL
- **Data Analysis**: NumPy, Pandas
- **Visualization**: Matplotlib, Seaborn
- **Model Architecture**: Convolutional Neural Network (CNN)

## 🏗️ Model Architecture

The CNN model features a sophisticated architecture optimized for medical image classification:

- **Input Layer**: 224x224x3 (RGB MRI images)
- **Convolutional Layers**: Multiple Conv2D layers with ReLU activation
- **Pooling Layers**: MaxPooling2D for feature reduction
- **Batch Normalization**: For training stability
- **Dropout Layers**: Prevents overfitting
- **Dense Layers**: Fully connected layers for classification
- **Output Layer**: 4 neurons with softmax activation

## 📊 Performance Metrics

- **Training Accuracy**: ~95%
- **Validation Accuracy**: ~94%
- **Test Accuracy**: ~94%
- **Precision**: High precision across all tumor types
- **Recall**: Excellent recall for critical tumor detection
- **F1-Score**: Balanced performance metric

## 🚀 Getting Started

### Prerequisites

```bash
Python 3.10
pip (Python package manager)
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/adeelahmed1293/Machine-Learning-projects-.git
cd Machine-Learning-projects-/Brain_Tumor_Prediction
```

2. **Install required packages**
```bash
pip install -r requirements.txt
```

3. **Run the Streamlit application**
```bash
streamlit run app.py
```

4. **Open your browser** and navigate to `http://localhost:8501`

## 💻 Usage

1. **Launch the Application**: Run the Streamlit app using the command above
2. **Upload MRI Image**: Use the file uploader to select a brain MRI scan
3. **Get Prediction**: The model will automatically process the image and provide:
   - Predicted tumor type
   - Confidence percentage
   - Visual display of the uploaded image
4. **Interpret Results**: Review the classification and confidence score



## 🎯 Model Training Process

1. **Data Collection**: Curated dataset of brain MRI images
2. **Data Preprocessing**: Image resizing, normalization, and augmentation
3. **Model Design**: CNN architecture with multiple layers
4. **Training**: Trained on GPU with early stopping and model checkpoints
5. **Validation**: Cross-validation and performance evaluation
6. **Optimization**: Hyperparameter tuning for best performance

## 📈 Results Visualization

The application provides comprehensive visualizations including:
- Prediction confidence charts
- Original vs. preprocessed images
- Model architecture diagrams
- Training/validation accuracy curves

## 🔬 Medical Applications

This tool can assist healthcare professionals in:
- **Early Detection**: Quick screening of brain MRIs
- **Second Opinion**: Supporting radiologist diagnoses
- **Educational Tool**: Training medical students
- **Research**: Supporting brain tumor research initiatives

## ⚠️ Important Disclaimer

**This application is for educational and research purposes only. It should not be used as a substitute for professional medical diagnosis. Always consult qualified healthcare professionals for medical decisions.**

## 🤝 Contributing

Contributions are welcome! Please feel free to:
1. Fork the repository
2. Create a feature branch
3. Make your improvements
4. Submit a pull request

## 📞 Contact

**Adeel Ahmed Satti**
- LinkedIn: [Connect with me](https://www.linkedin.com/in/zahra-batool-29a96a3b1/)
- GitHub: [@zahraghulam](https://github.com/zahraghulam)

## 🙏 Acknowledgments

- Medical imaging datasets used for training
- TensorFlow and Keras communities
- Streamlit development team
- Healthcare professionals who provided domain expertise

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

### 🌟 Star this repository if you found it helpful!

*Built with ❤️ for advancing healthcare through AI*
