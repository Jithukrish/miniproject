import functools
import os
#from email.headregistry import Address
#from unicodedata import category
#from click import password_option
from flask import *
from werkzeug.utils import secure_filename

from src.dbconnection import *
from datetime import datetime
app=Flask(__name__)
app.secret_key = 'abc'


def login_required(func):
	@functools.wraps(func)
	def secure_function():
		if "lid" not in session:
			return render_template('login_index.html')
		return func()
	return secure_function


@app.route('/logout')
@login_required
def logout():
	session.clear()
	return redirect('/')


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/log')
def log():
    return render_template("loginindex.html")

#login function
@app.route('/login', methods=['post'])
def login():
    username=request.form['username']
    password=request.form['password']
    qry=" SELECT * FROM login WHERE u_name=%s and password=%s"
    val=(username,password)
    res=selectone(qry,val)
    if res is None:
        return '''<script>alert("invalid");window.location="/log"</script>'''
    elif res['user type'] == "admin":
        session['lid'] = res['l_id']
        return '''<script>alert("valid");window.location="admin"</script>'''
    elif res['user type'] == "user":
         session['lid'] = res['l_id']
         return '''<script>alert("valid");window.location="userhome"</script>'''
    elif res['user type'] == "trainer":
         session['lid'] = res['l_id']

         q="SELECT * FROM `trainer` WHERE l_id =%s"
         res = selectone(q,session['lid'])
         session['type'] = res['type']
         return '''<script>alert("valid");window.location="trainerhome"</script>'''


    else:
        return '''<scrpit>alert("invalid");window.location="/log"</scrpit>'''

#adin functions
@app.route('/admin')
@login_required
def admin():
    return render_template("admin home.html")
#view user details
@app.route('/vuser')
@login_required
def viewuser():
    q="SELECT * FROM `registration`"
    res=selectall(q)
    print(res)
    return render_template("aduser.html",val=res)
#add trainer

@app.route('/add-trainer',methods=['post'])
@login_required
def addTraner():
    try:
        User = request.form['textfield']
        Place = request.form['textfield2']
        Gender = request.form['RadioGroup1']
        Email = request.form['textfield4']
        DOB = request.form['textfield5']
        Phoneno = request.form['textfield3']
        qualification=request.form['select']
        type = request.form['textfield6']
        u_name = request.form['textfield7']
        password = request.form['textfield8']
        qry = "INSERT INTO `login` VALUES(NULL,%s,%s,'trainer')"
        val = (u_name, password)
        id = iud(qry, val)
        qry1 = "INSERT INTO `trainer` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val1 = (str(id), User, Place, Gender,Phoneno,Email,DOB,type,qualification)
        iud(qry1, val1)

        return '''<script>alert("Registerd successfuly");window.location="viewtrainer"</script>'''
    except Exception as e:
        print(e)
        return '''<script>alert("Duplicate Entry!!!!!!!!!!1");window.location="viewtrainer"</script>'''

#view trainer
@app.route('/viewtrainer')
@login_required
def vtrainer():
    q="SELECT * FROM `trainer`"
    res = selectall(q)
    return render_template("view trainer.html",val=res)


@app.route('/addt')
@login_required

def addtrainer():

    return render_template("trainer.html")
@app.route('/verifytrainer')
def verft():
    q="SELECT `registration`.`username`,`request`.* FROM `registration` JOIN `request` ON `registration`.`l_id`=`request`.`u_id`"
    res=selectall(q)
    return render_template("admin verify req.html",val=res)

@app.route('/assigntrain/<rid>',methods=['get','post'])
def asstrain(rid):
    if request.method=="POST":
        tid = request.form['select']
        q = "UPDATE request set`t_id`=%s,status='assigned' where r_id=%s"
        iud(q, (tid,rid))
        return '''<script>alert("Assigned successfuly");window.location="/verifytrainer"</script>'''

    else:
        q="SELECT * FROM `trainer`"
        res=selectall(q)
        return render_template("ASSIGN_TRAINER.html",val=res)


# @app.route('/assign')
# def assign():
#
#     return render_template("ASSIGN_TRAINER.html",val)

#add services

@app.route('/addservic')
@login_required

def addservic():
    return render_template("service.html")
@app.route('/addser',methods=['get','post'])
@login_required

def addser():
        servicename = request.form['textfield']
        image = request.form['file']
        description = request.form['textfield2']

        qry1 = "INSERT INTO `service` VALUES(NULL,%s,%s,%s)"
        val1 = (servicename,image,description)
        iud(qry1, val1)
        return '''<script>alert("Add successfuly");window.location="admin home.html"</script>'''

