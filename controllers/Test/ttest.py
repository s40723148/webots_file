def Velocity(center , distance = distance ):
    end_t = time.time()
    dt = end_t - start_t
    distance.append(center)
    x0, y0 = distance[0][0]/2, distance[0][1]/2
    x1, y1 = distance[-1][0]/2, distance[-1][1]/2
    dx, dy= abs(x0 - x1), abs(y0 - y1)
    ds = (dx ** 2 + dy ** 2) ** 0.5
    velocity = ds / dt
    v_str = str(format(velocity, '.1f') + "cm/sec")

    cv2.putText(info, "velocity", (10, 23), cv2.FONT_HERSHEY_SIMPLEX,  0.6, (0,255,0), 1)
    cv2.putText(info, v_str, (10, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0,255,0), 1)
def position(center):
    color = (205, 205, 80)
    cv2.putText(info, "position", (120, 23), cv2.FONT_HERSHEY_SIMPLEX,  0.6, color, 1)
    cv2.putText(info, "(cm)", (195, 23), cv2.FONT_HERSHEY_SIMPLEX,  0.4, color, 1)
    px_str = "x:"+ str(int(center[0]/2))
    py_str = "y:"+ str(int(center[1]/2))
    cv2.putText(info, px_str, (120, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 1)
    cv2.putText(info, py_str, (180, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 1)