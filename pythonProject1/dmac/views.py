from django.shortcuts import render,redirect
import pandas as pd
import html5lib
import requests
from sqlalchemy import create_engine

# from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
# from django.core.mail import send_mail
from .models import EmployeeEmails
from django.conf import settings
# from django.contrib.auth import logout
import psycopg2
from iteration_utilities import unique_everseen
import json

# Create your views here.
#
# def glogin(request):
#     return render(request, 'dmac/index.html')

# Logout
# @login_required
# def logout_user(request):
#     logout(request)
#     return redirect('dmac:glogin')

# todo = [
#         {id: "01", name: "abhinav"},
#         {id: "02", name: "ashish"},
#         {id: "03", name: "ankit"},
#         {id: "04", name: "suresh"}
#     ]
# done = [
#     {id:"01",address:"rrrr"},
#     {id:"02",address:"tttt"},
#     {id:"03",address:"yyyy"},
#     {id:"04",address:"cvcvcv"}
#   ]
#  studentID=[
#     {id:"01",phone:"2344342"},
#     {id:"02",phone:"3434343"},
#     {id:"03",phone:"4334345"},
#     {id:"04",phone:"4545455"}
# ]
def loginpage(request):
    return render(request,'dmac/index.html')

# def logout(request):
#     loggout(request)
#     return redirect('dmac:loginpage')
# @login_required
def adminhome(request):
    print("this is my df dataframe!")
    # print(df1)
    todo = [
            {"id": "01", "name": "abhinav"},
            {"id": "02", "name": "ashish"},
            {"id": "03", "name": "ankit"},
            {"id": "04", "name": "suresh"}
        ]
    done = [
        {"id":"01","address":"rrrr"},
        {"id":"02","address":"tttt"},
        {"id":"03","address":"yyyy"},
        {"id":"04","address":"cvcvcv"}
      ]
    #  studentID=[
    #     {"id":"01","phone":"2344342"},
    #     {"id":"02","phone":"3434343"},
    #     {"id":"03","phone":"4334345"},
    #     {"id":"04","phone":"4545455"}
    # ]
    module_dict1 = [ "module 1", "module 2", "module 3"]
    # module_dict = {"0": "module x", "1": "module y", "2": "modulez"}
    # module_dict = json.dumps(module_dict)
    module_dict1 = json.dumps(module_dict1)
    try:
        engine = create_engine('postgresql://postgres:Programming123@localhost:5432/postgres')
        df_aws2 = pd.read_sql_query("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';", con=engine)
        tablename_list = list(df_aws2["relname"])
        module_dict = tablename_list
        module_dict11 = json.dumps(module_dict)
    except:
        tablename_list=["table1","table2","table3"]


    # data1=df_aws1.to_json(orient='records')

    print("Hello Hind this is your updated dataframe of D-mac")
    return render(request,'dmac/login.html',{'tablename_list':tablename_list,'module_dict1':module_dict1,'module_dict11':module_dict11})


def Table(request):
    todo = [
        {"id": "01", "name": "abhinav"},
        {"id": "02", "name": "ashish"},
        {"id": "03", "name": "ankit"},
        {"id": "04", "name": "suresh"}
    ]
    try:
        engine = create_engine('postgresql://postgres:Programming123@localhost:5432/postgres')
        # # df1.to_sql('dmac', engine, if_exists='append')
        l1 = pd.read_sql_query('select * from "legacytable1"', con=engine)
        l2 = pd.read_sql_query('select * from "legacytable1"', con=engine)
        l3 = pd.read_sql_query('select * from "legacytable1"', con=engine)
        # Manipulate DataFrame using to_html() function
        table1 = l1.to_html()
        table2 = l2.to_html()
        table3 = l3.to_html()
    except:
        l1=pd.DataFrame(todo)
        table1 = l1.to_html()


    return HttpResponse(table1)


