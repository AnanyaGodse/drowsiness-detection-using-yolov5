import os
import xml.etree.ElementTree as ET

def convert_to_yolo(xml_dir, output_dir, classes_file):
    with open(classes_file, 'r') as f:
        classes = [line.strip() for line in f.readlines()]

    os.makedirs(output_dir, exist_ok=True)

    for xml_file in os.listdir(xml_dir):
        if not xml_file.endswith(".xml"):
            continue
        
        tree = ET.parse(os.path.join(xml_dir, xml_file))
        root = tree.getroot()

        size = root.find("size")
        width = int(size.find("width").text)
        height = int(size.find("height").text)

        yolo_file = os.path.join(output_dir, xml_file.replace(".xml", ".txt"))
        with open(yolo_file, 'w') as f:
            for obj in root.findall("object"):
                class_name = obj.find("name").text
                if class_name not in classes:
                    continue
                class_id = classes.index(class_name)

                bndbox = obj.find("bndbox")
                xmin = int(bndbox.find("xmin").text)
                ymin = int(bndbox.find("ymin").text)
                xmax = int(bndbox.find("xmax").text)
                ymax = int(bndbox.find("ymax").text)

                x_center = (xmin + xmax) / (2.0 * width)
                y_center = (ymin + ymax) / (2.0 * height)
                box_width = (xmax - xmin) / width
                box_height = (ymax - ymin) / height

                f.write(f"{class_id} {x_center} {y_center} {box_width} {box_height}\n")

if __name__ == "__main__":
    parent_directory = "data/frames" 
    classes_file = "classes.txt"
    
    subfolders = ["eyes_open", "eyes_closed", "yawning"]
    for subfolder in subfolders:
        xml_directory = os.path.join(parent_directory, subfolder)
        output_directory = xml_directory  
        print(f"Processing: {subfolder}")
        convert_to_yolo(xml_directory, output_directory, classes_file)
