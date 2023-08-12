#!/usr/bin/env python3

from ..models import db, Swimmer, Team, Event, Time
from flask_migrate import Migrate
from flask import Flask, request, make_response
from flask_restful import Api, Resource
import os
import pdb


def generate_lineup(team_id1, team_id2):
    events = Event.query.all()
    lineup = {}

    for event in events:
        lineup[event.id] = {}

        for team_id in [team_id1, team_id2]:
            team_lineup = (
                Swimmer.query.filter_by(team_id=team_id)
                .join(Time)
                .filter(Time.event_id == event.id)
                .order_by(Time.time)
                .limit(3)  # Select the top 3 swimmers for each team.
                .all()
            )

            lineup[event.id][team_id] = team_lineup

    return lineup
pdb.set_trace()