def merge_table(request):
    try:
        engine = create_engine('postgresql://postgres:Programming123@localhost:5432/postgres')
        # l3.to_sql('legacytable3', engine,  if_exists='append')
        l1 = pd.read_sql_query('select * from "legacytable1"', con=engine)
        l2 = pd.read_sql_query('select * from "legacytable2"', con=engine)
        l3 = pd.read_sql_query('select * from "legacytable3"', con=engine)

        merg = pd.merge(l1, l2, on="Emp#", how="outer")
        merg1 = pd.merge(merg, l3, on="Emp#", how="outer")
        merg1["Full Name"] = merg1["First Name"] + "  " + merg1["Last Name"]

        def digit_tracker(x):
            d = str(x)
            k = len(d)
            spd = "0" * (11 - k) + d
            return spd

        merg1['uniqueid'] = merg1['Emp#'].apply(digit_tracker)
        final = merg1[["uniqueid", "Full Name", "Skills", "Technology", "Tax ID", "City", "Country Code", "Phone", "Email"]]
        final
        # final.to_sql('new_table', engine, if_exists='append')
        final.to_csv("new_table.csv")
        print("your new table is created and stored.")

        tablex = final.to_html()
    except:
        tablex="now you are not connected to database."


    return HttpResponse(tablex)


def finaljson(request):
    try:
        engine = create_engine('postgresql://postgres:Programming123@localhost:5432/postgres')
        # l3.to_sql('legacytable3', engine,  if_exists='append')
        l1 = pd.read_sql_query('select * from "legacytable1"', con=engine)
        l2 = pd.read_sql_query('select * from "legacytable2"', con=engine)
        l3 = pd.read_sql_query('select * from "legacytable3"', con=engine)

        merg = pd.merge(l1, l2, on="Emp#", how="outer")
        merg1 = pd.merge(merg, l3, on="Emp#", how="outer")
        merg1["Full Name"] = merg1["First Name"] + "  " + merg1["Last Name"]

        def digit_tracker(x):
            d = str(x)
            k = len(d)
            spd = "0" * (11 - k) + d
            return spd

        merg1['uniqueid'] = merg1['Emp#'].apply(digit_tracker)
        final = merg1[["uniqueid", "Full Name", "Skills", "Technology", "Tax ID", "City", "Country Code", "Phone", "Email"]]
        final
        # final.to_sql('new_table', engine, if_exists='append')
        # final.to_csv("new_table.csv")
        print("your new table is created and stored.")
        mergedata1 = [
            {"id": "03", "name": "ankit"},
            {"id": "03", "address": "yyyy"},
            {"id": "02", "phone": "3434343"},
            {"id": "03", "phone": "23344"},
            {"id": "01", "address": "rrrr"},
        ]

        tablex = final.to_json(orient='records')
        # code for reshape json and remove redundancy
        plusdata=mergedata1
        print(plusdata)
        plusdata.sort(key=lambda item: item.get("id"))
        print(plusdata)
        for i in range(len(plusdata)-1):
            if (plusdata[i]["id"] == plusdata[i + 1]["id"]):
                plusdata[i].update(plusdata[i + 1])

        for i in range(len(plusdata)-1):
            if (plusdata[i]["id"] == plusdata[i + 1]["id"]):
                plusdata[i].update(plusdata[i + 1])
                plusdata[i + 1].update(plusdata[i])
        fitdata=list(unique_everseen(plusdata, key=lambda item: frozenset(item.items())))
        print(fitdata)
        return render(request, 'dmac/product.html', {'tablex': tablex, 'fitdata': fitdata})
    except:
        mergedata1 = [
            {"id": "03", "name": "ankit"},
            {"id": "03", "address": "yyyy"},
            {"id": "02", "phone": "3434343"},
            {"id": "03", "phone": "23344"},
            {"id": "01", "address": "rrrr"},
        ]

        # tablex = final.to_json(orient='records')
        # code for reshape json and remove redundancy
        plusdata = mergedata1
        print(plusdata)
        plusdata.sort(key=lambda item: item.get("id"))
        print(plusdata)
        for i in range(len(plusdata) - 1):
            if (plusdata[i]["id"] == plusdata[i + 1]["id"]):
                plusdata[i].update(plusdata[i + 1])

        for i in range(len(plusdata) - 1):
            if (plusdata[i]["id"] == plusdata[i + 1]["id"]):
                plusdata[i].update(plusdata[i + 1])
                plusdata[i + 1].update(plusdata[i])
        fitdata = list(unique_everseen(plusdata, key=lambda item: frozenset(item.items())))
        print(fitdata)
        return render(request, 'dmac/product.html', {'fitdata': fitdata})


def posttable(request):
    module_dict={"0": "module 1", "1": "module 2", "2": "module3"}
    engine = create_engine('postgresql://postgres:Programming123@localhost:5432/postgres')
    df_aws2 = pd.read_sql_query("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';",con=engine)
    tablename_list = list(df_aws2["relname"])
    return render(request,'dmac/posttable.html',{'tablename_list':tablename_list,'module_dict':module_dict})

