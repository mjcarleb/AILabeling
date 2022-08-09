from bs4 import BeautifulSoup as bs
import cv2

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

    ###############
    video = cv2.VideoCapture(mp4_filename)
    ret, frame = video.read()

    frame_num = 0
    label = "none"
    stop_frame = -1
    skip_to_frame = 800

    for i in range(skip_to_frame):
        _, _ = video.read()
        frame_num += 1

    while (1):

        ret, frame = video.read()
        frame_num += 1
        if frame_num == stop_frame:
            label = "none"

        try:
            dict_value = annos_dict[frame_num]
            stop_frame = dict_value[1]  # see xml_utils
            label = dict_value[2]  # see xml_utils

        except KeyError:
            pass


        # cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q') or ret == False:
            video.release()
            cv2.destroyAllWindows()
            break

        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        color = (0, 0, 0)
        # put the dt variable over the
        # video frame
        frame = cv2.putText(frame, f"FRAME = {frame_num}",
                            (10, 100),
                            font, 2,
                            color,
                            4, cv2.LINE_4)
        frame = cv2.putText(frame, f"LABEL = {label}",
                            (10, 200),
                            font, 2,
                            color,
                            6, cv2.LINE_AA)
        cv2.imshow('frame', frame)


