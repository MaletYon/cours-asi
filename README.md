# Audit des Systèmes d'Information (ASI)

[← Tous les cours de MaletYon](https://github.com/maletyon) · [Livre (PDF)](ASI_main.pdf) · [Présentations](Présentation/) · [Fiches par chapitre](fiches/) · [Corrigés](correction/README.md)

**UE INF3226** · École Nationale Supérieure Polytechnique de l'Université de Yaoundé I · Département de Génie Informatique · 60 heures
Auteur : MINKA MI NGUIDJOÏ Thierry Emmanuel, enseignant-chercheur (LIMSI, ENSPY) · contact : maletyon@proton.me · année académique 2026-2027

> *Ce que l'organisation ignore de ses propres systèmes conditionne la qualité des décisions qu'elle peut prendre à leur sujet.*

Pour la plupart des élèves ingénieurs, ce cours est le seul consacré à l'audit, au contrôle interne, à la gestion des risques, à l'audit de sécurité et à l'audit de conformité. Il est autoportant. Il va du cas concret vers la méthode, de la méthode vers la pratique, et de la pratique vers la recherche. Il admet, à côté de OUI et de NON, une troisième réponse : NEK, « connaissance insuffisante », et lit chaque domaine avec trois mesures (conformité µ, incertitude U, entropie H). Trois missions fictives servent de fil rouge : LiZbiZ (logistique, cabinet AUDIX CONSEIL), la BANQUE SANAGA et l'ANPP (Chambre des comptes). Les noms et les montants sont fictifs ; les normes et les textes de loi sont cités d'après leur version officielle.

## Ce que contient ce dépôt

| Élément | Où | Description |
|---|---|---|
| Le livre du cours | [`ASI_main.pdf`](ASI_main.pdf) | Traité complet (prologue, six parties, 31 chapitres, annexes), compilé depuis [`ASI_main.tex`](ASI_main.tex) |
| Les présentations | [`Présentation/`](Présentation/) | 31 présentations PowerPoint : vision d'ensemble et 30 séances de 2 heures, avec notes du présentateur |
| Les fiches d'exercices | [`fiches/`](fiches/) | 32 fiches de 40 questions au format texte, une par chapitre (prologue compris) |
| Le livret de correction | [`correction/`](correction/) | Accès réservé : voir la page du dossier |
| Les sources LaTeX | `front/`, `partie0/` à `partie6/`, `annexes/`, `bibliographie/`, `figures/`, [`Style_ASI.sty`](Style_ASI.sty) | Sources du livre |

## Organisation du cours (60 heures, 30 séances de 2 heures)

| Partie | Chapitres | Séances | Fichiers |
|---|---|---|---|
| **Prologue** | Quarante-cinq questions et aucune réponse fiable | J01 | [`partie0/`](partie0/) |
| **I. Fondements** | 1. Auditer, contrôler, donner une assurance · 2. Grandes défaillances · 3. Contrôle interne · 4. Le risque · 5. Gérer les risques · 6. La fraude | J02 – J07 | [`partie1/`](partie1/) |
| **II. Méthode de la mission** | 7. La mission · 8. Préparer et planifier · 9. Décomposer · 10. Collecter la preuve · 11. Conclure et rédiger · 12. Suivre | J08 – J13 | [`partie2/`](partie2/) |
| **III. Cadre normatif, juridique et déontologique** | 13. Normes professionnelles · 14. Référentiels · 15. Cadre juridique · 16. Déontologie | J14 – J17 | [`partie3/`](partie3/) |
| **IV. Pratique de l'audit des SI** | 17. Gouvernance · 18. Applications · 19. Projets · 20. SMSI · 21. Sécurité technique · 22. Tests d'intrusion et code · 23. Production et continuité · 24. Tiers et nuage · 25. Conformité · 26. Cas intégrateurs | J18 – J27 | [`partie4/`](partie4/) |
| **V. Défis avancés** | 27. Audit continu · 28. Intelligence artificielle · 29. De l'audit à la preuve judiciaire | J28 – J29 | [`partie5/`](partie5/) |
| **VI. Recherche : l'auditologie** | 30. Objet, axiomes et piliers · 31. Mesurer l'incertitude et la stratégie | J30 | [`partie6/`](partie6/) |
| **Annexes** | A. Glossaire · B. Outils · C. Modèles · D. Textes juridiques et normatifs · E. Bibliographie commentée · F. Contacts | | [`annexes/`](annexes/) |

Chaque chapitre compte dix exercices gradués ; leurs corrigés, et ceux des fiches, sont dans le livret de correction. Les fiches et les labs se font hors des 60 heures.

## NDAP SUKULU, la salle de classe compagnon

*Ndap sukulu* signifie « la salle de classe » en bassa, et *Malet Yon* « ton enseignant ». NDAP SUKULU est l'environnement compagnon du cours : une fiche d'auto-évaluation de 40 questions par chapitre, corrigée automatiquement, des labs sur pièces et un tableau de bord de progression. Le code de cours est **INF3226**.

> **NDAP SUKULU en local.** La version téléchargeable et installable sur votre poste, avec un module autonome pour ce cours, est en cours de finalisation. En attendant, les fiches d'auto-évaluation de chaque chapitre (40 questions) sont fournies au format texte dans [`fiches/`](fiches/).

| Lab | Chapitre | Sujet |
|---|---|---|
| ASI-LAB-01 | 4 | Construire la cartographie des risques de LiZbiZ |
| ASI-LAB-02 | 3 | Analyser la matrice des droits de LiZbiZ |
| ASI-LAB-03 | 8 | Coter les documents sollicités, dimensionner les échantillons |
| ASI-LAB-04 | 9 | Contrôler une décomposition du domaine D |
| ASI-LAB-05 | 11 | Mesurer, situer et comparer les domaines |
| ASI-LAB-06 | 15 | Audit de conformité des paiements de l'ANPP |
| ASI-LAB-07 | 18 | Tests substantifs sur les données |
| ASI-LAB-08 | 21 | Audit d'infrastructure des quatre centres |
| ASI-LAB-09 | 23 | Auditer la continuité du système central de la BANQUE SANAGA |
| ASI-LAB-10 | 26 | Synthèse des trois cas |

## Compiler le livre

Avec une distribution LaTeX : `pdflatex ASI_main`, `biber ASI_main`, `makeindex ASI_main`, puis deux fois `pdflatex ASI_main`.
Les présentations se régénèrent avec `python Présentation/_sources/gen_specs.py` puis `python Présentation/_sources/run.py ASI all` (Python 3 et python-pptx).

## Recherche

La méthode du cours s'appuie sur deux prépublications déposées sur HAL : *Vers l'auditologie* (A0, `hal-05701007`) et l'instrument OUI/NON/NEK (A1, `hal-05701270`). Les autres appuis sont des travaux publiés et vérifiables, listés dans la bibliographie du livre.

## Normes et documents sous licence

Les normes ISO/IEC et les autres documents sous licence cités dans le cours **ne sont pas fournis** dans ce dépôt.

## Licence

Contenu pédagogique : [CC BY-NC-SA 4.0](LICENSE.md). Code du générateur de présentations : MIT. Voir [`LICENSE.md`](LICENSE.md).