def post(request):
    if request.method == "POST":
        table_name = request.POST.getlist('tablename')
        # table_name = json.loads(table_name.body)
    print(table_name)
    module_dict={"0": "module 1", "1": "module 2", "2": "module3"}
    engine = create_engine('postgresql://postgres:Programming123@localhost:5432/postgres')
    df_aws2 = pd.read_sql_query("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';",con=engine)
    tablename_list = list(df_aws2["relname"])
    mainvalues=[]
    maincolumns=[]
    colfunctionlist = []
    # for i in range(len(table_name)):
    #     l1 = pd.read_sql_query(f'select * from {table_name[i]}', con=engine)
    #     mkt = l1.iloc[0:, 1:]
    #     dataft = mkt.to_json(orient='records')
    #     s1 = json.loads(dataft)
    #     valuess1 = [list(x.values()) for x in s1]
    #     mainvalues.append(valuess1)
    #     columnss1 = [list(x.keys()) for x in s1][0]
    #     maincolumns.append(columnss1)

    for i in range(len(table_name)):
        l1 = pd.read_sql_query(f'select * from {table_name[i]}', con=engine)
        mkt = l1.iloc[0:, 1:]
        dataft = mkt.to_json(orient='records')
        colfunctionlist.append(dataft)
        s1 = json.loads(dataft)
        valuess1 = [list(x.values()) for x in s1]
        # d_cities = dict.fromkeys(cities, 'UK')
        mainvalues.append(valuess1)
        columnss1 = [list(x.keys()) for x in s1][0]
        maincolumns.append(columnss1)
    d_columns = dict(zip(table_name, maincolumns))
    d_values = dict(zip(table_name, mainvalues))
    manag=[1,2]
    # print(maincolumns)
    stick1=maincolumns[0]
    stick2=maincolumns[1]
    tab1=colfunctionlist[0]
    tab2=colfunctionlist[1]
    # colx=dict(zip(maincolumns,mainvalues))

    # print(colx)
    print(d_columns)
    print(d_values)
    # print(maincolumns)
    # print("values")
    # print(mainvalues)
    #     cid=mainvalues[0]
    #     cid1=mainvalues[1]
    #     cid2=mainvalues[2]
    #     lis=maincolumns[0]
    #     lis1=maincolumns[1]
    #     lis2=maincolumns[2]


    # l1 = pd.read_sql_query(f'select * from {table_name[0]}', con=engine)
    # l2 = pd.read_sql_query(f'select * from {table_name[1]}', con=engine)
    # mkt = l1.iloc[0:, 1:]
    # dataft = mkt.to_json(orient='records')
    # s1 = json.loads(dataft)
    # mkt1 = l2.iloc[0:, 1:]
    # dat = mkt1.to_json(orient='records')
    # s2 = json.loads(dat)
    # valuess1 = [list(x.values()) for x in s1]
    #     # # get the column names
    # columnss1 = [list(x.keys()) for x in s1][0]
    # valuess2 = [list(x.values()) for x in s2]
    # # # get the column names
    # columnss2 = [list(x.keys()) for x in s2][0]

    lists=[]
    for i in range(len(table_name)):
        l1 = pd.read_sql_query(f'select * from {table_name[i]}', con=engine)
        mkt = l1.iloc[0:, 1:]
        dataft = mkt.to_json(orient='records')
        dataftj = json.loads(dataft)
        # values = [list(x.values()) for x in dataftj]
        # # get the column names
        columns = [list(x.keys()) for x in dataftj][0]
        for j in columns:
            lists.append(j+"_"+(table_name[i]))
    # return render(request,'dmac/posttable.html',{'tablename_list':tablename_list,'module_dict':module_dict,'columnss1':columnss1,'columnss2':columnss2,'valuess1':valuess1,'valuess2':valuess2,'lists':lists})
    return render(request,'dmac/posttable.html',{'tab1':tab1,'tab2':tab2,'stick1':stick1,'stick2':stick2,'manag':manag,'tablename_list':tablename_list,'module_dict':module_dict,'maincolumns':maincolumns,'mainvalues':mainvalues,'lists':lists,'d_columns':d_columns,'d_values':d_values})

