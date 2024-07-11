import pytest #  type: ignore
import uuid
from .links_repository import LinksRepository
from src.models.settings.db_connection_handler import db_connection_handler


db_connection_handler.connect()
link_id = str(uuid.uuid4())
trip_id = str(uuid.uuid4())

def test_registry_link(): 
  conn = db_connection_handler.get_connection()
  links_repository = LinksRepository(conn)
  
  link_infos = {
    "id": link_id,
    "trip_id": trip_id,
    "link": "http://localhost:3000/links",
    "title": "Links Viagem"
  }
  
  links_repository.registry_link(link_infos)

def test_find_links_from_trip(): 
  conn = db_connection_handler.get_connection()
  links_repository = LinksRepository(conn)
  
  response = links_repository.find_links_from_trip(trip_id)
  
  assert isinstance(response, list)
  assert isinstance(response[0], tuple)