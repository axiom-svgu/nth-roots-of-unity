from sympy import Symbol, exp, I, pi

# Basic variables
n = Symbol('n')  # For representing the nth root
k = Symbol('k')  # For the kth root
z = Symbol('z')  # Complex variable

# Fundamental nth root of unity formula
NTH_ROOT_OF_UNITY = exp((2 * pi * I * k) / n)

# General form for any kth nth root of unity
KTH_ROOT_FORMULA = f"z_{k} = e^{{2\\pi i k/{n}}}"

# Polar form representation
POLAR_FORM = f"z_{k} = \\cos(\\frac{{2\\pi k}}{{{n}}}) + i\\sin(\\frac{{2\\pi k}}{{{n}}})"

# Properties and equations
UNITY_PROPERTY = f"(z_{k})^{n} = 1"
SUM_OF_ROOTS = f"\\sum_{{{k}=0}}^{{{n}-1}} z_{k} = 0"
PRODUCT_OF_ROOTS = f"\\prod_{{{k}=0}}^{{{n}-1}} z_{k} = (-1)^{{n+1}}"

# Common specific roots
PRIMITIVE_ROOT = exp(2 * pi * I / n)
PRINCIPAL_ROOT = exp(2 * pi * I / n)

# LaTeX strings for common values
ROOTS_OF_UNITY_TITLE = "n^{\\text{th}} \\text{ Roots of Unity}"
COMPLEX_PLANE_TITLE = "\\text{Complex Plane}"

# Properties in LaTeX for display
PROPERTIES = [
    "\\text{1. All } n^{\\text{th}} \\text{ roots lie on the unit circle}",
    "\\text{2. The roots are equally spaced by } \\frac{2\\pi}{n} \\text{ radians}",
    "\\text{3. The first root is at angle } \\frac{2\\pi}{n}",
    f"\\text{{4. The }} k^{{\\text{{th}}}} \\text{{ root is at angle }} \\frac{{2\\pi k}}{{{n}}}"
]

# Geometric properties
UNIT_CIRCLE_EQUATION = "x^2 + y^2 = 1"
ANGLE_BETWEEN_ROOTS = f"\\frac{{2\\pi}}{{{n}}}"

# Special cases
SQUARE_ROOTS_OF_UNITY = ["1", "-1"]
CUBE_ROOTS_OF_UNITY = ["1", "-\\frac{1}{2} + i\\frac{\\sqrt{3}}{2}", "-\\frac{1}{2} - i\\frac{\\sqrt{3}}{2}"]
FOURTH_ROOTS_OF_UNITY = ["1", "i", "-1", "-i"]

# Cyclotomic polynomial related
CYCLOTOMIC_POLYNOMIAL = f"\\Phi_{n}(x)"
MINIMAL_POLYNOMIAL = f"x^{n} - 1"

# Additional mathematical constants
EULER_FORMULA = "e^{ix} = \\cos(x) + i\\sin(x)"
DE_MOIVRE_FORMULA = f"(\\cos(\\theta) + i\\sin(\\theta))^{n} = \\cos({n}\\theta) + i\\sin({n}\\theta)"
