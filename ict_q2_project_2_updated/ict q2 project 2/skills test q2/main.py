from pyscript import document

# each key is an element symbol
# each value is (name, atomic number, atomic mass)
non_metals = {
    "H": ("Hydrogen", 1, 1.008),
    "He": ("Helium", 2, 4.0026),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "F": ("Fluorine", 9, 18.998),
    "Ne": ("Neon", 10, 20.180),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.06),
    "Cl": ("Chlorine", 17, 35.45),
    "Ar": ("Argon", 18, 39.948),
    "Se": ("Selenium", 34, 78.971),
    "Br": ("Bromine", 35, 79.904),
    "Kr": ("Krypton", 36, 83.798),
    "I": ("Iodine", 53, 126.90),
    "Xe": ("Xenon", 54, 131.29),
    "At": ("Astatine", 85, 210),
    "Rn": ("Radon", 86, 222),
    "Og": ("Oganesson", 118, 294),
    "Yg": ("Yuogliptonium", 246, 587)  # made-up element from the club story
}


def check_details(e):
    # clear the old result first
    document.getElementById('result').innerHTML = " "

    # get the symbol the user typed, remove spaces, and fix the capitals
    # (so "cl" or "CL" becomes "Cl")
    symbol = document.getElementById('element_input').value.strip().title()

    # look up the symbol, or use these default values if it isn't found
    name, number, mass = non_metals.get(
        symbol,
        ("Element does not exist in the non-metals list", "-", "-")
    )

    # show the details of the element on the page
    document.getElementById('result').innerHTML = f"""
        <b>Symbol:</b> {symbol}<br>
        <b>Element:</b> {name}<br>
        <b>Atomic Number:</b> {number}<br>
        <b>Atomic Mass:</b> {mass}<br>
    """