#view services
@app.route('/viewser')
@login_required

def viewser():
    q="SELECT *FROM`service`"
    res=selectall(q)
    return render_template("viewser.html",val=res)
#user virw service
@app.route('/viewservice')
def viewservice():
    q="SELECT *FROM`service`"
    res=selectall(q)
    return render_template("viewservice.html",val1=res)


# add bodymeasurement

@app.route('/bodymes',methods=['post'])
@login_required

def bodymes():
    ulid=request.form['select']
    shoulder = request.form['textfield2']
    leftsholtoelbow = request.form['textfield4']
    leftelbotohand = request.form['textfield5']
    rightsholtoelbow = request.form['textfield6']
    rightelbotohand = request.form['textfield7']
    Rwaisttoknee = request.form['textfield10']
    Rkneetofoot = request.form['textfield11']
    Lwaisttoknee = request.form['textfield8']
    Lkneetofoot = request.form['textfield9']
    qry1 = "INSERT INTO `bodymeasurement` VALUES(NULL,%s,curdate(),%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1 = (ulid ,shoulder,leftsholtoelbow,leftelbotohand,rightsholtoelbow,rightelbotohand,Lwaisttoknee,Lkneetofoot,Rwaisttoknee,Rkneetofoot )
    iud(qry1, val1)
    return '''<script>alert("Add successfuly");window.location="viewbody#about"</script>'''

@app.route('/updatebody',methods=['post'])
@login_required

def updatebody():

    shoulder = request.form['textfield2']
    date = request.form['textfield28']

    leftsholtoelbow = request.form['textfield4']
    leftelbotohand = request.form['textfield5']
    rightsholtoelbow = request.form['textfield6']
    rightelbotohand = request.form['textfield7']
    Rwaisttoknee = request.form['textfield10']
    Rkneetofoot = request.form['textfield11']
    Lwaisttoknee = request.form['textfield8']
    Lkneetofoot = request.form['textfield9']
    qry1="UPDATE  `bodymeasurement` SET `date`=%s,`shoulder`=%s,`right_shoulder_to_elbow`=%s,`right_elbow_to_hand`=%s,`left_shoulder_to_elbow`=%s,`left_elbow_to_hand`=%s,`right_waist_to_knee`=%s,`right_knee_to_foot`=%s,`left_waist_to_knee`=%s,`left_knee_to_foot`=%s WHERE `bd_id`=%s "
    val1=(date,shoulder,rightsholtoelbow,rightelbotohand,leftsholtoelbow,leftelbotohand,Rwaisttoknee,Rkneetofoot,Lwaisttoknee,Lkneetofoot,session['e_id'])
    iud(qry1, val1)
    return '''<script>alert("updated successfuly");window.location="viewbody#about"</script>'''
#adding

# @app.route('/addbody')
# def addbody():
#     qry="select * from registration "
#     res=selectall(qry)
#
#
#     return render_template("edit_measurement.html",val=res)

#edit measurement

# @app.route('/editmes')
# def editmes():
#     q="select * from measurement "
#     res=selectone(q)
#     return render_template("edit_measurement.html",val=res)

#view update bodymeasurement

@app.route('/editmesview')
def editmesview():
    id = request.args.get('id')
    session['e_id']=id
    q="SELECT * FROM `bodymeasurement` WHERE `bd_id`=%s"
    res=selectone(q,id)
    return render_template("edit_measurement.html",val=res)




@app.route('/delete_mesr')
def delete_mesr():
    id = request.args.get('id')
    q="delete  FROM `bodymeasurement` WHERE `bd_id`=%s"
    res=iud(q,id)
    return '''<script>alert("delete successfuly");window.location="viewbody"</script>'''
    # adding
#view bodymeasurement triner

@app.route('/viewbody')
def viewbody():
    q="SELECT `bodymeasurement`.*,`registration`.username FROM `bodymeasurement` JOIN `registration` ON `bodymeasurement`.u_id=`registration`.l_id"
    res=selectall(q)
    return render_template("view measurement(2).html",val=res)




# user view bodymeasurement
@app.route('/viewbodys')
def viewbodys():
    q="SELECT * FROM `bodymeasurement` where u_id=%s "
    res = selectall2(q, session['lid'])
    return render_template("view measurement user.html",val=res)

