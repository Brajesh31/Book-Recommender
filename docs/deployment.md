# Deployment

## Current deployment shape

This project is a single Flask process with in-memory data. At startup, app.py loads four pickle files into memory. It has no database, environment-based configuration, migration process, authentication, or health-check route. A deployment therefore needs the compatible model files and enough memory to hold them, in addition to the Python runtime and web server.

## Production server

Install requirements.txt in a Linux environment and start the WSGI application from the repository root. For example:

~~~sh
gunicorn --workers 2 --bind 0.0.0.0:8000 app:app
~~~

Choose worker count based on available memory because each worker can load its own copy of the artifacts. The command is an example; set the bind address, worker count, process supervision, TLS termination, and resource limits to match the hosting platform. Do not expose Flask's development server or run the app with debug mode enabled in production.

## Release contents

Ensure the deployment checkout contains full Git LFS objects for popular.pkl, pt.pkl, books.pkl, and similarity_scores.pkl. The four files must come from the same model build and match the code's expected data structures. A deployment that receives pointer text instead of model bytes will fail during startup. Keep code and model artifacts synchronized when updating a release.

The app uses relative artifact paths, so configure the service working directory as the project root. Confirm that the templates directory is included in the deployed package.

## Configuration, privacy, and operations

No environment variables are currently read by the application; .env.example does not define runtime settings. Do not put credentials or private values in a public repository. The app prints recommendation results to stdout; review logging behavior before deployment and avoid collecting user-submitted text unnecessarily.

The bundled datasets contain user IDs, locations, ages, and ratings. Review their provenance, terms, and privacy obligations before deploying or redistributing them. Cover images are loaded from remote URLs, so the page depends on those image hosts and on the continued validity of the URLs.

The code currently has no dedicated health, readiness, or metrics endpoints. Monitor process startup and HTTP errors through the hosting platform, and test the recommendation flow against the exact deployed artifact set before routing real traffic.
