import os
import re

def carve_files(disk_image, output_dir):
    """
    Recovers files from a raw disk image.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    carved_files = []
    file_signatures = {
        "jpg": b"\xFF\xD8\xFF",
        "png": b"\x89PNG\r\n\x1A\n",
        "pdf": b"%PDF-"
    }
    
    with open(disk_image, "rb") as img:
        data = img.read()
        
        for filetype, signature in file_signatures.items():
            matches = [m.start() for m in re.finditer(re.escape(signature), data)]
            for i, match in enumerate(matches):
                output_path = os.path.join(output_dir, f"carved_{i}.{filetype}")
                with open(output_path, "wb") as out:
                    out.write(data[match:match + 1024 * 100])  # Extract 100KB
                carved_files.append(output_path)
    
    return carved_files

if __name__ == "__main__":
    output_files = carve_files("disk_image.raw", "carved_files")
    print("Carved Files:", output_files)
