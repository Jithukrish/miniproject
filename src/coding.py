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
        return '''<script>alert("invalid");window.location="/"</script>'''
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
        return '''<scrpit>alert("invalid");window.location="/"</scrpit>'''

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
        User = request.form['textfield']
        Place = request.form['textfield2']
        Gender = request.form['RadioGroup1']
        Email = request.form['textfield4']
        DOB = request.form['textfield5']
        Phoneno = request.form['textfield3']
        type = request.form['textfield6']
        u_name = request.form['textfield7']
        password = request.form['textfield8']
        qry = "INSERT INTO `login` VALUES(NULL,%s,%s,'trainer')"
        val = (u_name, password)
        id = iud(qry, val)
        qry1 = "INSERT INTO `trainer` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s)"
        val1 = (str(id), User, Place, Gender,Phoneno,Email,DOB,type)
        iud(qry1, val1)
        return '''<script>alert("Registerd successfuly");window.location="viewtrainer"</script>'''
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
    return render_template("admin verify req.html")
@app.route('/assigntrain')
def asstrain():
    return render_template("admin verify req2.html")
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
    q="SELECT * FROM `bodymeasurement`"
    res=selectall(q)
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
    req=request.form['textfield']
    query="INSERT INTO `request` VALUES(NULL,%s,'0',%s,'pending',CURDATE())"
    vall=(str(session['lid']),req)
    iud(query,vall)
    return '''<script>alert("request sended successfully");window.location="/userhome"</script>'''

#check request user

@app.route('/checkreq')
def checreq():

    r="SELECT * FROM  `request` WHERE u_id=%s"
    res=selectall2(r,session['lid'])
    return render_template("admin reqview.html",val=res)
@app.route('/trainerhome')
def trainer():
    return render_template("trainerhome.html")



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
     date = request.form['textfield']
     time = request.form['textfield2']
     qry1 = "INSERT INTO `schedule personal user` VALUES(NULL,%s,%s,%s,%s)"
     val1 = (username,trainer,date, time)
     iud(qry1,val1)
     return '''<script>alert("Add successfuly");window.location="shedule_user_to_tr"</script>'''

#view personal hour
@app.route('/prhourh')
def prhourh():
    q="SELECT*FROM `work_hourper` WHERE `u_id`=%s "
    res=selectall2(q,session['lid'])
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



    amount = request.form['textfield']

    qry1 = "INSERT INTO `membership` VALUES(NULL,%s,curdate(),%s)"
    val1 = (session['lid'],amount)
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
    qry="SELECT`registration`.`username`,`payment`.`amount`,`date` FROM`registration` JOIN`payment`ON`registration`.`l_id`=`payment`.`u_id` WHERE`registration`.`l_id`=%s"
    res=selectall2(qry,id)
    return render_template("membershippage.html",val=res)

@app.route('/fee_dtl')
def fee_dtl():
    qry="SELECT`registration`.`username`,`payment`.`amount`,`date` FROM`registration` JOIN`payment`ON`registration`.`l_id`=`payment`.`u_id` WHERE`registration`.`l_id`=%s"
    res=selectall2(qry,session['lid'])
    return render_template("fee_dtl.html",val=res)


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









#@app.route('/addpay',methods=['post'])
#def addpay():
  #  email = request.form['textfield3']
   # phoneno = request.form['textfield4']
   # Amount = request.form['textfield5']
    #date = request.form['textfield6']




   # qry1 = "INSERT INTO `payment`VALUES(NULL,%s,%s,%s,%s,%s)"
   # val1 = (str(id),User,email,phoneno,Amount,date)
    #iud(qry1, val1)
    #return '''<script>alert("payment successfuly");window.location="adpayment "</script>'''
    #return render_template("payment.html")


#view payment details

#@app.route('/viwpay',methods=['get'])
#def viwpay():
   # q = "SELECT*FROM`payment`"
   # res = selectall(q)
    #return render_template("adpayment.html",val=res)

#scheduling users
#@app.route('/viwpay',methods=['get'])
#def viwpay():


   # q = "SELECT*FROM`payment`"
   # res = selectall(q)
    #return render_template("adpayment.html",val=res)
#view scheduling


#registration

@app.route('/registration', methods=['post'])
def registration():
    # print(request.form)
    # return "OOKK"
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
    Email = request.form['textfield3']
    DOB = request.form['textfield5']
    Phoneno = request.form['textfield4']



    qry1 = "UPDATE `registration` SET `username`=%s,`place`=%s,`gender`=%s,`dob`=%s,`email`=%s,`ph_no`=%s  WHERE `l_id`=%s"
    val1 = (User, Place, Gender,Email, DOB,Phoneno,session['lid'])
    iud(qry1, val1)
    return '''<script>alert("profile updated successfuly");window.location="userhome"</script>'''

@app.route("/userhome")
def userhome():
  return render_template("user home.html")

@app.route("/register")
def register():
    return render_template("regindex.html")


app.run(debug=True)
