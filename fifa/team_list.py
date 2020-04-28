from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from fifa.db import get_db

bp = Blueprint('team_list', __name__)

@bp.route('/team_list', methods=('GET', 'POST'))
def team_index():
    g.current = "team_list"
    db = get_db()
    cursor = db.cursor()
    teams = None
    error = None
    if request.method == 'POST':
        team_name = request.form['team_name']
        team_name = str(team_name)
        team_name = team_name.lower()

        error = None
        if not team_name:
            error = 'Basic information is not complete.'
        # cursor.execute("SELECT * FROM team WHERE LOWER(club_name) LIKE %s" , ("%"+team_name+"%",))
        cursor.execute("SELECT * FROM Club WHERE Club_Name LIKE %s" , ("%"+team_name+"%",))
        teams = cursor.fetchall()

        if teams is None:
            error = 'Team not found'
            return render_template('team_list.html', teams = teams)

        else:
            flash(error)
            for i in range(len(teams)):
                # teams[i]["overall"]=int(teams[i]["overall"])
                # teams[i]["potential"]=int(teams[i]["potential"])
                # teams[i]["totalvalue"]='%.1f'%(teams[i]["totalvalue"])
                # teams[i]["totalwage"]=int(teams[i]["totalwage"])
                teams[i]["Club_Name"]=str(teams[i]["Club_Name"])
                # teams[i]["Flag"]=str(teams[i]["Flag"])
                teams[i]["Total_Value"]='%.1f'%(teams[i]["Total_Value"])
                teams[i]["Total_Wage"]=int(teams[i]["Total_Wage"])
                teams[i]["Boss_Name"]=str(teams[i]["Boss_Name"])
            return render_template('team_list.html', teams = teams)
    
    else:
        cursor.execute(
            "SELECT *"
            " FROM Club"
            " ORDER BY Club.Total_Value desc LIMIT 50"
        )
        teams = cursor.fetchall()
        for i in range(len(teams)):
            # teams[i]["overall"]=int(teams[i]["overall"])
            # teams[i]["potential"]=int(teams[i]["potential"])
            # teams[i]["totalvalue"]='%.1f'%(teams[i]["totalvalue"])
            # teams[i]["totalwage"]=int(teams[i]["totalwage"])
            teams[i]["Club_Name"]=str(teams[i]["Club_Name"])
            # teams[i]["Flag"]=str(teams[i]["Flag"])
            teams[i]["Total_Value"]='%.1f'%(teams[i]["Total_Value"])
            teams[i]["Total_Wage"]=int(teams[i]["Total_Wage"])
            teams[i]["Boss_Name"]=str(teams[i]["Boss_Name"])
        return render_template('team_list.html', teams = teams)


