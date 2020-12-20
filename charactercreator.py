import random
import tkinter as tk

class PowerGenerator():
        powers=["fireball","ice-blast","void-leap","archery","luck","god's favour","religion","insanity",
                "aggravated assault","bloodlust","love of pain","instant death","swordcraft",
                "predict future","crazy hamborgur","spontanious human combustion"]
        def generatePower(self):

                power = random.choice(self.powers)
                return power

class NameGenerator():
        name_parts=["ree","sheek","ral","som","ta","qui","raak","kor","nour","sha",
                    "ming","fu","shi","na","har","keen","yee","gregory","quentin","III"]

        def generateName(self, max_names):
                random_number_of_names = random.randint(1,max_names)

                yourename = ""
                for index in range(0, random_number_of_names):
                        yourename = yourename+random.choice(self.name_parts)+" "
                return yourename



class ImagePicker():
        image_file_names = ["bart.PNG","telly.PNG","mouse.PNG"]
        def pickImage(self):
                cursedimage = random.choice(self.image_file_names)
                return cursedimage

class RpgCharacter():
        def __init__(self):
                self.strength=random.randint(1,50)
                self.speed=random.randint(1,50)
                self.smarts=random.randint(1,50)
                self.name=NameGenerator().generateName(10)
                self.looks=ImagePicker().pickImage()
                self.power=PowerGenerator().generatePower()
                self.otherpower=PowerGenerator().generatePower()

class DisplayCharacter():
        def __init__(self, root, myguy):

                print("Your name is: ",myguy.name)
                print("Your power is: ",myguy.power)
                print("Your strenth is: ",myguy.strength)
                print("Your speed is: ",myguy.speed)
                print("Your smarts is: ",myguy.smarts)
                print("Your looks is: ",myguy.looks)
            
                cursedimage = tk.PhotoImage(file=myguy.looks)
                pic = tk.Label(root, image=cursedimage).pack()

                lbl = tk.Label(root, text="Your name is: "+myguy.name, font=("Arial Bold", 40)).pack()
                lbl = tk.Label(root, text="Your power is: "+myguy.power, font=("Arial Bold", 30)).pack()
                lbl = tk.Label(root, text="Your other power is: "+myguy.otherpower, font=("Arial Bold", 30)).pack()
                lbl = tk.Label(root, text="Your strength is: "+str(myguy.strength), font=("Arial Bold", 30)).pack()
                lbl = tk.Label(root, text="Your speed is: "+str(myguy.speed), font=("Arial Bold", 30)).pack()
                lbl = tk.Label(root, text="Your smarts is: "+str(myguy.smarts), font=("Arial Bold", 30)).pack()
                root.mainloop()

app=tk.Tk()
DisplayCharacter(app, RpgCharacter())







    


    
