from typing import Dict
import uuid


class LinkCreator:
  def __init__(self, links_repository) -> None:
    self.__links_repository = links_repository
    
  def create_link(self, body, trip_id) -> Dict:
    try:
      link_id = str(uuid.uuid4())
      link_infos = {
        "link": body["url"],
        "title": body["title"],
        "trip_id": trip_id,
        "id": link_id
      }
      
      self.__links_repository.registry_link(link_infos)
      
      return {
        "body": {
          "id": link_infos
        },
        "status_code": 201
      }
    except Exception as exception:
       return {
        "body": { "error": "Bad Request", "message": str(exception) },
        "status_code": 400
      }