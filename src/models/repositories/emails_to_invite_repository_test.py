import pytest #  type: ignore
import uuid
from .emails_to_invite_repository import EmailsToInviteRepository
from src.models.settings.db_connection_handler import db_connection_handler


db_connection_handler.connect()
trip_id = str(uuid.uuid4())

def test_registry_email(): 
  conn = db_connection_handler.get_connection()
  emails_to_invite_repository = EmailsToInviteRepository(conn)
  
  email_trips_info = {
    "id": str(uuid.uuid4()),
    "email": "mariana@email.com",
    "trip_id": trip_id
  }
  
  emails_to_invite_repository.registry_email(email_trips_info)

def test_find_emails_from_trip(): 
  conn = db_connection_handler.get_connection()
  emails_to_invite_repository = EmailsToInviteRepository(conn)
  
  emails_to_invite_repository.find_emails_from_trip(trip_id)