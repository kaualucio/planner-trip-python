import uuid
from typing import Dict

from src.drivers.email_sender import send_mail

class TripCreator:
  def __init__(self, trips_repository, emails_repository) -> None:
    self.__trips_repository = trips_repository
    self.__emails_repository = emails_repository
    
  def create(self, body) -> Dict:
    try:
      
      emails = body.get('emails_to_invite')
      
      trip_id = str(uuid.uuid4())
      trip_infos = { **body, "id": trip_id } 
      
      self.__trips_repository.create_trip(trip_infos)
      
      if emails:
        for email in emails:
          self.__emails_repository.registry_email({
            "id": str(uuid.uuid4()),
            "trip_id": trip_id,
            "email": email
          })

      send_mail(
        [body['owner_email']],
        f'https://localhost:3000/trips/{trip_id}/confirm'
        )
      
      return {
        "body": { "id": trip_id },
        "status_code": 201
      }
    except Exception as exception:
       return {
        "body": { "error": "Bad Request", "message": str(exception) },
        "status_code": 400
      }
    