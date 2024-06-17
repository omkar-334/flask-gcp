import pandas as pd
from dotenv import dotenv_values
from flask import Flask, render_template, request, url_for


def create_dfs(file):
    dfmcols = [1, 2, 3, 4, 5]
    tempcols = [1, 2, 3, 7, 8, 11, 12, 13, 15, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 29, 30]

    xls = pd.ExcelFile(file)
    temp = xls.parse("Student Master", converters={"Cell": str, "Adm": str}, usecols=tempcols)

    main, overall, old, new = [
        temp.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]],
        temp.iloc[:, [9, 10, 11, 12]],
        temp.iloc[:, [13, 14, 15, 16]],
        temp.iloc[:, [17, 18, 19, 20]],
    ]
    dfe = xls.parse(
        "Daily Fees Entry",
        usecols=dfmcols,
        converters={"Adm": str, "Receipt Number": str},
    )
    return [main, overall, old, new, dfe]


filedict, dfdict = dict(dotenv_values()), {}
names = {k: v for k, v in filedict.items() if k.startswith("name")}.values()
files = {k: v for k, v in filedict.items() if k.startswith("file")}.values()

for name, file in zip(names, files):
    dfdict[name] = create_dfs(file)

app = Flask(__name__)


@app.route("/")
def my_form():
    return render_template("fees.html", names=names, enumerate=enumerate)


@app.route("/", methods=["POST", "GET"])
def admfun():
    def filter_df(df, var, varname):
        return df[varname].str.contains(var, na=False, case=False)

    option = request.form["options"]
    adm = request.form["adm"]
    name = request.form["name"]
    cell = request.form["cell"]

    if request.form.get("adm"):
        main, over, old, new, dfe = dfdict[option]
        mainloc = filter_df(main, adm, "Adm")
        dfeloc = filter_df(dfe, adm, "Adm")

        return render_template(
            "fees.html",
            main=[main.loc[mainloc].to_html(col_space="75px", classes="data", header="True")],
            overall=[over.loc[mainloc].to_html(col_space="125px", classes="data", header="True")],
            old=[old.loc[mainloc].to_html(col_space="125px", classes="data", header="True")],
            new=[new.loc[mainloc].to_html(col_space="125px", classes="data", header="True")],
            dfe=[dfe.loc[dfeloc].to_html(col_space="105px", classes="data", header="True")],
            titles=[""],
            option=option,
            names=names,
            enumerate=enumerate,
        )
    elif request.form.get("name"):
        main = dfdict[option][0]
        mainloc = filter_df(main, name, "Name")

        return render_template(
            "fees.html",
            main=[main.loc[mainloc].to_html(col_space="75px", classes="data", header="True")],
            titles=[""],
            option=option,
            names=names,
            enumerate=enumerate,
        )
    elif request.form.get("cell"):
        main = dfdict[option][0]
        mainloc = filter_df(main, cell, "Cell")

        return render_template(
            "fees.html",
            main=[main.loc[mainloc].to_html(col_space="75px", classes="data", header="True")],
            titles=[""],
            option=option,
            names=names,
            enumerate=enumerate,
        )
    else:
        return render_template("fees.html", names=names, enumerate=enumerate)


if __name__ == "__main__":
    app.run()
