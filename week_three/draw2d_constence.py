# Import the functions from the Draw 2-D library
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing

def main():
    scene_width = 800
    scene_height = 500
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    draw_grid(canvas, scene_width, scene_height, 50)
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    finish_drawing(canvas)

def draw_grid(canvas, width, height, interval):
    #draw a vertival line 
    label_y = 15
    for x in range(interval, width,interval):
        draw_line(canvas, x, 0,  x, height )
        draw_text(canvas, x , label_y , f"{x}")

    #draw a horzaontal line 
    label_x = 15
    for y in range(interval, height ,interval):
        draw_line(canvas, 0, y, width, y )
        draw_text(canvas, label_x,y, f"{y}"  )

def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3, scene_width, scene_height, width=0, fill="lightBlue1")
    draw_sun(canvas, 50, 480, 150, 380)
    draw_clouds(canvas, 300, 470, 350, 390, 100, 450, 250, 380, 300, 480, 500, 450, 200, 420, 380, 320 ) 

def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0, scene_width, scene_height / 3, width=0, fill="darkSeaGreen2")
    draw_house(canvas, 100, 100, 350, 250, 100, 250, 220, 375, 350, 250, 200, 170, 250, 100)
    draw_pine_tree(canvas, 550, 150, 250)
    draw_pine_tree(canvas, 450, 50, 150)
    draw_pine_tree(canvas, 400, 90, 150)
    draw_pine_tree(canvas, 700, 110, 200)
    draw_pine_tree(canvas, 750, 20, 180)
    draw_lake(canvas, 550, 50, 650, 130)
    draw_lake(canvas, 500, 140, 600, 50)
    draw_grass(canvas, 680, 100, 682, 110)
    draw_grass(canvas, 650, 100, 655, 110)
    draw_grass(canvas, 490, 100, 492, 110)
    draw_grass(canvas, 550, 30, 552, 40)
    draw_grass(canvas, 550, 30, 552, 40)
    draw_grass(canvas, 600, 20, 602, 30)
    draw_grass(canvas, 700, 40, 702, 50)
    draw_grass(canvas, 50, 60, 52, 70)
    draw_grass(canvas, 70, 100, 72, 110)
    draw_grass(canvas, 15, 120, 17, 130)




def draw_sun(canvas, sun_x, sun_y, sun_x1, sun_y2): 
      draw_oval(canvas, sun_x, sun_y, sun_x1, sun_y2, fill="khaki1") 

def draw_grass(canvas, grass_x1, grass_y1, grass_x2, grass_y2): 
    draw_line(canvas, grass_x1, grass_y1, grass_x2, grass_y2, width=5, fill="forestGreen")

def draw_clouds(canvas, c1_x1, c1_y1, c1_x2, c1_y2, c2_x1, c2_y1, c2_x2, c2_y2, c3_x1, c3_y1, c3_x2, c3_y2, c4_x1, c4_y1, c4_x2, c4_y2 ): 
    draw_oval(canvas, c1_x1, c1_y1, c1_x2, c1_y2, fill="ivory1", outline="ivory1")  
    draw_oval(canvas, c2_x1, c2_y1, c2_x2, c2_y2, fill="ivory1", outline="ivory1")  
    draw_oval(canvas, c3_x1, c3_y1, c3_x2, c3_y2, fill="ivory1", outline="ivory1") 
    draw_oval(canvas, c4_x1, c4_y1, c4_x2, c4_y2, fill="ivory1", outline="ivory1")  
 

def draw_house(canvas, house_x, house_y, house_x1, house_y1, roof_x1, roof_y1, roof_x2, roof_y2, roof_x3, roof_y3, door_x, door_y, door_x1, door_y2): 
    draw_rectangle(canvas, house_x, house_y, house_x1, house_y1, width=5, fill="sienna")
    draw_polygon(canvas, roof_x1, roof_y1, roof_x2, roof_y2, roof_x3, roof_y3, fill = "black" )
    draw_rectangle(canvas, door_x, door_y, door_x1, door_y2, width=5, fill="black")

def draw_lake(canvas, lake_x1, lake_y1, lake_x2, lake_y2): 
    draw_oval(canvas, lake_x1, lake_y1, lake_x2, lake_y2, fill="midnightBlue", outline="midnightBlue")  

def draw_pine_tree(canvas, center_x, bottom, height): 
    #tree trunk 
    trunk_width = height / 10
    trunk_height = height/ 6
    left_trunk = center_x - trunk_width / 2 
    bottom_trunk = bottom 
    right_trunk = center_x + trunk_width / 2 
    trunk_top = bottom + trunk_height
    draw_rectangle(canvas, left_trunk, bottom_trunk, right_trunk, trunk_top, fill = "tan4")

    #draw skirt
    skirt_width = height / 2 
    skirt_left = center_x - skirt_width / 2 
    skirt_bottom = trunk_top
    peak_x = center_x
    peak_y =  bottom + height 
    skirt_right= center_x + skirt_width / 2 
    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, peak_y, skirt_right, skirt_bottom, fill = "forestGreen" )


main()
