import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
from sklearn.utils import class_weight
import joblib

# -----------------------------
# 1. LOAD DATASET
# -----------------------------
df = pd.read_csv(r"D:\cloud-sec-project\ai_module\data\UNSW_NB15_training-set.csv")

# -----------------------------
# 2. SELECT FEATURES
# -----------------------------
features = ["dur", "sbytes", "dbytes", "sttl", "dttl"]

X = df[features]
y = df["label"]

# -----------------------------
# 3. SCALE DATA
# -----------------------------
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Save scaler
joblib.dump(scaler, "ai_module/scaler.pkl")

# -----------------------------
# 4. RESHAPE FOR LSTM
# -----------------------------
X_scaled = X_scaled.reshape((X_scaled.shape[0], 1, X_scaled.shape[1]))

# -----------------------------
# 5. HANDLE CLASS IMBALANCE
# -----------------------------
class_weights = class_weight.compute_class_weight(
    class_weight='balanced',
    classes=np.unique(y),
    y=y
)

class_weights = dict(enumerate(class_weights))

print("Class Weights:", class_weights)

# -----------------------------
# 6. BUILD MODEL
# -----------------------------
model = Sequential()
model.add(LSTM(64, input_shape=(1, X_scaled.shape[2])))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(
    loss='binary_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

# -----------------------------
# 7. TRAIN MODEL
# -----------------------------
history = model.fit(
    X_scaled,
    y,
    epochs=15,
    batch_size=64,
    class_weight=class_weights,
    verbose=1
)

# -----------------------------
# 8. SAVE MODEL
# -----------------------------
model.save("ai_module/anomaly_model.h5")

# -----------------------------
# 9. PRINT METRICS
# -----------------------------
final_accuracy = history.history['accuracy'][-1]
final_loss = history.history['loss'][-1]

print("\nModel Training Complete")
print("Final Accuracy:", round(final_accuracy, 4))
print("Final Loss:", round(final_loss, 4))