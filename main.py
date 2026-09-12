import os

from app import app


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)


    # ======================================
    # METER
    # ======================================

    draw_text(
        frame,
        f"USELESSNESS: {uselessness}%",
        20,
        180,
        0.65
    )


    meter_x = 20
    meter_y = 200
    meter_width = 500
    meter_height = 30


    cv2.rectangle(
        frame,
        (
            meter_x,
            meter_y
        ),
        (
            meter_x + meter_width,
            meter_y + meter_height
        ),
        (180, 180, 180),
        2
    )


    filled = int(
        meter_width *
        uselessness /
        100
    )


    if filled > 0:

        cv2.rectangle(
            frame,
            (
                meter_x,
                meter_y
            ),
            (
                meter_x + filled,
                meter_y + meter_height
            ),
            (255, 255, 255),
            -1
        )


    # ======================================
    # FUNNY MESSAGE
    # ======================================

    message = get_message(
        score
    )


    draw_text(
        frame,
        message,
        20,
        285,
        0.7
    )


    # ======================================
    # LAST ACTION
    # ======================================

    draw_text(
        frame,
        f"Last action: {last_action}",
        20,
        325,
        0.55
    )


    # ======================================
    # CONTROLS
    # ======================================

    draw_text(
        frame,
        "R = Reset    D = Detection areas    Q = Quit",
        20,
        height - 25,
        0.5
    )


    # ======================================
    # OPTIONAL DETECTION REGIONS
    # ======================================

    if show_regions:

        detector.draw_regions(
            frame
        )


    # ======================================
    # SHOW CAMERA
    # ======================================

    cv2.imshow(
        "USELESS GENERATOR",
        frame
    )


    # ======================================
    # KEYBOARD
    # ======================================

    key = cv2.waitKey(1) & 0xFF


    if key == ord("q"):

        break


    elif key == ord("r"):

        score = 0

        last_action = "Reset"

        last_score_time = 0

        print(
            "Score reset!"
        )


    elif key == ord("d"):

        show_regions = not show_regions


# ==========================================
# CLEANUP
# ==========================================

camera.release()

cv2.destroyAllWindows()


print()
print("========================================")
print("FINAL USELESS SCORE:", score)
print("========================================")