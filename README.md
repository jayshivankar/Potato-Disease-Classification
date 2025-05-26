# 🥔 Potato Disease Classification

A full-stack AI-powered solution to detect potato plant diseases using deep learning. This project includes a trained CNN model, a FastAPI backend (with optional TensorFlow Serving), a React web dashboard, and a React Native mobile app. The model can also be deployed on Google Cloud Functions using both `.h5` and `.tflite` formats.

---

## 🚀 Project Overview

This project leverages computer vision and deep learning to automate the classification of potato leaf diseases. It features:

- ✅ A trained CNN model on the PlantVillage dataset  
- ⚡ REST API built with FastAPI (supports TensorFlow Serving)  
- 🌐 ReactJS web interface for disease detection  
- 📱 React Native mobile app for portable usage  
- ☁️ Optional deployment on Google Cloud Functions  

---

## 🧠 Tech Stack

| Area            | Tech Used                                        |
|-----------------|--------------------------------------------------|
| **Model**       | TensorFlow, Keras, CNN, TFLite                   |
| **Training**    | Jupyter Notebook, NumPy, Matplotlib              |
| **API**         | FastAPI, Uvicorn, TensorFlow Serving (Docker)   |
| **Web App**     | ReactJS, REST API, Axios                         |
| **Mobile App**  | React Native, Yarn, Axios                        |
| **Deployment**  | Google Cloud Functions, Google Cloud Storage     |
| **Packaging**   | Docker, `.h5` and `.tflite` formats              |

---

## 📸 Sample Use Cases

- Farmers and agronomists can quickly diagnose plant diseases in the field.  
- Agricultural apps can integrate the API for disease detection.  
- Research and educational purposes for machine learning on crops.  

---

## 🧪 Model Training

The training pipeline uses the [PlantVillage dataset](https://www.kaggle.com/arjuntejaswi/plant-village), focusing only on potato-related classes. The model achieves high accuracy in classifying:

- **Healthy**  
- **Early Blight**  
- **Late Blight**  

Model formats supported:

- ✅ `.h5` for web/cloud inference  
- ✅ `.tflite` for mobile deployment  

---

## 🌐 Web Dashboard

- Upload an image of a potato leaf  
- Instantly get predictions from the trained model  
- Clean UI built with React and Axios  

---

## 📱 Mobile App (React Native)

- Supports both Android and iOS  
- Upload and classify leaf images in real-time  
- Communicates with the FastAPI backend or GCP Cloud Functions  

---

## ☁️ Cloud Deployment

Supports model deployment on **Google Cloud Functions** using:

- `.h5` (TensorFlow model)  
- `.tflite` (Lightweight mobile-optimized model)  

Easily test your deployed model via tools like Postman using the provided HTTP trigger URL.

---

## 📁 Project Structure

```
├── api/                   # FastAPI backend (with optional TF Serving)
├── frontend/              # React web app
├── mobile-app/            # React Native mobile app
├── training/              # Jupyter Notebooks and model training code
├── tf-lite-models/        # Exported TFLite models
├── models/                # Saved .h5 models
├── gcp/                   # Scripts for Google Cloud Function deployment
```

---

## 📸 Demo

<details>
<summary>Click to expand</summary>

#### Web UI
![Web UI Screenshot](https://via.placeholder.com/600x300?text=React+Web+UI)

#### Mobile App
![Mobile UI Screenshot](https://via.placeholder.com/300x600?text=React+Native+App)

</details>

---

## 📌 TODOs

- [ ] Add multilingual support to frontend  
- [ ] Integrate real-time camera input for mobile app  
- [ ] Add Firebase backend for user auth and logging  
- [ ] Deploy full-stack solution via Kubernetes  

---

## 💡 Inspiration

> *“Bringing AI to agriculture can help feed the future.”*  
> — Inspired by Google's ML solutions for farming and crop disease detection.