#add new member in bodymeasurement table


@app.route('/addbodyuser')
def addbodyuser():
    qry1="select * from registration"
    res1=selectall(qry1)
    return render_template("add measurement.html",val1=res1)

    # if type=="personal":
    #     qry="select `registration`.* from `registration` join `allocation` on `registration`.l_id=`allocation`.u_id"
    #     res=selectall(qry)
    #     return render_template("add measurement.html",val=res,val1=res1)
    # else:
    #     q="select * from `registration` where l_id not in(select  u_id from `allocation`)"
    #     res=selectall(q)


#user information

@app.route('/userhome')
def user():

    return render_template("user home.html")
#request send to admin
@app.route('/sndreq')
def sndreq():
  return render_template("user send req.html")
@app.route('/send',methods=["post"])
def snd():
    q="SELECT * FROM `request` WHERE `u_id`=%s"
    res=selectone(q,session['lid'])
    if res is None:
        req=request.form['textfield']
        query="INSERT INTO `request` VALUES(NULL,%s,'0',%s,'pending',CURDATE())"
        vall=(str(session['lid']),req)
        iud(query,vall)
        return '''<script>alert("request sended successfully");window.location="/userhome"</script>'''

    else:
        return '''<script>alert("already requested");window.location="/userhome"</script>'''


#check request user

@app.route('/checkreq')
def checreq():
    r="SELECT * FROM  `request` JOIN `trainer` ON `request`.`t_id`=`trainer`.`t_id` AND `request`.`u_id`=%s"
    res=selectall2(r,session['lid'])
    return render_template("admin reqview.html",val=res)
@app.route('/trainerhome')
def trainer():
    return render_template("trainerhome.html")
###########################################################################################################################################
############################ATTENDANCE$#####################################
@app.route('/ATTANDANCEMARK')
def ATTANDANCEMARK():
     q="SELECT * FROM `registration`"
     res=selectall(q)
     return render_template("MARKATTENDANCE.html",val=res)

@app.route('/ATTANDANCEMARK2')
def ATTANDANCEMARK2():
    id = request.args.get('id')
    session['l_id'] = id
    return render_template("ATTANDANCEMARK.html")

@app.route('/ATTANDANCEMARK3',methods=['post'])
def ATTANDANCEMARK3():
    attentance=request.form['RadioGroup1']
    qr="SELECT * FROM attendance WHERE `date`=CURDATE() AND `u_id`=%s"
    res=selectone(qr,session['l_id'])
    if res is None:
        q = "INSERT INTO `attendance` VALUES(NULL,%s,%s,CURDATE(),%s)"
        val=(str(session['l_id']),str(session['lid']),attentance)
        iud(q,val)
        return '''<script>alert("Attentance added successfully");window.location="/ATTANDANCEMARK"</script>'''
    else:
        return '''<script>alert("Attentance already added");window.location="/ATTANDANCEMARK"</script>'''

@app.route('/useratten')
def useratten():
     q = "SELECT `trainer`.`name`,`attendance`.* FROM `trainer` JOIN `attendance` ON `trainer`.l_id=`attendance`.t_id WHERE `attendance`.`u_id`=%s"
     res = selectall2(q,session['lid'])
     print(res)
     return render_template("VIEWATTENDANCEUSER.html", val=res)







#view work hour normal admin
@app.route('/wrkhr')
def wrkhr():
    q="SELECT*FROM `wrk_gen` "
    res=selectall(q)
    return render_template("workhourN.html",val=res)

#view work hour normal user
@app.route('/wrkhrn')
def wrkhrn():
    q="SELECT*FROM `wrk_gen` "
    res=selectall(q)
    return render_template("userviewgenhr.html",val=res)

@app.route('/view_gim_time')
def view_gim_time():
    q="SELECT*FROM `wrk_gen` "
    res=selectall(q)
    return render_template("view_gim_time.html",val=res)

#add hour

@app.route('/wrkhraddd',methods=['post'])
def wrkhraddd():

    day = request.form['select']
    from_time = request.form['textfield']
    to_time = request.form['textfield2']
    qry1 = "INSERT INTO `wrk_gen` VALUES(NULL,%s,%s,%s)"
    val1 = (day,from_time,to_time)
    iud(qry1, val1)
    return '''<script>alert("Add successfuly");window.location="wrkhr"</script>'''

@app.route('/wrkhradd')
def wrkhradd():
     return render_template("add new schedule.html")
