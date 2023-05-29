import asyncio
import unittest
from unittest.mock import AsyncMock

from aioemit import Emitter, Event


async def async_callback(event: Event):
    func = asyncio.Future()
    func.set_result(event)
    return func


class EmitterTestCase(unittest.TestCase):
    def setUp(self):
        self.emitter = Emitter()

    def test_subsribere_and_emit_event(self):
        event_type = "created"
        data = {"username": "foobar", "email": "john@example.com"}
        event = Event(event_type, data)
        observer = AsyncMock()
        self.emitter.subscribe(event_type, observer)
        asyncio.run(self.emitter.emit(event))

        observer.assert_called_once_with(event)

    def test_unsubsribe_event(self):
        event_type = "created"
        data = {"username": "foobar", "email": "john@example.com"}
        event = Event(event_type, data)
        observer = AsyncMock()
        self.emitter.subscribe(event_type, observer)
        self.emitter.unsubscribe(event_type, observer)
        asyncio.run(self.emitter.emit(event))

        observer.assert_not_called()


if __name__ == "__main__":
    unittest.main()
