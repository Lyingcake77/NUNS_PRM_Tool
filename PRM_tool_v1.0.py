import Tkinter
import Tkinter
from Tkinter import *
from ScrolledText import *
import tkFileDialog
import tkMessageBox
import binascii
import sys, os
import re
import string
class loading:
    def __init__(self, atkex,basea,baseb):
        self.atkex=atkex
        self.basea=basea
        self.baseb=baseb
    def base(self):
        print 'initilizing...'
        self.circle_atk=Tk(className="Base Data section")
        filly=('times', 10, 'bold')

        #atkex=basefile
        

        self.x=0
        self.y=0
        self.enlisting=[]


        # section 1
        self.atk=Entry(self.circle_atk)
        self.anim=Entry(self.circle_atk)

        self.direction=Entry(self.circle_atk)
        self.length=Entry(self.circle_atk)
        self.timer=Entry(self.circle_atk)
        self.preanm=Entry(self.circle_atk)
        self.nxtanim=Entry(self.circle_atk)
        self.nxtdmg=Entry(self.circle_atk)

        self.mvmtamt=Entry(self.circle_atk, )
        self.dmgamt=Entry(self.circle_atk, )


        # amount of items(already added)
        #frame when animation starts (wip)
        self.frame=Entry(self.circle_atk)
        #load type(usualy 3, wip)
        self.loadtype=Entry(self.circle_atk)
        #cloth value(wip)
        self.cloth=Entry(self.circle_atk)
        #face value(wip)
        self.face=Entry(self.circle_atk)
        #FFFF FFFF FFFF section?
        #buff/ debuff(wip)
        self.buff=Entry(self.circle_atk)
        #affects you/ enemy(wip)
        self.affect=Entry(self.circle_atk)
        #linking code conditions(wip)
        self.prevdata=Entry(self.circle_atk)
        self.linnkdata=Entry(self.circle_atk)
        #time before unable to play the next animation(wip)
        self.nxtlock=Entry(self.circle_atk)

        self.chh=0
        self.che=IntVar()
        self.checkbox=Checkbutton(self.circle_atk, text="check if you want to add the new PL_ANM \nto the end of the section check this box\n otherwise it will be in the beggining of the section", variable=self.che, command=self.cb)



        self.atk.insert(0,'PL_ANM_XXX')
        self.anim.insert(0,'#XXXNNN##')
        self.direction.insert(0,'01')
        self.length.insert(0,'0000')
        self.timer.insert(0,'0000')
        self.preanm.insert(0,'PL_ANM_ANY')
        self.nxtanim.insert(0,'PL_ANM_XXX')
        self.nxtdmg.insert(0,'PL_ANM_XXX_DMG')

        self.mvmtamt.insert(0,'0')
        self.dmgamt.insert(0,'0')



        self.frame.insert(0,'00')
        self.loadtype.insert(0,'03')
        self.cloth.insert(0,'00')
        self.face.insert(0,'00')
        self.buff.insert(0,'FFFF')
        self.affect.insert(0,'FFFF')

        self.prevdata.insert(0,'0000')
        self.linnkdata.insert(0,'00')
        self.nxtlock.insert(0,'0000')
        #hitbox, hitbox size, hitbox timer, damage_id,  vertical distance, horizontal distance, damage, number of hits, impact/effect, sound, time freeze, other


        
        self.atkl=Label(self.circle_atk, text="which PL_ANM_ are you makeing?")
        self.animl=Label(self.circle_atk, text="which animation?")

        self.directionl=Label(self.circle_atk, text="directional direction")
        self.lengthl=Label(self.circle_atk, text="animation length")
        self.timerl=Label(self.circle_atk, text="condition for the next animation link")
        self.preanml=Label(self.circle_atk, text="previous animation")
        self.nxtaniml=Label(self.circle_atk, text="next animation")
        self.nxtdmgl=Label(self.circle_atk, text="next animation _DMG")

        self.mvmtamtl=Label(self.circle_atk,text='how many movement sections will you add?')
        self.dmgamtl=Label(self.circle_atk, text="how many damage_id's will you have?")
        

        self.framel=Label(self.circle_atk, text="Frame when animation starts")               
        self.loadtypel=Label(self.circle_atk, text="load type (usualy 3)")
        self.clothl=Label(self.circle_atk, text="cloth value")
        self.facel=Label(self.circle_atk, text="face value")
        #FFFF FFFF FFFF section?
        self.buffl=Label(self.circle_atk, text="buff and debuff value")
        self.affectl=Label(self.circle_atk, text="value that affects you/ the enemy")
        self.prevdatal=Label(self.circle_atk, text='previouse animation conditions')
        self.linnkdatal=Label(self.circle_atk, text="previuse link conditions")
        self.nxtlockl=Label(self.circle_atk, text="time before you can't use the next animation")




        self.atkl.config(font=filly)
        self.atkl.grid(row=0, column=1)
        self.atk.grid(row=1, column=1)

        self.animl.config(font=filly)
        self.animl.grid(row=2, column=1)
        self.anim.grid(row=3, column=1)


        self.directionl.config(font=filly)
        self.directionl.grid(row=4, column=1)
        self.direction.grid(row=5, column=1)

        self.lengthl.config(font=filly)
        self.lengthl.grid(row=6, column=1)
        self.length.grid(row=7, column=1)

        self.timerl.config(font=filly)
        self.timerl.grid(row=8, column=1)
        self.timer.grid(row=9, column=1)

        self.preanml.config(font=filly)
        self.preanml.grid(row=10, column=1)
        self.preanm.grid(row=11, column=1)

        self.nxtaniml.config(font=filly)
        self.nxtaniml.grid(row=12, column=1)
        self.nxtanim.grid(row=13, column=1)

        self.nxtdmgl.config(font=filly)
        self.nxtdmgl.grid(row=14, column=1)
        self.nxtdmg.grid(row=15, column=1)


        self.mvmtamtl.config(font=filly)
        self.mvmtamtl.grid(row=16, column=1)
        self.mvmtamt.grid(row=17, column=1)

        self.dmgamtl.config(font=filly)
        self.dmgamtl.grid(row=18, column=1)
        self.dmgamt.grid(row=19, column=1)




        self.framel.config(font=filly)
        self.framel.grid(row=0, column=2)
        self.frame.grid(row=1, column=2)

        self.loadtypel.config(font=filly)
        self.loadtypel.grid(row=2, column=2)
        self.loadtype.grid(row=3, column=2)

        self.clothl.config(font=filly)
        self.clothl.grid(row=4, column=2)
        self.cloth.grid(row=5, column=2)

        self.facel.config(font=filly)
        self.facel.grid(row=6, column=2)
        self.face.grid(row=7, column=2)
        
        self.buffl.config(font=filly)
        self.buffl.grid(row=8, column=2)
        self.buff.grid(row=9, column=2)

        self.affectl.config(font=filly)
        self.affectl.grid(row=10, column=2)
        self.affect.grid(row=11, column=2)

        self.prevdatal.config(font=filly)
        self.prevdatal.grid(row=12, column=2)
        self.prevdata.grid(row=13, column=2)

        self.linnkdatal.config(font=filly)
        self.linnkdatal.grid(row=14, column=2)
        self.linnkdata.grid(row=15, column=2)

        self.nxtlockl.config(font=filly)
        self.nxtlockl.grid(row=16, column=2)
        self.nxtlock.grid(row=17, column=2)

        self.checkbox.grid(row=90, column=1)

        self.buttonatk4 = Button(self.circle_atk, text="next", command=self.baseget)
        self.buttonatk4.grid(row=101, column=1)
    def cb(self):
        self.chh=1

    def baseget(self):
        print 'receiving information...'
        
        temptotal=''
        
        if len(binascii.hexlify(self.atk.get())) < 64:
            templen=64-len(binascii.hexlify(self.atk.get()))
            temptotal=binascii.hexlify(self.atk.get())+('0'*templen)
        elif len(binascii.hexlify(self.atk.get())) == 64:
            temptotal=binascii.hexlify(self.atk.get())
        else:
            print 'error animation'
        

        if len(binascii.hexlify(self.anim.get())) < 96:
            templen=96-len(binascii.hexlify(self.anim.get()))
            temptotal=temptotal+binascii.hexlify(self.anim.get())+('0'*templen)
        elif len(binascii.hexlify(self.anim.get())) == 96:
            temptotal=temptotal+binascii.hexlify(self.anim.get())
        else:
            print 'error cmb'

        #temptotal=temptotal+('00'*36)
        num=hex(int(self.mvmtamt.get())+int(self.dmgamt.get()))
        num=num[2:]
        if len(num)%2!=0:
            num='0'+num
        
        
        j='FFFF'


        temptotal= temptotal+num+('00'*3)+self.frame.get()+'00'+self.loadtype.get()+('00')+self.cloth.get()+'00'+self.face.get()+('00'*3)+'00'+'00'+'00'+'00'+(self.affect.get()+self.buff.get()+self.affect.get())+self.direction.get()+('00')+self.prevdata.get()+self.linnkdata.get()+'00'+self.length.get()+self.timer.get()+self.nxtlock.get()
        

        if len(binascii.hexlify(self.preanm.get())) < 64:
            templen=64-len(binascii.hexlify(self.preanm.get()))
            temptotal=temptotal+binascii.hexlify(self.preanm.get())+('0'*templen)
        elif len(binascii.hexlify(self.preanm.get())) == 64:
            temptotal=temptotal+binascii.hexlify(self.preanm.get())
        else:
            print 'error prev'


        if len(binascii.hexlify(self.nxtanim.get())) < 64:
            templen=64-len(binascii.hexlify(self.nxtanim.get()))
            temptotal=temptotal+binascii.hexlify(self.nxtanim.get())+('0'*templen)
        elif len(binascii.hexlify(self.nxtanim.get())) == 64:
            temptotal=temptotal+binascii.hexlify(self.nxtanim.get())
        else:
            print 'error next'

        if len(binascii.hexlify(self.nxtdmg.get())) < 64:
            templen=64-len(binascii.hexlify(self.nxtdmg.get()))
            temptotal=temptotal+binascii.hexlify(self.nxtdmg.get())+('0'*templen)
        elif len(binascii.hexlify(self.nxtdmg.get())) == 64:
            temptotal=temptotal+binascii.hexlify(self.nxtdmg.get())
        else:
            print 'error next dmg'

        

        #'00'*424
        self.enlisting.append(temptotal)
        self.buttonatk4.destroy()
        self.next()

    

    def move(self):
        print 'initilizing the movement...'
        filly=('times', 10, 'bold')
        self.movement=Tk(className="movement section")
        
        self.mtxt=Entry(self.movement)
        self.mff=Entry(self.movement)
        self.mfb=Entry(self.movement)
        self.mval1=Entry(self.movement)
        self.mval2=Entry(self.movement )
        self.mval3=Entry(self.movement)
        self.mval4=Entry(self.movement)
        
    
        
        self.mff.insert(0,'0100')
        self.mfb.insert(0,'2400')
        self.mval1.insert(0,'1000')
        self.mval2.insert(0,'0001')
        self.mval3.insert(0,'0001')
        self.mval4.insert(0,'0000803F')

        

        #hitbox, hitbox size, hitbox timer, damage_id,  vertical distance, horizontal distance, damage, number of hits, impact/effect, sound, time freeze, other


        self.mtxtl=Label(self.movement, text="text")
        self.mffl=Label(self.movement, text="frame function start time")
        self.mfbl=Label(self.movement, text="function byte")
        self.mval1l=Label(self.movement, text="first value")
        self.mval2l=Label(self.movement, text="second value")
        self.mval3l=Label(self.movement, text="third value")
        self.mval4l=Label(self.movement, text="fourth value")


             
        

        self.mtxtl.config(font=filly)
        self.mtxtl.grid(row=0, column=1)
        self.mtxt.grid(row=1, column=1)

        self.mffl.config(font=filly)
        self.mffl.grid(row=2, column=1)
        self.mff.grid(row=3, column=1)

        self.mfbl.config(font=filly)
        self.mfbl.grid(row=4, column=1)
        self.mfb.grid(row=5, column=1)

        self.mval1l.config(font=filly)
        self.mval1l.grid(row=6, column=1)
        self.mval1.grid(row=7, column=1)

        self.mval2l.config(font=filly)
        self.mval2l.grid(row=8, column=1)
        self.mval2.grid(row=9, column=1)

        self.mval3l.config(font=filly)
        self.mval3l.grid(row=10, column=1)
        self.mval3.grid(row=11, column=1)

        self.mval4l.config(font=filly)
        self.mval4l.grid(row=12, column=1)
        self.mval4.grid(row=13, column=1)


        self.x+=1
        

        self.buttonatk5 = Button(self.movement, text="next", command=self.moveget)
        self.buttonatk5.grid(row=101, column=1)

        #atk00+,atk00_s,atk00_n,atk00_l,atk00_e,dmg00
    def moveget(self):
        print 'receiving information...'
        
        self.mtxt.get()
        self.mff.get()
        self.mfb.get()
        self.mval1.get()
        self.mval2.get()
        self.mval3.get()
        self.mval4.get()

        temptotal=''
        if len(binascii.hexlify(self.mtxt.get())) < 64:
            templen=64-len(binascii.hexlify(self.mtxt.get()))
            temptotal=binascii.hexlify(self.mtxt.get())+('0'*templen)
        elif len(binascii.hexlify(self.mtxt.get())) == 64:
            temptotal=binascii.hexlify(self.mtxt.get())
        else:
            print 'error text'
        temptotal=temptotal+self.mff.get()+self.mfb.get()+self.mval1.get()+self.mval2.get()+self.mval3.get()+'0000'+self.mval4.get()+('00'*16)
        
        self.enlisting.append(temptotal)
        
        self.movement.destroy()

        self.next()

    def dmg(self):
        print 'initilizing damage section...'
        filly=('times', 10, 'bold')
        self.damage=Tk(className="Damage section")
        
        self.hitbox=Entry(self.damage)
        self.hittime=Entry(self.damage)
        self.hitsize=Entry(self.damage)
        self.hitextra=Entry(self.damage)

        self.damage_id=Entry(self.damage)
        self.damage_eff=Entry(self.damage)
        self.damage_type=Entry(self.damage)
        self.damage_dmg=Entry(self.damage)
        self.damage_some=Entry(self.damage)
        self.damage_hor=Entry(self.damage)
        self.damage_ver=Entry(self.damage)
        self.damage_hits=Entry(self.damage)
        self.damage_time=Entry(self.damage)
        
        self.damage_bonus=Entry(self.damage)


        
        self.hitbox.insert(0,"#XXX00t0 r hand")
        self.hittime.insert(0,"00")
        self.hitsize.insert(0,"00")
        self.hitextra.insert(0,"D1")

        self.damage_id.insert(0,"DAMAGE_ID_")
        self.damage_eff.insert(0,"00")
        self.damage_type.insert(0,"FFFF")
        self.damage_dmg.insert(0,"803F")
        self.damage_some.insert(0,"80BF")
        self.damage_hor.insert(0,"803F")
        self.damage_ver.insert(0,"803F")
        self.damage_hits.insert(0,"01")
        self.damage_time.insert(0,"0000")

        self.damage_bonus.insert(0,'00')

        #self.damage_6=Entry(self.damage)

        #hitbox, hitbox size, hitbox timer, damage_id,  vertical distance, horizontal distance, damage, number of hits, impact/effect, sound, time freeze, other

        self.hitboxl=Label(self.damage, text="hitbox")
        self.hittimel=Label(self.damage, text="hitbox timing")
        self.hitsizel=Label(self.damage, text="hitbox size")
        self.hitextral=Label(self.damage, text="hitbox extra (avoid touching)")

        self.damage_idl=Label(self.damage, text="damage_id")
        self.damage_effl=Label(self.damage, text="visual effect")
        self.damage_typel=Label(self.damage, text="damage type")
        self.damage_dmgl=Label(self.damage, text="damage")
        self.damage_somel=Label(self.damage, text="not sure")
        self.damage_horl=Label(self.damage, text="horizantal push")
        self.damage_verl=Label(self.damage, text="vertical push")
        self.damage_hitsl=Label(self.damage, text="max amount of hits")
        self.damage_timel=Label(self.damage, text="time delay")
        self.damage_bonusl=Label(self.damage, text="bonus effect")


        self.hitboxl.config(font=filly)
        self.hitboxl.grid(row=0, column=1)
        self.hitboxl.grid(row=1, column=1)

        self.hitboxl.config(font=filly)
        self.hitboxl.grid(row=2, column=1)
        self.hitbox.grid(row=3, column=1)

        self.hittimel.config(font=filly)
        self.hittimel.grid(row=4, column=1)
        self.hittime.grid(row=5, column=1)

        self.hitsizel.config(font=filly)
        self.hitsizel.grid(row=6, column=1)
        self.hitsize.grid(row=7, column=1)

        self.hitextral.config(font=filly)
        self.hitextral.grid(row=8, column=1)
        self.hitextra.grid(row=9, column=1)

        self.damage_idl.config(font=filly)
        self.damage_idl.grid(row=10, column=1)
        self.damage_id.grid(row=11, column=1)

        self.damage_effl.config(font=filly)
        self.damage_effl.grid(row=12, column=1)
        self.damage_eff.grid(row=13, column=1)


        self.damage_typel.config(font=filly)
        self.damage_typel.grid(row=14, column=1)
        self.damage_type.grid(row=15, column=1)


        self.damage_dmgl.config(font=filly)
        self.damage_dmgl.grid(row=16, column=1)
        self.damage_dmg.grid(row=17, column=1)


        self.damage_somel.config(font=filly)
        self.damage_somel.grid(row=18, column=1)
        self.damage_some.grid(row=19, column=1)


        self.damage_horl.config(font=filly)
        self.damage_horl.grid(row=20, column=1)
        self.damage_hor.grid(row=21, column=1)


        self.damage_verl.config(font=filly)
        self.damage_verl.grid(row=22, column=1)
        self.damage_ver.grid(row=23, column=1)


        self.damage_hitsl.config(font=filly)
        self.damage_hitsl.grid(row=24, column=1)
        self.damage_hits.grid(row=25, column=1)


        self.damage_timel.config(font=filly)
        self.damage_timel.grid(row=26, column=1)
        self.damage_time.grid(row=27, column=1)

        self.damage_bonusl.config(font=filly)
        self.damage_bonusl.grid(row=28, column=1)
        self.damage_bonus.grid(row=29, column=1)

        self.y+=1

        self.buttonatk6 = Button(self.damage, text="next", command=self.dmgget)
        self.buttonatk6.grid(row=101, column=1)
        
    def dmgget(self):
        print 'receiving information...'
        temptotal=''
        if len(binascii.hexlify(self.hitbox.get())) < 64:
            templen=64-len(binascii.hexlify(self.hitbox.get()))
            temptotal=binascii.hexlify(self.hitbox.get())+('0'*templen)
        elif len(binascii.hexlify(self.hitbox.get())) == 64:
            temptotal=binascii.hexlify(self.hitbox.get())
        else:
            print 'error hitbox'
        temptotal=temptotal+self.hittime.get()+'00'+self.hitextra.get()+'00'+self.hitsize.get()+('00'*27)

        if len(binascii.hexlify(self.damage_id.get())) <128:
            templen=128-len(binascii.hexlify(self.damage_id.get()))
            temptotal=temptotal+(binascii.hexlify(self.damage_id.get())+('0'*templen))
        elif len(binascii.hexlify(self.damage_id.get())) ==128:
            temptotal=temptotal+binascii.hexlify(self.damage_id.get())
        else:
            print 'error damage id '
        temptotal=temptotal+'0000'+self.damage_eff.get()+'00'+self.damage_type.get()+self.damage_bonus.get() +'000000'+self.damage_dmg.get()+'0000'+self.damage_some.get()+'0000'+self.damage_hor.get()+'0000'+self.damage_ver.get()+self.damage_hits.get()+'00'+self.damage_time.get()+'00000000'
        
        self.enlisting.append(temptotal)
        self.damage.destroy()
        self.next()

    def compyle(self):
        print 'compiling... '
        self.k=''
        for i in self.enlisting:
            self.k=self.k+i
        self.merge()
    def next(self):
        print 'next function...'
        if self.x < int(self.mvmtamt.get()):
            self.move()

        elif self.y < int(self.dmgamt.get()):
            self.dmg()
        else:
            self.compyle()

    def merge(self):
        print 'fixing, merging, and writing...'
        temp=self.atkex
        a=temp.find(binascii.hexlify('PL_ANM_ATK'))
        
        if self.chh == 0:
            print 'a'
            newtemp=temp[:a]+self.k+temp[a:]
        elif self.chh == 1:
            print 'b'
            newtemp=temp[:a]+temp[a:]+self.k
        
        
        num1=int(newtemp[:8], 16)+(len(self.k)/2)
        num2=num1-4
        num3=int(newtemp[128:130], 16) + 1


        num1=hex(num1)[2:]
        num2=hex(num2)[2:]
        num3=hex(num3)[2:]

        if len(num1)%2!=0:
            num1='0'+num1
        if len(num1)!=8:
            t=8-len(num1)
            num1=('0'*t)+num1
        

        if len(num2)%2!=0:
            num2='0'+num2
        if len(num2)!=8:
            t=8-len(num2)
            num2=('0'*t)+num2

        if len(num3)%2!=0:
            num3='0'+num3
        

        newtemp[:8]
        newtemp=num1+newtemp[8:24]+num2+newtemp[32:128]+num3+newtemp[130:]

        self.atkex=newtemp
        self.circle_atk.destroy()
        self.ask()
    def saving(self):

        file = tkFileDialog.asksaveasfile(mode='wb')
        if file != None:
            file.write(binascii.unhexlify(self.basea+self.atkex+self.baseb))
            #file.write(binascii.unhexlify(newtemp))
            file.close()
        
        
        
    def ask(self):
        
        self.asker=Tk(className="A serious Question")
        self.Question=Label(self.asker, text="Do you want to make another PL_ANM or finish and save? ")
        self.Question.grid(row=0,column=0)

        butbut= Button(self.asker, text="Add another", command=self.live)
        butbut1= Button(self.asker, text="Compile and save", command=self.die)
        
        butbut.grid(row=1, column=0)
        butbut1.grid(row=2, column=0)
    def live(self):
        self.asker.destroy()
        print 'k'
        self.base()
        
        
        
    def die(self):
        self.asker.destroy()
        self.saving()
        print 'mkay'
        master.destroy()

