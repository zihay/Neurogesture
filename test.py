import scipy.io
import h5py
import numpy as np
import pandas as pd
import cv2
import os
import math
import scipy.stats
import seaborn as sns
import matplotlib.pyplot as plt

HEAD_X_THRESHOLD = 0.8
HEAD_Y_THRESHOLD = 0.8
HEAD_LOOK_WINDOW = 40
HEAD_LOOK_OFFSET = int(HEAD_LOOK_WINDOW)-5       # use t-win+offset:t+offset

TYPE_SLIDE = "slide"
TYPE_CAMERA = "camera"
TYPE_LOOK_DOWN = "look_down"
TYPE_LOOK_UP = "look_up"
TYPE_LOOK_LEFT = "look_away_slide"
TYPE_OTHER = "other"
TYPE_NOCAMER = "non-camera"


DATA_DIR = "/Users/fordevelopment/Downloads/HeadPoseClustering-master/data/"
BODY_POINT_FILE = DATA_DIR+"bodyKeyPointData.mat"
EXCLUDE_VID = {"vp"}
body_pts = {}
headpose = {}
headpose_count = {}
# ges, ges_type, headpose, score, score_non = [], [], [], [], []

def _get_head_pos(pts):
    ear_l = _get_body_pts_df(pts, 16)
    ear_r = _get_body_pts_df(pts, 17)
    nose = _get_body_pts_df(pts, 0)

    d_l = nose.subtract(ear_l)
    d_r = ear_r.subtract(nose)

    head_x = d_r['x'].subtract(d_l['x'])
    head_x = (head_x - head_x.mean()) / head_x.std()
    head_y = ear_l['y'].add(ear_r['y']) / 2.0
    head_y = head_y.subtract(nose['y'])
    head_y = (head_y - head_y.mean()) / head_y.std()

    head_pose = pd.concat([head_x, head_y], axis=1)

    return head_pose

def get_head_look(type, head_pose, window, offset, classify_function):
    h = head_pose.to_numpy()
    h = h[:len(h)//30 * 30]
    hh=h.reshape((-1,30,2))
    hh = hh.mean(1)
    he = [classify_function(coor[0],coor[1]) for coor in hh]
    np.savetxt("headpose"+type+".csv", np.array(he),fmt='%s')

    # head_pose_mean = head_pose.rolling(window).mean()
    # head_pose_mean['type'] = head_pose_mean.apply(
    #     lambda x: classify_function(x['x'], x['y']), axis=1)
    # head_pose_mean = head_pose_mean.shift(-offset)
    # return head_pose_mean['type']




def _get_body_pts_df(pts, idx):
    df = pd.DataFrame(pts[idx * 3:idx * 3 + 2, :]).transpose()
    df.columns = ['x', 'y']
    df = df.interpolate(method='linear', axis=0).ffill().bfill()
    return df

def _classify_head_look(x, y):
    if x <= -HEAD_X_THRESHOLD:
        return TYPE_SLIDE
    elif x >= HEAD_X_THRESHOLD:
        return TYPE_LOOK_LEFT
    elif -HEAD_X_THRESHOLD < x < HEAD_X_THRESHOLD \
            and -HEAD_Y_THRESHOLD < y < HEAD_Y_THRESHOLD:
        return TYPE_CAMERA
    elif y < -HEAD_Y_THRESHOLD * 1.2:
        return TYPE_LOOK_DOWN
    else:
        return TYPE_OTHER

def _classify_head_look_2(self, x, y):
    if -HEAD_X_THRESHOLD < x < HEAD_X_THRESHOLD \
            and -HEAD_Y_THRESHOLD < y < HEAD_Y_THRESHOLD:
        return TYPE_CAMERA
    else:
        return TYPE_NOCAMER

def _classify_head_look_4(x, y):
    if x <= -HEAD_X_THRESHOLD:
        return TYPE_SLIDE
    elif -HEAD_X_THRESHOLD < x < HEAD_X_THRESHOLD \
            and -HEAD_Y_THRESHOLD < y < HEAD_Y_THRESHOLD:
        return TYPE_CAMERA
    elif y < -HEAD_Y_THRESHOLD * 1.2:
        return TYPE_LOOK_DOWN
    else:
        return TYPE_OTHER

f = h5py.File(BODY_POINT_FILE,'r')
for k, v in f.items():
    vid = k[:2]
    if vid not in EXCLUDE_VID:
        body_pts[k[:2]] = v.value
for k in body_pts:
    cur_pts = body_pts[k]
    headpose[k] = _get_head_pos(cur_pts)


for k in headpose:
    head_look = get_head_look(k, headpose[k],
                            HEAD_LOOK_WINDOW,
                            HEAD_LOOK_OFFSET,
                            _classify_head_look)