
import Modèle

def testLitEtat():
    assert Modèle.litEtat('Tac') == 'affamé'

def testLitEtatNul():
    assert Modèle.litEtat('Bob') == None

testLitEtat()
testLitEtatNul()