import asyncio
from collections import defaultdict
from typing import Any, Callable, Dict, List, Optional


class Event:
    def __init__(self, event_type: str, data: Optional[Any]):
        """
        An event with a specified event type and optional data.

        Args:
            event_type (str): The type of the event.
            data (Any, optional): Additional data associated with the event. Defaults to None.
        """
        self.event_type = event_type
        self.data = data

    def __repr__(self) -> str:
        """
        Returns a string representation of the event.

        Returns:
            str: A string representation of the event.
        """
        return f"{self.event_type} {self.data}"


class Emitter:
    def __init__(self) -> None:
        """
        An event emitter that allows subscribing to and emitting events.
        """
        self.subscribers: Dict[str, List[Callable[[Event], None]]] = defaultdict(list)

    def subscribe(self, event_type: str, observer: Callable[[Event], None]):
        """
        Subscribes an observer function to a specific event type.

        Args:
            event_type (str): The type of the event to subscribe to.
            observer (Callable[[Event], None]): The observer function to be called when the event is emitted.
        """
        self.subscribers[event_type].append(observer)

    def unsubscribe(self, event_type: str, observer: Callable[[Event], None]):
        """
        Unsubscribes an observer function from a specific event type.

        Args:
            event_type (str): The type of the event to unsubscribe from.
            observer (Callable[[Event], None]): The observer function to be removed from the subscribers list.

        Raises:
            KeyError: If the event type does not exist in the subscribers dictionary.
        """
        if event_type in self.subscribers:
            self.subscribers[event_type].remove(observer)
        else:
            raise KeyError(f"{event_type} does not exist.")

    async def emit(self, event: Event):
        """
        Emits an event, calling all subscribed observer functions asynchronously.

        Args:
            event (Event): The event to be emitted.
        """
        event_type = event.event_type
        coroutines = []
        for observer in self.subscribers[event_type]:
            coroutine = observer(event)
            coroutines.append(coroutine)
        await asyncio.gather(*coroutines)
