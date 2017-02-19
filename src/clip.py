import pyglet
import pyautogui
import main2

class Assassin(pyglet.sprite.Sprite):
    def __init__(self, batch, img):
        pyglet.sprite.Sprite.__init__(self, img, x = 50, y = 30)

    def stand(self):
        #self.image = pyglet.image.load("clippy1.gif")
        self.image = pyglet.resource.animation("giphy.gif")
        return self

    def move(self):
        #self.image = pyglet.image.load('giphy.gif')
        self.image = pyglet.resource.animation('clippy1.gif')
        return self

class Game(pyglet.window.Window):
    def __init__(self):
        pyglet.window.Window.__init__(self, width = 400, height = 400)
        self.batch_draw = pyglet.graphics.Batch()
        self.player = Assassin(batch = self.batch_draw, img = pyglet.resource.animation("giphy.gif"))
        self.keys_held = []
        self.schedule = pyglet.clock.schedule_interval(func = self.update, interval = 1/60.)

    def on_draw(self):
        self.clear()
        self.batch_draw.draw()
        self.player.draw()
        main2.startupFunction()


    def on_key_press(self, symbol, modifiers):
        self.keys_held.append(symbol)
        if symbol == pyglet.window.key.RIGHT:
            self.player = self.player.move()
         #   print "The 'RIGHT' key was pressed"

    def on_key_release(self, symbol, modifiers):
        self.keys_held.pop(self.keys_held.index(symbol))
        self.player = self.player.stand()
        #print "The 'RIGHT' key was released"

    def update(self, interval):
       # if pyglet.window.key.RIGHT in self.keys_held:
            #self.player.x += 50 * interval
        main2.waitForInput()
        pass
    def run(self):
        while(1):
            pyautogui.keyDown('right')
            print "Right Pressed"


window = Game()
pyglet.app.run()
