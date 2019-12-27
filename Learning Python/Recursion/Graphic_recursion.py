import graphics as gr
from time import sleep

window = gr.GraphWin("Fractal Rectangle", 600, 600)
alpha = float(input("input alpha (full length is 1): "))

def fractal_Rectangle(A, B, C, D, deep = 10): #deep has a default value of 10
    if deep < 1:
        return #exit from a function
    #gr.Line(gr.Point(*A), gr.Point(*B)) .draw(window)  A* = A[0], A[1] synthax function
    #gr.Line(gr.Point(*B), gr.Point(*C)) .draw(window)
    #gr.Line(gr.Point(*C), gr.Point(*D)) .draw(window)
    #gr.Line(gr.Point(*D), gr.Point(*A)) .draw(window)
    #instead we can do this:
    for M, N in (A, B), (B, C), (C, D), (D, A): #the list of tuples
        gr.Line(gr.Point(*M), gr.Point(*N)) .draw(window)         
    
    A1 = (A[0]*(1-alpha) + B[0]*alpha, A[1]*(1-alpha) + B[1]*alpha)
    B1 = (B[0]*(1-alpha) + C[0]*alpha, B[1]*(1-alpha) + C[1]*alpha)
    C1 = (C[0]*(1-alpha) + D[0]*alpha, C[1]*(1-alpha) + D[1]*alpha)
    D1 = (D[0]*(1-alpha) + A[0]*alpha, D[1]*(1-alpha) + A[1]*alpha)
        #try with cycle of tuple list if possible
    
    fractal_Rectangle(A1, B1, C1, D1, deep - 1)

    window.getMouse() #without this string the window will be closed immediately after the call

fractal_Rectangle((100, 100), (500, 100), (500, 500), (100, 500))