# @api_view(["POST"])
def postdata(request):
    # try:
    if request.method == "POST":
        table_name = request.POST.get('table_name')
        # table_name = json.loads(table_name.body)
    print(table_name)
    # table="your selected table:"+" "+table_name
    engine = create_engine('postgresql://postgres:Programming123@localhost:5432/postgres')
    # engine = create_engine('postgresql://postgres:Programming123@localhost:5432/postgres')
    df_aws2 = pd.read_sql_query("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';",
                                con=engine)
    tablename_list = list(df_aws2["relname"])
    # l3.to_sql('legacytable3', engine,  if_exists='append')
    l1 = pd.read_sql_query(f'select * from {table_name}', con=engine)
    mkt = l1.iloc[0:, 1:]
    dataft = mkt.to_json(orient='records')
    dataftj =json.loads(dataft)
    values = [list(x.values()) for x in dataftj]
    # # get the column names
    columns = [list(x.keys()) for x in dataftj][0]
    return render(request,'dmac/login.html',{'tablename_list':tablename_list,'dataft':dataft,'columns':columns,'values':values})


# @api_view(["POST"])
def rest(request):
    # try:
    if request.method == "POST":
        table_names = request.POST.getlist('tablename')
        # desc = request.POST.get('desc')
        # table_name = json.loads(table_name.body)
    print(table_names)
    kim = []
    kim2 = []
    for i in table_names:
        kl=i.split("_")
        kim.append(kl[0])
        kim2.append(kl[1])
    print(kim)
    dim=set(kim2)
    print(dim)
    lik=list(dim)

    k1 = kim[0]
    k2 = kim[1]


        # table_name = json.loads(table_name.body)

    mainvalues = []
    maincolumns = []
    colfunctionlist = []
    module_dict = {"0": "module 1", "1": "module 2", "2": "module3"}
    engine = create_engine('postgresql://postgres:Programming123@localhost:5432/postgres')
    for i in range(len(lik)):
        l1 = pd.read_sql_query(f'select * from {lik[i]}', con=engine)
        mkt = l1.iloc[0:, 1:]
        dataft = mkt.to_json(orient='records')
        colfunctionlist.append(dataft)
        s1 = json.loads(dataft)
        valuess1 = [list(x.values()) for x in s1]
        # d_cities = dict.fromkeys(cities, 'UK')
        mainvalues.append(valuess1)
        columnss1 = [list(x.keys()) for x in s1][0]
        maincolumns.append(columnss1)
    d_columns = dict(zip(lik, maincolumns))
    d_values = dict(zip(lik, mainvalues))
    manag = [1, 2]
    # print(maincolumns)
    stick1 = maincolumns[0]
    stick2 = maincolumns[1]
    tab1 = colfunctionlist[0]
    tab2 = colfunctionlist[1]

    lists = []

    for i in range(len(lik)):
        l1 = pd.read_sql_query(f'select * from {lik[i]}', con=engine)
        mkt = l1.iloc[0:, 1:]
        dataft = mkt.to_json(orient='records')
        dataftj = json.loads(dataft)
        # values = [list(x.values()) for x in dataftj]
        # # get the column names
        columns = [list(x.keys()) for x in dataftj][0]
        for j in columns:
            lists.append(j + "_" + (lik[i]))

    # table="your selected table:"+" "+table_name

    # engine = create_engine('postgresql://postgres:Programming123@localhost:5432/postgres')
    df_aws2 = pd.read_sql_query("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';",
                                con=engine)
    tablename_list = list(df_aws2["relname"])

    # # # l3.to_sql('legacytable3', engine,  if_exists='append')
    # l1 = pd.read_sql_query(f'select * from {lik[0]}', con=engine)
    # mkt = l1.iloc[0:, 1:]
    # l2 = pd.read_sql_query(f'select * from {lik[1]}', con=engine)
    # mkt1 = l2.iloc[0:, 1:]
    # ckt1=pd.merge(mkt,mkt1,how="outer")
    #
    # # ckt1=pd.concat([mkt,mkt1],axis=1)
    # print(ckt1)
    # ckt=ckt1[kim]
    # ckt.to_sql(desc, engine, if_exists='append')
    # # obj=EmployeeEmails.objects.create(table1="new")
    # # print(ckt)
    # # fz=EmployeeEmails.objects.all()
    # # ms=fz
    # # print(ms)
    # dataft = ckt.to_json(orient='records')
    # dataftj =json.loads(dataft)
    # valuesld = [list(x.values()) for x in dataftj]
    # # # # get the column names
    # columnsld = [list(x.keys()) for x in dataftj][0]
    # return render(request,'dmac/posttable.html',{'tablename_list':tablename_list,'valuesld':valuesld,'columnsld':columnsld})
    # return render(request,'dmac/posttable.html',{'tablename_list':tablename_list,})
    return render(request,'dmac/posttable.html',{'k1':k1,'k2':k2,'tab1':tab1,'tab2':tab2,'stick1':stick1,'stick2':stick2,'manag':manag,'tablename_list':tablename_list,'module_dict':module_dict,'maincolumns':maincolumns,'mainvalues':mainvalues,'lists':lists,'d_columns':d_columns,'d_values':d_values})


