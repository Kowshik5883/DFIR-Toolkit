import os
import exifread

def extract_metadata(file_path):
    """
    Extracts metadata from images and documents.
    """
    if not os.path.exists(file_path):
        return {"error": "File not found"}
    
    metadata = {}
    with open(file_path, "rb") as file:
        tags = exifread.process_file(file)
        for tag, value in tags.items():
            metadata[tag] = str(value)
    
    return metadata

if __name__ == "__main__":
    file_path = "sample.jpg"  # Replace with actual file path
    metadata_info = extract_metadata(file_path)
    for key, value in metadata_info.items():
        print(f"{key}: {value}")
