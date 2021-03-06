"""
    py_lx6
    Raspberry Pi base hand controller for Meade LX-6 telescopes

    Copyright (C) 2020  Sven Coenye

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or any
    later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import RPi.GPIO as GPIO


class Button:
    """
    A single on/off button
    """

    def __init__(self, pin):
        self._pin = pin
        self._state = 0

    def _output(self):
        # Set the GPIO pin according to the button state
        GPIO.output(self._pin, self._state)

    def on(self):
        """
        Press the button
        """
        self._state = 1
        self._output()

    def off(self):
        """
        Release the button
        """
        self._state = 0
        self._output()

    def toggle(self):
        """
        Switch the state of the button
        :return:
        """
        self._state = 1 - self._state
        self._output()


class JoinedButton(Button):
    """
    On/off button which can turn a paired button off
    """
    def __init__(self, pin):
        """
        :param pin: GPIO pin controlled by this button
        """
        super().__init__(pin)
        self._other = None

    def join(self, other):
        """
        Connect the paired button. This method must be called before turning the button on.
        :param other:
        :return:
        """
        self._other = other

    def on(self):
        """
        Turn off the other button and turn off this one,
        :return:
        """
        # TODO: raise explanatory exception on missing _other
        self._other.off()
        super().on()

    def toggle(self):
        """
        Toggle the button state. Turns off the other button in case this one goes high.
        :return:
        """
        if self._state == 0:		# We're going high, turn off the other button.
            self._other.off()
            self.on()
        else:
            self.off()


class ButtonPair:
    """
    Two buttons working in tandem. Both can be off but only one can be on at any time.
    """

    def __init__(self, pin1, pin2):
        self._buttons = (JoinedButton(pin1), JoinedButton(pin2))
        self._buttons[0].join(self._buttons[1])
        self._buttons[1].join(self._buttons[0])

    def __getitem__(self, item):
        return self._buttons[item]
