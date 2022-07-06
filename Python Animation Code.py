
import simplegui

# Global Variables
snow1 = False
snow2 = False
snow3 = False
snow4 = False
snow5 = False
speed = 1
x = 200

#Event Handler
def toggle_snow1():
    global snow1
    snow1 = not snow1
    
def toggle_snow2():
    global snow2
    snow2 = not snow2
    
def toggle_snow3():
    global snow3
    snow3 = not snow3
    
def toggle_snow4():
    global snow4
    snow4 = not snow4
    
def toggle_snow5():
    global snow5
    snow5 = not snow5
    
def draw(canvas):
    if snow1:
            # Text Box
            canvas.draw_polygon([(2, 100), (250, 100), (250, 0), (2, 0)], 8, 'White', 'White')
            canvas.draw_text('The big red snowman had', (10, 20), 20, 'Red')
            canvas.draw_text('no friends and he was ', (10, 39), 20, 'Red')
            canvas.draw_text('very very sad.', (10, 60), 20, 'Red')

            #Big Red Snowman
            canvas.draw_polygon([(400, 300), (450, 300), (450, 350), (400, 350)], 5, 'Red', 'Red')
            canvas.draw_polygon([[375, 350], [480, 350], [480, 430], [375, 430]], 8, 'Red', 'Red')
            canvas.draw_polygon([[355, 490], [499, 490], [499, 400], [355, 400]], 8, 'Red', 'Red')
            canvas.draw_line((319, 374), (370, 359), 4, 'White') # First Arm
            canvas.draw_line((484, 363), (538, 374), 4, 'White') # Second Arm
            canvas.draw_circle((410, 320), 4, 4, 'Black', 'Black') # First Eye
            canvas.draw_circle((440, 320), 4, 4, 'Black', 'Black') # Seond Eye
            canvas.draw_line((406, 339), (445, 339), 4, 'Black') # Mouth
            canvas.draw_circle((425, 370), 4, 4, 'Black', 'Black')
            canvas.draw_circle((425, 390), 4, 4, 'Black', 'Black')
            canvas.draw_polygon([(401, 300), (448, 300), (420, 250)], 10, "Orange", "Orange")
            
            
            # Sun
            canvas.draw_circle((500, 90), 50, 9, 'Yellow', 'Yellow')
                
            # Ground
            canvas.draw_line((0, 500), (600, 500), 12, 'Green')
            canvas.draw_line((0, 510), (600, 510), 12, 'Green')
            for i in range(520, 600):   # 1st For Loop
                canvas.draw_line((0, i), (600, i), 12, '#663300')
                i = i + 10
                
                
    if snow2:
           # Text Box
            canvas.draw_polygon([(2, 100), (250, 100), (250, 0), (2, 0)], 8, 'White', 'White')
            canvas.draw_text('All of a sudden, a white ', (10, 20), 20, 'Red')
            canvas.draw_text('snowman comes over and ', (10, 39), 20, 'Red')
            canvas.draw_text('asks if the red snowman', (10, 60), 20, 'Red')
            canvas.draw_text('wants to play ball.', (10, 80), 20, 'Red')

            #Big Red Snowman
            canvas.draw_polygon([(400, 300), (450, 300), (450, 350), (400, 350)], 5, 'Red', 'Red')
            canvas.draw_polygon([[375, 350], [480, 350], [480, 430], [375, 430]], 8, 'Red', 'Red')
            canvas.draw_polygon([[355, 490], [499, 490], [499, 400], [355, 400]], 8, 'Red', 'Red')
            canvas.draw_line((319, 374), (370, 359), 4, 'White') # First Arm
            canvas.draw_line((484, 363), (538, 374), 4, 'White') # Second Arm
            canvas.draw_circle((410, 320), 4, 4, 'Black', 'Black') # First Eye
            canvas.draw_circle((440, 320), 4, 4, 'Black', 'Black') # Seond Eye
            canvas.draw_line((406, 339), (445, 339), 4, 'Black') # Mouth
            canvas.draw_circle((425, 370), 4, 4, 'Black', 'Black')
            canvas.draw_circle((425, 390), 4, 4, 'Black', 'Black')
            canvas.draw_polygon([(401, 300), (448, 300), (420, 250)], 10, "Orange", "Orange")
            
            # White Snowman
            canvas.draw_circle((100, 320), 25, 12, 'White', 'White')
            canvas.draw_circle((100, 380), 39, 12, 'White', 'White')
            canvas.draw_circle((100, 440), 50, 12, 'White', 'White')
            canvas.draw_circle((88, 315), 4, 4, 'Black', 'Black') # First Eye
            canvas.draw_circle((110, 315), 4, 4, 'Black', 'Black') # Second Eye
            canvas.draw_line((84, 335), (115, 335), 4, 'Red') # Mouth
            canvas.draw_line((140, 360), (187, 345), 4, 'White') # First Arm
            canvas.draw_line((140, 369), (190, 369), 4, 'White') # Second Arm 
            canvas.draw_circle((199, 360), 19, 12, 'Blue', 'Blue')
                
            # Sun
            canvas.draw_circle((500, 90), 50, 9, 'Yellow', 'Yellow')
                
            # Ground
            canvas.draw_line((0, 500), (600, 500), 12, 'Green')
            canvas.draw_line((0, 510), (600, 510), 12, 'Green')
            for i in range(520, 600):    # Second For Loop
                canvas.draw_line((0, i), (600, i), 12, '#663300')
                i = i + 10
                
    if snow3:
             # Text Box
            canvas.draw_polygon([(2, 100), (250, 100), (250, 0), (2, 0)], 8, 'White', 'White')
            canvas.draw_text('The snowmen begin to play', (10, 20), 20, 'Red')
            canvas.draw_text('ball. ', (10, 39), 20, 'Red')
            

            #Big Red Snowman
            canvas.draw_polygon([(400, 300), (450, 300), (450, 350), (400, 350)], 5, 'Red', 'Red')
            canvas.draw_polygon([[375, 350], [480, 350], [480, 430], [375, 430]], 8, 'Red', 'Red')
            canvas.draw_polygon([[355, 490], [499, 490], [499, 400], [355, 400]], 8, 'Red', 'Red')
            canvas.draw_line((319, 374), (370, 359), 4, 'White') # First Arm
            canvas.draw_line((484, 363), (538, 374), 4, 'White') # Second Arm
            canvas.draw_circle((410, 320), 4, 4, 'Black', 'Black') # First Eye
            canvas.draw_circle((440, 320), 4, 4, 'Black', 'Black') # Seond Eye
            canvas.draw_line((406, 339), (445, 339), 4, 'Black') # Mouth
            canvas.draw_circle((425, 370), 4, 4, 'Black', 'Black')
            canvas.draw_circle((425, 390), 4, 4, 'Black', 'Black')
            canvas.draw_polygon([(401, 300), (448, 300), (420, 250)], 10, "Orange", "Orange")
            
            # White Snowman
            canvas.draw_circle((100, 320), 25, 12, 'White', 'White')
            canvas.draw_circle((100, 380), 39, 12, 'White', 'White')
            canvas.draw_circle((100, 440), 50, 12, 'White', 'White')
            canvas.draw_circle((88, 315), 4, 4, 'Black', 'Black') # First Eye
            canvas.draw_circle((110, 315), 4, 4, 'Black', 'Black') # Second Eye
            canvas.draw_line((84, 335), (115, 335), 4, 'Red') # Mouth
            canvas.draw_line((140, 360), (187, 345), 4, 'White') # First Arm
            canvas.draw_line((140, 369), (190, 369), 4, 'White') # Second Arm
            global speed 
            global x
            if (x < 199 or x > 319):     # ANIMATION
                speed = speed * -1 
            canvas.draw_circle((x, 360), 19, 12, 'Blue', 'Blue')
            x = x + speed
                
            # Sun
            canvas.draw_circle((500, 90), 50, 9, 'Yellow', 'Yellow')
                
            # Ground
            canvas.draw_line((0, 500), (600, 500), 12, 'Green')
            canvas.draw_line((0, 510), (600, 510), 12, 'Green')
            for i in range(520, 600):
                canvas.draw_line((0, i), (600, i), 12, '#663300')
                i = i + 10
                
    if snow4:
            # Text Box
            canvas.draw_polygon([(2, 100), (250, 100), (250, 0), (2, 0)], 8, 'White', 'White')
            canvas.draw_text('The big red snowman was', (10, 20), 20, 'Red')
            canvas.draw_text('now very happy he had made ', (10, 39), 20, 'Red')
            canvas.draw_text('a new friend. ', (10, 60), 20, 'Red')
            
            #Big Red Snowman
            canvas.draw_polygon([(400, 300), (450, 300), (450, 350), (400, 350)], 5, 'Red', 'Red')
            canvas.draw_polygon([[375, 350], [480, 350], [480, 430], [375, 430]], 8, 'Red', 'Red')
            canvas.draw_polygon([[355, 490], [499, 490], [499, 400], [355, 400]], 8, 'Red', 'Red')
            canvas.draw_line((319, 334), (370, 359), 4, 'White') # First Arm
            canvas.draw_line((484, 363), (538, 334), 4, 'White') # Second Arm
            canvas.draw_circle((410, 320), 4, 4, 'Yellow', 'Yellow') # First Eye
            canvas.draw_circle((440, 320), 4, 4, 'Yellow', 'Yellow') # Seond Eye
            canvas.draw_line((406, 339), (445, 339), 4, 'Yellow') # Mouth
            canvas.draw_circle((425, 370), 4, 4, 'Yellow', 'Yellow')
            canvas.draw_circle((425, 390), 4, 4, 'Yellow', 'Yellow')
            canvas.draw_polygon([(401, 300), (448, 300), (420, 250)], 10, "Orange", "Orange")
            
            # Sun
            canvas.draw_circle((500, 90), 50, 9, 'Yellow', 'Yellow')
            
            # Ground
            canvas.draw_line((0, 500), (600, 500), 12, 'Green')
            canvas.draw_line((0, 510), (600, 510), 12, 'Green')
            for i in range(520, 600):  # Fourth For Loop
                canvas.draw_line((0, i), (600, i), 12, '#663300')
                i = i + 10
                
    if snow5:
            canvas.draw_text('The End', (147, 300), 89, 'Blue')
            
            
            
                
frame = simplegui.create_frame("Story", 600, 600) 
frame.set_draw_handler(draw)
frame.add_button("Part 1", toggle_snow1, 100)
frame.add_button("Part 2", toggle_snow2, 100)
frame.add_button("Part 3", toggle_snow3, 100)
frame.add_button("Part 4", toggle_snow4, 100)
frame.add_button("Part 5", toggle_snow5, 100)
frame.start()

