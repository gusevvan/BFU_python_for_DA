import cv2
from argparse import ArgumentParser

if __name__ == "__main__":
    argumentParser = ArgumentParser()
    argumentParser.add_argument("file_name")
    fileName = argumentParser.parse_args().file_name
    cap = cv2.VideoCapture(fileName)
    fps = cap.get(cv2.CAP_PROP_FPS)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        font = cv2.FONT_HERSHEY_TRIPLEX
        cv2.putText(frame, f"FPS:{str(fps)}", (50, 50), font, 1, (0, 255, 255), 2, cv2.LINE_4)
        cv2.putText(frame, f"Name:{fileName}", (50, 100), font, 1, (0, 255, 255), 2, cv2.LINE_4)
        cv2.imshow("Frame", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
