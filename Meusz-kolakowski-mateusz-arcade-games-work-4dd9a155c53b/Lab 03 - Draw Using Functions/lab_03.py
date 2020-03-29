import arcade


def draw_a_fish(x,y):
    arcade.draw_ellipse_filled(x,y,100,50,arcade.color.GUPPIE_GREEN)
    arcade.draw_triangle_filled(x-10,y+10,x,y+45,x+20,y+20,arcade.color.GUPPIE_GREEN)
    arcade.draw_triangle_filled(x-70,y-20,x-70,y+20,x-45,y,arcade.color.GUPPIE_GREEN)
def draw_a_torpedo(x,y):
    arcade.draw_rectangle_filled(x,y,100,20,arcade.color.REDWOOD)
    arcade.draw_circle_filled(x+50,y,10,arcade.color.REDWOOD)
    arcade.draw_triangle_filled(x-50,y,x-70,y+15,x-70,y-15,arcade.color.REDWOOD)

def moving_torpedo(delta_time):
    arcade.start_render()
    arcade.draw_rectangle_filled(2500,200,5000,400,arcade.color.BLUE_SAPPHIRE)
    draw_a_fish(150,150)
    draw_a_fish(300,300)
    draw_a_fish(700,80)
    draw_a_torpedo(moving_torpedo.torpedo1_x, 140)
    moving_torpedo.torpedo1_x+=1
def main():
    arcade.open_window(1000, 800, "Arcade")
    arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

    moving_torpedo.torpedo1_x=0
    arcade.schedule(moving_torpedo,0.000000000000001/60)
    arcade.run()

main()