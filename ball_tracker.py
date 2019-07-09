from __future__ import print_function
try:

    import sys
    import cv2
    from random import randint
    import math
    import matplotlib
    matplotlib.use("TkAgg")
    from matplotlib import pyplot as plt
    import pandas as pd
    import csv
    import collections
    import tkinter as tk
    from tkinter import filedialog
    # import pygame
    import config

    # import pygame
except ImportError as e:
    root = tk.Tk()
    root.title("Ball Tracker V1.1 2019 Séverin FERARD")
    label = tk.Label(root,
                     text="""Oops, it seems like you need to install some modules. Everything is gonna be alright don't worry, Severin got you.\n\n Just copy and past the following command to your Bash: \npip3 install opencv-contrib-python pandas easygui matplotlib config collections\n\n\n\n Dont forget, Severin loves you <3{}\n\n\n""".format(e),
                     font='Helvetica 15 bold')
    label.pack(side="top", fill="both", expand=True, padx=100, pady=100)
    button = tk.Button(root, text="Got it thanks!", command=lambda: root.destroy())
    button.pack(side="bottom", fill="none", expand=True)
    root.mainloop()
    sys.exit()


def Dist_between_two_points(pos1, pos2):
    x1 = pos1[0]
    y1 = pos1[1]
    x2 = pos2[0]
    y2 = pos2[1]
    dist = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
    return(dist)
    # Set video to load


