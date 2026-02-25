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

### Output 6ème question:

```bash
>>> for q in qs:
...   q.question_text, [x for x in q.choice_set.all().order_by("-votes").values()]
...
('Quel type de repas préférez-vous pour le dîner ?', [{'id': 1, 'question_id': 1, 'choice_text': 'Un plat asiatique prêt à consommer (nouilles, ramen, etc.)', 'votes': 2}, {'id': 2, 'question_id': 1, 'choice_text': 'Un plat frais à cuisiner rapidement (viande/poisson + accompagnement simple)', 'votes': 2}, {'id': 3, 'question_id': 1, 'choice_text': 'Un plat rapide à réchauffer (surgelés, conserves)', 'votes': 2}])
('Quel outil utilisez-vous le plus pour organiser vos projets ?', [{'id': 5, 'question_id': 2, 'choice_text': 'Backlog Kanban (Trello, Jira, etc.)', 'votes': 4}, {'id': 6, 'question_id': 2, 'choice_text': 'Un simple fichier texte ou tableau', 'votes': 3}, {'id': 4, 'question_id': 2, 'choice_text': 'Diagrammes de Gantt', 'votes': 0}])
('Comment gérez-vous vos tâches quotidiennes ?', [{'id': 7, 'question_id': 3, 'choice_text': 'Avec une liste papier ou un carnet', 'votes': 2}, {'id': 8, 'question_id': 3, 'choice_text': 'Avec une application dédiée (Todoist, Notion, etc.)', 'votes': 2}, {'id': 9, 'question_id': 3, 'choice_text': 'Je n’ai pas de méthode fixe', 'votes': 1}])
('Quelle activité vous aide le plus à décompresser après une journée de travail ?', [{'id': 11, 'question_id': 4, 'choice_text': 'Un moment de détente (lecture, musique, série)', 'votes': 3}, {'id': 10, 'question_id': 4, 'choice_text': 'Une activité physique (sport, marche)', 'votes': 2}, {'id': 12, 'question_id': 4, 'choice_text': 'Un projet personnel (codage, bricolage, etc.)', 'votes': 0}])
('Quel format préférez-vous pour apprendre de nouvelles compétences ?', [{'id': 14, 'question_id': 5, 'choice_text': 'Des articles ou documentations écrites', 'votes': 4}, {'id': 13, 'question_id': 5, 'choice_text': 'Des tutoriels vidéo (YouTube, Udemy)', 'votes': 1}, {'id': 15, 'question_id': 5, 'choice_text': 'Des ateliers ou formations en présentiel', 'votes': 1}])
```

### Output 7ème question:

```bash
>>> qs : Question.objects.all().order_by("id")
>>> for q in qs:
...   q
...
<Question: Quel type de repas préférez-vous pour le dîner ?>
<Question: Quel outil utilisez-vous le plus pour organiser vos projets ?>
<Question: Comment gérez-vous vos tâches quotidiennes ?>
<Question: Quelle activité vous aide le plus à décompresser après une journée de travail ?>
<Question: Quel format préférez-vous pour apprendre de nouvelles compétences ?>
```

### Output 8ème question:

```bash
>>> Question.objects.filter(question_text__contains="vous")
<QuerySet [<Question: Quel type de repas préférez-vous pour le dîner ?>, <Question: Quel outil utilisez-vous le plus pour organiser vos projets ?>, <Question: Comment gérez-vous vos tâches quotidiennes ?>, <Question: Quelle activité vous aide le plus à décompresser après une journée de travail ?>, <Question: Quel format préférez-vous pour apprendre de nouvelles compétences ?>]>
>>>
```

### Output 9ème question:

```bash
>>> from django.utils import timezone
>>> create_question = Question(question_text="Allez vous bien ?", pub_date=timezone.now())
>>> create_question.save()
>>> Question.objects.all()
<QuerySet [<Question: Quel type de repas préférez-vous pour le dîner ?>, <Question: Quel outil utilisez-vous le plus pour organiser vos projets ?>, <Question: Comment gérez-vous vos tâches quotidiennes ?>, <Question: Quelle activité vous aide le plus à décompresser après une journée de travail ?>, <Question: Quel format préférez-vous pour apprendre de nouvelles compétences ?>, <Question: Allez vous bien ?>]>
```
