from backend.database import SessionLocal
from backend.models import Feedback

db = SessionLocal()

deleted = db.query(Feedback).delete()

db.commit()

print(f"{deleted} feedback records deleted successfully.")

db.close()