#delete hour
@app.route('/delhr')
def delhr():
    id=request.args.get('id')

    q="delete FROM `wrk_gen` where `wrk_hid`=%s "
    iud(q,id)
    return '''<script>alert("delete successfuly");window.location="wrkhr"</script>'''
#personal user hour add

@app.route('/wrkhrpr',methods=['post'])
def wrkhrpr():

    day = request.form['textfield1']
    from_time = request.form['textfield2']
    to_time = request.form['textfield3']
    qry1 = "INSERT INTO `work_hourper` VALUES(NULL,%s,%s,%s)"
    val1 = (from_time,to_time,day)
    iud(qry1, val1)
    return '''<script>alert("Add successfuly");window.location="adminhome"</script>'''
    # return render_template("userpersonal.html",val=res)

@app.route('/wrkhrprr',methods=['post'])
def wrkhrprr():
    return render_template("userpersonal.html")


@app.route('/wrkhrprr_post',methods=['post'])
def wrkhrprr_post():
    print(request.form)
    uid = request.form['select']
    day = request.form['textfield3']
    from_time = request.form['textfield']
    to_time = request.form['textfield2']
    qry1 = "INSERT INTO `work_hourper` VALUES(NULL,%s,%s,%s,%s)"
    val1 = (uid,day,from_time, to_time)
    iud(qry1, val1)
    return '''<script>alert("Add successfuly");window.location="prhour"</script>'''
    # return render_template("userpersonal.html")


#view personal hour
@app.route('/prhour')
def prhour():
    q="SELECT*FROM `work_hourper` "

    qq = "SELECT * FROM `registration`,`request` WHERE `request`.`u_id`=`registration`.`l_id` AND `request`.`status`='accepted' "
    res=selectall(q)
    res1=selectall(qq)
    print(res,"+++++++++++++++++++++++++++")
    print(res1,"============================")
    return render_template("userpersonal.html",val=res,val2=res1)




@app.route('/shedule_user_to_tr')
def shedule_user_to_tr():
    qry="select * from registration"
    res=selectall(qry)
    qry1 = "select * from trainer"
    res1 = selectall(qry1)

    return render_template("shedule_user_to_tr.html",val=res,val1=res1)


@app.route('/shedule_user_to_tr1',methods=['post'])
def shedule_user_to_tr1():

     username=request.form['select']
     trainer=request.form['select2']

     from_time = request.form['textfield2']
     to_time = request.form['textfield3']
     qry1 = "INSERT INTO `schedule personal user` VALUES(NULL,%s,%s,curdate(),%s,%s)"
     val1 = (username,trainer,from_time,to_time)
     print("=======================================================================================")
     iud(qry1,val1)
     return '''<script>alert("Add successfuly");window.location="shedule_user_to_tr"</script>'''



@app.route('/personaltimeforuser')
def personaltimeforuser():
    qry="select * from registration"
    res=selectall(qry)
    qry1 = "select * from trainer"
    res1 = selectall(qry1)

    return render_template("personal time user.html",val=res,val1=res1)

@app.route('/personaltimeforuser1',methods=['post'])
def personaltimeforuser1():

     trainer=request.form['select']
     username=request.form['select1']
     from_time = request.form['textfield']
     to_time = request.form['textfield2']
     qry1 = "INSERT INTO `schedule personal user` VALUES(NULL,%s,%s,%s,%s)"
     val1 = (username,trainer,from_time, to_time)
     iud(qry1,val1)
     return '''<script>alert("Add successfuly");window.location="personaltimeforuser"</script>'''

#view personal hour
@app.route('/prhourh')
def prhourh():
    q="SELECT `trainer`.*,`schedule personal user`.*  FROM `trainer` JOIN `schedule personal user` ON `trainer`.l_id=`schedule personal user`.`t_id` WHERE `schedule personal user`.`u_id`=%s"
    res=selectall2(q,session['lid'])
    print(session['lid'])
    print(res,"=================")
    return render_template("personaltime.html",val=res)


@app.route('/viewservi')
def viewservi():
    q="SELECT *FROM `service` "
    res=selectall(q)
    print(res)
    return render_template("viewservice.html",val=res)

#view service

@app.route('/viewserv')
def viewserv():
    q="SELECT *FROM `service` "
    res=selectall(q)
    print(res)
    return render_template("view service ori.html",val=res)
