from sqlite3 import Connection
from typing import Dict, List, Tuple

class ParticipantRepository:
  def __init__(self, conn: Connection) -> None:
    self.__conn = conn

  def registry_participant(self, parcipant_infos: Dict) -> None:
    cursor = self.__conn.cursor()
    cursor.execute(
      '''
        INSERT INTO participants 
          (id, trip_id, emails_to_invite_id, name)
          VALUES (?, ?, ?, ?)
      ''', (
        parcipant_infos['id'],
        parcipant_infos['trip_id'],
        parcipant_infos['emails_to_invite_id'],
        parcipant_infos['name'],
      )
    )

    self.__conn.commit()
  
  def find_participats_from_trip(self, trip_id: str) -> List[Tuple]:
    cursor = self.__conn.cursor()
    cursor.execute(
        '''
        SELECT p.id, p.name, p.is_confirmed, e.email FROM participants as p
          JOIN emails_to_invite as e on e.id = p.emails_to_invite_id
          WHERE p.trip_id = ?
        ''', (trip_id,)
    )

    participants = cursor.fetchall()
    return participants

  def update_participant_status(self, participant_id: str) -> None:
    cursor = self.__conn.cursor()
    cursor.execute(
        '''
          UPDATE participants 
            SET is_confirmed = 1
          WHERE
            id = ?
        ''', (participant_id,)
    )
    self.__conn.commit()
