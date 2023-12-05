import json
from random import randint

from bottle import route, template, run, request, redirect


with open("config.json") as f:
    config = json.load(f)

base_dir = config["base_dir"]
points = config["points"]
users = {user: 0 for user in config["users"]}
vote_links = {user: randint(1, 1000) for user in users}


@route("/")
def main():
    return template("home", vote_links=vote_links, users=users)


@route("/vote/<vote_link:int>")
def vote(vote_link):
    this_user = None
    for user in vote_links:
        if vote_links[user] == vote_link:
            this_user = user
    if vote_link not in vote_links.values():
        return "Vote link with this id does not exist"
    return template(
        "vote",
        users={u: users[u] for u in users if u != this_user},
        vote_link=vote_link,
        msg="",
        points=points,
        base_dir=base_dir,
    )


@route("/vote", method="POST")
def submit_vote():
    vote_link = int(request.forms.get("vote_link"))
    this_user = None
    for user in vote_links:
        if vote_link == vote_links[user]:
            this_user = user
    if this_user is None:
        return "Already voted"

    sum = 0
    for user in users:
        if user == this_user:
            continue
        try:
            int(request.forms.get(user))
        except ValueError:
            return template(
                "vote",
                users={u: users[u] for u in users if u != this_user},
                vote_link=vote_link,
                msg="All values must be integers",
                points=points,
                base_dir=base_dir,
            )
        if int(request.forms.get(user)) < 0:
            return template(
                "vote",
                users={u: users[u] for u in users if u != this_user},
                vote_link=vote_link,
                msg="All points must be positive",
                points=points,
                base_dir=base_dir,
            )
        sum += int(request.forms.get(user))
    if sum != points:
        return template(
            "vote",
            users={u: users[u] for u in users if u != this_user},
            vote_link=vote_link,
            msg=f"Points must add up to {points}, vote again please",
            points=points,
            base_dir=base_dir,
        )

    vote_links.pop(this_user)
    for user in users:
        if user == this_user:
            continue
        users[user] += int(request.forms.get(user))
    redirect(base_dir or "/", 302)


run(host="localhost", port=8069)
