import cv2

cap = cv2.VideoCapture(0)

frames = []
gap = 5
count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frames.append(gray)

    if len(frames) > gap + 1:
        frames.pop(0)

    cv2.putText(
        frame,
        f"Frame Count: {count}",
        org=(10, 30),
        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=1,
        color=(0, 0, 255),
        thickness=2,
    )

    if len(frames) > gap:
        diff = cv2.absdiff(frames[0], frames[-1])
        _, thres = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

        contours, _ = cv2.findContours(
            thres, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        motion = False
        for c in contours:
            if cv2.contourArea(c) < 500:
                continue
            motion = True
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 244, 200), 2)

        if motion:
            cv2.putText(
                frame,
                "Motion Detected",
                (10, 70),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1,
                color=(0, 255, 0),
                thickness=2,
            )
            # cv2.imwrite(f"motion_frame_{count}.jpg", frame)
            print(f"Saved: motion_frame_{count}.jpg")

    cv2.imshow("Motion Detection", frame)
    count += 1

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'ESC' to exit
        break

cap.release()
cv2.destroyAllWindows()