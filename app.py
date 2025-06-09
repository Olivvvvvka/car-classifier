from flask import Flask, request, render_template_string
import numpy as np
import pandas as pd
import tensorflow as tf
import joblib
import os

model = tf.keras.models.load_model("models/car_classification_model.keras")
scaler = joblib.load("models/scaler.pkl")
class_encoder = joblib.load("models/class_encoder.pkl")
feature_columns = joblib.load("models/feature_columns.pkl")