# def capital(request,ckt):
#     print(ckt)
#     return render(request,'dmac/posttable.html')
def thankyou(request):
    engine = create_engine('postgresql://postgres:Programming123@localhost:5432/postgres')
    # engine = create_engine('postgresql://postgres:Programming123@localhost:5432/postgres')
    df_aws2 = pd.read_sql_query("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';",
                                con=engine)
    tablename_list = list(df_aws2["relname"])

    # # l3.to_sql('legacytable3', engine,  if_exists='append')
    l1 = pd.read_sql_query('select * from "saptable1" ', con=engine)
    mkt = l1.iloc[0:, 1:]
    data=mkt

    # response = requests.get('http://127.0.0.1:8000/rest/')
    # tables = pd.read_html(r.text)
    # print('Tables found:', len(tables))
    # print(tables)
    # print(r.text)
    # Parse the HTML pages

    # from bs4 import BeautifulSoup
    # soup = BeautifulSoup(response.text, 'html.parser')
    # det = soup.find_all("table")
    # tables = pd.read_html(response.text)
    # print(tables)

    # You can extract the page title as string as well

    # Find all the h3 elements
    # print(f"{tutorialpoints_page.find_all('h2')}")
    # tags = tutorialpoints_page.find(
    #     lambda elm: elm.name == "h2" or elm.name == "h3" or elm.name == "h4" or elm.name == "h5" or elm.name == "h6")
    # for sibling in tags.find_next_siblings():
    #     if sibling.name == "table":
    #         my_table = sibling
    # df = pd.read_html(str(my_table))
    # print(df)
    if request.method == "POST":
        tabl = request.POST.get('jsonData')
        rules = request.POST.getlist('rules')
        print(rules)
        sit = json.loads(tabl)
        frame = pd.DataFrame(sit)
        frame = frame.iloc[0:, 1:]
        plusdata1 = frame.to_json(orient='records')
        plusdata2 = json.loads(plusdata1)
        # git = {'lispr':sit}
        # print(git)

        def del_none(d):
            """
            Delete keys with the value ``None`` in a dictionary, recursively.

            This alters the input so you may wish to ``copy`` the dict first.
            """
            # For Python 3, write `list(d.items())`; `d.items()` won’t work
            # For Python 2, write `d.items()`; `d.iteritems()` won’t work
            for key, value in list(d.items()):
                if value == "":
                    del d[key]
                elif isinstance(value, dict):
                    del_none(value)
            return d  # For convenience
        listdf = []
        for f in plusdata2:
            listdf.append(del_none(f.copy()))
            print(del_none(f.copy()))



            # def del_none(f):
            #     for key, value in list(f.items()):
            #         if value is None:
            #             del f[key]
            #         elif isinstance(value, dict):
            #             del_none(value)
            #         lift.append(f)
            # # return d
            #
            # del_none(f.copy())





        print(listdf)





        # print(frame)
        # print(frame.info)

        # print(plusdata)
        # tablu = JSONParser().parse('jsonData')
        # desc = request.POST.get('desc')
        # table_name = json.loads(table_name.body)
    # print(type(plusdata))
    plusdata = listdf
    plusdata.sort(key=lambda item: item.get("NAME"))
    # print(plusdata)


    for i in range(len(plusdata) - 1):
        if (plusdata[i]["NAME"] == plusdata[i + 1]["NAME"]):
                plusdata[i].update(plusdata[i + 1])

        for i in range(len(plusdata) - 1):
            if (plusdata[i]["NAME"] == plusdata[i + 1]["NAME"]):
                plusdata[i].update(plusdata[i + 1])
                plusdata[i + 1].update(plusdata[i])
        fitdata = list(unique_everseen(plusdata, key=lambda item: frozenset(item.items())))
        # print(fitdata)
        l1 = pd.DataFrame(fitdata)

        print(l1)
    try:
        if rules[0]=="name_spliter":
            def string_split(x):
                fd = x.split(" ")
                return fd[0]

            l1["first_name"] = l1["NAME"].apply(string_split)

            def string_last(x):
                try:
                    fd = x.split(" ")
                    return fd[1]
                except:
                    pass

            l1["last_name"] = l1["NAME"].apply(string_last)
            table1 = l1.to_html()
        elif rules[0]=="string resizer":
            def digit_tracker(x):
                d = str(x)
                k = len(d)
                if k <= 8:
                    spd = "0" * (8 - k) + d
                    return spd
                else:
                    spd = d[0:8]
                    return spd

            l1['PHONE_new'] = l1['PHONE'].apply(digit_tracker)
            table1 = l1.to_html()

        elif rules[0]=="first+last":
            l1["merge_two_column"] = l1["NAME"]+" "+l1["WERKS"]
            table1= l1.to_html()
        else:
            table1 = l1.to_html()
    except:
        l1.to_sql('mckinsolteam', engine, if_exists='append')
        table1 = l1.to_html()


    # print(rules[0])

    return HttpResponse(table1)
        # concat = l1.to_json(orient='records')
        # final = json.loads(concat)
    # return render(request,'dmac/thankyou.html',{'data':data})




