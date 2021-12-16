# encoding = utf-8
"""
1. ⼀个回合制游戏，有两个英雄，分别以两个类进⾏定义。
分别是Timo和Jinx。每个英雄都有 hp 属性和 power属性，hp 代表⾎量，power 代表攻击⼒
2. 每个英雄都有⼀个 fight ⽅法， fight ⽅法需要传⼊“enemy_hp”（敌⼈的⾎量），“enemy_power”（敌⼈的攻击⼒）两个参数。
需要计算对打一轮过后双方的最终血量，
英雄最终的⾎量 = 英雄hp属性-敌⼈的攻击⼒enemy_power
敌⼈最终的⾎量 = 敌⼈的⾎量enemy_hp-英雄的power属性
3. 对⽐英雄最终的⾎量和敌⼈最终的⾎量，⾎量剩余多的⼈获胜。如果英雄赢了打印 “英雄获胜”，如果敌⼈赢了，打印“敌⼈获胜”
4. 使用继承、简单工厂方法等各种方式优化你的代码"""
class Hero:
    hero_hp = 0
    hero_power = 0
    hero_round = 1

    def fight(self,enemy_hp,enemy_power):
        while True:

            self.hero_hp = self.hero_hp - enemy_power
            enemy_hp = enemy_hp - self.hero_power
            print(f"第{self.hero_round}回合，英雄剩余血量{self.hero_hp},敌人剩余血量{enemy_hp}")
            self.hero_round += 1

            if self.hero_hp <= 0:
                print("敌⼈获胜")
                break
            elif enemy_hp <= 0:
                print("英雄获胜")
                break


class Jinx(Hero):
    hero_hp = 1100
    hero_power = 200
class Timo(Hero):
    hero_hp = 1000
    hero_power = 250

