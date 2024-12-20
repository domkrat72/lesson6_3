import  random
class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed
    def move(self, dx, dy, dz):
        cord_x = dx * self.speed
        cord_y = dy * self.speed
        cord_z = dz * self.speed
        self._cords[0] = self._cords[0] + cord_x
        self._cords[1] = self._cords[1] + cord_y
        self._cords[2] = self._cords[2] + cord_z
        if self._cords[2]<0:
            print("It's too deep, i can't dive :(")
            # pass
        # else:
        #     self._cords[2] = self._cords[2] + cord_z
    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")
    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print(f'Sorry, i`m peaceful:)')
        elif self._DEGREE_OF_DANGER >= 5:
            print('Be careful, i`m attacking yuo 0_0')

class Bird:
    beak = True
    def lay_eggs(self):
        num_of_eggs = random.randint(1, 4)
        print(f"Here are(is) {random.randint(1, 4)} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        dive_speed = self.speed * 0.5
        dive = abs(dz) * dive_speed
        self._cords[2] = self._cords[2] - dive
class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
    sound = "Click-click-click"
    def __init__(self, speed):
        super().__init__(speed)
    def speak(self):
        print(self.sound)
db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()