import mediapipe as mp
import cv2 as cv

class BodyCapture():
    def __init__(self):
        self.capture = cv.VideoCapture(0)
        self.in_exercise = False
        #Setup Body
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose()

    def update_detection(self):
        ret, frame = self.capture.read()
        if not ret:
            return None
        
        frame = cv.flip(frame, 1)
        height, width, _ = frame.shape
        frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

        results = self.pose.process(frame_rgb)
        if results.pose_landmarks is None:
            cv.putText(frame, "Not body detected", (0, height - 50), cv.FONT_ITALIC, 1, (0, 0, 0), 3)
        #Arms Tracking
        else:
            right_wrist_x = int(results.pose_landmarks.landmark[self.mp_pose.PoseLandmark.RIGHT_WRIST].x * width)
            right_wrist_y = int(results.pose_landmarks.landmark[self.mp_pose.PoseLandmark.RIGHT_WRIST].y * height)

            right_elbow_x = int(results.pose_landmarks.landmark[self.mp_pose.PoseLandmark.RIGHT_ELBOW].x * width)
            right_elbow_y = int(results.pose_landmarks.landmark[self.mp_pose.PoseLandmark.RIGHT_ELBOW].y * height)

            right_shoulder_x = int(results.pose_landmarks.landmark[self.mp_pose.PoseLandmark.RIGHT_SHOULDER].x * width)
            right_shoulder_y = int(results.pose_landmarks.landmark[self.mp_pose.PoseLandmark.RIGHT_SHOULDER].y * height)

            left_wrist_x = int(results.pose_landmarks.landmark[self.mp_pose.PoseLandmark.LEFT_WRIST].x * width)
            left_wrist_y = int(results.pose_landmarks.landmark[self.mp_pose.PoseLandmark.LEFT_WRIST].y * height)

            left_elbow_x = int(results.pose_landmarks.landmark[self.mp_pose.PoseLandmark.LEFT_ELBOW].x * width)
            left_elbow_y = int(results.pose_landmarks.landmark[self.mp_pose.PoseLandmark.LEFT_ELBOW].y * height)

            left_shoulder_x = int(results.pose_landmarks.landmark[self.mp_pose.PoseLandmark.LEFT_SHOULDER].x * width)
            left_shoulder_y = int(results.pose_landmarks.landmark[self.mp_pose.PoseLandmark.LEFT_SHOULDER].y * height)

            #Draw wrists
            cv.circle(frame, (right_wrist_x, right_wrist_y), 8, (0, 40, 255), -1)
            cv.circle(frame, (left_wrist_x, left_wrist_y), 8, (0, 40, 255), -1)

            #Draw elbows
            cv.circle(frame, (right_elbow_x, right_elbow_y), 8, (0, 40, 255), -1)
            cv.circle(frame, (left_elbow_x, left_elbow_y), 8, (0, 40, 255), -1)

            #Draw shoulders
            cv.circle(frame, (right_shoulder_x, right_shoulder_y), 8, (0, 40, 255), -1)
            cv.circle(frame, (left_shoulder_x, left_shoulder_y), 8, (0, 40, 255), -1)

            #Join lines
            cv.line(frame, (right_wrist_x, right_wrist_y), (right_elbow_x, right_elbow_y), (255, 30, 0), 4)
            cv.line(frame, (right_elbow_x, right_elbow_y), (right_shoulder_x, right_shoulder_y), (255, 30, 0), 4)
            cv.line(frame, (right_shoulder_x, right_shoulder_y), (left_shoulder_x, left_shoulder_y), (255, 30, 0), 4)
            cv.line(frame, (left_shoulder_x, left_shoulder_y), (left_elbow_x, left_elbow_y), (255, 30, 0), 4)
            cv.line(frame, (left_elbow_x, left_elbow_y), (left_wrist_x, left_wrist_y), (255, 30, 0), 4)

            #mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            if left_wrist_y < left_elbow_y and left_elbow_y < left_shoulder_y \
            and right_wrist_y < right_elbow_y and right_elbow_y < right_shoulder_y:
                self.in_exercise = True

            if left_wrist_y > left_elbow_y and left_elbow_y > left_shoulder_y \
            and right_wrist_y > right_elbow_y and right_elbow_y > right_shoulder_y:
                self.in_exercise = False

            cv.putText(frame, "Workout: " + str(self.in_exercise), (0, height - 50), cv.FONT_ITALIC, 1, (0, 0, 0), 3)
        return frame
    
    def stop_detection(self):
        self.capture.release()
        cv.destroyAllWindows()