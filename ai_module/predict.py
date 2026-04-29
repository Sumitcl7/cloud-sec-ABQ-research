def predict_activity(data):
    import numpy as np
    from tensorflow.keras.models import load_model
    import joblib

    model = load_model("ai_module/anomaly_model.h5")
    scaler = joblib.load("ai_module/scaler.pkl")

    data_np = np.array(data).reshape(1, -1)
    data_scaled = scaler.transform(data_np)
    data_scaled = data_scaled.reshape((1, 1, data_scaled.shape[1]))

    prediction = model.predict(data_scaled)[0][0]

    print("Prediction Score:", prediction)

    # 🔥 HYBRID LOGIC
    if (
        prediction > 0.2 or
        data[1] > 10000 or   # sbytes high
        data[2] > 10000 or   # dbytes high
        data[3] < 5 or       # TTL suspicious
        data[4] < 5
    ):
        return "⚠️ Anomaly Detected"
    else:
        return "✅ Normal Activity"