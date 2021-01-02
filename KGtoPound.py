#KGtoPound.py
#Janet Lee
#Lab M3
#KG to pounds

from graphics import *

def main():
    #Set up the graphic window
    win=GraphWin("Kilograms to Pounds Converter",400,600)
    win.setBackground("green")
    win.setCoords(0,0,4,6)

    #draw horizontal line 
    hl=Line(Point(0,2),Point(4,2))
    hl.draw(win)
    
    #make a fake button for clicking for computation
    button=Rectangle(Point(1,1.5),Point(3,.5))
    button.setFill("cyan")
    buttonLabel=Text(Point(2,1),"Click to Calculate")
    button.draw(win)
    buttonLabel.draw(win)

    #draw text entry box for entering weight in kg
    Text(Point(1,5.7),"Weight in kilograms").draw(win)
    KGdisplay=Entry(Point(1, 5.5), 10)
    KGdisplay.setText("0.0")  
    KGdisplay.draw(win)

    #display weight in pounds.
    Text(Point(3.3,5.7),"Weight in pounds").draw(win)
    pounds=0  
    poundBox=Text(Point(3, 5.5),str(pounds))
    poundBox.draw(win)

    #read value in entry box, compute and display kilograms
    win.getMouse() #Don't click until value has been entered
    kg=float(KGdisplay.getText())
    pounds=kg/0.453592
    poundBox.setText(str(pounds))

main()
