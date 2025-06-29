from ursina import *

print('Starting Ursina FPS Demo...')
try:
    app = Ursina()

    window.title = 'Python FPS Demo'
    window.borderless = False

    ground = Entity(model='plane', scale=(100,1,100), color=color.green, collider='box')
    sky = Sky()

    player = FirstPersonController(
        model='cube',
        color=color.orange,
        origin_y=-.5,
        speed=5,
        jump_height=2,
        position=(0,2,0)
    )

    print('Running app...')
    app.run()
    print('App closed.')
except Exception as e:
    print('An error occurred:', e)
    import traceback
    traceback.print_exc()