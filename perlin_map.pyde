SCALE = 20
w = 1800
h = 2400
flying = 0

recording = False

def setup():
    global cols
    global rows
    size(1024, 768, P3D)
    cols = w / SCALE
    rows = w / SCALE


def draw():
    global flying
    flying -= 0.098
    terrain = []
    j_off = 0
    for j in range(cols):
        new = []
        i_off = flying
        for i in range(rows):
            new.append(map(noise(i_off, j_off), 0, 1, -205, 215))
            i_off += 0.107
        terrain.append(new)
        j_off += 0.107
        
    background(0)
    stroke(255)
    noFill()
    
    translate(width/2, height/2 + 195)
    rotateX(PI/2.4)
    translate(-w/2, -h/2)
    
    for j in range(rows-1):
        beginShape(TRIANGLE_STRIP)
        for i in range(cols):
            vertex(i*SCALE, j*SCALE, terrain[i][j])
            vertex(i*SCALE, (j+1)*SCALE, terrain[i][j+1])
        endShape()

    if recording:
        saveFrame("output/ppp_####.png")
