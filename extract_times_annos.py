from bs4 import BeautifulSoup as bs
from xml_utils import populate_times, populate_annos

def get_bs_content(file_name):

    with open(file_name, "r") as f:
        content = f.readlines()
    content = "".join(content)
    bs_content = bs(content, features="xml")
    return bs_content


if __name__ == "__main__":

    elan_file_name = "data/Cactus 4_8_22_Satya_V3.eaf"
    bs_content = get_bs_content(elan_file_name)
    root = next(bs_content.children)

    time_dict = populate_times(root)
    anno_dict = populate_annos(root)
