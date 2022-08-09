from bs4 import BeautifulSoup as bs
from xml_utils import populate_times, populate_annos

def get_bs_content(file_name):

    with open(file_name, "r") as f:
        content = f.readlines()
    content = "".join(content)
    bs_content = bs(content, features="xml")
    return bs_content

def recast_annos_dict(annos_dict, time_dict):

    new_dict = dict()

    for start_time_ref in annos_dict.keys():

        dict_value = annos_dict[start_time_ref]

        end_time_ref = dict_value[1]  # see xml_utils.py

        start_time_ms = time_dict[start_time_ref]
        end_time_ms = time_dict[end_time_ref]

        new_dict[start_time_ms] = [dict_value[0], end_time_ms, dict_value[2]]

    return new_dict

if __name__ == "__main__":

    elan_file_name = "data/Cactus 4_8_22_Satya_V3.eaf"
    bs_content = get_bs_content(elan_file_name)
    root = next(bs_content.children)

    time_dict = populate_times(root)
    annos_dict = populate_annos(root)
    annos_dict = recast_annos_dict(annos_dict, time_dict)
    a=3