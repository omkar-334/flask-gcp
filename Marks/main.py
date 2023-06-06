from flask import Flask,request,render_template
import pandas as pd

usecols=[0,1,2,3,5,9,13,17,21,25,29,33,37,38,39]
usenames=['Adm','Cell','Name','Class','Telugu', 'Hindi', 'English', 'Maths', 'Phy Sci', 'Bio Sci', 'Science','Social', 'Total', 'GPA', 'Grade']
useindex=["FA-1","FA-2","FA-3","FA-4","SA-1","SA-2"]
[sheet1,sheet2,sheet3,sheet4,sheet5,sheet6]=useindex

file1='markscopy1.xlsx'
file2='markscopy2.xlsx'
file3='markscopy3.xlsx'
file4='markscopy4.xlsx'

main_1a=pd.read_excel(
    io=file1,
    sheet_name=sheet1,
    usecols=usecols,
    names=usenames,
    converters={'Cell':str,'Adm':str})
main_1b=pd.read_excel(
    io=file1,
    sheet_name=sheet2,
    usecols=usecols,
    names=usenames,
    converters={'Cell':str,'Adm':str})
main_1c=pd.read_excel(
    io=file1,
    sheet_name=sheet3,
    usecols=usecols,
    names=usenames,
    converters={'Cell':str,'Adm':str})
main_1d=pd.read_excel(
    io=file1,
    sheet_name=sheet4,
    usecols=usecols,
    names=usenames,
    converters={'Cell':str,'Adm':str})
main_1e=pd.read_excel(
    io=file1,
    sheet_name=sheet5,
    usecols=usecols,
    names=usenames,
    converters={'Cell':str,'Adm':str})
main_1f=pd.read_excel(
    io=file1,
    sheet_name=sheet6,
    usecols=usecols,
    names=usenames,
    converters={'Cell':str,'Adm':str})
main_1a.index=len(main_1a)*["FA-1"]
main_1b.index=len(main_1b)*["FA-2"]
main_1c.index=len(main_1c)*["FA-3"]
main_1d.index=len(main_1d)*["FA-4"]
main_1e.index=len(main_1e)*["SA-1"]
main_1f.index=len(main_1f)*["SA-2"]
main_2a=pd.read_excel(
    io=file2,
    sheet_name=sheet1,
    usecols=usecols,
    names=usenames,
    converters={'Cell':str,'Adm':str})
main_2b=pd.read_excel(
    io=file2,
    sheet_name=sheet2,
    usecols=usecols,
    names=usenames,
    converters={'Cell':str,'Adm':str})
main_2c=pd.read_excel(
    io=file2,
    sheet_name=sheet3,
    usecols=usecols,
    names=usenames,
    converters={'Cell':str,'Adm':str})
main_2d=pd.read_excel(
    io=file2,
    sheet_name=sheet4,
    usecols=usecols,
    names=usenames,
    converters={'Cell':str,'Adm':str})
main_2e=pd.read_excel(
    io=file2,
    sheet_name=sheet5,
    usecols=usecols,
    names=usenames,
    converters={'Cell':str,'Adm':str})
main_2f=pd.read_excel(
    io=file2,
    sheet_name=sheet6,
    usecols=usecols,
    names=usenames,
    converters={'Cell':str,'Adm':str})
main_2a.index=len(main_2a)*["FA-1"]
main_2b.index=len(main_2b)*["FA-2"]
main_2c.index=len(main_2c)*["FA-3"]
main_2d.index=len(main_2d)*["FA-4"]
main_2e.index=len(main_2e)*["SA-1"]
main_2f.index=len(main_2f)*["SA-2"]
main_3a=pd.read_excel(
    io=file3,
    sheet_name=sheet1,
    usecols=usecols,
    names=usenames,
    converters={'Cell':str,'Adm':str})
main_3b=pd.read_excel(
    io=file3,
    sheet_name=sheet2,
    usecols=usecols,
    names=usenames,
    converters={'Cell':str,'Adm':str})
main_3c=pd.read_excel(
    io=file3,
    sheet_name=sheet3,
    usecols=usecols,
    names=usenames,
    converters={'Cell':str,'Adm':str})
main_3d=pd.read_excel(
    io=file3,
    sheet_name=sheet4,
    usecols=usecols,
    names=usenames,
    converters={'Cell':str,'Adm':str})
main_3e=pd.read_excel(
    io=file3,
    sheet_name=sheet5,
    usecols=usecols,
    names=usenames,
    converters={'Cell':str,'Adm':str})
main_3f=pd.read_excel(
    io=file3,
    sheet_name=sheet6,
    usecols=usecols,
    names=usenames,
    converters={'Cell':str,'Adm':str})
