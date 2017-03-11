To create translations from scratch:
1) cd to the app folder, 
2) wrap words like this: {{ _('word')}}
3) pybabel extract -F babel.cfg -o messages.pot .
4) pybabel init -i messages.pot -d translations -l ru
5) pybabel compile -d translations

To update translations:
1) cd to the app folder, 
2) wrap words like this: {{ _('word')}}
3) pybabel extract -F babel.cfg -o messages.pot .
   pybabel update -i messages.pot -d translations
	translate...
   pybabel compile -d translations