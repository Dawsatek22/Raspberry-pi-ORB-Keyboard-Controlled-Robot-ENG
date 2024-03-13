     #this code is in english.
#this code is made with the intention to use the robot parts with(is not nesscasary by the way ) Openroboticsplatform components. more info here:https://openroboticplatform.com/
#and the SunFounder Robot HAT Expansion Board Designed for Raspberry Pi. documentation for more info is in this link : https://docs.sunfounder.com/projects/robot-hat-v4/en/latest/# 
# also it is ment to use with VNC Viewer. more info in this link :https://www.realvnc.com/en/connect/download/viewer/   


import pygame # for keyboard control. if you dont have pygame library here a link for mor info:https://www.pygame.org/
from time import sleep

# Import Motor class
from robot_hat import Motors

# Create Motor object
motors = Motors()
motors.set_left_id(1) #Setting the left Motor.
motors.set_right_id(2)#Setting the right Motor.
#!Warning i dont know if it is the code or the parts but to make the work the motors."direction"() commands are reversed to make it work(you can chang it yourself if yo want.).


pygame.init()
window = pygame.display.set_mode((300,300))
pygame.display.set_caption("Pygame Demonstration")

   

    
    

mainloop=True
while mainloop:

    pygame.time.delay(100)
    for event in pygame.event.get():

        if event.type==pygame.QUIT:

            mainloop=False

        pressed = pygame.key.get_pressed()
        buttons = [pygame.key.name(k) for k,v in enumerate(pressed) if v]
        print(buttons)  # print list to console
     
            
        if pressed[pygame.K_s]: # s key stops the robot
            
            motors.stop()
            print("s = stop")
            sleep(0.1)
           
           
        
        if pressed[pygame.K_f]: # f key drives forward the robot
            
            motors.turn_right(100)
          
            sleep(0.1)
            motors.stop()
            print("forward")
        if pressed[pygame.K_b]: # b key drives the robot backwards
            
            motors.turn_left(100)
            sleep(0.1)
            motors.stop()
            print("backwards")
        if pressed[pygame.K_l]: # l key drives the robot left
            
            motors.backward(50)
            
            sleep(0.1)
            motors.stop()
            print("left")
        if pressed[pygame.K_r]: # r key drives the robot right.
            
            motors.forward(50)
            sleep(0.1)
            motors.stop()
            print("right")
        if pressed[pygame.K_1]: # 1 key drives the robot right forward .
            
            motors.turn_right(100)
           
            sleep(1)
            motors.backward(50)
            sleep(0.1)
            motors.stop()
            print("right forward ")
        if pressed[pygame.K_2]: # 1 key drives the robot left forward .
            
            motors.turn_right(100)
           
            sleep(1)
            motors.forward(50)
            sleep(0.1)
            motors.stop()
            print("left forward ")
        
        if pressed[pygame.K_3]: # 1 key drives the robot left backward 
            
            motors.turn_left(100)
           
            sleep(1)
            motors.forward(60)
            sleep(0.1)
            motors.stop()
            print("left forward ")
        
        if pressed[pygame.K_4]: # 1 key drives the robot right backward 
            
            motors.turn_left(100)
           
            sleep(1)
            motors.backward(60)
            sleep(0.1)
            motors.stop()
            print("left forward ")
            
                              

pygame.quit()                
