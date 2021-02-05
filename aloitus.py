def ympyran_ala(halkaisija):
    """Funktio laskee ympyrän pinta-alan halkaisijan perusteella

    Args:
        halkaisija (float): Ympyrän halkaisija

    Returns:
        float: Ympyrän pinta-ala
    """
    sade = halkaisija / 2
    pinta_ala = sade ** 2 * 3.14159
    return pinta_ala

kayttaja = "Markku"
kaupungit = ["Raisio", "Turku", "Lieto", "Kaarina"]
print("Metrin halkaisijaltaan olevan ympyrän pinta-ala on", ympyran_ala(1))