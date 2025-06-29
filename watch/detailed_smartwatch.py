from vpython import *

# Scene setup
scene.title = "Detailed 3D Smartwatch Model"
scene.width = 900
scene.height = 700
scene.background = color.white

# Watch body (main cylinder)
watch_body = cylinder(pos=vector(0,0,0), axis=vector(0,0,0.25), radius=1, color=vector(0.2,0.2,0.2))

# Bezel (slightly larger, thinner ring)
bezel = ring(pos=vector(0,0,0.25), axis=vector(0,0,1), radius=1.05, thickness=0.08, color=color.gray(0.7))

# Watch face (screen)
watch_face = cylinder(pos=vector(0,0,0.25), axis=vector(0,0,0.03), radius=0.92, color=color.black)

# Digital time display (simple)
time_display = text(text="12:45", align='center', depth=0.02, color=color.green, height=0.3,
                    pos=vector(-0.5, -0.15, 0.29))

# Crown (side button)
crown = cylinder(pos=vector(1,0.3,0.13), axis=vector(0.18,0,0), radius=0.11, color=color.red)

# Side button (opposite side)
side_button = cylinder(pos=vector(-1,0.3,0.13), axis=vector(-0.18,0,0), radius=0.08, color=color.gray(0.5))

# Strap (bottom, with rounded ends)
strap1 = box(pos=vector(0,-1.7,0.12), size=vector(0.5,2.2,0.18), color=vector(0.1,0.1,0.5))
strap1_end = cylinder(pos=vector(0,-2.8,0.12), axis=vector(0,0.2,0), radius=0.25, color=vector(0.1,0.1,0.5))

# Strap (top, with rounded ends)
strap2 = box(pos=vector(0,1.7,0.12), size=vector(0.5,2.2,0.18), color=vector(0.1,0.1,0.5))
strap2_end = cylinder(pos=vector(0,2.8,0.12), axis=vector(0,-0.2,0), radius=0.25, color=vector(0.1,0.1,0.5))

# Sensors on the back
sensor1 = cylinder(pos=vector(0.3,0,0), axis=vector(0,0,-0.05), radius=0.12, color=color.green)
sensor2 = cylinder(pos=vector(-0.3,0,0), axis=vector(0,0,-0.05), radius=0.08, color=color.blue)

# Group all parts for rotation
smartwatch = compound([
    watch_body, bezel, watch_face, time_display, crown, side_button,
    strap1, strap1_end, strap2, strap2_end, sensor1, sensor2
])

# Animation loop for rotation
while True:
    rate(60)
    smartwatch.rotate(angle=0.01, axis=vector(0,1,0)) 