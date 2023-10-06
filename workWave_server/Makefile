runserver:
	python manage.py runserver --settings=workwave.config.settings.dev

runprod:
	python manage.py runserver --settings=workwave.config.settings.prod

collectprod:
	python manage.py collectstatic --settings=workwave.config.settings.prod

superuserprod:
	python manage.py createsuperuser --settings=workwave.config.settings.prod

migrationsprod:
	python manage.py makemigrations --settings=workwave.config.settings.prod

migrateprod:
	python manage.py migrate --settings=workwave.config.settings.prod