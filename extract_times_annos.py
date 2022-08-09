from bs4 import BeautifulSoup as bs
from xml_utils import populate_times, populate_annos, recast_annos_absT, get_mspf, recast_annos_frames

def get_bs_content(file_name):

    with open(file_name, "r") as f:
        content = f.readlines()
    content = "".join(content)
    bs_content = bs(content, features="xml")
    return bs_content

if __name__ == "__main__":

    anno_filename = "data/Cactus 4_8_22_Satya_V3.eaf"
    mp4_filename = "data/Cactus 4_8_22_V3.mp4"

    bs_content = get_bs_content(anno_filename)
    root = next(bs_content.children)

    time_dict = populate_times(root)
    annos_dict = populate_annos(root)
    annos_dict = recast_annos_absT(annos_dict, time_dict)
    mspf = get_mspf(mp4_filename)
    annos_dict = recast_annos_frames(annos_dict, mspf)
    a=3
