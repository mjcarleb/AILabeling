elan_file_names = [
    "data/Cactus 4_8_22_Satya_V3.eaf",
    "data/Cactus 4_8_22_Satya_V3_tsconf.xml",
    "data/Cactus 4_8_22_Satya_V3.pfsx"]

import xml.etree.ElementTree as ET

def show_tree(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()
    print(ET.tostring(root, encoding='utf8').decode('utf8'))
    # for i, child in enumerate(root):
    #    print(f"{i}:  tag={child.tag}   &   attr={child.attrib}")


print(f"Showing tree for {elan_file_names[0]}:")
show_tree(elan_file_names[0])

