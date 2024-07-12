from typing import Dict
import uuid


class ActivityCreator:
  def __init__(self, activities_repository) -> None:
    self.__activities_repository = activities_repository

  def create(self, body, trip_id) -> Dict:
    try:
      activity_id = str(uuid.uuid4())
      
      activity_infos = {
        "title": body["title"],
        "id": activity_id,
        "trip_id": trip_id,
        "occurs_at": body["occurs_at"]
      }
    
      self.__activities_repository.registry_activity(activity_infos)

      return {
        "body": { "id": activity_id },
        "status_code": 201
      }
    except Exception as exception:
      return {
        "body": { "error": "Bad Request", "message": str(exception) },
        "status_code": 400
      }
