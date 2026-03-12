import pandas as pd
import os

def run_validation():

    print("Running Forensic Validation...")

    data = pd.read_csv("../data/processed/train_clean.csv")

    data["forensic_confirmed"] = (
        (data["serror_rate"] > 0.3) |
        (data["count"] > 50) |
        (data["dst_host_serror_rate"] > 0.3)
    )

    data["forensic_confirmed"] = data["forensic_confirmed"].astype(int)

    confirmed_attacks = data[data["forensic_confirmed"] == 1]

    print("Forensically Confirmed Attacks:", len(confirmed_attacks))

    os.makedirs("../results", exist_ok=True)
    confirmed_attacks.to_csv("../results/forensic_validation_report.csv", index=False)

    print("Forensic Validation Report Saved")


if __name__ == "__main__":
    run_validation()