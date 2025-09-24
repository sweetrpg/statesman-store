from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="statesman-store",
    install_requires=[
        "flask~=3.0",
        "flask-dotenv",
        "flask-executor",
        "flask-inputs",
        "flask-migrate~=4.0",
        "flask-redis",
        "flask-script",
        "flask-session",
        "flask-sqlalchemy~=3.0",
        "jsonschema",
        "pika",
        "psycopg2",
        "python-dotenv",
        "pyyaml",
        "redis~=6.0",
        "requests",
        "sentry-sdk[flask]",
    ],
    extras_require={},
)
