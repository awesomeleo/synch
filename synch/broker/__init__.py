import abc
from typing import Dict


class Broker:
    source_db: Dict

    def __init__(self, source_db: Dict):
        self.source_db = source_db

    @abc.abstractmethod
    def send(self, schema: str, msg: dict):
        """
        send msg to broker
        """
        raise NotImplementedError

    @abc.abstractmethod
    def msgs(self, schema: str, last_msg_id, block: int = None):
        """
        get msgs from broker
        """
        raise NotImplementedError

    @abc.abstractmethod
    def commit(
        self, schema: str,
    ):
        """
        commit mgs
        """
        raise NotImplementedError

    @abc.abstractmethod
    def close(self,):
        raise NotImplementedError
