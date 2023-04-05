import cv2
import datetime

video_file = ['test-link1','test-link2']

for vid  in video_file:
    # Create a VideoCapture object
    cap = cv2.VideoCapture(vid)

    # Get the total number of frames in the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Define the position and size of the progress bar
    bar_x = 50
    bar_y = 50
    bar_width = 500
    bar_height = 30

    # Set the font and font scale for the progress bar text
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1

    # Loop through the video frames and display them on the TV
    while True:
        # Read a frame from the video
        ret, frame = cap.read()

        # If there are no more frames, stop the playback
        if not ret:
            break

        now = datetime.datetime.now()

        # Format the timestamp string as "YYYY-MM-DD HH:MM:SS"
        timestamp = now.strftime("%H:%M:%S")

        # Draw the timestamp text on the frame
        cv2.putText(frame, timestamp, (50, 50), font, font_scale, (255, 255, 255), 2)


        # Get the current frame number
        current_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))

        # Calculate the progress percentage
        progress = int((current_frame / total_frames) * 100)

        # Draw the progress bar background
        cv2.rectangle(frame, (bar_x, bar_y), (bar_x + bar_width, bar_y + bar_height), (0, 0, 255), -1)

        # Draw the progress bar fill
        fill_width = int((current_frame / total_frames) * bar_width)
        cv2.rectangle(frame, (bar_x, bar_y), (bar_x + fill_width, bar_y + bar_height), (0, 255, 0), -1)

        # Draw the progress percentage text
        text = f'{progress}%'
        cv2.putText(frame, text, (bar_x + 10, bar_y + bar_height - 5), font, font_scale, (255, 255, 255), 2)

        # Display the frame on the TV
        cv2.imshow('video player', frame)

        # Wait for a key press and quit the program if the 'q' key is pressed
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

# Release the video capture object and destroy the display window
cap.release()
cv2.destroyAllWindows()
