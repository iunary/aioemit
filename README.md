# aioemit

aioemit allows you to manage events asynchonosly and notify subscribers when those events occur. It provides a simple way to implement event bus pattern in an event driven architecture application.

## Installation

```bash
pip install aioemit
```

## Usage

### Creating Events

The `Event` class represents an event with a specified event type and optional data. You can create an event by initializing an instance of the `Event` class with the event type and data (if any).

```python
event = Event("example_event", "example_data")
```

### Creating an Emitter

To use the event emitter, create an instance of the `Emitter` class.

```python
emitter = Emitter()
```

### Subscribing to Events

To subscribe to events, use the `subscribe` method of the `Emitter` class. Pass the event type and an observer function that will be called when the event is emitted.

```python
def event_observer(event):
    # Handle the event
    print("Received event:", event)

emitter.subscribe("example_event", event_observer)
```

### Unsubscribing from Events

If you no longer want to receive notifications for a specific event, you can unsubscribe from it using the `unsubscribe` method. Provide the event type and the observer function that you want to remove.

```python
emitter.unsubscribe("example_event", event_observer)
```

### Emitting Events

To emit an event and notify all subscribers, use the `emit` method of the `Emitter` class. Pass the event you want to emit.

```python
event = Event("example_event", "example_data")
await emitter.emit(event)
```

The `emit` method will asynchronously call all the subscribed observer functions that are associated with the event type.


## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code as per the terms of the license.
