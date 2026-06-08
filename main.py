from datetime import datetime

from flask import Flask, request, render_template

from models.activity import Activity
from repository.list import ActivityList
from repository.schedule import Schedule

DATETIME_PT_BR_FORMAT = "%d/%m/%Y %H:%M"


def format_datetime_ptbr(value: datetime) -> str:
    return value.strftime(DATETIME_PT_BR_FORMAT)


app = Flask(__name__)
app.jinja_env.filters["datetime_ptbr"] = format_datetime_ptbr

schedule = Schedule()
activity_list = ActivityList(filename="activities.json")
schedule.rebuild_from(activity_list.list)


@app.route("/")
def index():
    return render_template(
        "index.html",
        activities=activity_list.list,
        schedule=schedule,
    )


@app.route("/activity/create", methods=["POST"])
def create_activity():
    next_id = max((a.id for a in activity_list.list), default=0) + 1

    activity = Activity(
        id=next_id,
        name=request.form["name"],
        description=request.form["description"],
        start_time=datetime.strptime(request.form["start_time"], "%Y-%m-%dT%H:%M"),
        end_time=datetime.strptime(request.form["end_time"], "%Y-%m-%dT%H:%M"),
        priority=int(request.form["priority"]),
        participants=int(request.form["participants"]),
    )

    activity_list.add(activity)
    schedule.rebuild_from(activity_list.list)

    return render_template(
        "_tables.html",
        activities=activity_list.list,
        schedule=schedule,
    )


@app.route("/activities/sort", methods=["POST"])
def sort_activities():
    reverse = request.form.get("dir", "asc") == "desc"
    activity_list.sort(request.form["key"], reverse=reverse)
    return render_template("_activity_rows.html", activities=activity_list.list)


@app.route("/activity/delete", methods=["POST"])
def delete_activity():
    activity_id = int(request.form["id"])
    activity_list.delete(activity_id)
    schedule.rebuild_from(activity_list.list)
    return render_template(
        "_tables.html",
        activities=activity_list.list,
        schedule=schedule,
    )


@app.route("/activity/clear", methods=["POST"])
def clear_activities():
    activity_list.clear()
    schedule.clear()
    return render_template(
        "_tables.html",
        activities=activity_list.list,
        schedule=schedule,
    )


@app.route("/activity/create-random", methods=["POST"])
def create_random_activity():
    count = int(request.form["count"])
    next_id = max((a.id for a in activity_list.list), default=0) + 1

    for _ in range(count):
        activity_list.add(Activity.random(next_id))
        next_id += 1

    schedule.rebuild_from(activity_list.list)

    return render_template(
        "_tables.html",
        activities=activity_list.list,
        schedule=schedule,
    )