#add service
@app.route('/addserv',methods=['post'])
def addserv():
    service_name= request.form['textfield']
    image = request.files['file']
    ii=secure_filename(image.filename)
    image.save(os.path.join('static/services',ii))

    description = request.form['textfield2']
    qry1 = "INSERT INTO `service` VALUES(NULL,%s,%s,%s)"
    val1 = (service_name, ii, description)
    iud(qry1, val1)
    return '''<script>alert("Add successfuly");window.location="viewserv"</script>'''
@app.route('/addservi',methods=['post'])
def addservi():
    return render_template("add service.html")
#delete service
@app.route('/delser')
def delser():
    id = request.args.get('id')

    q = "delete FROM `service` where `s_id`=%s "
    iud(q, id)
    return '''<script>alert("delete successfuly");window.location="viewserv"</script>'''
#submit

@app.route('/subaddservi',methods=['post'])
def subaddservi():

    return '''<script>alert("add successfuly");window.location="viewservi"</script>'''
#make membership


@app.route('/makemembership1')
def makemembership1():
    qry="SELECT * FROM `membership` WHERE`u_id`=%s"
    res=selectone(qry,session['lid'])
    if res is None:
        return render_template("makemembership.html")

    else:
        return '''<script>alert("Already requested");window.location="userhome"</script>'''


@app.route('/makemembership',methods=['post'])
def makemembership():




    qry1 = "INSERT INTO `membership` VALUES(NULL,%s,curdate(),'1000')"
    val1 = (session['lid'])
    iud(qry1, val1)
    return '''<script>alert("Add successfuly");window.location="userhome"</script>'''


# @app.route('/addservi', methods=['post'])


    # return render_template("membershippage.html")

#view member by trainer
@app.route('/viewusertrainer')
def viewusertrainer():
    q="SELECT * FROM `registration`"
    res=selectall(q)
    return render_template("viewusertrainer.html",val=res)


@app.route('/viewmember')
def viewmember():
    id=request.args.get('id')
    qry="SELECT `registration`.*,`membership`.* FROM `registration` JOIN `membership` ON `registration`.`l_id`=`membership`.`u_id` WHERE `registration`.`l_id`=%s"
    res=selectall2(qry,id)
    return render_template("membershippage.html",val=res)

# @app.route('/fee_dtl')
# def fee_dtl():
#     qry="SELECT`registration`.`username`,`payment`.`amount`,`date` FROM`registration` JOIN`payment`ON`registration`.`l_id`=`payment`.`u_id` WHERE`registration`.`l_id`=%s"
#     res=selectall2(qry,session['lid'])
#     return render_template("fee_dtl.html",val=res)
#

#join membership

@app.route('/membership',methods=['post'])
def membership():
        q="INSERT INTO `membership` values(NULL,%s,curdate(),'pending')"
        iud(q,session['lid'])
        return '''<script>alert("join successfuly");window.location="user home"</script>'''

#admin view membership
@app.route('/mum')
def mum():
    q="SELECT `registration`.*,membership.date FROM`registration`  JOIN membership ON `registration`.l_id=`membership`.u_id"
    res=selectall(q)
    return render_template("viewmember.html",val=res)
################################################################################################################################################
# WORKOUT



@app.route('/WORKOUTADD1')
def WORKOUTADD1():
    q="SELECT *FROM `workout_user`"
    res=selectall(q)
    return render_template("WORKOUTVIEW.html",val=res)

@app.route('/WORKOUTADD2',methods=['post'])
def WORKOUTADD2():

    return render_template("WORKOUTADD.html")


@app.route('/WORKOUTADD', methods=['post'])
def WORKOUTADD():
    workout = request.form['textfield']
    tip = request.form['textarea']

    qry1 = "INSERT INTO `workout_user`VALUES(NULL,%s,%s,%s)"
    val1 = (session['lid'],workout,tip)
    iud(qry1, val1)
    return '''<script>alert("added successfuly");window.location="WORKOUTADD1 "</script>'''

#################################EDIT##########################################

@app.route('/EDITWORKOUT')
def EDITWORKOUT():
    id = request.args.get('id')
    session['wrk_id'] = id
    q = "SELECT * FROM `workout_user` WHERE `wrk_id`=%s"
    res = selectone(q, id)
    return render_template("WORKOUTADD1.html", val=res)

@app.route('/EDITWORKOUT1',methods=['post'])
def EDITWORKOUT1():
    workout = request.form['textfield']
    tip = request.form['textarea']
    print(tip)

    qry1 = "update `workout_user` set workout=%s,tip=%s where wrk_id=%s"
    val1 = (workout,tip,session['wrk_id'])
    iud(qry1, val1)
    return '''<script>alert("edit successfuly");window.location="WORKOUTADD1 "</script>'''
