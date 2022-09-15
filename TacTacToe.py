"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from turtle import *

from freegames import line

SIZE = 100

board = [False for i in range(9)]


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
    diff = 133 - SIZE #Diferencia entre el tamaño de la cuadrícula y el icono
    line(x+diff, y+diff, x + SIZE, y + SIZE)
    line(x+diff, y + SIZE, x + SIZE, y+diff)


def drawo(x, y):
    """Draw O player."""
    diff = 133 - SIZE
    up()
    goto(x + 67, y + diff//2 + 10)
    down()
    circle(SIZE//2 - 10)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)

    index = int((x+200)//133 + (abs(y-66))//133*3)

    if not board[index]:
        board[index] = True
        player = state['player']
        draw = players[player]
        draw(x, y)
        update()
        state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