main_3a.index=len(main_3a)*["FA-1"]
main_3b.index=len(main_3b)*["FA-2"]
main_3c.index=len(main_3c)*["FA-3"]
main_3d.index=len(main_3d)*["FA-4"]
main_3e.index=len(main_3e)*["SA-1"]
main_3f.index=len(main_3f)*["SA-2"]
main_4a=pd.read_excel(
    io=file4,
    sheet_name=sheet1,
    usecols=usecols,
    names=usenames,
    converters={'Cell':str,'Adm':str})
main_4b=pd.read_excel(
    io=file4,
    sheet_name=sheet2,
    usecols=usecols,
    names=usenames,
    converters={'Cell':str,'Adm':str})
main_4c=pd.read_excel(
    io=file4,
    sheet_name=sheet3,
    usecols=usecols,
    names=usenames,
    converters={'Cell':str,'Adm':str})
main_4d=pd.read_excel(
    io=file4,
    sheet_name=sheet4,
    usecols=usecols,
    names=usenames,
    converters={'Cell':str,'Adm':str})
main_4e=pd.read_excel(
    io=file4,
    sheet_name=sheet5,
    usecols=usecols,
    names=usenames,
    converters={'Cell':str,'Adm':str})
main_4f=pd.read_excel(
    io=file4,
    sheet_name=sheet6,
    usecols=usecols,
    names=usenames,
    converters={'Cell':str,'Adm':str})
main_4a.index=len(main_4a)*["FA-1"]
main_4b.index=len(main_4b)*["FA-2"]
main_4c.index=len(main_4c)*["FA-3"]
main_4d.index=len(main_4d)*["FA-4"]
main_4e.index=len(main_4e)*["SA-1"]
main_4f.index=len(main_4f)*["SA-2"]


app=Flask(__name__)
@app.route('/')
def my_form():
    return render_template('marks.html',file1=file1,file2=file2,file3=file3,file4=file4)

@app.route('/', methods=['POST'])
def admfun():
    option = request.form['options']
    if option==file1:
        [main_a,main_b,main_c,main_d,main_e,main_f]=[main_1a,main_1b,main_1c,main_1d,main_1e,main_1f]
    elif option == file2:
        [main_a,main_b,main_c,main_d,main_e,main_f]=[main_2a,main_2b,main_2c,main_2d,main_2e,main_2f]
    elif option == file3:
        [main_a,main_b,main_c,main_d,main_e,main_f]=[main_3a,main_3b,main_3c,main_3d,main_3e,main_3f]
    else:
        [main_a,main_b,main_c,main_d,main_e,main_f]=[main_4a,main_4b,main_4c,main_4d,main_4e,main_4f]

    admvar = request.form['studentadm']
    cellvar = request.form['studentphone']
    namevar = request.form['studentname']

    if request.form.get("studentadm"):
        result=pd.concat([main_a,main_b,main_c,main_d,main_e,main_f])
        final=result.loc[result["Adm"].str.contains(admvar,na=False,case=False)]
        head=final[["Adm","Cell","Name","Class"]].drop_duplicates(subset=["Adm"], keep='first')
        admtable=[head.loc[head["Adm"].str.contains(admvar,na=False,case=False)].to_html(col_space='75px',classes='data',header='True')][0:2]
        del final["Adm"]
        del final["Cell"]
        del final["Name"]
        del final["Class"]
        contable=final.to_html(col_space='75px',classes="table table-striped",header='True')
        return render_template('marks.html',tables=admtable,titles=[''],contable=contable,option=option,file1=file1,file2=file2,file3=file3,file4=file4)
    elif request.form.get("studentphone"):
        result=pd.concat([main_a,main_b,main_c,main_d,main_e,main_f])
        final=result.loc[result["Adm"].str.contains(admvar,na=False,case=False)]
        head=final[["Adm","Cell","Name","Class"]].drop_duplicates(subset=["Adm"], keep='first')
        celltable=[head.loc[head["Cell"].str.contains(cellvar,na=False,case=False)].to_html(col_space='75px',classes='data',header='True')][0:2]
        return render_template('marks.html',tables=celltable,titles=[''],option=option,file1=file1,file2=file2,file3=file3,file4=file4)
    elif request.form.get("studentname"):
        result=pd.concat([main_a,main_b,main_c,main_d,main_e,main_f])
        final=result.loc[result["Adm"].str.contains(admvar,na=False,case=False)]
        head=final[["Adm","Cell","Name","Class"]].drop_duplicates(subset=["Adm"], keep='first')
        nametable=[head.loc[head["Name"].str.contains(namevar,na=False,case=False)].to_html(col_space='75px',classes='data',header='True')][0:2]
        return render_template('marks.html',tables=nametable,titles=[''],option=option,file1=file1,file2=file2,file3=file3,file4=file4)
    else:
        return render_template('marks.html',option=option,file1=file1,file2=file2,file3=file3,file4=file4)

if __name__=="__main__":
    app.run(port=2000)