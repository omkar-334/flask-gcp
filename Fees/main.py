import pandas as pd
from flask import Flask,request,render_template

file1='feescopy1.xlsx'
file2='feescopy2.xlsx'
file3='feescopy3.xlsx'
file4='feescopy4.xlsx'

dfmcols=[1,2,3,4,5]
colnames=[1,2,3,7,11,12,13,15,17,18,19,20,22,23,24,25,27,28,29,30]

def1=pd.read_excel(
        io=file1,
        sheet_name='Student Master',
        converters={'Cell':str,'Adm':str},
        usecols=colnames)
[main1,overall1,old1,new1]=[def1.iloc[:,[0,1,2,3,4,5,6,7]],def1.iloc[:,[8,9,10,11]],def1.iloc[:,[12,13,14,15]],def1.iloc[:,[16,17,18,19]]]
dfm1=pd.read_excel(
        io=file1,
        sheet_name='Daily Fees Entry',
        usecols=dfmcols,
        converters={'Adm':str,'Receipt Number':str})

def2=pd.read_excel(
        io=file2,
        sheet_name='Student Master',
        converters={'Cell':str,'Adm':str},
        usecols=colnames)
[main2,overall2,old2,new2]=[def2.iloc[:,[0,1,2,3,4,5,6,7]],def2.iloc[:,[8,9,10,11]],def2.iloc[:,[12,13,14,15]],def2.iloc[:,[16,17,18,19]]]
dfm2=pd.read_excel(
        io=file2,
        sheet_name='Daily Fees Entry',
        usecols=dfmcols,
        converters={'Adm':str,'Receipt Number':str})

def3=pd.read_excel(
        io=file3,
        sheet_name='Student Master',
        converters={'Cell':str,'Adm':str},
        usecols=colnames)
[main3,overall3,old3,new3]=[def3.iloc[:,[0,1,2,3,4,5,6,7]],def3.iloc[:,[8,9,10,11]],def3.iloc[:,[12,13,14,15]],def3.iloc[:,[16,17,18,19]]]
dfm3=pd.read_excel(
        io=file3,
        sheet_name='Daily Fees Entry',
        usecols=dfmcols,
        converters={'Adm':str,'Receipt Number':str})

def4=pd.read_excel(
        io=file4,
        sheet_name='Student Master',
        converters={'Cell':str,'Adm':str},
        usecols=colnames)
[main4,overall4,old4,new4]=[def4.iloc[:,[0,1,2,3,4,5,6,7]],def4.iloc[:,[8,9,10,11]],def4.iloc[:,[12,13,14,15]],def4.iloc[:,[16,17,18,19]]]
dfm4=pd.read_excel(
        io=file4,
        sheet_name='Daily Fees Entry',
        usecols=dfmcols,
        converters={'Adm':str,'Receipt Number':str})

app=Flask(__name__)
@app.route('/')
def my_form():
    return render_template('fees.html',file1=file1,file2=file2,file3=file3,file4=file4)

@app.route('/', methods=['POST'])
def admfun():
    option = request.form['options']
    if option==file1:
        [main,overall,old,new,dfm]=[main1,overall1,old1,new1,dfm1]
    elif option == file2:
        [main,overall,old,new,dfm]=[main2,overall2,old2,new2,dfm2]
    elif option == file3:
        [main,overall,old,new,dfm]=[main3,overall3,old3,new3,dfm3]
    else:
        [main,overall,old,new,dfm]=[main4,overall4,old4,new4,dfm4]

    admvar = request.form['studentadm']
    namevar = request.form['studentname']
    phonevar = request.form['studentphone']

    overalltable=[overall.loc[main["Adm"].str.contains(admvar,na=False,case=False)].to_html(col_space='125px',classes='data',header='True')]
    newtable=[new.loc[main["Adm"].str.contains(admvar,na=False,case=False)].to_html(col_space='125px',classes='data',header='True')]
    oldtable=[old.loc[main["Adm"].str.contains(admvar,na=False,case=False)].to_html(col_space='125px',classes='data',header='True')]
    dfmtable=[dfm.loc[dfm["Adm"].str.contains(admvar,na=False,case=False)].to_html(col_space='105px',classes='data',header='True')]

    if request.form.get("studentadm"):
        return render_template('fees.html',tables=[main.loc[main["Adm"].str.contains(admvar,na=False,case=False)].to_html(col_space='75px',classes='data',header='True')],titles=[''],overalltable=overalltable,oldtable=oldtable,newtable=newtable,dfmtable=dfmtable,option=option,file1=file1,file2=file2,file3=file3,file4=file4)
    elif request.form.get("studentname"):
        return render_template('fees.html',tables=[main.loc[main["Name"].str.contains(namevar,na=False,case=False)].to_html(col_space='75px',classes='data',header='True')],titles=[''],option=option,file1=file1,file2=file2,file3=file3,file4=file4)
    elif request.form.get("studentphone"):
         return render_template('fees.html',tables=[main.loc[main["Cell"].str.contains(phonevar,na=False,case=False)].to_html(col_space='75px',classes='data',header='True')],titles=[''],option=option,file1=file1,file2=file2,file3=file3,file4=file4)
    else:
        return render_template('fees.html',file1=file1,file2=file2,file3=file3,file4=file4)

if __name__=="__main__":
    app.run()