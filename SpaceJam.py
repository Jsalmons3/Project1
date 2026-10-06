from direct.showbase.ShowBase import ShowBase

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

    def SetupScene(self):
        self.Universe = self.loader.loadModel("./Assets/Universe/Universe/Universe.x")
        self.Universe.reparentTo(self.render)
        self.Universe.setScale(15000)
        self.Planet1 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet1.reparentTo(self.render)
        self.Planet1.setPos(-600, 5000, 67)
        self.Planet1.setScale(350)
        self.Planet2 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet2.reparentTo(self.render)
        self.Planet2.setPos(400, 5000, 67)
        self.Planet2.setScale(400)
        self.Planet3 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet3.reparentTo(self.render)
        self.Planet3.setPos(1600, 5000, 67)
        self.Planet3.setScale(600)
        self.Planet4 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet4.reparentTo(self.render)
        self.Planet4.setPos(2700, 5000, 67)
        self.Planet4.setScale(200)
        self.Planet5 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet5.reparentTo(self.render)
        self.Planet5.setPos(3400, 5000, 67)
        self.Planet5.setScale(100)
        self.Planet6 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet6.reparentTo(self.render)
        self.Planet6.setPos(4500, 5000, 67)
        self.Planet6.setScale(500)
        self.Spacestation = self.loader.loadModel("./Assets/Space Station/SpaceStation1B/spaceStation.x")
        self.Spacestation.reparentTo(self.render)
        self.Spacestation.setPos(6000, 1000, 67)
        self.Spacestation.setScale(200)
        self.Ship = self.loader.loadModel("./Assets/Spaceships/Dumbledore/Dumbledore.x")
        self.Ship.reparentTo(self.render)
        self.Ship.setPos(0, 0, 100)
        self.Ship.setScale(50)

    def loadTexture(self):
        tex = self.loader.loadTexture("./Assets/Universe/Universe/Universe.jpg")
        self.Universe.setTexture(tex, 1)
        shipTex = self.loader.loadTexture("./Assets/Spaceships/Dumbledore/Dumbledore.jpg")
        self.Ship.setTexture(shipTex, 1)

app = MyApp()
app.SetupScene()
app.run()

#credits: https://www.pinterest.com/47of74/cool-fictional-planets/ Jesse Green - All 6 planets
#credits: https://www.pinterest.com/pin/207024914124205138/ BLINK_SOFT - The universe