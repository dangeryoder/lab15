#########################################
#
#    100pt - Putting it together!
#
#########################################

# Animate the target area to bounce from left to right.
# Add in buttons for movement left, right, up and down
# Add in boundary detection for the edges (don't let the player move off screen)
# Add in collision detection - and STOP the target when you catch it!

from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=480,height=320, background='black')
targetx1 = 200
targety1 = 20
targetx2 = 280
targety2 = 80
target = drawpad.create_rectangle(targetx1,targety1,targetx2,targety2, fill="red")
player = drawpad.create_rectangle(240,240,260,260, fill="white")
direction = 4


class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.up = Button(self.myContainer1)
		self.up.configure(text="Up", background= "green")
		self.up.grid(row=0,column=1)											
		self.up.bind("<Button-1>", self.moveUp)
                
		self.down = Button(self.myContainer1)
		self.down.configure(text="Down", background= "green")
		self.down.grid(row=0,column=2)											
		self.down.bind("<Button-1>", self.moveDown)
		
		self.left = Button(self.myContainer1)
		self.left.configure(text="Left", background= "green")
		self.left.grid(row=0,column=0)											
		self.left.bind("<Button-1>", self.moveLeft)
		
		self.right = Button(self.myContainer1)
		self.right.configure(text="Right", background= "green")
		self.right.grid(row=0,column=3)											
		self.right.bind("<Button-1>", self.moveRight)
		
		# This creates the drawpad - no need to change this 
		drawpad.pack()
		self.animate()

		
	def moveUp(self, event):   
		global player
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player)
		drawpad.move(player,0,-10)
    
        def moveDown(self, event):   
		global player
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player)
                drawpad.move(player,0,10)
                
        def moveRight(self, event):   
		global player
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player)
		drawpad.move(player,10, 0)
                
        def moveLeft(self, event):   
		global player
		global drawpad
		global target
                x1,y1,x2,y2 = drawpad.coords(player)
		drawpad.move(player,-10,0)
    
    
    
        # Animate function that will bounce target left and right, and trigger the collision detection  
	def animate(self):
	    global target
	    global direction
	    global player
	    tx1,ty1,tx2,ty2 = drawpad.coords(target)
	    
	    if tx1 < 0:
	        direction = 4
	    if tx2 > 480:
	        direction = -4
	    drawpad.move(target, direction, 0)
	        
            
            
            #  This will trigger our collision detect function
            didWeHit = self.collisionDetect()
            if (didWeHit == False):
                drawpad.after(5,self.animate)
            else:
                print "Game Over Man!"
                
            # Use the value of didWeHit to create an if statement
            # that determines whether to run drawpad.after(1,self.animate) or not
            
	# Use a function to do our collision detection
	def collisionDetect(self):
                global target
		global drawpad
                global player
                x1, x2, y1, y2 = drawpad.coords(player)
                tx1, tx2, ty1, ty2 = drawpad.coords(target)
                if (tx1 < x1 and tx2 > x2) and (ty1 < y1 and ty2 > y2):
                    return True
                else:
                    return False
                # Do your if statement - remember to return True if successful!                
		
myapp = MyApp(root)

root.mainloop()