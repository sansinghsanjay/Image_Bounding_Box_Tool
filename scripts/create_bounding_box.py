# libraries
import os
import cv2
import numpy as np
import shutil
import sys

# global variables
x1 = 0
y1 = 0
x2 = 0
y2 = 0
x3 = 0
y3 = 0
x4 = 0
y4 = 0
click_count = 0

# mouse callback function
def mark_number_plate(event, x, y, flags, param):
	# global variables
	global image, x1, y1, x2, y2, x3, y3, x4, y4, click_count
	# if mouse is double clicked
	if(event == cv2.EVENT_LBUTTONDBLCLK and click_count == 0):
		# save (x, y) location of cursor
		x1 = x
		y1 = y
		print(x1, y1)
		# increase click count
		click_count += 1
		event = None
	if(event == cv2.EVENT_LBUTTONDBLCLK and click_count == 1):
		# save (x, y) location of cursor
		x2 = x
		y2 = y
		print(x2, y2)
		# increase click count
		click_count += 1
		event = None
	if(event == cv2.EVENT_LBUTTONDBLCLK and click_count == 2):
		# save (x, y) location of cursor
		x3 = x
		y3 = y
		print(x3, y3)
		# increase click count
		click_count += 1
		event = None
	if(event == cv2.EVENT_LBUTTONDBLCLK and click_count == 3):
		# save (x, y) location of cursor
		x4 = x
		y4 = y
		print(x4, y4)
		# increase click count
		click_count += 1
		event = None

# paths
source_image_path = ""
destination_image_path = ""
masks_path = ""

# get paths from user
source_image_path = input("Enter source path of image(s): ")
destination_image_path = input("Enter destination path of image(s): ")
masks_path = input("Enter path to save mask(s): ")

# check if path is valid (exists) - if not, terminate the program
if(os.path.exists(source_image_path) == False):
	print("XXX Error: source path not found XXX")
	sys.exit(0)
if(os.path.exists(destination_image_path) == False):
	print("XXX Error: destination path not found XXX")
	sys.exit(0)
if(os.path.exists(masks_path) == False):
	print("XXX Error: masks path not found XXX")
	sys.exit(0)

# if paths don't have '/' at end, then append it
if(source_image_path[len(source_image_path) - 1] != '/'):
	source_image_path = source_image_path + "/"
if(destination_image_path[len(destination_image_path) - 1] != '/'):
	destination_image_path = destination_image_path + "/"
if(masks_path[len(masks_path) - 1] != '/'):
	masks_path = masks_path + "/"

# getting list of files inside source_image_path
files = os.listdir(source_image_path)

# reading one by one all images
i = 0
# do you want to work more
work_more = ''
while(i < len(files) and work_more != 'q'):
	# status to use
	print(files[i], "Press 'm' key after Marking number plate")
	# read image
	image = cv2.imread(source_image_path + files[i])
	# copying image
	image_copy = image.copy()
	# naming cv2 imshow window
	cv2.namedWindow(files[i])
	# setting mouse callback
	cv2.setMouseCallback(files[i], mark_number_plate)
	while(True):
		# show image so that user can mark number plate
		cv2.imshow(str(files[i]), image)
		op_status = cv2.waitKey(20) & 0xFF
		# if user press 'm' key
		if(op_status == ord('m')):
			# create copy of image
			mask_image = image.copy()
			# put zeros in all cells
			mask_image[:, :, 0] = np.zeros([image.shape[0], image.shape[1]])
			mask_image[:, :, 1] = np.zeros([image.shape[0], image.shape[1]])
			mask_image[:, :, 2] = np.zeros([image.shape[0], image.shape[1]])
			# put 255 in place of number plate
			corners = np.array([[[x1,y1], [x2,y2], [x3,y3], [x4,y4]]])
			cv2.fillPoly(mask_image, corners, (255, 255, 255))
			# resetting click_count
			click_count = 0
			# do a multiplication operation of image and mask to extract number plate
			number_plate = image_copy * (mask_image/255)
			# show number plate
			cv2.imshow("Object of Interest", number_plate)
			cv2.waitKey(0)
			cv2.destroyAllWindows()
			# asking user response on above marking
			user_response = input("Press 'd' key for DONE or 'r' key to repeat: ")
			# if number is properly marked
			if(user_response == 'd'):
				# save mask
				mask_image_name = files[i].split(".")[0] + "_mask.jpg"
				cv2.imwrite(masks_path + mask_image_name, mask_image)
				# move image file to another folder, as it is done
				shutil.move(source_image_path + files[i], destination_image_path + files[i])
				# increase image file pointer
				i += 1
				# break previous while loop
				break
			# if user not satisfied with marking, then remark it
			elif(user_response == 'r'):
				# simply break the previous while loop
				break
	# enter q to quit or any other key to continue
	if(user_response == 'd'):
		work_more = input("Enter 'q' to quit or 'c' to work more: ")

