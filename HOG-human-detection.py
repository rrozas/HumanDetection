import cv2
import time
import argparse



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("video_path", type=str, help="video path")
    parser.add_argument("--threshold", type=int, default = 0, help="threshold")


    args = parser.parse_args()

    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    cap = cv2.VideoCapture(args.video_path)

    r = True
    while r :
        r, frame = cap.read()
        if r:
            start_time = time.time()
            frame = cv2.resize(frame,(1280, 720)) # Downscale to improve frame rate
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY) # HOG needs a grayscale image

            rects, weights = hog.detectMultiScale(gray_frame)

            # Measure elapsed time for detections
            end_time = time.time()
            print("Elapsed time:", end_time-start_time)

            for i, (x, y, w, h) in enumerate(rects):
                if weights[i] < args.threshold:
                    continue
                cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,0),2)

            cv2.imshow("preview", frame)
        k = cv2.waitKey(1)
        if k & 0xFF == ord("q"): # Exit condition
            break