#####################DELETE###################

@app.route('/EDITWORKOUT2')
def EDITWORKOUT2():
    id = request.args.get('id')
    q="delete  FROM `workout_user` WHERE `wrk_id`=%s"
    res=iud(q,id)
    return '''<script>alert("delete successfuly");window.location="WORKOUTADD1"</script>'''




@app.route('/VIEWWORKOUTUSER')
def VIEWWORKOUTUSER():
    q="SELECT *FROM `workout_user`"
    res=selectall(q)
    return render_template("WORKOUTVIEWUSER.html",val=res)
#################################################################################################################################################
#EQUIPMENT
@app.route('/EQUIPMENTADD')
def EQUIPMENTADD():
    q="SELECT *FROM `equipments`"
    res=selectall(q)
    return render_template("EQUIPMENTVIEWADMIN.html",val=res)

@app.route('/EQUIPMENTADD1',methods=['post'])
def EQUIPMENTADD1():

    return render_template("EQUIPMENTADD1.html")

@app.route('/EQUIPMENTADD2', methods=['post'])
def EQUIPMENTADD2():
    e_name= request.form['textfield']
    description = request.form['textfield2']
    image = request.files['file']
    n=secure_filename(image.filename)
    image.save(os.path.join('static/equipmemts',n))

    qry1 = "INSERT INTO `equipments`VALUES(NULL,%s,%s,%s)"
    val1 = (e_name,description,n)
    iud(qry1, val1)
    return '''<script>alert("added successfuly");window.location="EQUIPMENTADD "</script>'''





@app.route('/EDITEQUIPMENT')
def EDITEQUIPMENT():
    id = request.args.get('id')
    session['e_id'] = id
    q = "SELECT * FROM `equipments` WHERE `e_id`=%s"
    res = selectone(q, id)
    return render_template("EQUIPMENTADD2.html", val=res)

@app.route('/EDITEQUIPMENT1',methods=['post'])
def EDITEQUIPMENT1():
    try:
        e_name = request.form['textfield']
        description = request.form['textfield2']
        image = request.files['file']
        n = secure_filename(image.filename)
        image.save(os.path.join('static/equipmemts', n))

        qry1 = "update `equipments` set e_name=%s,description=%s,image=%s where e_id=%s"
        val1 = (e_name,description,n,session['e_id'])
        iud(qry1, val1)
        return '''<script>alert("edit successfuly");window.location="EQUIPMENTADD "</script>'''
    except Exception as e:
        e_name = request.form['textfield']
        description = request.form['textfield2']


        qry1 = "update `equipments` set e_name=%s,description=%s where e_id=%s"
        val1 = (e_name, description, session['e_id'])
        iud(qry1, val1)
        return '''<script>alert("edit successfuly");window.location="EQUIPMENTADD "</script>'''



#####DELETE

@app.route('/EDITEQUIPMENT2')
def EDITEQUIPMENT2():
    id = request.args.get('id')
    q="delete  FROM `equipments` WHERE `e_id`=%s"
    res=iud(q,id)
    return '''<script>alert("delete successfuly");window.location="EQUIPMENTADD"</script>'''

######USER VIEW EQUIPMENT


@app.route('/VIEWEQUIPMENTUSER')
def VIEWEQUIPMENTUSER():
    q="SELECT *FROM `equipments`"
    res=selectall(q)
    return render_template("EQUIPMENTVIEWUSER.html",val=res)
####################################################################################################################################
##########################send back
@app.route('/feedbacksend')
def feedbacksend():
    return render_template("SENDFEEDBACK.html")

@app.route('/feed',methods=['post'])
def feed():

        feedback= request.form['textfield']

        qry1 ="INSERT INTO `feedback` VALUES (NULL,%s,%s,curdate())"
        val1 = (session['lid'],feedback)
        iud(qry1, val1)
        return '''<script>alert("send successfuly");window.location="feedbacksend"</script>'''

@app.route('/viewfeedback')
def viewfeedback():
    qry="SELECT * FROM `feedback` INNER JOIN `registration` ON `feedback`.u_id=`registration`.l_id"

    # qry = "SELECT * FROM `feedback`"

    res=selectall(qry)
    return render_template("VIEWFEEDBACK.html",val=res)


#########################################################################################################################################

