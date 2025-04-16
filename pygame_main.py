import pygame
import sys
from tictactoelogic import TicTacToe as ttt
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption('TicTacToe')
run=True
square=pygame.Surface((200,200))
square.fill('Blue')
clock=pygame.time.Clock()
board=pygame.image.load(r"C:\Users\91957\Desktop\pyfiles\board2.jpg").convert_alpha()
retry_but=pygame.image.load(r"C:\Users\91957\Downloads\retrybut.png").convert_alpha()
Vline=pygame.Surface((10,330))
Hline=pygame.Surface((350,10))
space=pygame.Surface((100,100),pygame.SRCALPHA)
a=space.get_rect()
b=space.get_rect()
c=space.get_rect()
d=space.get_rect()
e=space.get_rect()
f=space.get_rect()
g=space.get_rect()
h=space.get_rect()
i=space.get_rect()
text_disp1,text_disp2,text_disp3=True,True,True
x=pygame.image.load(r"C:\Users\91957\Desktop\pyfiles\xo1.png").convert_alpha()
o=pygame.image.load(r"C:\Users\91957\Desktop\pyfiles\xo2.png").convert_alpha()
img1=pygame.image.load(r"C:\Users\91957\Desktop\pyfiles\ttttext.png").convert_alpha()
img2=pygame.image.load(r"C:\Users\91957\Desktop\pyfiles\tttpic.png").convert_alpha()
img3=pygame.image.load(r"C:\Users\91957\Desktop\pyfiles\playbut.png").convert_alpha()
img4=pygame.image.load(r"C:\Users\91957\Desktop\pyfiles\bgscr(2).png").convert_alpha()
surf4=pygame.Surface((100,100),pygame.SRCALPHA)
rect_retry=surf4.get_rect()
rect=pygame.Surface((150,50))
rect2=rect.get_rect()
rect2.x,rect2.y=230,380
txt=['  Player 1 Wins!','  Player 2 Wins!',' Draw!']
font=pygame.font.Font(None,50)
txt1=font.render(txt[0],False,'Yellow')
txt2=font.render(txt[1],False,'Yellow')
txt3=font.render(txt[2],False,'Yellow')
surf2=pygame.Surface((400,120))
surf2.fill('Red')
btns=['b1','b2','b3','b4','b5','b6','b7','b8','b9']
out1=None
xos='x'
arr=[[7,7,7],[7,7,7],[7,7,7]]
nam11,nam12=False,False
nam21,nam22=False,False
nam31,nam32=False,False
nam41,nam42=False,False
nam51,nam52=False,False
nam61,nam62=False,False
nam71,nam72=False,False
nam81,nam82=False,False
nam91,nam92=False,False
text1,text2,text3=False,False,False
retrybut=True
res=None
screen1=False
screen2=True
def xo(arg):
    global xos,out1
    if arg in btns:
        match arg:
            case 'b1':
                btns.remove('b1')
                out1=xos
                if xos=='x':
                    xos='o'
                else:
                    xos='x'                
            case 'b2':
                btns.remove('b2')
                out1=xos
                if xos=='x':
                    xos='o'
                else:
                    xos='x'
            case 'b3':
                btns.remove('b3')
                out1=xos
                if xos=='x':
                    xos='o'
                else:
                    xos='x'
            case 'b4':
                btns.remove('b4')
                out1=xos
                if xos=='x':
                    xos='o'
                else:
                    xos='x'
            case 'b5':
                btns.remove('b5')
                out1=xos
                if xos=='x':
                    xos='o'
                else:
                    xos='x'
            case 'b6':
                btns.remove('b6')
                out1=xos
                if xos=='x':
                    xos='o'
                else:
                    xos='x'
            case 'b7':
                btns.remove('b7')
                out1=xos
                if xos=='x':
                    xos='o'
                else:
                    xos='x' 
            case 'b8':
                btns.remove('b8')
                out1=xos
                if xos=='x':
                    xos='o'
                else:
                    xos='x'
                    
            case 'b9':
                btns.remove('b9')
                out1=xos
                if xos=='x':
                    xos='o'
                else:
                    xos='x'
        return out1                        
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if rect2.collidepoint(event.pos):
                screen1=True    
        if event.type==pygame.MOUSEBUTTONDOWN:
            if a.collidepoint(event.pos):
                out=xo('b1')
                if out is not None:  
                  if out=='x':  
                   nam11=True
                   arr[0][0]=1
                   res=ttt(arr)
                   res=res.full_check()
                  else:   
                   nam12=True
                   arr[0][0]=0
                   res=ttt(arr)
                   res=res.full_check()
            if b.collidepoint(event.pos):
                out=xo('b2')
                if out is not None:
                   if out=='x':   
                      nam21=True
                      arr[0][1]=1
                      res=ttt(arr)
                      res=res.full_check()
                   else:
                       nam22=True
                       arr[0][1]=0
                       res=ttt(arr)
                       res=res.full_check()
            if c.collidepoint(event.pos):
                out=xo('b3')
                if out is not None:
                   if out=='x':   
                      nam31=True
                      arr[0][2]=1
                      res=ttt(arr)
                      res=res.full_check()
                   else:
                       nam32=True
                       arr[0][2]=0
                       res=ttt(arr)
                       res=res.full_check()
            if d.collidepoint(event.pos):
                out=xo('b4')  
                if out is not None:
                   if out=='x':   
                      nam41=True
                      arr[1][0]=1
                      res=ttt(arr)
                      res=res.full_check()
                   else:
                       nam42=True
                       arr[1][0]=0
                       res=ttt(arr)
                       res=res.full_check()
            if e.collidepoint(event.pos):
                out=xo('b5')
                if out is not None:
                   if out=='x':   
                      nam51=True
                      arr[1][1]=1
                      res=ttt(arr)
                      res=res.full_check()
                   else:
                       nam52=True
                       arr[1][1]=0
                       res=ttt(arr)
                       res=res.full_check()
            if f.collidepoint(event.pos):
                out=xo('b6')
                if out is not None:
                   if out=='x':   
                      nam61=True
                      arr[1][2]=1
                      res=ttt(arr)
                      res=res.full_check()
                   else:
                       nam62=True
                       arr[1][2]=0
                       res=ttt(arr)
                       res=res.full_check()
            if g.collidepoint(event.pos):
                out=xo('b7')
                if out is not None:
                   if out=='x':   
                      nam71=True
                      arr[2][0]=1
                      res=ttt(arr)
                      res=res.full_check()
                   else:
                       nam72=True
                       arr[2][0]=0
                       res=ttt(arr)
                       res=res.full_check()
            if h.collidepoint(event.pos):
                out=xo('b8')
                if out is not None:
                   if out=='x':   
                      nam81=True
                      arr[2][1]=1
                      res=ttt(arr)
                      res=res.full_check()
                   else:
                       nam82=True
                       arr[2][1]=0
                       res=ttt(arr)
                       res=res.full_check()
            if i.collidepoint(event.pos):
                out=xo('b9')
                if out is not None:
                   if out=='x':
                     nam91=True
                     arr[2][2]=1
                     res=ttt(arr)
                     res=res.full_check()
                   else:
                      nam92=True
                      arr[2][2]=0
                      res=ttt(arr)
                      res=res.full_check()
            if h.collidepoint(event.pos) and rect_retry.collidepoint(event.pos):
                        print('clicked!')
                        nam11,nam12=False,False
                        nam21,nam22=False,False
                        nam31,nam32=False,False
                        nam41,nam42=False,False
                        nam51,nam52=False,False
                        nam61,nam62=False,False
                        nam71,nam72=False,False
                        nam81,nam82=False,False
                        nam91,nam92=False,False
                        retrybut=False
                        text_disp3,text_disp1,text_disp2=False,False,False
                        btns=['b1','b2','b3','b4','b5','b6','b7','b8','b9']
                              
    if screen2:
        screen.fill((1,70,32))
        screen.blit(img4,(0,0))        
        screen.blit(img1,(125,70))
        screen.blit(img2,(155,200))        
        screen.blit(img3,(145,290))                  
    if screen1:
        screen2=False
        screen.blit(board,(0,0))
        screen.blit(Vline,(230,90))
        screen.blit(Hline,(125,190))
        screen.blit(Vline,(360,90))
        screen.blit(Hline,(125,310))
        a.x,a.y=125,85
        b.x,b.y=250,85
        c.x,c.y=375,85
        d.x,d.y=125,205
        e.x,e.y=250,205
        f.x,f.y=375,205 
        g.x,g.y=125,325
        h.x,h.y=250,325
        i.x,i.y=375,325
        if nam11:
            screen.blit(x,(120,80))
        if nam12:
            screen.blit(o,(120,80))
        if nam21:
            screen.blit(x,(250,80))
        if nam22:
            screen.blit(o,(250,80))
        if nam31:
            screen.blit(x,(380,80))
        if nam32:
            screen.blit(o,(380,80))
        if nam41:
            screen.blit(x,(120,205))
        if nam42:
            screen.blit(o,(120,205))
        if nam51:
            screen.blit(x,(250,205))
        if nam52:
            screen.blit(o,(250,205))
        if nam61:
            screen.blit(x,(380,205))
        if nam62:
            screen.blit(o,(380,205))
        if nam71:
            screen.blit(x,(120,330))
        if nam72:
            screen.blit(o,(120,330))
        if nam81:
            screen.blit(x,(250,330))
        if nam82:
            screen.blit(o,(250,330))
        if nam91:
            screen.blit(x,(380,330))
        if nam92:
            screen.blit(o,(380,330))
        if res is not None:
            if len(btns)<6: 
               if res=='Draw!':  
                 if btns==[]:
                  text3=True
               if res=='Player 1 wins!':
                  text1=True
               if res=='Player 2 wins!':
                 text2=True
        if text3 or text2 or text1:
            rect_retry.x,rect_retry.y=290,330
            if retrybut:
                screen.blit(retry_but,(250,320))
                screen.blit(surf4,rect_retry)
        if text3 and text_disp3:
            screen1=False
            screen.blit(surf2,(110,170))
            screen.blit(txt3,(250,220))
        if text2 and text_disp2:
            screen1=False
            screen.blit(surf2,(110,170))
            screen.blit(txt2,(180,220))
        if text1 and text_disp1:
            screen1=False
            screen.blit(surf2,(110,170))
            screen.blit(txt1,(180,220))
    pygame.display.update()
    clock.tick(60)


            
