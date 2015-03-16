
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "a4c55ba4-f58d-435d-a83c-2df7ba35b68e36da57fd-d009-41ec-8530-8aebc053229cc67244b2-723a-4ee9-9c5c-0bde0f247ebe"
NEVERCACHE_KEY = "826d5e1b-1783-4f91-8f0f-e00e6bfe28813d654fc5-30ad-4d01-8190-c497523d1936588cffe2-b334-490a-a84b-201ea510cc1f"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
