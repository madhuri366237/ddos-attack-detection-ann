from preprocessing import run_preprocessing
from model import run_model
from mitigation import run_mitigation
from validation import run_validation

def main():

    print("\n===== STEP 1: Preprocessing =====")
    run_preprocessing()

    print("\n===== STEP 2: Model Training =====")
    run_model()

    print("\n===== STEP 3: Mitigation =====")
    run_mitigation()

    print("\n===== STEP 4: Forensic Validation =====")
    run_validation()

    print("\n🚀 Full Pipeline Executed Successfully!")


if __name__ == "__main__":
    main()