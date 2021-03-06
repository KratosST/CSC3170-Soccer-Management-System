from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from fifa.db import get_db

bp = Blueprint('player_list', __name__)

@bp.route('/player_list', methods=('GET', 'POST'))
def player_index():
    g.current = "player_list"
    db = get_db()
    cursor = db.cursor()
    players = None
    error = None
    if request.method == 'POST':
        player_name = request.form['player_name']
        player_name = str(player_name)
        player_name = player_name.lower()
        error = None
        if not player_name:
            error = 'Basic information is not complete.'

        cursor.execute(
        "SELECT p.ID ID, p.Age Age, p.Name Name, p.Position Position, n.nationid nationid, n.Nation_Name Nation_Name, p.Value Value, p.Wage Wage, p.Overall Overall, p.Potential Potential"
        " FROM Player p, Nation n "
        " WHERE p.Nation_Name = n.Nation_Name AND LOWER(p.Name) LIKE %s", ("%"+ player_name + "%")
        )
        players = cursor.fetchall()
        if players is None:
            error = 'Player not found'
            return render_template('player_list.html', players = players)

        else:
            flash(error)
            for player in players:
                player["Value"] = '%.1f' % (player["Value"])
            return render_template('player_list.html', players = players)

    else: 
        cursor.execute(
        "SELECT p.ID ID, p.Age Age, p.Name Name, p.Position Position, n.nationid nationid, n.Nation_Name Nation_Name, p.Value Value, p.Wage Wage, p.Overall Overall, p.Potential Potential"
        " FROM Player p, Nation n "
        " WHERE p.Nation_Name = n.Nation_Name"
        " ORDER BY p.Overall desc LIMIT 50"
        )
        players = cursor.fetchall()
        for player in players:
            player["Value"] = '%.1f' % (player["Value"])
            
        return render_template('player_list.html', players = players)


