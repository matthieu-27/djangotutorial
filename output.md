### Output 1ère boucle for:

```bash
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

```bash
>>> for i in q:
...   print(i) if i.pub_date.year == 2026 else print()
...

Quel outil utilisez-vous le plus pour organiser vos projets ?
Comment gérez-vous vos tâches quotidiennes ?
Quelle activité vous aide le plus à décompresser après une journée de travail ?
Quel format préférez-vous pour apprendre de nouvelles compétences ?
>>>
```

### Output 3ème question:

```bash
>>> choices = Choice.objects.filter(question_id=2)
>>> for i in choices:
...   print(i.question)
...   print(i.choice_text)
...   print(i.votes)
...
Quel outil utilisez-vous le plus pour organiser vos projets ?
Diagrammes de Gantt
0
Quel outil utilisez-vous le plus pour organiser vos projets ?
Backlog Kanban (Trello, Jira, etc.)
0
Quel outil utilisez-vous le plus pour organiser vos projets ?
Un simple fichier texte ou tableau
0
```

### Output 4ème question:

```bash
>>> qs = Question.objects.all()
>>> for q in qs:
...   q.question_text, [x for x in q.choice_set.all()]
...
('Quel type de repas préférez-vous pour le dîner ?', [<Choice: Un plat asiatique prêt à consommer (nouilles, ramen, etc.)>, <Choice: Un plat frais à cuisiner rapidement (viande/poisson + accompagnement simple)>, <Choice: Un plat rapide à réchauffer (surgelés, conserves)>])
('Quel outil utilisez-vous le plus pour organiser vos projets ?', [<Choice: Diagrammes de Gantt>, <Choice: Backlog Kanban (Trello, Jira, etc.)>, <Choice: Un simple fichier texte ou tableau>])
('Comment gérez-vous vos tâches quotidiennes ?', [<Choice: Avec une liste papier ou un carnet>, <Choice: Avec une application dédiée (Todoist, Notion, etc.)>, <Choice: Je n’ai pas de méthode fixe>])
('Quelle activité vous aide le plus à décompresser après une journée de travail ?', [<Choice: Une activité physique (sport, marche)>, <Choice: Un moment de détente (lecture, musique, série)>, <Choice: Un projet personnel (codage, bricolage, etc.)>])
('Quel format préférez-vous pour apprendre de nouvelles compétences ?', [<Choice: Des tutoriels vidéo (YouTube, Udemy)>, <Choice: Des articles ou documentations écrites>, <Choice: Des ateliers ou formations en présentiel>])
>>>
```

### Output 5ème question:

```bash
>>> for q in qs:
...   q.question_text, len(q.choice_set.all())
...
('Quel type de repas préférez-vous pour le dîner ?', 3)
('Quel outil utilisez-vous le plus pour organiser vos projets ?', 3)
('Comment gérez-vous vos tâches quotidiennes ?', 3)
('Quelle activité vous aide le plus à décompresser après une journée de travail ?', 3)
('Quel format préférez-vous pour apprendre de nouvelles compétences ?', 3)
```
