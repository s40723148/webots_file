from controller import Robot, Camera, Motor
import cv2

robot = Robot()
timestep = 64

camera = robot.getCamera('camera')
Camera.enable(camera, timestep)

#YPosition = 0.0
#XPosition = 0.0

Yspeed = 0.0
Xspeed = 0.0
#Device
#Yaxis = robot.getMotor('Yaxis')
#Yaxis.setPosition(float('inf'))

Xaxis = robot.getMotor('Xaxis')
Xaxis.setPosition(float('inf'))

while robot.step(timestep) != -1:
    k = cv2.waitKey(10) & 0xFF
    Camera.getImage(camera)
    Camera.saveImage(camera, 'img.png', 1)
    frame = cv2.imread('img.png')
    frame = cv2.resize(frame, (1310, 500), interpolation=cv2.INTER_AREA)
    cv2.imshow('frame', frame)
    #if k == ord('w'):
    #    print('w')
    #    #YPosition = 0.41
    #    Yspeed = Yspeed + 1.0
    #elif k == ord('s'):
    #    print('s')
    #    #YPosition = 0
    #    Yspeed = Yspeed - 1.0
    #else:
    #    pass
    if k == ord('a'):
        print('a')
        #XPosition = 0.4
        Xspeed = Xspeed + 1.0

    elif k == ord('d'):
        print('d')
        #XPosition = 0
        Xspeed = Xspeed - 1.0
        if Xspeed > 1.0 :
            Xspeed = 0
        else:
            pass
    else:
        pass
    #Yaxis.setPosition(YPosition)
    #Xaxis.setPosition(XPosition)

    #Yaxis.setVelocity(Yspeed)
    Xaxis.setVelocity(Xspeed)

    if k == 27:
        break

cv2.destroyAllWindows()