def postdata1(request):
    # try:
    if request.method == "POST":
        table_name1 = request.POST.get('table_name1')
        # table_name = json.loads(table_name.body)
    engine = create_engine('postgresql://postgres:Programming123@localhost:5432/postgres')
    # engine = create_engine('postgresql://postgres:Programming123@localhost:5432/postgres')
    df_aws2 = pd.read_sql_query("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';",
                                con=engine)
    tablename_list = list(df_aws2["relname"])
    # l3.to_sql('legacytable3', engine,  if_exists='append')
    l2 = pd.read_sql_query(f'select * from {table_name1}', con=engine)
    mkt = l2.iloc[0:, 1:]
    dataft1 = mkt.to_json(orient="records")
    dataftj1 = json.loads(dataft1)
    values1 = [list(x.values()) for x in dataftj1]
    # # get the column names
    columns1 = [list(x.keys()) for x in dataftj1][0]
    return render(request,'dmac/login.html',{'tablename_list':tablename_list,'dataft1':dataft1,'columns1':columns1,'values1':values1})

def postdata3(request):
    # try:
    if request.method == "POST":
        table_name1 = request.POST.get('table_name1')
        # table_name = json.loads(table_name.body)
    engine = create_engine('postgresql://postgres:Programming123@localhost:5432/postgres')
    # engine = create_engine('postgresql://postgres:Programming123@localhost:5432/postgres')
    df_aws2 = pd.read_sql_query("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';",
                                con=engine)
    tablename_list = list(df_aws2["relname"])
    # l3.to_sql('legacytable3', engine,  if_exists='append')
    l2 = pd.read_sql_query(f'select * from {table_name1}', con=engine)
    mkt = l2.iloc[0:, 1:]
    dataft1 = mkt.to_json(orient="records")
    dataftj1 = json.loads(dataft1)
    valuesx = [list(x.values()) for x in dataftj1]
    # # get the column names
    columnsx = [list(x.keys()) for x in dataftj1][0]
    # return redirect('dmac:adminhome',{columnsx,valuesx})
    return render(request,'dmac/login.html',{'tablename_list':tablename_list,'dataft1':dataft1,'columnsx':columnsx,'valuesx':valuesx})




