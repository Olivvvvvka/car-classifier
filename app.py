import tensorflow as tf
model = tf.keras.models.load_model("models/car_classification_model.keras")
scaler = joblib.load("models/scaler.pkl")
class_encoder = joblib.load("models/class_encoder.pkl")
feature_columns = joblib.load("models/feature_columns.pkl")
