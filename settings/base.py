# python modules
from argparse import ArgumentParser

# user-defined modules
from database import connection

# command-line arguments
parser = ArgumentParser()

parser.add_argument("--settings",
                    choices=['local', 'develop'],
                    help="Required argument: --settings")

args = parser.parse_args()

if args.settings == "local":
    from settings import local as settings
    conn = connection.DataBaseConnector(settings.DB_NAME, settings.DB_USER,
                                        settings.DB_PASSWORD,
                                        settings.DB_HOST).get_connection()
elif args.settings == "develop":
    from settings import develop as settings
    conn = connection.DataBaseConnector(settings.DB_NAME, settings.DB_USER,
                                        settings.DB_PASSWORD,
                                        settings.DB_HOST).get_connection()
else:
    raise SystemExit("Invalid `--settings` argument.")
