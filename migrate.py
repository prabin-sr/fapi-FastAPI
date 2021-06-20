# user-defined modules
from settings.base import conn
from users.models import User


# Initialize Connection
conn.connect()

# Migration: 1
conn.create_tables([User])

# Migration: 2
# conn.db.create_tables([models.User, models.Item])

# Close Connection
conn.close()
