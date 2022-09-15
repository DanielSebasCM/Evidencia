# Evidencia
## Diego Ernesto Sandoval Vargas - Memory game

Se realizaron los siguientes cambios:
  -Funcion que cuenta y muestra los "taps"
  -Funcion que detecta cuando todas las casillas se han descubierto
  
  **Tapcount**
  
  ```
    def tapCount():
    """Count and show the number of taps"""
    global taps
    taps += 1
    print(taps)    
  ```
 Funcion en la cual existe una variable global llamada taps, la cual aumenta cada que el usuario realice un click
  
  **DetectWin**
  
  ```
  def detectWin():
    """Detect if all the tiles are uncovered"""
    if (not any(hide)):
        print("Congratulations! \n all the tiles are open")
  ```
  Funcion en la que se detecta cuando las casillas estan descubiertas
  
  **Modificacion de funcion tap**
  
  Se modifico la funcion tap() del codigo original para implementar las funciones TapCount y DetectWin, para que cuando el usuario haga click en alguna de las casillas se aumente el contador de taps y se detecte si las casillas han sido descubiertas en su totalidad
  
  **Funcion tap original**
   ```
   def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
   ```
   
   
 **Funcion tap Modificada**
  ```
  def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        detectWin()
    tapCount()
  ```
    
  
