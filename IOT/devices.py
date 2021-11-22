from device import Device
from message import MessageType


class HueLight(Device):
    def connect(self) -> None:
        print("Connecting Hue Light")

    def disconnect(self) -> None:
        print("Disconnecting Hue Light")

    def send_message(self, message_type: MessageType, data: str) -> None:
        print(
            f"Hue light handling message of type {message_type.name} with data [{data}]")

    def status_update(self) -> str:
        return "hue_light_status_OK"


class SmartSpeaker(Device):
    def connect(self) -> None:
        print("Connecting Smart Speaker")

    def disconnect(self) -> None:
        print("Disconnecting Smart Speaker")

    def send_message(self, message_type: MessageType, data: str) -> None:
        print(
            f"Smart Speaker handling message of type {message_type.name} with data [{data}]")

    def status_update(self) -> str:
        return "Smart_Speaker_status_OK"


class Curtains(Device):
    def connect(self) -> None:
        print("Connecting Curtains")

    def disconnect(self) -> None:
        print("Disconnecting Curtains.")

    def send_message(self, message_type: MessageType, data: str) -> None:
        print(
            f"Curtains handling message of type {message_type.name} with data [{data}]")

    def status_update(self) -> str:
        return "Curtains_status_OK"