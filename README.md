# ANN-Based DDoS Attack Detection System

## Overview

This project implements a machine learning pipeline to detect **Distributed Denial of Service (DDoS)** attacks using an **Artificial Neural Network (ANN)**.

The system analyzes network traffic features from the **NSL-KDD dataset** and identifies malicious traffic patterns.  
The project also includes **attack mitigation simulation and forensic validation**, forming a small cybersecurity detection pipeline.

---

## Project Pipeline

Network Traffic Data  
⬇  
Data Preprocessing  
⬇  
Feature Selection  
⬇  
ANN Model Training  
⬇  
Attack Detection  
⬇  
Mitigation Simulation  
⬇  
Forensic Validation  

---

## Features

- Data preprocessing and feature selection
- ANN-based DDoS attack detection
- Detection of malicious network traffic
- Simulated mitigation (incident reporting)
- Forensic validation of detected attacks
- Modular and clean project structure

---

## Dataset

This project uses the **NSL-KDD dataset**, an improved version of the **KDD Cup 1999 dataset** used for intrusion detection research.

The dataset contains network traffic features such as:

- protocol type  
- service  
- flag  
- connection statistics  
- error rates  

These features help classify network traffic as **normal or attack**.

---

## Technologies Used

- Python  
- TensorFlow / Keras  
- Scikit-learn  
- Pandas  
- NumPy
