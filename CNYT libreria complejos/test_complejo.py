import complejo as c

def test_suma():
    assert c.suma([3,2],[7,5]) == [10,7], 'Deber ser 10+7i'

def test_resta():
    assert c.resta([3,-2],[4,6]) == [-1,-8], 'Debe ser -1-8i'

def test_multiplicacion():
    assert c.multiplicacion([5,3],[15,-6]) == [93,15], 'Debe ser 93+15i'

def test_conjugado():
    assert c.conjugado([3,7]) == [3,-7], 'Debe ser 3-7i'
    assert c.conjugado([8,-3]) == [8,3], 'Debe ser 8+3i'

def test_division():
    assert c.division([3,-2],[5,4]) == [0.17073170731707318, -0.5365853658536586], 'Debe ser (7/41)-(22i/41)'

def test_imprimir():
    assert c.imprimir([3,9]) == '3+9i', 'Debe ser 3+9i'
    assert c.imprimir([3,-9]) == '3-9i', 'Debe ser 3-9i'

def test_modulo():
    assert c.modulo([4,3]) == 5.0, 'Debe ser 5'

def test_fase():
    assert c.fase([1,1]) == 0.7853981633974483, 'Debe ser pi/4'

def test_cov_de_car_a_polar():
    assert c.conv_a_polar([-2,2]) == [2.8284271247461903, 2.356194490192345],'Debe ser raiz(8),3pi/4'
    assert c.conv_a_polar([2,2]) == [2.8284271247461903, 0.7853981633974483],'Debe ser raiz(8),pi/4'

def test_cov_de_pol_a_car():
    assert c.conv_a_cartesiana([2.8284271247461903, 0.7853981633974483]) == [2.0,2.0], 'Debe ser [2,2]'

def test_imprimir_expon_po():
    assert c.imprimir_po_exponencial([2.8284271247461903, 0.7853981633974483]) == '2.8284271247461903e^0.7853981633974483i', 'Debe ser 2.8284271247461903e^0.7853981633974483i'

def test_imprimir_expo_car():
    assert c.imprimir_ca_exponencial([-2,2]) == '2.8284271247461903e^2.356194490192345i','Debe ser 2.8284271247461903e^2.356194490192345i'

def test_potencia():
    assert c.potencia(10,[1,1]) == [32.00000000000002, 7.853981633974483],'Debe ser [32.00000000000002, 7.853981633974483]'

def main():
    test_suma()
    test_resta()
    test_multiplicacion()
    test_conjugado()
    test_division()
    test_imprimir()
    test_modulo()
    test_fase()
    test_cov_de_car_a_polar()
    test_cov_de_pol_a_car()
    test_imprimir_expon_po()
    test_imprimir_expo_car()
    test_potencia()
    print("Prueba exitosa")
main()

