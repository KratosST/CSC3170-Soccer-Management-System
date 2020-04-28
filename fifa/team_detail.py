from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from fifa.db import get_db

bp = Blueprint('team_detail', __name__)

@bp.route('/<int:id>/team_detail', methods=('GET', 'POST'))
def index(id):
    g.current = "team_detail"
    db = get_db()
    cursor = db.cursor()

    if request.method == 'POST':
        team_id = request.form['team_id']
        team_id = int(team_id)
        error = None
        if not team_id:
            error = 'Basic information is not complete.'

        cursor.execute(
            "SELECT Club_Name"
            " FROM Club"
             " WHERE teamid = %s", team_id
        )
        club_name = cursor.fetchone()
        
        if club_name is None:
            cursor.execute(
            "SELECT p.ID ID, p.Age Age, p.Name Name, p.Position Position, n.nationid nationid, n.Nation_Name Nation_Name, p.Value Value, p.Wage Wage, p.Overall Overall, p.Potential Potential"
            " FROM Player p, Nation n "
            " WHERE p.Nation_Name = n.Nation_Name AND (SELECT c.teamid FROM Club c WHERE p.Club_Name = c.Club_Name) = %s", id
            )
            players = cursor.fetchall()
            for player in players:
                player["Value"] = '%.1f' % (player["Value"])
            cursor.execute(
                "SELECT Club_Name"
                " FROM Club"
                " WHERE teamid = %s", id
            )
            club_name = cursor.fetchone()

            cursor.execute(
            "SELECT *"
            " FROM Player p"
            " WHERE (SELECT c.teamid FROM Club c WHERE p.Club_Name = c.Club_Name) = %s", id
            )
            attributes = cursor.fetchall()

            cursor.execute(
                "SELECT *"
                " FROM Club"
                " WHERE teamid = %s", id
            )
            team_attribute = cursor.fetchone()
            # team_attribute["Overall"]=int(team_attribute["Overall"])
            # team_attribute["Potential"]=int(team_attribute["Potential"])
            team_attribute["Boss_Name"]=str(team_attribute["Boss_Name"])
            team_attribute["Total_Value"]='%.1f'%(team_attribute["Total_Value"])
            team_attribute["Total_Wage"]=int(team_attribute["Total_Wage"])
            return render_template('team_detail.html', players = players, club_name = club_name, attributes = attributes, team_attribute = team_attribute)


        else:
            flash(error)
            cursor.execute(
            "SELECT p.ID ID, p.Age Age, p.Name Name, p.Position Position, n.nationid nationid, n.Nation_Name Nation_Name, p.Value Value, p.Wage Wage, p.Overall Overall, p.Potential Potential"
            " FROM Player p, Nation n "
            " WHERE p.Nation_Name = n.Nation_Name AND (SELECT c.teamid FROM Club c WHERE p.Club_Name = c.Club_Name) = %s", team_id
            )
            players = cursor.fetchall()
            for player in players:
                player["Value"] = '%.1f' % (player["Value"])
            cursor.execute(
                "SELECT Club_Name"
                " FROM Club"
                " WHERE teamid = %s", team_id
            )
            club_name = cursor.fetchone()

            cursor.execute(
            "SELECT *"
            " FROM Player p"
            " WHERE (SELECT c.teamid FROM Club c WHERE p.Club_Name = c.Club_Name) = %s", team_id
            )
            attributes = cursor.fetchall()

            cursor.execute(
                "SELECT *"
                " FROM Club"
                " WHERE teamid = %s", team_id
            )
            team_attribute = cursor.fetchone()
            # team_attribute["Overall"]=int(team_attribute["Overall"])
            # team_attribute["Potential"]=int(team_attribute["Potential"])
            team_attribute["Boss_Name"]=str(team_attribute["Boss_Name"])
            team_attribute["Total_Value"]='%.1f'%(team_attribute["Total_Value"])
            team_attribute["Total_Wage"]=int(team_attribute["Total_Wage"])
            return render_template('team_detail.html', players = players, club_name = club_name, attributes = attributes, team_attribute = team_attribute)

    
    else:
        cursor.execute(
        "SELECT p.ID ID, p.Age Age, p.Name Name, p.Position Position, n.nationid nationid, n.Nation_Name Nation_Name, p.Value Value, p.Wage Wage, p.Overall Overall, p.Potential Potential"
        " FROM Player p, Nation n "
        " WHERE p.Nation_Name = n.Nation_Name AND (SELECT c.teamid FROM Club c WHERE p.Club_Name = c.Club_Name) = %s", id
        )
        players = cursor.fetchall()
        for player in players:
            player["Value"] = '%.1f' % (player["Value"])
        cursor.execute(
            "SELECT Club_Name"
            " FROM Club"
            " WHERE teamid = %s", id
        )
        club_name = cursor.fetchone()

        cursor.execute(
        "SELECT *"
        " FROM Player p"
        " WHERE (SELECT c.teamid FROM Club c WHERE p.Club_Name = c.Club_Name) = %s", id
        )
        attributes = cursor.fetchall()

        cursor.execute(
            "SELECT *"
            " FROM Club"
            " WHERE teamid = %s", id
        )
        team_attribute = cursor.fetchone()
        # team_attribute["Overall"]=int(team_attribute["Overall"])
        # team_attribute["Potential"]=int(team_attribute["Potential"])
        team_attribute["Boss_Name"]=str(team_attribute["Boss_Name"])
        team_attribute["Total_Value"]='%.1f'%(team_attribute["Total_Value"])
        team_attribute["Total_Wage"]=int(team_attribute["Total_Wage"])
        return render_template('team_detail.html', players = players, club_name = club_name, attributes = attributes, team_attribute = team_attribute)

