from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

class Draw (QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__polygon = QPolygonF()


    def mousePressEvent(self, event : QMouseEvent):
        #Get x, y coordinates
        x = event.position().x()
        y = event.position().y()

        #Create new QPointF
        p = QPointF(x, y)

        #Add to polygon
        self.__polygon.append(p)

        #Repaint
        self.repaint()


    def paintEvent(self, QPaintEvent):
        #Create new graphic object
        qp = QPainter(self)

        #Start draw
        qp.begin(self)

        #Draw polygon
        qp.drawPolygon(self.__polygon)

        #End draw
        qp.end()


