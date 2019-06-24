# Welcome to the object detection tutorial !

# Imports
import cv2
import numpy as np
import os
import sys
# run on CPU
# os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
import tensorflow as tf
from distutils.version import StrictVersion
from collections import defaultdict

# title of our window
title = "CAPTCHA"

# Env setup
from object_detection.utils import ops as utils_ops
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util


# Model preparation
PATH_TO_FROZEN_GRAPH = 'frozen_inference_graph.pb'
# List of the strings that is used to add correct label for each box.
PATH_TO_LABELS = 'labelmap.pbtxt'
NUM_CLASSES = 37


# Load a (frozen) Tensorflow model into memory.
label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_FROZEN_GRAPH, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')


# Detection
def Captcha_detection(image_np, avg_distance_error=3):
    with detection_graph.as_default():
        with tf.Session(graph=detection_graph) as sess:
            # Open image
             #image_np = cv2.imread(image)
            # To get real color we do this:
            image_np = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)
            # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
            image_np_expanded = np.expand_dims(image_np, axis=0)
            # Actual detection.
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
            boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
            scores = detection_graph.get_tensor_by_name('detection_scores:0')
            classes = detection_graph.get_tensor_by_name('detection_classes:0')
            num_detections = detection_graph.get_tensor_by_name('num_detections:0')
            # Visualization of the results of a detection.
            (boxes, scores, classes, num_detections) = sess.run(
              [boxes, scores, classes, num_detections],
              feed_dict={image_tensor: image_np_expanded})
            vis_util.visualize_boxes_and_labels_on_image_array(
              image_np,
              np.squeeze(boxes),
              np.squeeze(classes).astype(np.int32),
              np.squeeze(scores),
              category_index,
              use_normalized_coordinates=True,
              line_thickness=2)
            # Show image with detection
            # cv2.imshow(title, cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB))
            # cv2.imwrite("Predicted_captcha.jpg", cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB))


            #Choose the correct boxes
            captcha_array = []
            for i,b in enumerate(boxes[0]):
                for Symbol in range(37):
                    if classes[0][i] == Symbol:
                        if scores[0][i] >= 0.6:
                            mid_x = (boxes[0][i][1] + boxes[0][i][3]) / 2
                            captcha_array.append([category_index[Symbol].get('name'), mid_x, scores[0][i]])


            #Re-order character
            for number in range(20):
                for captcha_number in range(len(captcha_array) - 1):
                    if captcha_array[captcha_number][1] > captcha_array[captcha_number + 1][1]:
                        temporary_captcha = captcha_array[captcha_number]
                        captcha_array[captcha_number] = captcha_array[captcha_number + 1]
                        captcha_array[captcha_number + 1] = temporary_captcha

            #Show all the letter in boxes
            average = 0
            captcha_len = len(captcha_array) - 1
            while captcha_len > 0:
                average += captcha_array[captcha_len][1] - captcha_array[captcha_len - 1][1]
                captcha_len -= 1
            average = average / (len(captcha_array) + avg_distance_error)


            average_array_filter = list(captcha_array)
            captcha_len = len(captcha_array) - 1
            while captcha_len > 0:
                if captcha_array[captcha_len][1] - captcha_array[captcha_len - 1][1] < average:
                    if captcha_array[captcha_len][2] >  captcha_array[captcha_len - 1][2]:
                        del  average_array_filter[captcha_len - 1]
                    else:
                        del  average_array_filter[captcha_len]
                captcha_len -= 1


            #print output as string
            captcha_string = ""
            for captcha_letter in range(len(average_array_filter)):
                captcha_string += average_array_filter[captcha_letter][0]

            return image_np,captcha_string


# print(Captcha_detection("8.jpg"))