def run(Circle, Label_dist_max, Label_current_dist, Frame_Count, Drift_Warning, treshold, Path, refresh, videopath):

    if videopath == -1:
        return("VideopathError")
    test = []
    positions = {}
    dicdistorigin = {}
    dicdistrelative = {}

    countimage = -1
    num_of_img = 0
    distlist = []
    distrib = {}
    circle_color = (0, 255, 0)
    txt_color = (0, 255, 0)

    # Create a video capture object to read videos
    print("videopath provided", videopath)
    cap = cv2.VideoCapture(videopath)

    # Read first frame
    success, frame = cap.read()
    config.frame = frame
    # quit if unable to read the video file
    if not success:
        print('Failed to read video')
        sys.exit(1)

    bboxes = []
    colors = []

    # OpenCV's selectROI function doesn't work for selecting multiple objects in Python
    # So we will call this function in a loop till we are done selecting all objects

    while True:
        # draw bounding boxes over objects
        # selectROI's default behaviour is to draw box starting from the center
        # when fromCenter is set to false, you can draw box starting from top left corner
        cv2.namedWindow('ROI Selecter', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('ROI Selecter', 1000, 700)
        cv2.moveWindow('ROI Selecter', 10, 50)
        cv2.imshow('ROI Selecter', frame)
        bbox = cv2.selectROI('ROI Selecter', frame)
        bboxes.append(bbox)
        colors.append((randint(0, 255), randint(0, 255), randint(0, 255)))
        print("\n")
        print("Press q to quit selecting boxes and start tracking")
        print("Press any other key to select next object")
        print("Click on the frame window and press escape to quit")
        k = cv2.waitKey(0) & 0xFF
        if (k == 113):  # q is pressed
            break
        elif (k == 104):
            easygui.msgbox(msg="Select a ball by drawing a box over it then press enter. To select another ball press any key and repeat the process. To quit the selecting process and start the tracking press q.", title="How it works", ok_button="Got it!")

    cv2.destroyWindow('ROI Selecter')
    print('Selected bounding boxes {}'.format(bboxes))

    trackerType = "CSRT"

    # Create MultiTracker object
    multiTracker = cv2.MultiTracker_create()

    # Initialize MultiTracker
    for bbox in bboxes:
        multiTracker.add(cv2.TrackerCSRT_create(), frame, bbox)

    # cv2.namedWindow('Analysis', cv2.WINDOW_NORMAL)
    # cv2.resizeWindow('Analysis', 1000, 900)
    # cv2.moveWindow('Analysis', 10, 10)
    while cap.isOpened():
        countimage += 1
        success, frame = cap.read()
        if not success:
            cv2.imwrite('img_path{}_lastframe.jpg'.format(num_of_img), lastframe)
            num_of_img += 1
            print("\n Last Image save in your working directory !")
            break
        lastframe = frame
        # get updated location of objects in subsequent frames
        success, boxes = multiTracker.update(frame)

        if countimage < 1:  # initialize dataframes type
            for i, newbox in enumerate(boxes):
                positions[i] = []
                dicdistorigin[i] = []
                distrib[i] = []
                dicdistrelative[i] = []
        # draw tracked objects

        for i, newbox in enumerate(boxes):

            # coordinates of the tracking box
            p1 = (int(newbox[0]), int(newbox[1]))
            p2 = (int(newbox[0] + newbox[2]), int(newbox[1] + newbox[3]))
            cv2.rectangle(frame, p1, p2, colors[i], 2, 1)
            # append the center of the box to dict "positions[index of box]" according to refresh rate
            if countimage % refresh == 0:
                xcenter = (p1[0] + p2[0]) / 2
                ycenter = (p1[1] + p2[1]) / 2
                positions[i].append((xcenter, ycenter))
                # print(p1, p2)
                # print(positions)

                if len(positions[i]):  # set origin as the coordinates of the center of the first frame's box
                    origin = positions[i][0]
                    xorigin = origin[0]
                    yorigin = origin[1]

                if len(positions[i]) >= 2:  # set 2 varibles corresponding to the x en y of the previous point
                    previousxcenter = positions[i][-2][0]
                    previousycenter = positions[i][-2][1]

                if len(positions[i]) >= 3:  # set 2 varibles corresponding to the x en y of the second to previous point
                    ndpreviousxcenter = positions[i][-3][0]
                    ndpreviousycenter = positions[i][-3][1]
                    # drawn a line between the current point previous point
                    cv2.line(frame, (int(xcenter), int(ycenter)), (int(previousxcenter), int(previousycenter)), (0, 0, 255), 1)

                distorigin = Dist_between_two_points((xcenter, ycenter), origin)
                dicdistorigin[i].append(distorigin)
                if len(positions[i]) >= 2:
                    distrelative = Dist_between_two_points((xcenter, ycenter), (previousxcenter, previousycenter))
                    dicdistrelative[i].append(distrelative)

            for pos in positions[i]:
                xcenter = pos[0]
                ycenter = pos[1]

                circle_color = (0, 255, 0)
                txt_color = (0, 255, 0)

                origin = positions[i][0]
                xorigin = origin[0]
                yorigin = origin[1]

                if Path:  # drawn a point for every coordinates in positions[i] so thats all the previous pos of the center of the box
                    cv2.circle(frame, (int(xcenter), int(ycenter)), 1, (0, 255, 255), -1)
                longest_from_origin = max(dicdistorigin[i])
                # print("longest", longest_from_origin)
            if Drift_Warning:
                if longest_from_origin > treshold:
                    circle_color = (0, 0, 255)
                    txt_color = (0, 0, 255)
                    cv2.putText(frame, f"Warning: Drift", (int(xcenter) + 20, int(ycenter) + 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1)

            if Circle:
                cv2.circle(frame, (int(xorigin), int(yorigin)), int(longest_from_origin), circle_color, 2)

            if Label_dist_max:
                cv2.putText(frame, f"dist max {longest_from_origin}", (int(xcenter) + 20, int(ycenter) + 20), cv2.FONT_HERSHEY_PLAIN, 1, txt_color, 1)
            if Label_current_dist:
                cv2.putText(frame, f"dist max {distorigin}", (int(xcenter) + 20, int(ycenter) + 20), cv2.FONT_HERSHEY_PLAIN, 1, txt_color, 1)

                # print(f"Subject {i} , distance from origin : {int(max(dicdistorigin[i]))}")

        if Frame_Count:
            cv2.putText(frame, f"Frame {countimage}", (10, 37), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)
            cv2.putText(frame, f"Refresh {refresh}", (150, 37), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)

        cv2.imshow('Analysis', frame)

        # quit on ESC button and save last frame
        if cv2.waitKey(1) & 0xFF == 27:  # Esc pressed
            cv2.imwrite('img_path{}_lastframe.jpg'.format(num_of_img), frame)
            num_of_img += 1
            print("\n Last Image save in your working directory !")

            break
    return(positions, dicdistrelative, dicdistorigin)


# run(True, True, True, True, True, 40, True, 10, "PICT0004.AVI")


def write_to_csv_file(positions, dicdistrelative, dicdistorigin, file):
    print("file to srite to, file")
    towrite = []
    for i in range(len(dicdistrelative)):
        dicdistrelative[i].insert(0, 0.0)

    for i in range(len(positions[0])):
        row = []
        for j in range(len(positions)):
            row.append((i, positions[j][i], round(dicdistorigin[j][i], 6), round(dicdistrelative[j][i], 6), "       ",))
        towrite.append(row)

    # savefile = easygui.filesavebox(title="Saving CSV file")
    with open(file, "w")as f:
        n = 0
        head = ""
        for i in range(len(positions)):
            n += 1
            head = head + f"Frame{n} ,posX{n} ,posY{n} ,Dist from origin{n}, Dist from previous point{n},'',"
        head = head + "\n"
        f.write(head)

        for i in towrite:
            string = [str(value) for value in i]
            string = ",".join(string)
            string = string.replace("(", "")
            string = string.replace(")", "")
            print(string)
            f.write(string + "\n")
