import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
import os

def run_preprocessing():

    columns = [
        "duration","protocol_type","service","flag","src_bytes","dst_bytes","land",
        "wrong_fragment","urgent","hot","num_failed_logins","logged_in",
        "num_compromised","root_shell","su_attempted","num_root",
        "num_file_creations","num_shells","num_access_files","num_outbound_cmds",
        "is_host_login","is_guest_login","count","srv_count",
        "serror_rate","srv_serror_rate","rerror_rate","srv_rerror_rate",
        "same_srv_rate","diff_srv_rate","srv_diff_host_rate",
        "dst_host_count","dst_host_srv_count","dst_host_same_srv_rate",
        "dst_host_diff_srv_rate","dst_host_same_src_port_rate",
        "dst_host_srv_diff_host_rate","dst_host_serror_rate",
        "dst_host_srv_serror_rate","dst_host_rerror_rate",
        "dst_host_srv_rerror_rate","label"
    ]

    file_path = "../data/raw/KDDTrain+_20Percent.txt"

    train = pd.read_csv(
        file_path,
        names=columns + ["difficulty"],
        usecols=columns
    )

    print("Original Shape:", train.shape)

    selected_features = [
        "duration","protocol_type","service","flag","src_bytes","dst_bytes",
        "count","srv_count",
        "serror_rate","srv_serror_rate",
        "rerror_rate","srv_rerror_rate",
        "same_srv_rate","diff_srv_rate",
        "dst_host_count","dst_host_srv_count",
        "dst_host_serror_rate","dst_host_srv_serror_rate",
        "dst_host_rerror_rate","dst_host_srv_rerror_rate",
        "label"
    ]

    train = train[selected_features]

    print("After Feature Selection:", train.shape)

    dos_attacks = [
        "neptune","smurf","teardrop","back",
        "apache2","mailbomb","processtable","udpstorm"
    ]

    train['label'] = train['label'].apply(lambda x: 1 if x in dos_attacks else 0)

    print("Label Distribution:")
    print(train['label'].value_counts())

    categorical_cols = ["protocol_type", "service", "flag"]
    encoder = LabelEncoder()

    for col in categorical_cols:
        train[col] = encoder.fit_transform(train[col])

    scaler = StandardScaler()
    numerical_cols = train.columns.drop("label")
    train[numerical_cols] = scaler.fit_transform(train[numerical_cols])

    os.makedirs("../data/processed", exist_ok=True)
    train.to_csv("../data/processed/train_clean.csv", index=False)

    print("Preprocessing Completed")


if __name__ == "__main__":
    run_preprocessing()