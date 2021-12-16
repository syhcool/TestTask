# encoding = utf-8
from testpro1.GameProperties import Jinx,Timo
class HeroFactory:
    def create_hero(self,hero):
        if hero == "Timo":
            return Timo()
        elif hero == "Jinx":
            return Jinx()
        else:
            raise Exception("无此英雄")

herofactory = HeroFactory()
jinx = herofactory.create_hero("Jinx")
jinx.fight(1000,150)