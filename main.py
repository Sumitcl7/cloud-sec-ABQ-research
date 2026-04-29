from ai_module.predict import predict_activity
from blockchain_module.blockchain import Blockchain
from quantum_module.quantum import quantum_encrypt

# Initialize blockchain
blockchain = Blockchain()

# 🔹 Change input here for testing
activity = [10, 20000, 15000, 1, 1]   # Try abnormal values for demo

# Step 1: AI Prediction
result = predict_activity(activity)
print("Prediction:", result)

# Step 2: If anomaly → encrypt + log in blockchain
if "Anomaly" in result:
    encrypted_data = quantum_encrypt(activity)

    block = blockchain.add_data({
        "activity": activity,
        "encrypted_data": encrypted_data,
        "result": result
    })

    print("\n⚡ Logged in Blockchain with Quantum Encryption:")
    print(block)

else:
    print("No logging needed")