# tex editor
master = Tkinter.Tk(className=" Storm 4 Mod Tool ")
#root = Tkinter.Tk(className=" Storm 4 Hex Editor ")
#textPad = ScrolledText(root, width=32, height=80)
#hexpad = ScrolledText(root, width=16, height=80)

def open_command():
    file = tkFileDialog.askopenfile(parent=master,mode='rb',title='Select a file')
    if file != None:
        contents = file.read()

        global hexfile
        hexfile=binascii.hexlify(contents)

        file.close()

def save_command(self):
    file = tkFileDialog.asksaveasfile(mode='wb')
    if file != None:
        # slice off the last character from get, as an extra return is added

        data = self
        
        #data = string.replace(data, '\r\n', '\r')
        #data = string.replace(data, '\r', '\n')
        #data = re.sub("\r(?!\n)|(?<!\r)\n", "\r\n", data)
        file.write(data)
        file.close()

def exit_command():
    if tkMessageBox.askokcancel("Quit", "It's faster to quite via the close button?"):
        master.destroy()

def about_command():
    label = tkMessageBox.showinfo("About", "Just Another TextPad \n Copyright \n No rights left to reserve")


def dummy():
    global hexfile
    master.destroy()
    master.mainloop()
    movement.destroy()
    hexfile=""
    print "you are not useing the file anymore"

