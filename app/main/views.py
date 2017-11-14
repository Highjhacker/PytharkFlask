from flask import render_template, request, json
from . import main
from pythark import Delegate


@main.route('/', methods=["GET", "POST"])
def index():
    deleg = Delegate()
    if request.method == 'POST':
        delegate_name = request.form.get("delegate_name")
        searched_delegate = deleg.search_delegates(query=delegate_name)
        resp = json.dumps(searched_delegate, sort_keys=True, indent=4, separators=(',', ': '))
        return render_template("index.html", searched_delegate=resp)
    return render_template("index.html")