#package
@app.route('/addpackage1',methods=['post'])
def addpackage1():
    packagename = request.form['textfield']
    Amount = request.form['textfield2']
    description = request.form['textfield3']
    qry1 = "INSERT INTO `package`VALUES(NULL,%s,%s,%s)"
    val1 = (packagename,Amount,description)
    iud(qry1, val1)
    return '''<script>alert("added successfuly");window.location="addpackage "</script>'''


@app.route('/addpackage')
def addpackage():
    q="SELECT *FROM `package`"
    res=selectall(q)
    return render_template("ADD AND MANAGEPACK.html",val=res)

@app.route('/addpackage2',methods=['post'])
def addpackage2():

    return render_template("package.html")

#edit package
@app.route('/editpackage')
def editpackage():
    id = request.args.get('id')
    session['pack_id'] = id
    q = "SELECT * FROM `package` WHERE `pack_id`=%s"
    res = selectone(q, id)
    return render_template("editpackage.html", val=res)

@app.route('/editpackage1',methods=['post'])
def editpackage1():
    packagename = request.form['textfield']
    Amount = request.form['textfield2']
    description = request.form['textfield3']
    qry1 = "update `package` set p_name=%s,price=%s,description=%s where pack_id=%s"
    val1 = (packagename,Amount,description,session['pack_id'])
    iud(qry1, val1)
    return '''<script>alert("edit successfuly");window.location="addpackage "</script>'''


@app.route('/deletepack')
def deletepack():
    id = request.args.get('id')
    q="delete  FROM `package` WHERE `pack_id`=%s"
    res=iud(q,id)
    return '''<script>alert("delete successfuly");window.location="addpackage"</script>'''

@app.route('/addpay8',methods=['post'])
def addpay8():

    Amount = request.form['textfield5']
    qry1 = "INSERT INTO `payment`VALUES(NULL,%s,%s,curdate())"
    val1 = (session['lid'],Amount)
    iud(qry1, val1)
    return






#view package table
@app.route('/viewpack')
def viewpack():
    q="SELECT *FROM `package` "
    res=selectall(q)
    return render_template("makepayment.html",val=res)

@app.route('/makepack')
def makepack():
    id=request.args.get('id')
    session['Pckk_id']=id
    q = "SELECT *FROM `package`  where pack_id=%s"
    res = selectone(q,id)
    session['amount']=res['price']
    print(res,"===========================")
    return render_template("payment.html",val=res)


#payment
@app.route('/makepack1',methods=['post'])
def makepack1():
    qr="SELECT * FROM `payment` WHERE `u_id`=%s "
    res=selectone(qr,session['lid'])
    if res is None:

        return render_template("PAYMENTNEW.html")
    else:
        return '''<script>alert("already added");window.location="viewpack"</script>'''

@app.route('/paymntnew', methods=['post','get'])
def paymntnew():
    return render_template("PAYMENTNEW.html")

@app.route('/paymntnew1', methods=['post','get'])
def paymntnew1():
    scc=request.files['file']
    fname=secure_filename(scc.filename)
    scc.save(os.path.join('static/screenshot',fname))
    qry1 = "insert into payment values(null,%s,%s,%s,curdate(),%s)"
    val1 = (session['lid'], session['Pckk_id'], session['amount'],fname)
    iud(qry1, val1)
    return '''<script>alert("done");window.location="userhome"</script>'''

#view payment details

@app.route('/paystatus')
def paystatus():
     q = "SELECT `payment`.`amount`,`date`,`registration`.`l_id`,username,`package`.`p_name` FROM `payment` JOIN `registration` ON `payment`.u_id=`registration`.`l_id` JOIN `package` ON `payment`.pk_id=`package`.pack_id"
     res = selectall(q)
     print
     return render_template("adminpaymentstatus.html",val=res)


@app.route('/userpaymentstatus')
def userpaymentstatus():
     q = "SELECT `payment`.`amount`,`date`,`registration`.`l_id`,username,`package`.`p_name` FROM `payment` JOIN `registration` ON `payment`.u_id=`registration`.`l_id` JOIN `package` ON `payment`.pk_id=`package`.pack_id WHERE`registration`.`l_id`=%s"

     res = selectall2(q,session['lid'])
     print
     return render_template("userpaymentstatus.html",val=res)




###############################################################################################################
#DIET PLAN DETAILS