def addtable(request):
    if request.method == "POST":
        table1 = request.POST.get('table_name1')
        table2 = request.POST.get('table_name2')
        # print(table1)
        # print(table2)

    engine = create_engine('postgresql://postgres:Programming123@localhost:5432/postgres')
    # l3.to_sql('legacytable3', engine,  if_exists='append')
    df_aws2 = pd.read_sql_query("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';",
                                con=engine)
    tablename_list = list(df_aws2["relname"])
    l1 = pd.read_sql_query(f'select * from {table1}', con=engine)
    l2 = pd.read_sql_query(f'select * from {table2}', con=engine)
    m1 = l1.iloc[0: ,1:]
    m2 = l2.iloc[0: ,1:]

    merg1 = pd.merge(m1, m2, how="outer")
    # mkt=merg1.iloc[0: ,1:]
    concat = merg1.to_json(orient='records')
    dataftj1 = json.loads(concat)
    values2 = [list(x.values()) for x in dataftj1]
    # # get the column names
    columns2 = [list(x.keys()) for x in dataftj1][0]
    # merg1["Full Name"] = merg1["First Name"] + "  " + merg1["Last Name"]

    # display colums
    lists = []
    # for i in range(len(table_name))
    dataft = m1.to_json(orient='records')
    dataftj = json.loads(dataft)
    dill = m2.to_json(orient='records')
    dill2 = json.loads(dill)
    col1 = [list(x.keys()) for x in dataftj][0]
    col2 = [list(x.keys()) for x in dill2][0]
    for j in col1:
        lists.append(j + "_" + (table1))
    for j in col2:
        lists.append(j + "_" + (table2))
    # for i in range(len(table_name)):
    #     l1 = pd.read_sql_query(f'select * from {table_name[i]}', con=engine)
    #     mkt = l1.iloc[0:, 1:]
    #     dataft = mkt.to_json(orient='records')
    #     dataftj = json.loads(dataft)
    #     # values = [list(x.values()) for x in dataftj]
    #     # # get the column names
    #     columns = [list(x.keys()) for x in dataftj][0]
    #     for j in columns:
    #         lists.append(j + "_" + (table_name[i]))
    module_dict = json.dumps(lists)

    return render(request,'dmac/login.html',{'merg1':merg1,'concat':concat,'tablename_list':tablename_list,'columns2':columns2,'values2':values2,'module_dict':module_dict})



def concattable(request):
    return render(request,'dmac/concat.html')

# @api_view(["POST"])
def concatdata(request):
    try:
        if request.method == "POST":
            table1 = request.POST.get('table_name1')
            table2 = request.POST.get('table_name2')
            print(table1)
            print(table2)

        engine = create_engine('postgresql://postgres:Programming123@localhost:5432/postgres')
        # l3.to_sql('legacytable3', engine,  if_exists='append')
        l1 = pd.read_sql_query(f'select * from {table1}', con=engine)
        l2 = pd.read_sql_query(f'select * from {table2}', con=engine)
        merg1 = pd.merge(l1, l2, how="outer")
        concat = merg1.to_json(orient='records')
        # merg1["Full Name"] = merg1["First Name"] + "  " + merg1["Last Name"]

        return render(request,'dmac/concat.html',{'merg1':merg1,'concat':concat})
    except:
        table_name = json.loads(request.body)
        # table_name=pd.read_csv(request.body)
        print(table_name)

        #
        # engine = create_engine('postgresql://postgres:Programming123@localhost:5432/postgres')
        # # l3.to_sql('legacytable3', engine,  if_exists='append')
        # l1 = pd.read_sql_query(f'select * from {table_name}', con=engine)
        # data1 = l1.to_json(orient='records')

        # return JsonResponse("Ideal weight should be:" + data1, safe=False)
        return JsonResponse(table_name, safe=False)

def dragdrop(request):
    if request.method== 'POST':
        datam = request.POST.get('json_items')
        data=datam.split(",")
        # data1 = request.POST.get('page_contents[]')
        print(data)
        print(type(data))

        kim = []
        kim2 = []
        for i in data:
            kl = i.split("_")
            kim.append(kl[0])
            kim2.append(kl[1])
        print(kim)
        dim = set(kim2)
        print(dim)
        lik = list(dim)

        # table="your selected table:"+" "+table_name
        engine = create_engine('postgresql://postgres:Programming123@localhost:5432/postgres')
        # engine = create_engine('postgresql://postgres:Programming123@localhost:5432/postgres')
        df_aws2 = pd.read_sql_query("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';",
                                    con=engine)
        tablename_list = list(df_aws2["relname"])

        # # l3.to_sql('legacytable3', engine,  if_exists='append')
        l1 = pd.read_sql_query(f'select * from {lik[0]}', con=engine)
        mkt = l1.iloc[0:, 1:]
        l2 = pd.read_sql_query(f'select * from {lik[1]}', con=engine)
        mkt1 = l2.iloc[0:, 1:]
        ckt1 = pd.merge(mkt, mkt1, how="outer")

        # ckt1=pd.concat([mkt,mkt1],axis=1)
        print(ckt1)
        ckt = ckt1[kim]
        # ckt.to_sql(desc, engine, if_exists='append')
        # obj=EmployeeEmails.objects.create(table1="new")
        # print(ckt)
        # fz=EmployeeEmails.objects.all()
        # ms=fz
        # print(ms)
        dataft = ckt.to_json(orient='records')
        dataftj = json.loads(dataft)
        valuesld = [list(x.values()) for x in dataftj]
        # # # get the column names
        columnsld = [list(x.keys()) for x in dataftj][0]
    return render(request, 'dmac/login.html',{'columnsld':columnsld,'valuesld':valuesld,'tablename_list':tablename_list})

