###########################
#- CC1-S01 Part Three
#- Reid A. Martin
###########################

#This program draws what appears to be the first person perspective of looking down a really long tunnel


import turtle
t = turtle.Turtle() 
myWin = turtle.Screen()

#radius = 100
t.speed(100) #cranks the turtles speed up bc he is just too slow

def tunnel(radius): 
    if radius >= 5: #runs when the radius is greater than or equal to 10
        t.circle(radius) # draws a circle
        tunnel(radius - 2.5) #runs with the radius being 2.5 units smaller than the last time
        
def main(): #puts the turtle in position (at the bottom of the screen)
    t.up()
    t.right(90)
    t.forward(400)
    t.left(90)
    t.down()
    tunnel(700) #runs the tunnel function
    myWin.exitonclick()
    
main()