from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, Response, request, jsonify,json
)
from werkzeug.exceptions import abort
from werkzeug.security import check_password_hash, generate_password_hash

from fifa.db import get_db

bp = Blueprint('player', __name__)


# @bp.route('/<int:id>/score')
# def player_score(id):
#     db = get_db()
#     cursor = db.cursor()
#     cursor.execute(
#         "SELECT s.Finishing Finishing, s.Volleys Volleys, s.Penalties Penalties, f.Interceptions Interceptions, f.Heading_Accuracy Heading_Accuracy, f.Standing_Tackle Standing_Tackle"
#         " FROM Shooting s"
#         " WHERE ID = %s", id
#     )
#     player = cursor.fetchone()
#     player_score = []
#     for key in player:
#         player_score.append(player[key])
#     return  jsonify(player_score)

@bp.route('/<int:id>/passing')
def passing_func(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "SELECT Vision, Crossing, FK_Accuracy, Short_passing, Long_passing, Crossing"
        " FROM Ball_Passing"
        " WHERE ID = %s", id
    )
    passing = cursor.fetchone()
    passing_list = []
    for key in passing:
        passing_list.append(passing[key])
    return jsonify(passing_list)

@bp.route('/<int:id>/shooting')
def shooting_func(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "SELECT Positioning, Finishing, Shot_power, Long_shots, Volleys, Penalties"
        " FROM Shooting"
        " WHERE ID = %s", id
    )
    shooting = cursor.fetchone()
    shooting_list = []
    for key in shooting:
        shooting_list.append(shooting[key])
    return jsonify(shooting_list)

@bp.route('/<int:id>/defending')
def defending_func(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "SELECT Interceptions, Heading_Accuracy, Marking, Standing_Tackle, Sliding_Tackle"
        " FROM Defending"
        " WHERE ID = %s", id
    )
    defending = cursor.fetchone()
    defending_list = []
    for key in defending:
        defending_list.append(defending[key])
    return jsonify(defending_list)


@bp.route('/<int:id>/dribbling2')
def dribbling2_func(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "SELECT Agility, Balance, Reactions, Ball_Control, Dribbling, Composure"
        " FROM Dribble"
        " WHERE ID = %s", id
    )
    dribbling2 = cursor.fetchone()
    dribbling2_list = []
    for key in dribbling2:
        dribbling2_list.append(dribbling2[key])
    return jsonify(dribbling2_list)
    
@bp.route('/<int:id>/physical')
def physical_func(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "SELECT Jumping, Stamina, Shot_Power, Strength, Aggression"
        " FROM Body_Strength"
        " WHERE ID = %s", id
    )
    physical = cursor.fetchone()
    physical_list = []
    for key in physical:
        physical_list.append(physical[key])
    return jsonify(physical_list)

@bp.route('/<int:id>/gk')
def gk_func(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "SELECT GK_Diving, GK_Handling, GK_Kicking, GK_Positioning, GK_Reflects"
        " FROM GK_Score"
        " WHERE ID = %s", id
    )
    gk = cursor.fetchone()
    gk_list = []
    for key in gk:
        gk_list.append(gk[key])
    return jsonify(gk_list)

@bp.route('/<int:id>/player', methods=('GET', 'POST'))
def index(id):
    g.current = "player"
    db = get_db()
    cursor = db.cursor()
    if request.method == 'POST':
        player_id = request.form['player_id']
        player_id = int(player_id)
        error = None
        if not player_id:
            error = 'Basic information is not complete.'

        cursor.execute(
        "SELECT p.ID ID, p.Age Age, p.Name Name, p.Position Position, n.Nation_Name Nation_Name, p.Value Value, p.Wage Wage, p.Overall Overall, p.Potential Potential, c.Club_Name Club_Name"
        " FROM Player p, Nation n, Club c "
        " WHERE p.Nation_Name = n.Nation_Name AND p.Club_Name=c.Club_Name AND p.id = %s", player_id
        )
        player_detail = cursor.fetchone()

        if player_detail is None:
            # error = 'Player not found'
            cursor.execute(
            "SELECT p.ID ID, p.Age Age, p.Name Name, p.Position Position, n.Nation_Name Nation_Name, p.Value Value, p.Wage Wage, p.Overall Overall, p.Potential Potential, c.Club_Name Club_Name"
            " FROM Player p, Nation n, Club c "
            " WHERE p.Nation_Name = n.Nation_Name AND p.Club_Name=c.Club_Name AND p.id = %s", id
            )
            player_detail = cursor.fetchone()
            return render_template('player.html', id = id, player_detail = player_detail)

        else:
            flash(error)
            player_detail["Value"] = '%.1f' % (player_detail["Value"])
            return render_template('player.html', id = player_id, player_detail = player_detail)
    
    else:
        cursor.execute(
        "SELECT p.ID ID, p.Age Age, p.Name Name, p.Position Position, n.Nation_Name Nation_Name, p.Value Value, p.Wage Wage, p.Overall Overall, p.Potential Potential, c.Club_Name Club_Name"
        " FROM Player p, Nation n, Club c "
        " WHERE p.Nation_Name = n.Nation_Name AND p.Club_Name=c.Club_Name AND p.id = %s", id
        )
        player_detail = cursor.fetchone()
        player_detail["Value"] = '%.1f' % (player_detail["Value"])
        return render_template('player.html', id = id, player_detail = player_detail)