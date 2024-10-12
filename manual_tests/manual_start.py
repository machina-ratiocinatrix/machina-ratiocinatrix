# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from automat import MethodicalMachine


class CoffeeBrewer(object):
    _machine = MethodicalMachine()

    def _heating_element_turn_on(self):
        pass

    @_machine.input()
    def brew_button(self):
        "The user pressed the brew button"

    @_machine.output()
    def _heat_the_heating_element(self):
        "Heat up the heating element, which should cause coffee to happen."
        self._heating_element_turn_on()

    @_machine.state()
    def have_beans(self):
        "In this state, you have some beans."
    @_machine.state(initial=True)
    def dont_have_beans(self):
        "In this state, you don't have any beans."

    @_machine.input()
    def put_in_beans(self):
        "The user put in some beans."

    # When we don't have beans, upon putting in beans, we will then have beans
    # (and produce no output)
    dont_have_beans.upon(put_in_beans, enter=have_beans, outputs=[])

    # When we have beans, upon pressing the brew button, we will then not have
    # beans anymore (as they have been entered into the brewing chamber) and
    # our output will be heating the heating element.
    have_beans.upon(brew_button, enter=dont_have_beans,
                    outputs=[_heat_the_heating_element])


if __name__ == "__main__":
    coffee_machine = CoffeeBrewer()
    coffee_machine.put_in_beans()
    coffee_machine.brew_button()