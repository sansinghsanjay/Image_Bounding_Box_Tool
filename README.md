# Image Bounding Box Tool
This is a Python project for creating bounding box masks. This tool is useful in creating masks of images. Following is input/output flow of this tool:

|![Object of Interest](https://github.com/sansinghsanjay/Image_Bounding_Box_Tool/blob/master/images/object_of_interest.png) |
|:--:|
| *Object of Interest* |


|![Input Output Flow](https://github.com/sansinghsanjay/Image_Bounding_Box_Tool/blob/master/images/object_of_interest.png) |
|:--:|
| *Input Output Flow* |

## Application
This tool is useful for creating mask, which marks the region of interest (roi) in an image. Such kind of data, image and its mask, is useful in training Machine Learning - Neural Networks (such as U-Net) for Image Segmentation problem.

Sometimes, people have only images and they want to create masks for those images. These masks are white in the region of object of interest, and black in rest of the regions.

## Steps
Following are the steps to use this Python script:
1. Create a folder "source_dir" and put all images in it.
2. Create two more folders (outside "source_dir"): "masks_dir" and "destination_dir".
3. Now, run the script "create_bounding_box.py":
		$ python3 create_bounding_box.py
4. This script will ask the following paths:
	i. source path: Enter the full path of "source_dir"
	ii. destination path: Enter the full path of "destination_dir"
	iii. masks path: Enter the full path of "masks_dir"
5. Afterwards, this script will open all images one by one, following is the sequence of operations to perform by user:
	i. Double click (mouse's left button) on the top-left corner of the object of interest.
	ii. Double click (mouse's left button) on the top-right corner of the object of interest.
	iii. Double click (mouse's left button) on the bottom-right corner of the object of interest.
	iv. Double click (mouse's left button) on the bottom-left corner of the object of interest.
	v. Now, press "m" button to signal "marked". After this, script will show a cropped picture of object of interest (don't worry if it looks slightly distorted), just hit the "d" key as a mark of "done".
	vi. Script will ask you to enter 'd', if you are done with this image, or to enter 'r', if user want to repeat all the operations with this image. If user save the mask in "masks_dir" and move this image from "source_dir" to "destination_dir", so that you don't see this image again, since it is done.
	vii. Script will ask that whether you want to continue ("c") or you want to quit ("q"). If user entered "c", then next image will open, and the all the above steps will repeat.

## Environment
This Python script is developed and tested in Python-3.6.7, Ubuntu-18.04 (OS).

|![Python3](https://github.com/sansinghsanjay/Image_Bounding_Box_Tool/blob/master/images/python3.png) |![Ubuntu](https://github.com/sansinghsanjay/Image_Bounding_Box_Tool/blob/master/images/ubuntu_logo.png) |
|:--:|:--:|
| *Python3* | *Ubuntu* |
