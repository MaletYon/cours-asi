"""Construit les présentations : python run.py ASI 1 3 5   (ou: python run.py ASI all)."""
import sys, os, importlib.util
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from slides import Deck
from courses import ALL

LABS = {
    "ASI": {
        "LAB-01": "Construire la cartographie des risques de LiZbiZ",
        "LAB-02": "Analyser la matrice des droits de LiZbiZ",
        "LAB-03": "Coter les documents sollicités, dimensionner les échantillons",
        "LAB-04": "Contrôler une décomposition du domaine D",
        "LAB-05": "Mesurer, situer et comparer les domaines de LiZbiZ",
        "LAB-06": "Audit de conformité des paiements de l'ANPP",
        "LAB-07": "Tests substantifs sur les données de LiZbiZ",
        "LAB-08": "Audit d'infrastructure des quatre centres de LiZbiZ",
        "LAB-09": "Auditer la continuité du système central de la BANQUE SANAGA",
        "LAB-10": "Synthèse des trois cas",
    },
}

HERE = os.path.dirname(os.path.abspath(__file__))


def load(sigle, name):
    path = os.path.join(HERE, "specs", sigle, name + ".py")
    spec = importlib.util.spec_from_file_location(f"{sigle}_{name}", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.SPEC


def complete(sigle, day, spec):
    c = ALL[sigle]
    theme, contenu, ateliers, labs = c["jours"][day]
    for d in spec:
        if d["k"] == "maison":
            d.setdefault("ateliers", [f"**Atelier {a}** : fiche {sigle}-FICHE-{a}" for a in ateliers])
            d.setdefault("labs", [f"**{sigle}-{l}** : {LABS[sigle][l]}" for l in labs])
    return spec


def build_day(sigle, day):
    c = ALL[sigle]
    spec = complete(sigle, day, load(sigle, f"J{day:02d}"))
    deck = Deck(c, day)
    out = os.path.join(c["dossier"], f"{sigle}_J{day:02d}.pptx")
    n = deck.build(spec, out)
    print(f"{out}  ({n} diapositives)")


def build_global(sigle):
    c = ALL[sigle]
    spec = load(sigle, "J00")
    deck = Deck(c, None)
    out = os.path.join(c["dossier"], f"{sigle}_00_vision_globale.pptx")
    n = deck.build(spec, out)
    print(f"{out}  ({n} diapositives)")


if __name__ == "__main__":
    sigle = sys.argv[1]
    days = sys.argv[2:]
    if days == ["all"]:
        days = ["0"] + [str(i) for i in range(1, ALL[sigle].get("n_jours", 15) + 1)]
    for dd in days:
        if int(dd) == 0:
            build_global(sigle)
        else:
            build_day(sigle, int(dd))
