from backend.database import SessionLocal
from backend.models import Admin

db = SessionLocal()

admin = db.query(Admin).filter(Admin.username == "admin").first()

if not admin:
    admin = Admin(
        username="admin",
        password="admin123"
    )
    db.add(admin)
    db.commit()
    print("✅ Admin created successfully.")
else:
    print("✅ Admin already exists.")

db.close()