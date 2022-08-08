elan_file_names = [
    "data/Cactus 4_8_22_Satya_V3.eaf",
    "data/Cactus 4_8_22_Satya_V3_tsconf.xml",
    "data/Cactus 4_8_22_Satya_V3.pfsx"]

import xml.etree.ElementTree as ET

# Passing the path of the
# xml document to enable the
# parsing process
tree = ET.parse(elan_file_names[0])
root = tree.getroot()

for i, child in enumerate(root):
    print(f"{i}:  tag={child.tag}   &   attr={child.attrib}")


print("===================================")
tree = ET.parse(elan_file_names[1])
root = tree.getroot()

for i, child in enumerate(root):
    print(f"{i}:  tag={child.tag}   &   attr={child.attrib}")

print("===================================")
tree = ET.parse(elan_file_names[2])
root = tree.getroot()

for i, child in enumerate(root):
    print(f"{i}:  tag={child.tag}   &   attr={child.attrib}")