menu = Menu(master)
master.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
#filemenu.add_command(label="New", command=dummy)
filemenu.add_command(label="Open...", command=open_command)
#filemenu.add_command(label="Save", command=save_command)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_command)
helpmenu = Menu(menu)
#menu.add_cascade(label="Help", menu=helpmenu)
#helpmenu.add_command(label="About...", command=about_command)


# mod tool start
#master = Tk(className=" Storm 4 Mod Tool ")

var = StringVar(master)
var.set("what section would you like to edit?") # default value

w = OptionMenu(master, var,"base", "awakening")
#to work on at  a later date: "jutsu","projectiles","ultimate"
w.pack()
def versection():
    ver="ver0.00"
    hexver=binascii.hexlify(ver)

    global awaver
    global basever
    global jutsuver
    global ultver
    global projver
    global zerobyte


    zerobyte=hexfile[8:10]
    awaver=hexfile.find(hexver)
    basever=(hexfile[awaver+16:].find(hexver))
    jutsuver=(hexfile[(basever+16+awaver+16):].find(hexver))
    ultver=(hexfile[(basever+16+awaver+16+jutsuver+16):].find(hexver))
    projver=""

def awakening():
    #movement, square attacks, circle attacks, tilt attacks, grab attacks, air attacks, animations, awakening action
    awakez=StringVar(master)
    awakez.set("what would you like to edit in the awakening section?") # default value
    
    a = OptionMenu(master, awakez, "movement", "add a PRM")
    # extra: "Square attack", "circle attack", "air attack", "tilt attack","grab attack", "awakening action"
    a.pack()

    basefile=hexfile[(awaver-32):basever+awaver-32-16]
    basea=hexfile[:awaver-32]
    baseb=hexfile[basever+awaver-32-16:]

    '''
    basefile=hexfile[basever+awaver-16:jutsuver+basever+awaver]

    basea=hexfile[:basever+awaver-16]
    baseb=hexfile[jutsuver+basever+awaver:]
    '''

    def movement():
        #nut,run1,run0,rxn0,jmp0,jmp1,fall0,fall1,,lan,dash_fwd_l,dash_fwd_r, dsh_l0,dsh_l1,dsh_r0,dsh_r1,dsh_bk, chadash_begin,chadash_loop,chakra_dash, chadash_back_loop,guradpose_0, guardhit_itm0,guardhit_itm1, guardhit_itm2,guardhit_itm3,guardhit_1,guardhit_f0,guardhit_r0,guardhit_l0, guardhit_A0, face_nut, face_nut_dying, face_damage_normal, face_speak, win_s, win_l, entry, exit, etc01, nxj0, INN0, ixn0, awake_s, awake_l, awa_cutin, awa_cutin2,
        movement=Tk(className="movement & other stuff")


        nut=Entry(movement)
        run1=Entry(movement)
        run0=Entry(movement)
        rxn0=Entry(movement)
        jmp0=Entry(movement)
        jmp1=Entry(movement)
        fall0=Entry(movement)
        fall1=Entry(movement)
        lan=Entry(movement)
        dash_fwd_l=Entry(movement)
        dash_fwd_r=Entry(movement)
        dsh_l0=Entry(movement)
        dsh_l1=Entry(movement)
        dsh_r0=Entry(movement)
        dsh_r1=Entry(movement)
        dsh_bk=Entry(movement)
        chadash_begin=Entry(movement)
        chadash_loop=Entry(movement)
        chakra_dash=Entry(movement)
        chadash_back_loop=Entry(movement)
        guardpose_0=Entry(movement)
        guardhit_itm0=Entry(movement)
        guardhit_itm1=Entry(movement)
        guardhit_itm2=Entry(movement)
        guardhit_itm3=Entry(movement)
        guardhit_1=Entry(movement)
        guardhit_f0=Entry(movement)
        guardhit_r0=Entry(movement)
        guardhit_l0=Entry(movement)
        guardhit_A0=Entry(movement) 
        face_nut=Entry(movement)
        face_nut_dying=Entry(movement)
        face_damage_normal=Entry(movement)
        face_speak=Entry(movement)
        win_s=Entry(movement)
        win_l=Entry(movement)
        entry=Entry(movement)
        exit=Entry(movement)
        etc01=Entry(movement)
        nxj0=Entry(movement)
        inn0=Entry(movement)
        ixn0=Entry(movement)
        awake_s=Entry(movement)
        awake_l=Entry(movement)
        awa_cutin=Entry(movement)
        awa_cutin2=Entry(movement)


        nutl=Label(movement, text="PL_ANM_NUT (idle stance)")
        run1l=Label(movement, text="PL_ANM_RUN1 (run)")
        run0l=Label(movement, text="PL_ANM_RUN0 (error)")
        rxn0l=Label(movement, text="PL_ANM_RXN0 (???)")
        jmp0l=Label(movement, text="PL_ANM_JMP0 (first jump)")
        jmp1l=Label(movement, text="PL_ANM_JMP1 (second jump)")
        fall0l=Label(movement, text="PL_ANM_FALL0 (fall)")
        fall1l=Label(movement, text="PL_ANM_FALL1 (other fall)")
        lanl=Label(movement, text="PL_ANM_LAN (landing)")
        dash_fwd_ll=Label(movement, text="PL_ANM_DASH_FWD_L (ninja movement)")
        dash_fwd_rl=Label(movement, text="PL_ANM_DASH_FWD_R (ninja movement)")
        dsh_l0l=Label(movement, text="PL_ANM_DSH_L0 (ninja movement)")
        dsh_l1l=Label(movement, text="PL_ANM_DSH_L1 (ninja movement)")
        dsh_r0l=Label(movement, text="PL_ANM_DSH_R0 (ninja movement)")
        dsh_r1l=Label(movement, text="PL_ANM_DSH_R1 (ninja movement)")
        dsh_bkl=Label(movement, text="PL_ANM_DSH_BKL (ninja movement)")
        chadash_beginl=Label(movement, text="PL_ANM_CHADASH_BEGIN (chakra dash)")
        chadash_loopl=Label(movement, text="PL_ANM_CHADASH_LOOP (chakra dash)")
        chakra_dashl=Label(movement, text="PL_ANM_CHAKRA_DASH (error)")
        chadash_back_loopl=Label(movement, text="PL_ANM_CHADASH_BACK_LOOP (chakra dash)")
        guardpose_0l=Label(movement, text="PL_ANM_GUARDPOSE_0 (guard)")
        guardhit_itm0l=Label(movement, text="PL_ANM_GUARDHIT_ITM0 (guard)")
        guardhit_itm1l=Label(movement, text="PL_ANM_GUARDHIT_ITM1 (guard)")
        guardhit_itm2l=Label(movement, text="PL_ANM_GUARDHIT_ITM2 (guard)")
        guardhit_itm3l=Label(movement, text="PL_ANM_GUARDHIT_ITM3 (guard)")
        guardhit_1l=Label(movement, text="PL_ANM_GUARDHIT_1 (guard)")
        guardhit_f0l=Label(movement, text="PL_ANM_GUARDHIT_F0 (guard)")
        guardhit_r0l=Label(movement, text="PL_ANM_GUARDHIT_R0 (guard)")
        guardhit_l0l=Label(movement, text="PL_ANM_GUARDHIT_L0 (guard)")
        guardhit_A0l=Label(movement, text="PL_ANM_GUARDHIT_A0 (guard)")
        face_nutl=Label(movement, text="PL_ANM_FACE_NUT (normal facial bones)")
        face_nut_dyingl=Label(movement, text="PL_ANM_FACE_NUT_DYING (dying facial bones)")
        face_damage_normall=Label(movement, text="PL_ANM_DAMAGE_NORMAL (damaged facial bones)") 
        face_speakl=Label(movement, text="PL_ANM_FACE_SPEAK (speaking facial bones)")
        win_sl=Label(movement, text="PL_ANM_WIN_S (victory pose)")
        win_ll=Label(movement, text="PL_ANM_WIN_L (victory pose)")
        entryl=Label(movement, text="PL_ANM_ENTRY (support entrance)")
        exitl=Label(movement, text="PL_ANM_EXIT (support exit)")
        etc01l=Label(movement, text="PL_ANM_ETC01 (???)")
        nxj0l=Label(movement, text="PL_ANM_NXJ0 (chakra charge start)")
        inn0l=Label(movement, text="PL_ANM_INN0 (chakra charge loop)")
        ixn0l=Label(movement, text="PL_ANM_IXN0 (chakra charge end)")
        awake_sl=Label(movement, text="PL_ANM_AWAKE_S (awakening)")
        awake_ll=Label(movement, text="PL_ANM_AWAKE_L (awakening)")
        awa_cutinl=Label(movement, text="PL_ANM_AWAKE_CUTIN (awakening)")
        awa_cutin2l=Label(movement, text="PL_ANM_AWAKE_CUTIN2 (awakening)")
        

        filly=('times', 9, 'bold')
        nutl.config(font=filly)
        run1l.config(font=filly)
        run0l.config(font=filly)
        rxn0l.config(font=filly)
        jmp0l.config(font=filly)
        jmp1l.config(font=filly)
        fall0l.config(font=filly)
        fall1l.config(font=filly)
        lanl.config(font=filly)
        dash_fwd_ll.config(font=filly)
        dash_fwd_rl.config(font=filly)
        dsh_l0l.config(font=filly)
        dsh_l1l.config(font=filly)
        dsh_r0l.config(font=filly)
        dsh_r1l.config(font=filly)
        dsh_bkl.config(font=filly)
        chadash_beginl.config(font=filly)
        chadash_loopl.config(font=filly)
        chakra_dashl.config(font=filly)
        chadash_back_loopl.config(font=filly)
        guardpose_0l.config(font=filly)
        guardhit_itm0l.config(font=filly)
        guardhit_itm1l.config(font=filly)
        guardhit_itm2l.config(font=filly)
        guardhit_itm3l.config(font=filly)
        guardhit_1l.config(font=filly)
        guardhit_f0l.config(font=filly)
        guardhit_r0l.config(font=filly)
        guardhit_l0l.config(font=filly)
        guardhit_A0l.config(font=filly)
        face_nutl.config(font=filly)
        face_nut_dyingl.config(font=filly)
        face_damage_normall.config(font=filly)
        face_speakl.config(font=filly)
        win_sl.config(font=filly)
        win_ll.config(font=filly)
        entryl.config(font=filly)
        exitl.config(font=filly)
        etc01l.config(font=filly)
        nxj0l.config(font=filly)
        inn0l.config(font=filly)
        ixn0l.config(font=filly)
        awake_sl.config(font=filly)
        awake_ll.config(font=filly)
        awa_cutinl.config(font=filly)
        awa_cutin2l.config(font=filly)

        
        nutl.grid(row=0, column=1)
        run1l.grid(row=2, column=1)
        run0l.grid(row=4, column=1)
        rxn0l.grid(row=6, column=1)
        jmp0l.grid(row=8, column=1)
        jmp1l.grid(row=10, column=1)
        fall0l.grid(row=12, column=1)
        fall1l.grid(row=14, column=1)
        lanl.grid(row=16, column=1)
        dash_fwd_ll.grid(row=18, column=1)
        dash_fwd_rl.grid(row=20, column=1)
        dsh_l0l.grid(row=0, column=2)
        dsh_l1l.grid(row=2, column=2)
        dsh_r0l.grid(row=4, column=2)
        dsh_r1l.grid(row=6, column=2)
        dsh_bkl.grid(row=8, column=2)
        chadash_beginl.grid(row=10, column=2)
        chadash_loopl.grid(row=12, column=2)
        chakra_dashl.grid(row=14, column=2)
        chadash_back_loopl.grid(row=16, column=2)
        guardpose_0l.grid(row=18, column=2)
        guardhit_itm0l.grid(row=20, column=2)
        guardhit_itm1l.grid(row=0, column=3)
        guardhit_itm2l.grid(row=2, column=3)
        guardhit_itm3l.grid(row=4, column=3)
        guardhit_1l.grid(row=6, column=3)
        guardhit_f0l.grid(row=8, column=3)
        guardhit_r0l.grid(row=10, column=3)
        guardhit_l0l.grid(row=12, column=3)
        guardhit_A0l.grid(row=14, column=3)
        face_nutl.grid(row=16, column=3)
        face_nut_dyingl.grid(row=18, column=3)
        face_damage_normall.grid(row=20, column=3)
        face_speakl.grid(row=0, column=4)
        win_sl.grid(row=2, column=4)
        win_ll.grid(row=4, column=4)
        entryl.grid(row=6, column=4)
        exitl.grid(row=8, column=4)
        etc01l.grid(row=10, column=4)
        nxj0l.grid(row=12, column=4)
        inn0l.grid(row=14, column=4)
        ixn0l.grid(row=16, column=4)
        awake_sl.grid(row=18, column=4)
        awake_ll.grid(row=20, column=4)
        awa_cutinl.grid(row=0, column=5)
        awa_cutin2l.grid(row=2, column=5)

        
        nut.grid(row=1, column=1)
        run1.grid(row=3, column=1)
        run0.grid(row=5, column=1)
        rxn0.grid(row=7, column=1)
        jmp0.grid(row=9, column=1)
        jmp1.grid(row=11, column=1)
        fall0.grid(row=13, column=1)
        fall1.grid(row=15, column=1)
        lan.grid(row=17, column=1)
        dash_fwd_l.grid(row=19, column=1)
        dash_fwd_r.grid(row=21, column=1)
        dsh_l0.grid(row=1, column=2)
        dsh_l1.grid(row=3, column=2)
        dsh_r0.grid(row=5, column=2)
        dsh_r1.grid(row=7, column=2)
        dsh_bk.grid(row=9, column=2)
        chadash_begin.grid(row=11, column=2)
        chadash_loop.grid(row=13, column=2)
        chakra_dash.grid(row=15, column=2)
        chadash_back_loop.grid(row=17, column=2)
        guardpose_0.grid(row=19, column=2)
        guardhit_itm0.grid(row=21, column=2)
        guardhit_itm1.grid(row=1, column=3)
        guardhit_itm2.grid(row=3, column=3)
        guardhit_itm3.grid(row=5, column=3)
        guardhit_1.grid(row=7, column=3)
        guardhit_f0.grid(row=9, column=3)
        guardhit_r0.grid(row=11, column=3)
        guardhit_l0.grid(row=13, column=3)
        guardhit_A0.grid(row=15, column=3) 
        face_nut.grid(row=17, column=3)
        face_nut_dying.grid(row=19, column=3)
        face_damage_normal.grid(row=21, column=3)
        face_speak.grid(row=1, column=4)
        win_s.grid(row=3, column=4)
        win_l.grid(row=5, column=4)
        entry.grid(row=7, column=4)
        exit.grid(row=9, column=4)
        etc01.grid(row=11, column=4)
        nxj0.grid(row=13, column=4)
        inn0.grid(row=15, column=4)
        ixn0.grid(row=17, column=4)
        awake_s.grid(row=19, column=4)
        awake_l.grid(row=21, column=4)
        awa_cutin.grid(row=1, column=5)
        awa_cutin2.grid(row=3, column=5)
        x=0
        y=1
        mo=["NUT","RUN1","RUN0","RXN0","JMP0","JMP1","FALL0","FALL1","LAN","DSH_FWD_L","DSH_FWD_R","DSH_L0","DSH_L1","DSH_R0","DSH_R1","DSH_BK","CHADASH_BEGIN","CHADASH_LOOP","CHAKRA_DASH","CHADASH_BACK_LOOP","GUARDPOSE_0","GUARDHIT_ITM0","GUARDHIT_ITM1","GUARDHIT_ITM2","GUARDHIT_ITM3","GUARDHIT_1","GUARDHIT_F0","GUARDHIT_R0","GUARDHIT_L0","GUARDHIT_A0","FACE_NUT","FACE_NUT_DYING","FACE_DAMAGE_NORMAL","FACE_SPEAK","WIN_S","WIN_L","ENTRY","EXIT","ETC01","NXJ0","INN0","IXN0","AWAKE_S","AWAKE_L", "AWA_CUTIN", "AWA_CUTIN2"]
        while x<len(mo):
        
            plnut=basefile.find(binascii.hexlify("PL_ANM_"+mo[x]))
            plmove=binascii.unhexlify(basefile[plnut+64:plnut+128])
            
            
            if x==0:
                nut.insert(0, plmove)
            elif x==1:
                run1.insert(0, plmove)
            elif x==2:
                run0.insert(0, plmove)
            elif x==3:
                rxn0.insert(0, plmove)
            elif x==4:
                jmp0.insert(0, plmove)
            elif x==5:
                jmp1.insert(0, plmove)
            elif x==6:
                fall0.insert(0, plmove)
            elif x==7:
                fall1.insert(0, plmove)
            elif x==8:
                lan.insert(0, plmove)
            elif x==9:
                dash_fwd_l.insert(0, plmove)
            elif x==10:
                dash_fwd_r.insert(0, plmove)
            elif x==11:
                dsh_l0.insert(0, plmove)
            elif x==12:
                dsh_l1.insert(0, plmove)
            elif x==13:
                dsh_r0.insert(0, plmove)
            elif x==14:    
                dsh_r1.insert(0, plmove)
            elif x==15:    
                dsh_bk.insert(0, plmove)
            elif x==16:    
                chadash_begin.insert(0, plmove)
            elif x==17:    
                chadash_loop.insert(0, plmove)
            elif x==18:    
                chakra_dash.insert(0, plmove)
            elif x==19:    
                chadash_back_loop.insert(0, plmove)
            elif x==20:    
                guardpose_0.insert(0, plmove)
            elif x==21:    
                guardhit_itm0.insert(0, plmove)
            elif x==22:    
                guardhit_itm1.insert(0, plmove)

            elif x==23:    
                guardhit_itm2.insert(0, plmove)
                
            elif x==24:    
                guardhit_itm3.insert(0, plmove)
                
            elif x==25:    
                guardhit_1.insert(0, plmove)
            elif x==26:    
                guardhit_f0.insert(0, plmove)
            elif x==27:
                guardhit_r0.insert(0, plmove)
            elif x==28:   
                guardhit_l0.insert(0, plmove)
            elif x==29:   
                guardhit_A0.insert(0, plmove)
            elif x==30:    
                face_nut.insert(0, plmove)
            elif x==31:    
                face_nut_dying.insert(0, plmove)
            elif x==32:    
                face_damage_normal.insert(0, plmove)
            elif x==33:    
                face_speak.insert(0, plmove)
            elif x==34:    
                win_s.insert(0, plmove)
            elif x==35:    
                win_l.insert(0, plmove)
            elif x==36:    
                entry.insert(0, plmove)
            elif x==37:    
                exit.insert(0, plmove)
            elif x==38:    
                etc01.insert(0, plmove)
            elif x==39:    
                nxj0.insert(0, plmove)
            elif x==40:    
                inn0.insert(0, plmove)
            elif x==41:    
                ixn0.insert(0, plmove)
            elif x==42:    
                awake_s.insert(0, plmove)
            elif x==43:    
                awake_l.insert(0, plmove)
            elif x==44:    
                awa_cutin.insert(0, plmove)
            elif x==45:   
                awa_cutin2.insert(0, plmove)

            x+=1
        def buttonmove():
            x=0
            y=1
            mo=["NUT","RUN1","RUN0","RXN0","JMP0","JMP1","FALL0","FALL1","LAN","DSH_FWD_L","DSH_FWD_R","DSH_L0","DSH_L1","DSH_R0","DSH_R1","DSH_BK","CHADASH_BEGIN","CHADASH_LOOP","CHAKRA_DASH","CHADASH_BACK_LOOP","GUARDPOSE_0","GUARDHIT_ITM0","GUARDHIT_ITM1","GUARDHIT_ITM2","GUARDHIT_ITM3","GUARDHIT_1","GUARDHIT_F0","GUARDHIT_R0","GUARDHIT_L0","GUARDHIT_A0","FACE_NUT","FACE_NUT_DYING","FACE_DAMAGE_NORMAL","FACE_SPEAK","WIN_S","WIN_L","ENTRY","EXIT","ETC01","NXJ0","INN0","IXN0","AWAKE_S","AWAKE_L", "AWA_CUTIN", "AWA_CUTIN2"]
            movenow=basefile
            while x<(len(mo)):
            
                plnut=basefile.find(binascii.hexlify("PL_ANM_"+mo[x]))
                plmove=binascii.unhexlify(basefile[plnut+64:plnut+128])

                
                
                plsimple=movenow[plnut:plnut+128]

                plpl=("PL_ANM_"+mo[x])
                zeropl=32-len(plpl)
                
                zeropl=zeropl* zerobyte
                fullpl=binascii.hexlify(plpl)+zeropl

                if x==0:
                    movegot=nut.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                

                elif x==1:
                    movegot=run1.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                    x+=1
                elif x==2:
                    movegot=run0.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==3:
                    movegot=rxn0.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                
                elif x==4:
                    movegot=jmp0.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==5:
                    movegot=jmp1.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==6:
                    movegot=fall0.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==7:
                    movegot=fall1.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==8:
                    movegot=lan.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==9:
                    movegot=dash_fwd_l.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==10:
                    movegot=dash_fwd_r.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==11:
                    movegot=dsh_l0.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==12:
                    movegot=dsh_l1.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==13:
                    movegot=dsh_r0.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==14:
                    movegot=dsh_r1.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==15:
                    movegot=dsh_bk.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==16:
                    movegot=chadash_begin.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==17:
                    movegot=chadash_loop.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                    x+=1
                elif x==18:
                    movegot=chakra_dash.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==19:
                    movegot=chadash_back_loop.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==20:
                    movegot=guardpose_0.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                    
                    

                elif x==21:
                    movegot=guardhit_itm0.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                    
                elif x==22:
                    movegot=guardhit_itm1.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                   

                elif x==23:
                    movegot=guardhit_itm2.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                    
                elif x==24:
                    movegot=guardhit_itm3.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                    
                elif x==25:
                    movegot=guardhit_1.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==26:
                    movegot=guardhit_f0.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==27:
                    movegot=guardhit_r0.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==28:
                    movegot=guardhit_l0.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==29:   
                    movegot=guardhit_A0.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==30:    
                    movegot=face_nut.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==31:    
                    movegot=face_nut_dying.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==32:    
                    movegot=face_damage_normal.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==33:    
                    movegot=face_speak.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==34:    
                    movegot=win_s.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==35:    
                    movegot=win_l.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==36:    
                    movegot=entry.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==37:    
                    movegot=exit.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==38:    
                    movegot=etc01.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==39:    
                    movegot=nxj0.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==40:    
                    movegot=inn0.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==41:    
                    movegot=ixn0.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==42:    
                    movegot=awake_s.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==43:    
                    movegot=awake_l.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==44:    
                    movegot=awa_cutin.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==45:   
                    movegot=awa_cutin2.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                    anothersave()
                x+=1
                print x
                def anothersave():
                    #print movenow
                    #print basefile
                    
                    movesave= hexfile[:awaver-32] +movenow+ hexfile[basever+awaver-48:]
                    
                    save_command(binascii.unhexlify(movesave))
        buttonmove = Button(movement, text="Save", command=buttonmove)
        buttonmove.grid(row=22, column=1)

    def circle():
        #atk00+,atk00_s,atk00_n,atk00_l,atk00_e,dmg00
        x=loading(basefile,basea,baseb)
        x.base()
    
    def button2():
        
        but2=awakez.get()
        if (but2 == "movement"):
            but2=movement
        elif (but2 == "add a PRM"):
            but2=circle
        but2()
        button1.pack_forget()
    button1 = Button(master, text="select", command=button2)
    button1.pack()


