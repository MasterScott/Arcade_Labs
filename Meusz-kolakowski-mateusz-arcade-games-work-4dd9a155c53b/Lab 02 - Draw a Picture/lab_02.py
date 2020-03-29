import arcade
def draw_a_fish(x,y):
    arcade.draw_ellipse_filled(x,y,100,50,arcade.color.GUPPIE_GREEN)
    arcade.draw_triangle_filled(x-10,y+10,x,y+45,x+20,y+20,arcade.color.GUPPIE_GREEN)
    arcade.draw_triangle_filled(x-70,y-20,x-70,y+20,x-45,y,arcade.color.GUPPIE_GREEN)
def main():
    arcade.open_window(1000, 800, "Arcade")
    arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
    arcade.start_render()
    arcade.draw_rectangle_filled(2500,200,5000,400,arcade.color.BLUE_SAPPHIRE)
    draw_a_fish(150,150)
    draw_a_fish(300,300)
    draw_a_fish(700,80)
    arcade.finish_render()
    arcade.run()

main()