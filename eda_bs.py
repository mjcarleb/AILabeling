from bs4 import BeautifulSoup as bs

elan_file_names = [
    "data/Cactus 4_8_22_Satya_V3.eaf",
    "data/Cactus 4_8_22_Satya_V3_tsconf.xml",
    "data/Cactus 4_8_22_Satya_V3.pfsx"]


def get_bs_content(file_name):

    with open(file_name, "r") as f:
        content = f.readlines()
    content = "".join(content)
    bs_content = bs(content, features="xml")
    return bs_content

bs_content = get_bs_content(elan_file_names[0])

root = next(bs_content.children)
children = root.children
for i, child in enumerate(children):
    print(f"{i}:  {child}")

#print(bs_content.prettify())