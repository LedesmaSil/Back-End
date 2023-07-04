"""
Plantear un programa que permita jugar a los dados. Las reglas de juego son:
se tiran tres dados y si los tres salen con el mismo valor se debe mostrar un mensaje que
diga "ganó", sino "perdió".
"""
from clases.JuegoDados import JuegoDados

juego = JuegoDados()
juego.jugar()