def dmacpage(request):
    engine = create_engine('postgresql://postgres:Programming123@localhost:5432/postgres')
    df_aws2 = pd.read_sql_query("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';",con=engine)
    tablename_list = list(df_aws2["relname"])
    return render(request,'dmac/dmac.html',{'tablename_list':tablename_list})

#
# @csrf_exempt
# def article_list(request):
#
#     if request.method == 'GET':
#         articles = Lead.objects.all()
#         serializer =LeadSerializer(articles, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         s1=data["table1"]
#         s2=data["table2"]
#         engine = create_engine('postgresql://postgres:Programming123@localhost:5432/postgres')
#         # l3.to_sql('legacytable3', engine,  if_exists='append')
#         l1 = pd.read_sql_query(f'select * from {s1}', con=engine)
#         l2 = pd.read_sql_query(f'select * from {s2}', con=engine)
#         merg1 = pd.merge(l1, l2, how="outer")
#         print(merg1)
#         concat = merg1.to_json(orient='records')
#         final=json.loads(concat)
#         print(final)
#         print(type(final))
#         serializer = LeadSerializer(data=data)
#         # print(serializer.data["table1"])
#         # print(serializer.data["table2"])
#
#         # if serializer.is_valid():
#         #     serializer.save()
#         # return concat
#         return JsonResponse(final, safe=False)
#         # return JsonResponse(serializer.errors, status=400)
#
#
# @csrf_exempt
# def tab_details(request):
#         data = JSONParser().parse(request)
#         print(type(data))
#         # s1=data["table1"]
#         engine = create_engine('postgresql://postgres:Programming123@localhost:5432/postgres')
#         # # l3.to_sql('legacytable3', engine,  if_exists='append')
#         l1 = pd.read_sql_query(f'select * from {data}', con=engine)
#         print(l1)
#         # l2 = pd.read_sql_query(f'select * from {s2}', con=engine)
#         # merg1 = pd.merge(l1, l2, how="outer")
#         # print(merg1)
#         concat = l1.to_json(orient='records')
#         final=json.loads(concat)
#
#         return JsonResponse(final, safe=False)
#         # return JsonResponse(serializer.errors, status=400)
#
#
# @csrf_exempt
# def jsonreducer(request):
#     data = JSONParser().parse(request)
#     print(data)
#     plusdata = data
#     print(plusdata)
#     plusdata.sort(key=lambda item: item.get("id"))
#     print(plusdata)
#     for i in range(len(plusdata) - 1):
#         if (plusdata[i]["id"] == plusdata[i + 1]["id"]):
#             plusdata[i].update(plusdata[i + 1])
#
#     for i in range(len(plusdata) - 1):
#         if (plusdata[i]["id"] == plusdata[i + 1]["id"]):
#             plusdata[i].update(plusdata[i + 1])
#             plusdata[i + 1].update(plusdata[i])
#     fitdata = list(unique_everseen(plusdata, key=lambda item: frozenset(item.items())))
#
#     # concat = l1.to_json(orient='records')
#     # final = json.loads(concat)
#
#     return JsonResponse(fitdata, safe=False)
#     # return JsonResponse(serializer.errors, status=400)
#
# @csrf_exempt
# def save_json_to_table(request):
#     data = JSONParser().parse(request)
#     mdata=pd.DataFrame(data)
#     print(mdata)
#     # print(data)
#     engine = create_engine('postgresql://postgres:Programming123@localhost:5432/postgres')
#     mdata.to_sql('legacy', engine,  if_exists='append')
#
#
#     # concat = l1.to_json(orient='records')
#     # final = json.loads(concat)
#
#     return JsonResponse(data, safe=False)
#     # return JsonResponse(serializer.errors, status=400)

def tables(request):
    return render(request,'dmac/table.html')
