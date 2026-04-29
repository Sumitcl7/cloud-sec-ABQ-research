import os
port = int(os.environ.get("PORT", 8501))
import streamlit as st
from ai_module.predict import predict_activity
from blockchain_module.blockchain import Blockchain
from quantum_module.quantum import quantum_encrypt
import pandas as pd
import hashlib

# Initialize blockchain
blockchain = Blockchain()

# Page config
st.set_page_config(
    page_title="Cloud Security Monitoring System",
    layout="wide"
)

# ---------- HEADER ----------
st.title("Cloud Security Monitoring System")
st.markdown("""
This system demonstrates a multi-layered cloud security architecture integrating:

- AI-based anomaly detection (LSTM)
- Blockchain-based immutable logging
- Quantum-resistant encryption (simulation)

The system analyzes network activity and automatically logs suspicious behavior.
""")

# ---------- SIDEBAR ----------
st.sidebar.header("System Information")
st.sidebar.markdown("""
**Model:** LSTM (Sequence-based anomaly detection)  
**Dataset:** UNSW-NB15  
**Blockchain:** Custom SHA-256 chain  
**Encryption:** SHA3-256 (Quantum-resistant simulation)
""")

# ---------- INPUT SECTION ----------
st.subheader("Network Activity Input")

col1, col2, col3 = st.columns(3)

with col1:
    dur = st.number_input("Duration", value=0.1)

with col2:
    sbytes = st.number_input("Source Bytes", value=500)

with col3:
    dbytes = st.number_input("Destination Bytes", value=300)

col4, col5 = st.columns(2)

with col4:
    sttl = st.number_input("Source TTL", value=64)

with col5:
    dttl = st.number_input("Destination TTL", value=64)

activity = [dur, sbytes, dbytes, sttl, dttl]

# ---------- ANALYSIS ----------
if st.button("Analyze Activity"):

    st.divider()

    # AI Prediction
    result = predict_activity(activity)

    colA, colB = st.columns(2)

    with colA:
        st.subheader("Detection Result")

        if "Anomaly" in result:
            st.error("Anomalous activity detected")
        else:
            st.success("Normal activity detected")

    with colB:
        st.subheader("Input Summary")
        df = pd.DataFrame([activity], columns=["dur", "sbytes", "dbytes", "sttl", "dttl"])
        st.table(df)

    # ---------- BLOCKCHAIN + QUANTUM ----------
    if "Anomaly" in result:

        st.divider()
        st.subheader("Security Response")

        # Quantum encryption
        encrypted_data = quantum_encrypt(activity)

        # Blockchain logging
        block = blockchain.add_data({
            "activity": activity,
            "encrypted_data": encrypted_data,
            "result": result
        })

        colC, colD = st.columns(2)

        with colC:
            st.markdown("**Encrypted Data (SHA3-256)**")
            st.code(encrypted_data)

        with colD:
            st.markdown("**Blockchain Record**")
            st.json(block)

    else:
        st.info("No security action required. Activity within normal range.")

# ---------- FOOTER ----------
st.divider()
st.markdown("""
**Architecture Flow:**

1. Input network activity  
2. AI model detects anomalies  
3. Suspicious data is encrypted  
4. Event is stored in blockchain ledger  

This ensures confidentiality, integrity, and traceability of security events.
""")