@app.route('/adddiet1')
def adddiet1():
    q="SELECT`diet plan`.*,`registration`.username FROM `diet plan` JOIN `registration` ON `diet plan`.u_id=`registration`.l_id"
    res=selectall(q)
    return render_template("add and managemnet diet plan.html",val=res)

@app.route('/adddiet2',methods=['post'])
def adddiet2():
    q="select * from registration"
    res=selectall(q)

    return render_template("DIETPLANADD.html",val=res)


@app.route('/adddiet',methods=['post'])
def adddiet():
    username=request.form['select']
    dietname = request.form['textfield']
    description = request.form['textfield2']
    qry1 = "INSERT INTO `diet plan`VALUES(NULL,%s,%s,%s,%s)"
    val=(dietname,session['lid'],username,description)
    iud(qry1, val)
    return '''<script>alert("added successfuly");window.location="adddiet1 "</script>'''



#view user diet
@app.route('/diet')
def diet():
    q="SELECT`diet plan`.*,`registration`.username FROM `diet plan` JOIN `registration` ON `diet plan`.u_id=`registration`.l_id"
    res=selectall(q)
    return render_template("VIEWDIETPLANUSER.html",val=res)


@app.route('/diet1')
def diet1():
    q="SELECT`diet plan`.*,`registration`.username FROM `diet plan` JOIN `registration` ON `diet plan`.u_id=`registration`.l_id  WHERE  l_id=%s"
    psd=(session['lid'])
    res=selectall2(q,psd)
    return render_template("VIEWDIETPLANUSER1.html",val=res)

############################################################edit diet##################################################################

@app.route('/editdiet1')
def editdiet1():
    id = request.args.get('id')
    session['d_id'] = id
    q = "SELECT * FROM `diet plan` WHERE `d_id`=%s"
    res = selectone(q, id)
    qry="select * from registration"
    res1=selectall(qry)
    return render_template("editdietplan1.html", val=res,val1=res1)


@app.route('/editdiet',methods=['post'])
def editdiet():
    username=request.form['select']
    dietname = request.form['textfield']

    description = request.form['textfield2']
    qry1 = "update `diet plan` set u_id=%s,dietname=%s,description=%s where d_id=%s"
    val1 = (username,dietname,description,session['d_id'])
    iud(qry1, val1)
    return '''<script>alert("edit successfuly");window.location="adddiet1 "</script>'''

############################################################delete diet###################################################################

@app.route('/deletediet')
def deletediet():
    id = request.args.get('id')
    q="delete  FROM `diet plan` WHERE `d_id`=%s"
    iud(q,id)
    return '''<script>alert("delete successfuly");window.location="adddiet1"</script>'''

########################################################################################################################
#registration

@app.route('/registration', methods=['post'])
def registration():

    User = request.form['textfield']
    Place = request.form['textfield2']
    Gender = request.form['radiobutton']
    Email = request.form['textfield3']
    DOB = request.form['textfield5']
    Phoneno = request.form['textfield4']
    height = request.form['textfield8']
    weight = request.form['textfield9']
    u_name = request.form['textfield6']
    password = request.form['textfield7']

    qry = "INSERT INTO `login` VALUES(NULL,%s,%s,'user')"
    val = (u_name, password)
    id = iud(qry, val)
    qry1 = "INSERT INTO registration VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1 = (str(id),User,Place,Gender,DOB,Email,Phoneno, height,weight)

    iud(qry1, val1)

    return '''<script>alert("Registerd successfuly");window.location="/"</script>'''


#PROFILE UPDATION CODING PART
@app.route("/updprof")
def updprof():
    q1 = "SELECT * FROM `registration` WHERE registration.l_id=%s"
    res=selectone(q1,session['lid'])
    return render_template("registra.html",val=res)


@app.route("/updpro",methods=['post','get'])
def updpro():
    User = request.form['textfield']
    Place = request.form['textfield2']
    Gender = request.form['Radio']
    Email = request.form['email']
    DOB = request.form['dob']
    Phoneno = request.form['textfield4']



    qry1 = "UPDATE `registration` SET `username`=%s,`place`=%s,`gender`=%s,`dob`=%s,`email`=%s,`ph_no`=%s  WHERE `l_id`=%s"
    val1 = (User, Place, Gender,DOB, Email,Phoneno,session['lid'])
    iud(qry1, val1)
    return '''<script>alert("profile updated successfuly");window.location="userhome"</script>'''

@app.route("/userhome")
def userhome():
  return render_template("user home.html")

@app.route("/register")
def register():
    return render_template("regindex.html")


app.run(debug=True)
