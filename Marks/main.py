import pandas as pd
from dotenv import dotenv_values
from flask import Flask, render_template, request, url_for

cols = [0, 1, 2, 3, 5, 9, 13, 17, 21, 25, 29, 33, 37, 38, 39]
names = ["Adm", "Cell", "Name", "Class", "Telugu", "Hindi", "English"]
names.extend(["Maths", "Phy Sci", "Bio Sci", "Science", "Social", "Total", "GPA", "Grade"])
sheets = ["FA-1", "FA-2", "FA-3", "FA-4", "SA-1", "SA-2"]


def create_dfs(file):
    dfs = []
    xls = pd.ExcelFile(file)
    for sheet in sheets:
        df = xls.parse(sheet, usecols=cols, names=names, converters={"Cell": str, "Adm": str})
        df.index = len(df) * [sheet]
        dfs.append(df)
    return pd.concat(dfs)


filedict, dfdict = dict(dotenv_values()), {}
names = {k: v for k, v in filedict.items() if k.startswith("name")}
files = {k: v for k, v in filedict.items() if k.startswith("file")}
names, files = names.values(), files.values()

for name, file in zip(names, files):
    df = create_dfs(file)
#     dfdict[name] = create_dfs(file)


app = Flask(__name__)


@app.route("/")
def my_form():
    return render_template("marks.html")


@app.route("/", methods=["POST"])
def admfun():
    adm = request.form["adm"]
    cell = request.form["cell"]
    name = request.form["name"]

    def filter_df(df, var, varname):
        df = df.loc[df[varname].str.contains(var, na=False, case=False)]
        outdf = df[["Adm", "Cell", "Name", "Class"]].drop_duplicates(subset=["Adm"], keep="first")
        outdf = outdf.to_html(col_space="75px", classes="data", header="True")

        if varname == "Adm":
            outdf2 = df.drop(["Adm", "Cell", "Name", "Class"], axis=1)
            outdf2 = outdf2.to_html(col_space="75px", classes="table table-striped", header="True")
            return [[outdf], [outdf2]]

        return [outdf]

    if request.form.get("adm"):
        table, marks = filter_df(df, adm, "Adm")
        return render_template("marks.html", main=table, titles=[""], marks=marks)

    elif request.form.get("cell"):
        table = filter_df(df, cell, "Cell")
        return render_template("marks.html", main=table, titles=[""])

    elif request.form.get("name"):
        table = filter_df(df, name, "Name")
        return render_template("marks.html", main=table, titles=[""])
    else:
        return render_template("marks.html")


if __name__ == "__main__":
    app.run()
