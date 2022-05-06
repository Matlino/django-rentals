
1. `docker-compose build`
2. `docker-compose run web python manage.py loaddata rentals_reservations`
3. `docker-compose up`
4. Go to `http://0.0.0.0:8000/`

Run tests
1. `docker-compose run web python manage.py test`