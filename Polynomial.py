class Polynomial:

    # konstruktor
    def __init__(self, coefficients):
        if isinstance(coefficients, dict):
            self.coefficients = {k: v for k, v in coefficients.items() if v != 0}
        else:
           raise ValueError("Coefficients must a dictionary")

    # odczyt stopnia wielomianu
    def degree(self):
        return max(self.coefficients.keys(), default=0)

    # sprawdzanie czy wielomian jest wielomianem zerowym (=czy słownik jest pusty)
    def is_zero(self):
        return not self.coefficients

    # przeciązenie operatora ==
    def __eq__(self, other):
        return self.coefficients == other.coefficients

    # przeciążenie operatora !=
    def __ne__(self, other):
        return not self == other

    # wyświetlanie wielomianu
    def __str__(self):
        if self.is_zero():
            return "0"
        elements = []

        for k in sorted(self.coefficients.keys(), reverse=True):
            coeff = self.coefficients[k]
            sign = " + " if coeff.real >= 0 else " - "
            coeff_str = f"({coeff})" if isinstance(coeff, complex) else ("" if abs(coeff) == 1 and k != 0 else str(abs(coeff)))
            if k == 0:
                elements.append(f"{sign}{coeff_str}")
            elif k == 1:
                elements.append(f"{sign}{coeff_str}x")
            else:
                elements.append(f"{sign}{coeff_str}x^{k}")
        result = "".join(elements)
        return result.lstrip(" +")

    # przeciążenie [] (odczyt współczynnika wielomianu przy danej potędze x)
    def __getitem__(self, index):
            return self.coefficients.get(index, 0)

    # przeciążenie operatora + (dodawania stałej do wielomianu lub dodawania dwóch wielomianów)
    def __add__(self, other):
        if isinstance(other, (int, float)):
            result = self.coefficients.copy()
            result[0] = result.get(0, 0) + other
            return Polynomial(result)
        result = self.coefficients.copy()
        for k, coeff in other.coefficients.items():
            result[k] = result.get(k, 0) + coeff
        return Polynomial(result)

    def __radd__(self, other):
        return self + other

    # przeciążenie operatora - (odejmowania stałej od wielomianu lub odejmowania dwóch wielomianów)
    def __sub__(self, other):
        if isinstance(other, (int, float)):
            result = self.coefficients.copy()
            result[0] = result.get(0, 0) - other
            return Polynomial(result)
        result = self.coefficients.copy()
        for k, coeff in other.coefficients.items():
            result[k] = result.get(k, 0) - coeff
        return Polynomial(result)

    def __rsub__(self, other):
        return Polynomial({0: other}) - self

    # przeciążenie operatora * (mnożenia dwóch wielomianów)
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = {k: coeff * other for k, coeff in self.coefficients.items()}
            return Polynomial(result)
        result = {}
        for k1, coeff1 in self.coefficients.items():
            for k2, coeff2 in other.coefficients.items():
                result[k1 + k2] = result.get(k1 + k2, 0) + coeff1 * coeff2
        return Polynomial(result)

    def __rmul__(self, other):
        return self * other

    # obliczanie wartości wielomianu dla podanej wartości x (Algorytm Hornera)
    def __call__(self, x):
        result = 0
        max_degree = self.degree()
        for k in range(max_degree, -1, -1):
            result = result * x + self.coefficients.get(k, 0)
        return result

    # całkowanie wielomianu
    def integrate(self, constant=0):
        result = {k + 1: coeff / (k + 1) for k, coeff in self.coefficients.items()}
        result[0] = constant
        return Polynomial(result)

    # różniczkowanie wielomianu
    def differentiate(self):
        result = {k - 1: k * coeff for k, coeff in self.coefficients.items() if k > 0}
        return Polynomial(result)





