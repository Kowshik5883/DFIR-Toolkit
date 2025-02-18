import os
import json

def create_case(case_id, description, evidence_files):
    """
    Creates a new case with metadata and associated evidence.
    """
    case_data = {
        "case_id": case_id,
        "description": description,
        "evidence": evidence_files
    }
    
    case_file = f"case_{case_id}.json"
    with open(case_file, "w") as file:
        json.dump(case_data, file, indent=4)
    
    return f"Case {case_id} created successfully."

def load_case(case_id):
    """
    Loads an existing case.
    """
    case_file = f"case_{case_id}.json"
    if not os.path.exists(case_file):
        return {"error": "Case not found"}
    
    with open(case_file, "r") as file:
        case_data = json.load(file)
    
    return case_data

if __name__ == "__main__":
    case_id = "001"
    description = "Sample forensic case"
    evidence_files = ["sample.jpg", "log.txt"]
    print(create_case(case_id, description, evidence_files))
    print(load_case(case_id))
