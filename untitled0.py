# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 15:14:48 2022

@author: HP
"""

def generate_state():
    return ".....0..0..."

def evolve(stato):
    return stato

def simulation(nsteps):
    initial_state = generate_state()
    states_seq = [initial_state]
    for i in range(nsteps):
        old_state = states_seq[-1]
        new_state = evolve(old_state)
        states_seq.append(new_state)
    return states_seq


def test_generation_valid_state():
    state = generate_state()
    assert set(state) == {'.', '0'}



def test_result():
    state = simulation(nsteps)
    assert isinstance(state, str)