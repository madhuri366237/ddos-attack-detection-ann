import pandas as pd
import os
from datetime import datetime
import tensorflow as tf

def run_mitigation():

    print("Loading Trained Model...")
    model = tf.keras.models.load_model("../results/ddos_ann_model.h5")

    print("Loading Clean Dataset...")
    data = pd.read_csv("../data/processed/train_clean.csv")

    X = data.drop("label", axis=1)

    print("Predicting Attacks...")
    predictions = model.predict(X)
    predicted_labels = (predictions > 0.5).astype(int)

    data["predicted_attack"] = predicted_labels

    attacks_detected = data[data["predicted_attack"] == 1]

    print("Total Attacks Detected:", len(attacks_detected))

    blocked_ips = []
    alerts = []

    for index, row in attacks_detected.iterrows():
        fake_ip = f"192.168.1.{index % 255}"

        blocked_ips.append(fake_ip)

        alert_message = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "source_ip": fake_ip,
            "action": "BLOCKED",
            "reason": "DDoS Attack Detected"
        }

        alerts.append(alert_message)

    os.makedirs("../results", exist_ok=True)

    incident_report = pd.DataFrame(alerts)
    incident_report.to_csv("../results/incident_report.csv", index=False)

    print("Mitigation Completed")
    print("Blocked IPs:", len(blocked_ips))
    print("Incident Report Saved")


if __name__ == "__main__":
    run_mitigation()