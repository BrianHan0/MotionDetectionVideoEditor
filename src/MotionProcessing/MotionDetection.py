import cv2
import numpy as np
import matplotlib.pyplot as plt

def motion_detector(video_paths,feed=False):
    all_motion_levels = []
    video_boundaries = [0]
    for video_path in video_paths:
        # Read the video from file
        video = cv2.VideoCapture(video_path)  # Replace with your video path

        # Initialize frames
        ret, frame1 = video.read()  # Read the first frame
        ret, frame2 = video.read()  # Read the second frame

        # Process video frame by frame
        while video.isOpened():

            # Calculate the absolute difference between frames
            diff = cv2.absdiff(frame1, frame2)

            # Convert color image to grayscale
            gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

            # Apply Gaussian blur to smooth the image
            blur = cv2.GaussianBlur(gray, (9,9), 0)

            # Apply thresholding to create a binary image
            _, thresh = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY)

            # Dilate the image to fill in gaps
            dilated = cv2.dilate(thresh, None, iterations=3)

            # Find contours in the image
            contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            motion = sum(cv2.contourArea(contour) for contour in contours if cv2.contourArea(contour) > 900)

            all_motion_levels.append(motion)
            if(feed==True):
                # Draw rectangles around detected contours
                for contour in contours:
                    (x, y, w, h) = cv2.boundingRect(contour)

                    # Filter out small contours that may be noise
                    if cv2.contourArea(contour) < 1100:
                        continue
                    motion+= cv2.contourArea(contour)
                    # Draw rectangles for significant contours
                    cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)

                # Display the result in a window named 'feed'

                cv2.imshow("feed", frame1)

            # Assign the second frame to the first frame for the next iteration
            frame1 = frame2

            # Read the next frame
            ret, frame2 = video.read()

            # Break the loop if no more frames are available
            if not ret:
                break

            # Break the loop if 'ESC' key is pressed
            if cv2.waitKey(40) == 27:
                break


        # Clean up: close all OpenCV windows and release video capture
        cv2.destroyAllWindows()
        video.release()
        video_boundaries.append(len(all_motion_levels))

    return all_motion_levels, video_boundaries



