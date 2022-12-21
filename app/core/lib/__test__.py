import unittest
from event import EventEmitter


class Counter(EventEmitter):
    def __init__(self) -> None:
        super().__init__()
        self.number = 0

    def add(self, quantity=1):
        self.number += quantity
        self.emit("add", self.number)

    def subtract(self, quantity=1):
        self.number -= quantity
        self.emit("subtract", self.number)

    def reset(self):
        self.number = 0
        self.emit("reset", self.number)


class TestEventEmitter(unittest.TestCase):

    def test_constructor(self):
        target = Counter()
        self.assertIsInstance(target, EventEmitter)
        self.assertEqual(target.number, 0)

    def test_add(self):
        target = Counter()
        target.on("add", lambda x: self.assertEqual(x, 1))
        target.add()

    def test_subtract(self):
        target = Counter()
        target.on("subtract", lambda x: self.assertEqual(x, -1))
        target.subtract()

    def test_removeEvent(self):
        target = Counter()
        count = 0

        def listener(x):
            nonlocal count
            count += x
        target.on("add", listener)
        target.add(2)
        self.assertEqual(count, 2)
        target.removeEvent("add", listener)
        target.add(2)
        self.assertEqual(count, 2)

    def test_removeAllEvents(self):
        target = Counter()
        counter1 = 0
        counter2 = 0

        def listener1(x):
            nonlocal counter1
            counter1 += x

        def listener2(x):
            nonlocal counter2
            counter2 += x*2

        target.on("add", listener1)
        target.on("add", listener2)
        target.add(2)
        self.assertEqual(counter1, 2)
        self.assertEqual(counter2, 4)
        target.removeAllEvents("add")
        target.add(2)
        self.assertEqual(counter1, 2)
        self.assertEqual(counter2, 4)

    def test_once(self):
        target = Counter()
        counter = 0

        def handle_add(x):
            nonlocal counter
            counter += x

        def handle_reset(x):
            nonlocal counter
            counter = x

        target.on("add", handle_add)
        target.add(2)
        self.assertEqual(counter, 2)
        target.once("reset", handle_reset)
        target.reset()
        self.assertEqual(counter, 0)


if __name__ == "__main__":
    unittest.main()