def base():
    #movement, square attacks, circle attacks, tilt attacks, grab attacks, air attacks, animations
    basez=StringVar(master)
    basez.set("what would you like to edit in the base section?") # default value
    
    b = OptionMenu(master, basez, "movement", "add a PRM")
    b.pack()

    basefile=hexfile[basever+awaver-16:jutsuver+basever+awaver]

    basea=hexfile[:basever+awaver-16]
    baseb=hexfile[jutsuver+basever+awaver:]

    #print basefile
    #print binascii.unhexlify(basefile)
    def movement():
        #nut,run1,run0,rxn0,jmp0,jmp1,fall0,fall1,,lan,dash_fwd_l,dash_fwd_r, dsh_l0,dsh_l1,dsh_r0,dsh_r1,dsh_bk, chadash_begin,chadash_loop,chakra_dash, chadash_back_loop,guradpose_0, guardhit_itm0,guardhit_itm1, guardhit_itm2,guardhit_itm3,guardhit_1,guardhit_f0,guardhit_r0,guardhit_l0, guardhit_A0, face_nut, face_nut_dying, face_damage_normal, face_speak, win_s, win_l, entry, exit, etc01, nxj0, INN0, ixn0, awake_s, awake_l, awa_cutin, awa_cutin2,
        movement=Tk(className="movement & other stuff")


        nut=Entry(movement)
        run1=Entry(movement)
        run0=Entry(movement)
        rxn0=Entry(movement)
        jmp0=Entry(movement)
        jmp1=Entry(movement)
        fall0=Entry(movement)
        fall1=Entry(movement)
        lan=Entry(movement)
        dash_fwd_l=Entry(movement)
        dash_fwd_r=Entry(movement)
        dsh_l0=Entry(movement)
        dsh_l1=Entry(movement)
        dsh_r0=Entry(movement)
        dsh_r1=Entry(movement)
        dsh_bk=Entry(movement)
        chadash_begin=Entry(movement)
        chadash_loop=Entry(movement)
        chakra_dash=Entry(movement)
        chadash_back_loop=Entry(movement)
        guardpose_0=Entry(movement)
        guardhit_itm0=Entry(movement)
        guardhit_itm1=Entry(movement)
        guardhit_itm2=Entry(movement)
        guardhit_itm3=Entry(movement)
        guardhit_1=Entry(movement)
        guardhit_f0=Entry(movement)
        guardhit_r0=Entry(movement)
        guardhit_l0=Entry(movement)
        guardhit_A0=Entry(movement) 
        face_nut=Entry(movement)
        face_nut_dying=Entry(movement)
        face_damage_normal=Entry(movement)
        face_speak=Entry(movement)
        win_s=Entry(movement)
        win_l=Entry(movement)
        entry=Entry(movement)
        exit=Entry(movement)
        etc01=Entry(movement)
        nxj0=Entry(movement)
        inn0=Entry(movement)
        ixn0=Entry(movement)
        awake_s=Entry(movement)
        awake_l=Entry(movement)
        awa_cutin=Entry(movement)
        awa_cutin2=Entry(movement)


        nutl=Label(movement, text="PL_ANM_NUT (idle stance)")
        run1l=Label(movement, text="PL_ANM_RUN1 (run)")
        run0l=Label(movement, text="PL_ANM_RUN0 (error)")
        rxn0l=Label(movement, text="PL_ANM_RXN0 (???)")
        jmp0l=Label(movement, text="PL_ANM_JMP0 (first jump)")
        jmp1l=Label(movement, text="PL_ANM_JMP1 (second jump)")
        fall0l=Label(movement, text="PL_ANM_FALL0 (fall)")
        fall1l=Label(movement, text="PL_ANM_FALL1 (other fall)")
        lanl=Label(movement, text="PL_ANM_LAN (landing)")
        dash_fwd_ll=Label(movement, text="PL_ANM_DASH_FWD_L (ninja movement)")
        dash_fwd_rl=Label(movement, text="PL_ANM_DASH_FWD_R (ninja movement)")
        dsh_l0l=Label(movement, text="PL_ANM_DSH_L0 (ninja movement)")
        dsh_l1l=Label(movement, text="PL_ANM_DSH_L1 (ninja movement)")
        dsh_r0l=Label(movement, text="PL_ANM_DSH_R0 (ninja movement)")
        dsh_r1l=Label(movement, text="PL_ANM_DSH_R1 (ninja movement)")
        dsh_bkl=Label(movement, text="PL_ANM_DSH_BKL (ninja movement)")
        chadash_beginl=Label(movement, text="PL_ANM_CHADASH_BEGIN (chakra dash)")
        chadash_loopl=Label(movement, text="PL_ANM_CHADASH_LOOP (chakra dash)")
        chakra_dashl=Label(movement, text="PL_ANM_CHAKRA_DASH (error)")
        chadash_back_loopl=Label(movement, text="PL_ANM_CHADASH_BACK_LOOP (chakra dash)")
        guardpose_0l=Label(movement, text="PL_ANM_GUARDPOSE_0 (guard)")
        guardhit_itm0l=Label(movement, text="PL_ANM_GUARDHIT_ITM0 (guard)")
        guardhit_itm1l=Label(movement, text="PL_ANM_GUARDHIT_ITM1 (guard)")
        guardhit_itm2l=Label(movement, text="PL_ANM_GUARDHIT_ITM2 (guard)")
        guardhit_itm3l=Label(movement, text="PL_ANM_GUARDHIT_ITM3 (guard)")
        guardhit_1l=Label(movement, text="PL_ANM_GUARDHIT_1 (guard)")
        guardhit_f0l=Label(movement, text="PL_ANM_GUARDHIT_F0 (guard)")
        guardhit_r0l=Label(movement, text="PL_ANM_GUARDHIT_R0 (guard)")
        guardhit_l0l=Label(movement, text="PL_ANM_GUARDHIT_L0 (guard)")
        guardhit_A0l=Label(movement, text="PL_ANM_GUARDHIT_A0 (guard)")
        face_nutl=Label(movement, text="PL_ANM_FACE_NUT (normal facial bones)")
        face_nut_dyingl=Label(movement, text="PL_ANM_FACE_NUT_DYING (dying facial bones)")
        face_damage_normall=Label(movement, text="PL_ANM_DAMAGE_NORMAL (damaged facial bones)") 
        face_speakl=Label(movement, text="PL_ANM_FACE_SPEAK (speaking facial bones)")
        win_sl=Label(movement, text="PL_ANM_WIN_S (victory pose)")
        win_ll=Label(movement, text="PL_ANM_WIN_L (victory pose)")
        entryl=Label(movement, text="PL_ANM_ENTRY (support entrance)")
        exitl=Label(movement, text="PL_ANM_EXIT (support exit)")
        etc01l=Label(movement, text="PL_ANM_ETC01 (???)")
        nxj0l=Label(movement, text="PL_ANM_NXJ0 (chakra charge start)")
        inn0l=Label(movement, text="PL_ANM_INN0 (chakra charge loop)")
        ixn0l=Label(movement, text="PL_ANM_IXN0 (chakra charge end)")
        awake_sl=Label(movement, text="PL_ANM_AWAKE_S (awakening)")
        awake_ll=Label(movement, text="PL_ANM_AWAKE_L (awakening)")
        awa_cutinl=Label(movement, text="PL_ANM_AWAKE_CUTIN (awakening)")
        awa_cutin2l=Label(movement, text="PL_ANM_AWAKE_CUTIN2 (awakening)")
        

        filly=('times', 9, 'bold')
        nutl.config(font=filly)
        run1l.config(font=filly)
        run0l.config(font=filly)
        rxn0l.config(font=filly)
        jmp0l.config(font=filly)
        jmp1l.config(font=filly)
        fall0l.config(font=filly)
        fall1l.config(font=filly)
        lanl.config(font=filly)
        dash_fwd_ll.config(font=filly)
        dash_fwd_rl.config(font=filly)
        dsh_l0l.config(font=filly)
        dsh_l1l.config(font=filly)
        dsh_r0l.config(font=filly)
        dsh_r1l.config(font=filly)
        dsh_bkl.config(font=filly)
        chadash_beginl.config(font=filly)
        chadash_loopl.config(font=filly)
        chakra_dashl.config(font=filly)
        chadash_back_loopl.config(font=filly)
        guardpose_0l.config(font=filly)
        guardhit_itm0l.config(font=filly)
        guardhit_itm1l.config(font=filly)
        guardhit_itm2l.config(font=filly)
        guardhit_itm3l.config(font=filly)
        guardhit_1l.config(font=filly)
        guardhit_f0l.config(font=filly)
        guardhit_r0l.config(font=filly)
        guardhit_l0l.config(font=filly)
        guardhit_A0l.config(font=filly)
        face_nutl.config(font=filly)
        face_nut_dyingl.config(font=filly)
        face_damage_normall.config(font=filly)
        face_speakl.config(font=filly)
        win_sl.config(font=filly)
        win_ll.config(font=filly)
        entryl.config(font=filly)
        exitl.config(font=filly)
        etc01l.config(font=filly)
        nxj0l.config(font=filly)
        inn0l.config(font=filly)
        ixn0l.config(font=filly)
        awake_sl.config(font=filly)
        awake_ll.config(font=filly)
        awa_cutinl.config(font=filly)
        awa_cutin2l.config(font=filly)

        
        nutl.grid(row=0, column=1)
        run1l.grid(row=2, column=1)
        run0l.grid(row=4, column=1)
        rxn0l.grid(row=6, column=1)
        jmp0l.grid(row=8, column=1)
        jmp1l.grid(row=10, column=1)
        fall0l.grid(row=12, column=1)
        fall1l.grid(row=14, column=1)
        lanl.grid(row=16, column=1)
        dash_fwd_ll.grid(row=18, column=1)
        dash_fwd_rl.grid(row=20, column=1)
        dsh_l0l.grid(row=0, column=2)
        dsh_l1l.grid(row=2, column=2)
        dsh_r0l.grid(row=4, column=2)
        dsh_r1l.grid(row=6, column=2)
        dsh_bkl.grid(row=8, column=2)
        chadash_beginl.grid(row=10, column=2)
        chadash_loopl.grid(row=12, column=2)
        chakra_dashl.grid(row=14, column=2)
        chadash_back_loopl.grid(row=16, column=2)
        guardpose_0l.grid(row=18, column=2)
        guardhit_itm0l.grid(row=20, column=2)
        guardhit_itm1l.grid(row=0, column=3)
        guardhit_itm2l.grid(row=2, column=3)
        guardhit_itm3l.grid(row=4, column=3)
        guardhit_1l.grid(row=6, column=3)
        guardhit_f0l.grid(row=8, column=3)
        guardhit_r0l.grid(row=10, column=3)
        guardhit_l0l.grid(row=12, column=3)
        guardhit_A0l.grid(row=14, column=3)
        face_nutl.grid(row=16, column=3)
        face_nut_dyingl.grid(row=18, column=3)
        face_damage_normall.grid(row=20, column=3)
        face_speakl.grid(row=0, column=4)
        win_sl.grid(row=2, column=4)
        win_ll.grid(row=4, column=4)
        entryl.grid(row=6, column=4)
        exitl.grid(row=8, column=4)
        etc01l.grid(row=10, column=4)
        nxj0l.grid(row=12, column=4)
        inn0l.grid(row=14, column=4)
        ixn0l.grid(row=16, column=4)
        awake_sl.grid(row=18, column=4)
        awake_ll.grid(row=20, column=4)
        awa_cutinl.grid(row=0, column=5)
        awa_cutin2l.grid(row=2, column=5)

        
        nut.grid(row=1, column=1)
        run1.grid(row=3, column=1)
        run0.grid(row=5, column=1)
        rxn0.grid(row=7, column=1)
        jmp0.grid(row=9, column=1)
        jmp1.grid(row=11, column=1)
        fall0.grid(row=13, column=1)
        fall1.grid(row=15, column=1)
        lan.grid(row=17, column=1)
        dash_fwd_l.grid(row=19, column=1)
        dash_fwd_r.grid(row=21, column=1)
        dsh_l0.grid(row=1, column=2)
        dsh_l1.grid(row=3, column=2)
        dsh_r0.grid(row=5, column=2)
        dsh_r1.grid(row=7, column=2)
        dsh_bk.grid(row=9, column=2)
        chadash_begin.grid(row=11, column=2)
        chadash_loop.grid(row=13, column=2)
        chakra_dash.grid(row=15, column=2)
        chadash_back_loop.grid(row=17, column=2)
        guardpose_0.grid(row=19, column=2)
        guardhit_itm0.grid(row=21, column=2)
        guardhit_itm1.grid(row=1, column=3)
        guardhit_itm2.grid(row=3, column=3)
        guardhit_itm3.grid(row=5, column=3)
        guardhit_1.grid(row=7, column=3)
        guardhit_f0.grid(row=9, column=3)
        guardhit_r0.grid(row=11, column=3)
        guardhit_l0.grid(row=13, column=3)
        guardhit_A0.grid(row=15, column=3) 
        face_nut.grid(row=17, column=3)
        face_nut_dying.grid(row=19, column=3)
        face_damage_normal.grid(row=21, column=3)
        face_speak.grid(row=1, column=4)
        win_s.grid(row=3, column=4)
        win_l.grid(row=5, column=4)
        entry.grid(row=7, column=4)
        exit.grid(row=9, column=4)
        etc01.grid(row=11, column=4)
        nxj0.grid(row=13, column=4)
        inn0.grid(row=15, column=4)
        ixn0.grid(row=17, column=4)
        awake_s.grid(row=19, column=4)
        awake_l.grid(row=21, column=4)
        awa_cutin.grid(row=1, column=5)
        awa_cutin2.grid(row=3, column=5)
        x=0
        y=1
        mo=["NUT","RUN1","RUN0","RXN0","JMP0","JMP1","FALL0","FALL1","LAN","DSH_FWD_L","DSH_FWD_R","DSH_L0","DSH_L1","DSH_R0","DSH_R1","DSH_BK","CHADASH_BEGIN","CHADASH_LOOP","CHAKRA_DASH","CHADASH_BACK_LOOP","GUARDPOSE_0","GUARDHIT_ITM0","GUARDHIT_ITM1","GUARDHIT_ITM2","GUARDHIT_ITM3","GUARDHIT_1","GUARDHIT_F0","GUARDHIT_R0","GUARDHIT_L0","GUARDHIT_A0","FACE_NUT","FACE_NUT_DYING","FACE_DAMAGE_NORMAL","FACE_SPEAK","WIN_S","WIN_L","ENTRY","EXIT","ETC01","NXJ0","INN0","IXN0","AWAKE_S","AWAKE_L", "AWA_CUTIN", "AWA_CUTIN2"]
        while x<len(mo):
        
            plnut=basefile.find(binascii.hexlify("PL_ANM_"+mo[x]))
            plmove=binascii.unhexlify(basefile[plnut+64:plnut+128])
            
            
            if x==0:
                nut.insert(0, plmove)
            elif x==1:
                run1.insert(0, plmove)
            elif x==2:
                run0.insert(0, plmove)
            elif x==3:
                rxn0.insert(0, plmove)
            elif x==4:
                jmp0.insert(0, plmove)
            elif x==5:
                jmp1.insert(0, plmove)
            elif x==6:
                fall0.insert(0, plmove)
            elif x==7:
                fall1.insert(0, plmove)
            elif x==8:
                lan.insert(0, plmove)
            elif x==9:
                dash_fwd_l.insert(0, plmove)
            elif x==10:
                dash_fwd_r.insert(0, plmove)
            elif x==11:
                dsh_l0.insert(0, plmove)
            elif x==12:
                dsh_l1.insert(0, plmove)
            elif x==13:
                dsh_r0.insert(0, plmove)
            elif x==14:    
                dsh_r1.insert(0, plmove)
            elif x==15:    
                dsh_bk.insert(0, plmove)
            elif x==16:    
                chadash_begin.insert(0, plmove)
            elif x==17:    
                chadash_loop.insert(0, plmove)
            elif x==18:    
                chakra_dash.insert(0, plmove)
            elif x==19:    
                chadash_back_loop.insert(0, plmove)
            elif x==20:    
                guardpose_0.insert(0, plmove)
            elif x==21:    
                guardhit_itm0.insert(0, plmove)
            elif x==22:    
                guardhit_itm1.insert(0, plmove)
            elif x==23:    
                guardhit_itm2.insert(0, plmove)
            elif x==24:    
                guardhit_itm3.insert(0, plmove)
            elif x==25:    
                guardhit_1.insert(0, plmove)
            elif x==26:    
                guardhit_f0.insert(0, plmove)
            elif x==27:
                guardhit_r0.insert(0, plmove)
            elif x==28:   
                guardhit_l0.insert(0, plmove)
            elif x==29:   
                guardhit_A0.insert(0, plmove)
            elif x==30:    
                face_nut.insert(0, plmove)
            elif x==31:    
                face_nut_dying.insert(0, plmove)
            elif x==32:    
                face_damage_normal.insert(0, plmove)
            elif x==33:    
                face_speak.insert(0, plmove)
            elif x==34:    
                win_s.insert(0, plmove)
            elif x==35:    
                win_l.insert(0, plmove)
            elif x==36:    
                entry.insert(0, plmove)
            elif x==37:    
                exit.insert(0, plmove)
            elif x==38:    
                etc01.insert(0, plmove)
            elif x==39:    
                nxj0.insert(0, plmove)
            elif x==40:    
                inn0.insert(0, plmove)
            elif x==41:    
                ixn0.insert(0, plmove)
            elif x==42:    
                awake_s.insert(0, plmove)
            elif x==43:    
                awake_l.insert(0, plmove)
            elif x==44:    
                awa_cutin.insert(0, plmove)
            elif x==45:   
                awa_cutin2.insert(0, plmove)

            x+=1
        def buttonmove():
            x=0
            y=1
            mo=["NUT","RUN1","RUN0","RXN0","JMP0","JMP1","FALL0","FALL1","LAN","DSH_FWD_L","DSH_FWD_R","DSH_L0","DSH_L1","DSH_R0","DSH_R1","DSH_BK","CHADASH_BEGIN","CHADASH_LOOP","CHAKRA_DASH","CHADASH_BACK_LOOP","GUARDPOSE_0","GUARDHIT_ITM0","GUARDHIT_ITM1","GUARDHIT_ITM2","GUARDHIT_ITM3","GUARDHIT_1","GUARDHIT_F0","GUARDHIT_R0","GUARDHIT_L0","GUARDHIT_A0","FACE_NUT","FACE_NUT_DYING","FACE_DAMAGE_NORMAL","FACE_SPEAK","WIN_S","WIN_L","ENTRY","EXIT","ETC01","NXJ0","INN0","IXN0","AWAKE_S","AWAKE_L", "AWA_CUTIN", "AWA_CUTIN2"]
            movenow=basefile
            while x<(len(mo)):
            
                plnut=basefile.find(binascii.hexlify("PL_ANM_"+mo[x]))
                plmove=binascii.unhexlify(basefile[plnut+64:plnut+128])

                
                
                plsimple=movenow[plnut:plnut+128]

                plpl=("PL_ANM_"+mo[x])
                zeropl=32-len(plpl)
                
                zeropl=zeropl* zerobyte
                fullpl=binascii.hexlify(plpl)+zeropl

                if x==0:
                    movegot=nut.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                

                elif x==1:
                    movegot=run1.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                    x+=1
                elif x==2:
                    movegot=run0.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==3:
                    movegot=rxn0.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==4:
                    movegot=jmp0.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==5:
                    movegot=jmp1.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==6:
                    movegot=fall0.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==7:
                    movegot=fall1.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==8:
                    movegot=lan.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==9:
                    movegot=dash_fwd_l.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==10:
                    movegot=dash_fwd_r.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==11:
                    movegot=dsh_l0.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==12:
                    movegot=dsh_l1.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==13:
                    movegot=dsh_r0.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==14:
                    movegot=dsh_r1.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==15:
                    movegot=dsh_bk.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==16:
                    movegot=chadash_begin.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==17:
                    movegot=chadash_loop.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                    x+=1
                elif x==18:
                    movegot=chakra_dash.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==19:
                    movegot=chadash_back_loop.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==20:
                    movegot=guardpose_0.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==21:
                    movegot=guardhit_itm0.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==22:
                    movegot=guardhit_itm1.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==23:
                    movegot=guardhit_itm2.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==24:
                    movegot=guardhit_itm3.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==25:
                    movegot=guardhit_1.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==26:
                    movegot=guardhit_f0.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==27:
                    movegot=guardhit_r0.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==28:
                    movegot=guardhit_l0.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==29:   
                    movegot=guardhit_A0.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==30:    
                    movegot=face_nut.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==31:    
                    movegot=face_nut_dying.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==32:    
                    movegot=face_damage_normal.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==33:    
                    movegot=face_speak.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==34:    
                    movegot=win_s.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==35:    
                    movegot=win_l.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==36:    
                    movegot=entry.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==37:    
                    movegot=exit.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==38:    
                    movegot=etc01.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==39:    
                    movegot=nxj0.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==40:    
                    movegot=inn0.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==41:    
                    movegot=ixn0.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==42:    
                    movegot=awake_s.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==43:    
                    movegot=awake_l.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==44:    
                    movegot=awa_cutin.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                elif x==45:   
                    movegot=awa_cutin2.get()
                    zeroget=32-(len(movegot))
                    movegot=binascii.hexlify(movegot)
                    if fullpl=='':
                        fullpl='0000000000000000000000000000000000000000000000000000000000000000'
                    if plsimple=='':
                        plsimple='0000000000000000000000000000000000000000000000000000000000000000'
                    
                    if plsimple!='0000000000000000000000000000000000000000000000000000000000000000':
                        movenow=movenow.replace(plsimple,fullpl+movegot+(zeroget*zerobyte))
                
                    anothersave()
                x+=1
                def anothersave():
                    #print movenow
                    #print basefile
                    
                    movesave= hexfile[:basever+awaver-16] +movenow+ hexfile[jutsuver+basever+awaver:]
                    
                    save_command(binascii.unhexlify(movesave))
                    movement.destroy()
                    master.destroy()
                

                        #movesave=movesave+end+hexfile[jutsuver+basever+awaver:]


                        #print hexfile
                        #print movesave
                
                
        buttonmove = Button(movement, text="Save", command=buttonmove)
        buttonmove.grid(row=22, column=1)
    
    def circle():
        

                
        x=loading(basefile,basea,baseb)
        x.base()
        #master.destroy()
        #button7 = Button(master, text="start", command=x.base)
        #button7.pack()
        
    def button2():
        
        but2=basez.get()
        if (but2 == "movement"):
            but2=movement
        elif (but2 == "add a PRM"):
            but2=circle
        
        but2()
        button2.pack_forget()
    button2 = Button(master, text="select", command=button2)
    button2.pack()



def button():
    
    x=var.get()
    if (x == "base"):
        x=base
    elif (x == "awakening"):
        x=awakening
    elif (x == "jutsu"):
        x=jutsu
    elif (x == "projectiles"):
        x=projectiles
    elif (x == "ultimate"):
        x=ultimate
    button.pack_forget()
    versection()
    x()

button = Button(master, text="select", command=button)
button.pack()


# launcher
#hexpad.pack(side=RIGHT)
#textPad.pack(side=LEFT)
#root.mainloop()
master.mainloop()