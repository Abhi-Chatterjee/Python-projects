#Assumption:
#Slope of required line is < 1
import matplotlib.pyplot as plt
x_coordinates=[]
y_coordinates=[]

def bresenham(x1,y1,x2, y2):
    dy=y2-y1
    dx=x2-x1
    p0=2*dy-dx
    dp1=2*dy
    dp2=2*(dy-dx)
    pk=p0
    y=y1
    
    for x in range(x1,x2+1):  
      
        print("(",x ,",",y ,")\n")  
        x_coordinates.append(x)
        y_coordinates.append(y)

        if(pk<0):
            pk=pk+dp1
        else:
            pk=pk+dp2
            y=y+1

if __name__=='__main__': 
    x1 = int(input("Enter x coordinate of first point"))
    y1 = int(input("Enter y coordinate of first point"))
    x2 = int(input("Enter x coordinate of second point"))
    y2 = int(input("Enter y coordinate of second point"))
    bresenham(x1, y1, x2, y2)  
    plt.plot(x_coordinates,y_coordinates)
