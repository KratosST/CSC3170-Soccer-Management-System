document.getElementById('newForm').style.display = "none";
function addNew() {
    document.getElementById('newForm').style.display = "block";
}
function newhidder() {
    document.getElementById('newForm').style.display = "none";
}

document.getElementById('editPlayer').style.display = "none";
function editPlayer() {
    document.getElementById('editPlayer').style.display = "block";
}
function edithidder() {
    document.getElementById('editPlayer').style.display = "none";
}

function validate() {
    if (document.getElementById("id").value == "") { alert("Please enter player ID"); return; }
    if (document.getElementById("name").value == "") { alert("Please enter player name"); return; }
    if (document.getElementById("age").value == "") { alert("Please enter player age"); return; }
    if (document.getElementById("height").value == "") { alert("Please enter player height"); return; }
    if (document.getElementById("weight").value == "") { alert("Please enter player weight"); return; }
    if (document.getElementById("overall").value == "") { alert("Please enter the overall "); return; }
    if (document.getElementById("potential").value == "") { alert("Please enter the overall "); return; }
    if (document.getElementById("value").value == "") { alert("Please enter the overall "); return; }
    if (document.getElementById("wage").value == "") { alert("Please enter the overall "); return; }
    if (document.getElementById("position").value == "") { alert("Please enter the overall "); return; }
    if (document.getElementById("preferred-foot").value == "") { alert("Please enter the overall "); return; }
    if (document.getElementById("weak-foot").value == "") { alert("Please enter the overall "); return; }
    if (document.getElementById("skill-moves").value == "") { alert("Please enter the overall "); return; }
    if (document.getElementById("reputation").value == "") { alert("Please enter the overall "); return; }
}    

