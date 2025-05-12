from company_blog import db
from company_blog.models import User

db.drop_all()
db.create_all()

admin = User(email="admin_user@test.com", username="Admin User", password="123", administrator="1")
user = User(email="user@test.com", username="ito User", password="123", administrator="0")
db.session.add_all([admin, user])
db.session.commit()