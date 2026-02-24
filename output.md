### Output 1ère boucle for:

```shell
>>> for i in q:
...   print(i)
...
Quel type de repas préférez-vous pour le dîner ?
Quel outil utilisez-vous le plus pour organiser vos projets ?
Comment gérez-vous vos tâches quotidiennes ?
Quelle activité vous aide le plus à décompresser après une journée de travail ?
Quel format préférez-vous pour apprendre de nouvelles compétences ?
```

### Output 2ème boucle for (filtre date):

```shell
>>> for i in q:
...   print(i) if i.pub_date.year == 2026 else print()
...

Quel outil utilisez-vous le plus pour organiser vos projets ?
Comment gérez-vous vos tâches quotidiennes ?
Quelle activité vous aide le plus à décompresser après une journée de travail ?
Quel format préférez-vous pour apprendre de nouvelles compétences ?
>>>
```
