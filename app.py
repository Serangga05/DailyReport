from pymongo import MongoClient 
import jwt 
from datetime import datetime, timedelta
import hashlib
from flask import Flask, render_template,jsonify,request,redirect,url_for
from bson import ObjectId
from pymongo import DESCENDING
import math

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME =  os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

app.config['TEMPLATES_AUTO_RELOAD'] = True

TOKEN_KEY = 'mytoken'
SECRET_KEY = 'mykey'

@app.route('/login', methods=['GET'])
def login():
    msg = request.args.get('msg')
    return render_template('login.html', msg=msg)


@app.route("/sign_in", methods=["POST"])
def sign_in():
    username_receive = request.form["username_give"]
    password_receive = request.form["password_give"]
    pw_hash = hashlib.sha256(password_receive.encode("utf-8")).hexdigest()
    result = db.teknisi.find_one(
        {
            "username": username_receive,
            "password": pw_hash,
        }
    )
    if result:
        payload = {
            "id": username_receive,
            "exp": datetime.utcnow() + timedelta(seconds=60 * 60 * 24),
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

        return jsonify(
            {
                "result": "success",
                "token": token,
            }
        )
    else:
        return jsonify(
            {
                "result": "fail",
                "msg": "We could not find a user with that id/password combination",
            }
        )

        

def get_current_page():
    page = request.args.get('page', 1, type=int)
    return page

def get_total_pages(items_per_page, total_data):
    total_pages = math.ceil(total_data / items_per_page)
    return total_pages

@app.route('/', methods=['GET'])
def home():
    token_receive = request.cookies.get(TOKEN_KEY)
    try:
        payload = jwt.decode(
            token_receive, 
            SECRET_KEY, 
            algorithms=["HS256"],
        )
        total_data_cc = db.cc.count_documents({})
        total_data_rtg = db.rtg.count_documents({})
        total_data_ab = db.ab.count_documents({})
        total_data_ht = db.ht.count_documents({})
        

        items_per_page = 3  # Update the number of items per page to 3
        current_page = get_current_page()

        total_pages_cc = get_total_pages(items_per_page, total_data_cc)
        total_pages_rtg = get_total_pages(items_per_page, total_data_rtg)
        total_pages_ab = get_total_pages(items_per_page, total_data_ab)
        total_pages_ht = get_total_pages(items_per_page, total_data_ht)
        

        skip = (current_page - 1) * items_per_page

        cc = get_report_data(db.cc, skip, items_per_page)
        rtg = get_report_data(db.rtg, skip, items_per_page)
        ab = get_report_data(db.ab, skip, items_per_page)
        ht = get_report_data(db.ht, skip, items_per_page)
        

        user_info = db.teknisi.find_one({'username': payload.get('id')})
        return render_template('dashboard.html', user_info=user_info, cc=cc, rtg=rtg, ab=ab, ht=ht,
                               current_page=current_page, 
                               total_pages_cc=total_pages_cc, total_pages_rtg=total_pages_rtg, total_pages_ab=total_pages_ab, total_pages_ht=total_pages_ht)
    
    except jwt.ExpiredSignatureError:
        msg = 'Token Anda sudah kadaluarsa'
        return redirect(url_for('login', msg=msg))
    except jwt.exceptions.DecodeError:
        msg = 'Terjadi masalah saat login'
        return redirect(url_for('login', msg=msg))

def get_report_data(collection, skip, limit):
    return list(collection.find({}).sort('_id', -1).skip(skip).limit(limit))


@app.route('/dailyCC', methods=['GET'])
def dailyCC():
    token_receive = request.cookies.get(TOKEN_KEY)
    try:
        payload = jwt.decode(
            token_receive,
            SECRET_KEY,
            algorithms=['HS256']
        )
        user_info = db.teknisi.find_one({'username': payload.get('id')})
        return render_template('dailyCC.html', user_info=user_info)
    except jwt.ExpiredSignatureError:
        msg = 'Token Anda sudah kadaluarsa'
        return redirect(url_for('home', msg=msg))
    except jwt.exceptions.DecodeError:
        msg = 'Terjadi masalah saat login'
        return redirect(url_for('home', msg=msg))


@app.route("/inputcc", methods=["POST"])
def inputcc():
    unit_receive = request.form.get('unit_give')
    tanggal_receive = request.form.get('tanggal_give')
    
    cc01jam1_receive = request.form.get('cc01jam1_give')
    cc01jam2_receive = request.form.get('cc01jam2_give')
    cc01jam3_receive = request.form.get('cc01jam3_give')
    cc01jam4_receive = request.form.get('cc01jam4_give')
    cc01jam5_receive = request.form.get('cc01jam5_give')
    cc01jam6_receive = request.form.get('cc01jam6_give')
    cc01jam7_receive = request.form.get('cc01jam7_give')
    cc01jam8_receive = request.form.get('cc01jam8_give')
    cc01jam9_receive = request.form.get('cc01jam9_give')
    cc01jam10_receive = request.form.get('cc01jam10_give')
    cc01jam11_receive = request.form.get('cc01jam11_give')
    cc01jam12_receive = request.form.get('cc01jam12_give')
    cc01jam13_receive = request.form.get('cc01jam13_give')
    cc01jam14_receive = request.form.get('cc01jam14_give')
    cc01jam15_receive = request.form.get('cc01jam15_give')
    cc01jam16_receive = request.form.get('cc01jam16_give')
    cc01jam17_receive = request.form.get('cc01jam17_give')
    cc01jam18_receive = request.form.get('cc01jam18_give')
    cc01jam19_receive = request.form.get('cc01jam19_give')
    cc01jam20_receive = request.form.get('cc01jam20_give')
    cc01jam21_receive = request.form.get('cc01jam21_give')
    cc01jam22_receive = request.form.get('cc01jam22_give')
    cc01jam23_receive = request.form.get('cc01jam23_give')
    cc01jam24_receive = request.form.get('cc01jam24_give')

    cc03jam1_receive = request.form.get('cc03jam1_give')
    cc03jam2_receive = request.form.get('cc03jam2_give')
    cc03jam3_receive = request.form.get('cc03jam3_give')
    cc03jam4_receive = request.form.get('cc03jam4_give')
    cc03jam5_receive = request.form.get('cc03jam5_give')
    cc03jam6_receive = request.form.get('cc03jam6_give')
    cc03jam7_receive = request.form.get('cc03jam7_give')
    cc03jam8_receive = request.form.get('cc03jam8_give')
    cc03jam9_receive = request.form.get('cc03jam9_give')
    cc03jam10_receive = request.form.get('cc03jam10_give')
    cc03jam11_receive = request.form.get('cc03jam11_give')
    cc03jam12_receive = request.form.get('cc03jam12_give')
    cc03jam13_receive = request.form.get('cc03jam13_give')
    cc03jam14_receive = request.form.get('cc03jam14_give')
    cc03jam15_receive = request.form.get('cc03jam15_give')
    cc03jam16_receive = request.form.get('cc03jam16_give')
    cc03jam17_receive = request.form.get('cc03jam17_give')
    cc03jam18_receive = request.form.get('cc03jam18_give')
    cc03jam19_receive = request.form.get('cc03jam19_give')
    cc03jam20_receive = request.form.get('cc03jam20_give')
    cc03jam21_receive = request.form.get('cc03jam21_give')
    cc03jam22_receive = request.form.get('cc03jam22_give')
    cc03jam23_receive = request.form.get('cc03jam23_give')
    cc03jam24_receive = request.form.get('cc03jam24_give')
    
    cc04jam1_receive = request.form.get('cc04jam1_give')
    cc04jam2_receive = request.form.get('cc04jam2_give')
    cc04jam3_receive = request.form.get('cc04jam3_give')
    cc04jam4_receive = request.form.get('cc04jam4_give')
    cc04jam5_receive = request.form.get('cc04jam5_give')
    cc04jam6_receive = request.form.get('cc04jam6_give')
    cc04jam7_receive = request.form.get('cc04jam7_give')
    cc04jam8_receive = request.form.get('cc04jam8_give')
    cc04jam9_receive = request.form.get('cc04jam9_give')
    cc04jam10_receive = request.form.get('cc04jam10_give')
    cc04jam11_receive = request.form.get('cc04jam11_give')
    cc04jam12_receive = request.form.get('cc04jam12_give')
    cc04jam13_receive = request.form.get('cc04jam13_give')
    cc04jam14_receive = request.form.get('cc04jam14_give')
    cc04jam15_receive = request.form.get('cc04jam15_give')
    cc04jam16_receive = request.form.get('cc04jam16_give')
    cc04jam17_receive = request.form.get('cc04jam17_give')
    cc04jam18_receive = request.form.get('cc04jam18_give')
    cc04jam19_receive = request.form.get('cc04jam19_give')
    cc04jam20_receive = request.form.get('cc04jam20_give')
    cc04jam21_receive = request.form.get('cc04jam21_give')
    cc04jam22_receive = request.form.get('cc04jam22_give')
    cc04jam23_receive = request.form.get('cc04jam23_give')
    cc04jam24_receive = request.form.get('cc04jam24_give')
    
    cc05jam1_receive = request.form.get('cc05jam1_give')
    cc05jam2_receive = request.form.get('cc05jam2_give')
    cc05jam3_receive = request.form.get('cc05jam3_give')
    cc05jam4_receive = request.form.get('cc05jam4_give')
    cc05jam5_receive = request.form.get('cc05jam5_give')
    cc05jam6_receive = request.form.get('cc05jam6_give')
    cc05jam7_receive = request.form.get('cc05jam7_give')
    cc05jam8_receive = request.form.get('cc05jam8_give')
    cc05jam9_receive = request.form.get('cc05jam9_give')
    cc05jam10_receive = request.form.get('cc05jam10_give')
    cc05jam11_receive = request.form.get('cc05jam11_give')
    cc05jam12_receive = request.form.get('cc05jam12_give')
    cc05jam13_receive = request.form.get('cc05jam13_give')
    cc05jam14_receive = request.form.get('cc05jam14_give')
    cc05jam15_receive = request.form.get('cc05jam15_give')
    cc05jam16_receive = request.form.get('cc05jam16_give')
    cc05jam17_receive = request.form.get('cc05jam17_give')
    cc05jam18_receive = request.form.get('cc05jam18_give')
    cc05jam19_receive = request.form.get('cc05jam19_give')
    cc05jam20_receive = request.form.get('cc05jam20_give')
    cc05jam21_receive = request.form.get('cc05jam21_give')
    cc05jam22_receive = request.form.get('cc05jam22_give')
    cc05jam23_receive = request.form.get('cc05jam23_give')
    cc05jam24_receive = request.form.get('cc05jam24_give')

    cc06jam1_receive = request.form.get('cc06jam1_give')
    cc06jam2_receive = request.form.get('cc06jam2_give')
    cc06jam3_receive = request.form.get('cc06jam3_give')
    cc06jam4_receive = request.form.get('cc06jam4_give')
    cc06jam5_receive = request.form.get('cc06jam5_give')
    cc06jam6_receive = request.form.get('cc06jam6_give')
    cc06jam7_receive = request.form.get('cc06jam7_give')
    cc06jam8_receive = request.form.get('cc06jam8_give')
    cc06jam9_receive = request.form.get('cc06jam9_give')
    cc06jam10_receive = request.form.get('cc06jam10_give')
    cc06jam11_receive = request.form.get('cc06jam11_give')
    cc06jam12_receive = request.form.get('cc06jam12_give')
    cc06jam13_receive = request.form.get('cc06jam13_give')
    cc06jam14_receive = request.form.get('cc06jam14_give')
    cc06jam15_receive = request.form.get('cc06jam15_give')
    cc06jam16_receive = request.form.get('cc06jam16_give')
    cc06jam17_receive = request.form.get('cc06jam17_give')
    cc06jam18_receive = request.form.get('cc06jam18_give')
    cc06jam19_receive = request.form.get('cc06jam19_give')
    cc06jam20_receive = request.form.get('cc06jam20_give')
    cc06jam21_receive = request.form.get('cc06jam21_give')
    cc06jam22_receive = request.form.get('cc06jam22_give')
    cc06jam23_receive = request.form.get('cc06jam23_give')
    cc06jam24_receive = request.form.get('cc06jam24_give')

    breakdown_receive = request.form.get('breakdown_give')
    corrective_receive = request.form.get('corrective_give')
    preventive_receive = request.form.get('preventive_give')
    accident_receive = request.form.get('accident_give')
    remark_receive = request.form.get('remark_give')

    doc = {
        'unit': unit_receive,
        'tanggal': tanggal_receive,

        'cc01jam1': cc01jam1_receive,
        'cc01jam2': cc01jam2_receive,
        'cc01jam3': cc01jam3_receive,
        'cc01jam4': cc01jam4_receive,
        'cc01jam5': cc01jam5_receive,
        'cc01jam6': cc01jam6_receive,
        'cc01jam7': cc01jam7_receive,
        'cc01jam8': cc01jam8_receive,
        'cc01jam9': cc01jam9_receive,
        'cc01jam10': cc01jam10_receive,
        'cc01jam11': cc01jam11_receive,
        'cc01jam12': cc01jam12_receive,
        'cc01jam13': cc01jam13_receive,
        'cc01jam14': cc01jam14_receive,
        'cc01jam15': cc01jam15_receive,
        'cc01jam16': cc01jam16_receive,
        'cc01jam17': cc01jam17_receive,
        'cc01jam18': cc01jam18_receive,
        'cc01jam19': cc01jam19_receive,
        'cc01jam20': cc01jam20_receive,
        'cc01jam21': cc01jam21_receive,
        'cc01jam22': cc01jam22_receive,
        'cc01jam23': cc01jam23_receive,
        'cc01jam24': cc01jam24_receive,
        
        'cc03jam1': cc03jam1_receive,
        'cc03jam2': cc03jam2_receive,
        'cc03jam3': cc03jam3_receive,
        'cc03jam4': cc03jam4_receive,
        'cc03jam5': cc03jam5_receive,
        'cc03jam6': cc03jam6_receive,
        'cc03jam7': cc03jam7_receive,
        'cc03jam8': cc03jam8_receive,
        'cc03jam9': cc03jam9_receive,
        'cc03jam10': cc03jam10_receive,
        'cc03jam11': cc03jam11_receive,
        'cc03jam12': cc03jam12_receive,
        'cc03jam13': cc03jam13_receive,
        'cc03jam14': cc03jam14_receive,
        'cc03jam15': cc03jam15_receive,
        'cc03jam16': cc03jam16_receive,
        'cc03jam17': cc03jam17_receive,
        'cc03jam18': cc03jam18_receive,
        'cc03jam19': cc03jam19_receive,
        'cc03jam20': cc03jam20_receive,
        'cc03jam21': cc03jam21_receive,
        'cc03jam22': cc03jam22_receive,
        'cc03jam23': cc03jam23_receive,
        'cc03jam24': cc03jam24_receive,
        
        'cc04jam1': cc04jam1_receive,
        'cc04jam2': cc04jam2_receive,
        'cc04jam3': cc04jam3_receive,
        'cc04jam4': cc04jam4_receive,
        'cc04jam5': cc04jam5_receive,
        'cc04jam6': cc04jam6_receive,
        'cc04jam7': cc04jam7_receive,
        'cc04jam8': cc04jam8_receive,
        'cc04jam9': cc04jam9_receive,
        'cc04jam10': cc04jam10_receive,
        'cc04jam11': cc04jam11_receive,
        'cc04jam12': cc04jam12_receive,
        'cc04jam13': cc04jam13_receive,
        'cc04jam14': cc04jam14_receive,
        'cc04jam15': cc04jam15_receive,
        'cc04jam16': cc04jam16_receive,
        'cc04jam17': cc04jam17_receive,
        'cc04jam18': cc04jam18_receive,
        'cc04jam19': cc04jam19_receive,
        'cc04jam20': cc04jam20_receive,
        'cc04jam21': cc04jam21_receive,
        'cc04jam22': cc04jam22_receive,
        'cc04jam23': cc04jam23_receive,
        'cc04jam24': cc04jam24_receive,
        
        'cc05jam1': cc05jam1_receive,
        'cc05jam2': cc05jam2_receive,
        'cc05jam3': cc05jam3_receive,
        'cc05jam4': cc05jam4_receive,
        'cc05jam5': cc05jam5_receive,
        'cc05jam6': cc05jam6_receive,
        'cc05jam7': cc05jam7_receive,
        'cc05jam8': cc05jam8_receive,
        'cc05jam9': cc05jam9_receive,
        'cc05jam10': cc05jam10_receive,
        'cc05jam11': cc05jam11_receive,
        'cc05jam12': cc05jam12_receive,
        'cc05jam13': cc05jam13_receive,
        'cc05jam14': cc05jam14_receive,
        'cc05jam15': cc05jam15_receive,
        'cc05jam16': cc05jam16_receive,
        'cc05jam17': cc05jam17_receive,
        'cc05jam18': cc05jam18_receive,
        'cc05jam19': cc05jam19_receive,
        'cc05jam20': cc05jam20_receive,
        'cc05jam21': cc05jam21_receive,
        'cc05jam22': cc05jam22_receive,
        'cc05jam23': cc05jam23_receive,
        'cc05jam24': cc05jam24_receive,
        
        'cc06jam1': cc06jam1_receive,
        'cc06jam2': cc06jam2_receive,
        'cc06jam3': cc06jam3_receive,
        'cc06jam4': cc06jam4_receive,
        'cc06jam5': cc06jam5_receive,
        'cc06jam6': cc06jam6_receive,
        'cc06jam7': cc06jam7_receive,
        'cc06jam8': cc06jam8_receive,
        'cc06jam9': cc06jam9_receive,
        'cc06jam10': cc06jam10_receive,
        'cc06jam11': cc06jam11_receive,
        'cc06jam12': cc06jam12_receive,
        'cc06jam13': cc06jam13_receive,
        'cc06jam14': cc06jam14_receive,
        'cc06jam15': cc06jam15_receive,
        'cc06jam16': cc06jam16_receive,
        'cc06jam17': cc06jam17_receive,
        'cc06jam18': cc06jam18_receive,
        'cc06jam19': cc06jam19_receive,
        'cc06jam20': cc06jam20_receive,
        'cc06jam21': cc06jam21_receive,
        'cc06jam22': cc06jam22_receive,
        'cc06jam23': cc06jam23_receive,
        'cc06jam24': cc06jam24_receive,

        'breakdown': breakdown_receive,
        'corrective': corrective_receive,
        'preventive': preventive_receive,
        'accident': accident_receive,
        'remark': remark_receive,
    }
    db.cc.insert_one(doc)
    return jsonify({'msg': 'Data berhasil disimpan!'})


    
@app.route('/viewCC', methods=['GET'])
def viewCC():
    token_receive = request.cookies.get(TOKEN_KEY)
    try:
        payload = jwt.decode(
            token_receive,
            SECRET_KEY,
            algorithms=['HS256']
        )
        id = request.args.get("id")
        data = db.cc.find_one({"_id": ObjectId(id)})
        data["_id"] = str(data["_id"])
        print(data)
        user_info = db.teknisi.find_one({'username': payload.get('id')})
        return render_template('viewCC.html', user_info=user_info, data=data)
    except jwt.ExpiredSignatureError:
        msg = 'Token Anda sudah kadaluarsa'
        return redirect(url_for('home', msg=msg))
    except jwt.exceptions.DecodeError:
        msg = 'Terjadi masalah saat login'
        return redirect(url_for('home', msg=msg))



    

@app.route('/editCC', methods=['GET', 'POST'])
def editCC():
    if request.method == "GET":
        token_receive = request.cookies.get(TOKEN_KEY)
        try:
            payload = jwt.decode(
                token_receive,
                SECRET_KEY,
                algorithms=['HS256']
            )
            id = request.args.get("id")
            data = db.cc.find_one({"_id": ObjectId(id)})
            data["_id"] = str(data["_id"])
            print(data)
            user_info = db.teknisi.find_one({'username': payload.get('id')})
            return render_template('editCC.html', user_info=user_info, data=data)
        except jwt.ExpiredSignatureError:
            msg = 'Token Anda sudah kadaluarsa'
            return redirect(url_for('home', msg=msg))
        except jwt.exceptions.DecodeError:
            msg = 'Terjadi masalah saat login'
            return redirect(url_for('home', msg=msg))

    elif request.method == "POST":
            id = request.form["id"]
            unit_receive = request.form["unit"]
            tanggal_receive = request.form["tanggal"]
        
            cc01jam1_receive = request.form["cc01jam1"]
            cc01jam2_receive = request.form["cc01jam2"]
            cc01jam3_receive = request.form["cc01jam3"]
            cc01jam4_receive = request.form["cc01jam4"]
            cc01jam5_receive = request.form["cc01jam5"]
            cc01jam6_receive = request.form["cc01jam6"]
            cc01jam7_receive = request.form["cc01jam7"]
            cc01jam8_receive = request.form["cc01jam8"]
            cc01jam9_receive = request.form["cc01jam9"]
            cc01jam10_receive = request.form["cc01jam10"]
            cc01jam11_receive = request.form["cc01jam11"]
            cc01jam12_receive = request.form["cc01jam12"]
            cc01jam13_receive = request.form["cc01jam13"]
            cc01jam14_receive = request.form["cc01jam14"]
            cc01jam15_receive = request.form["cc01jam15"]
            cc01jam16_receive = request.form["cc01jam16"]
            cc01jam17_receive = request.form["cc01jam17"]
            cc01jam18_receive = request.form["cc01jam18"]
            cc01jam19_receive = request.form["cc01jam19"]
            cc01jam20_receive = request.form["cc01jam20"]
            cc01jam21_receive = request.form["cc01jam21"]
            cc01jam22_receive = request.form["cc01jam22"]
            cc01jam23_receive = request.form["cc01jam23"]
            cc01jam24_receive = request.form["cc01jam24"]
            
            cc03jam1_receive = request.form["cc03jam1"]
            cc03jam2_receive = request.form["cc03jam2"]
            cc03jam3_receive = request.form["cc03jam3"]
            cc03jam4_receive = request.form["cc03jam4"]
            cc03jam5_receive = request.form["cc03jam5"]
            cc03jam6_receive = request.form["cc03jam6"]
            cc03jam7_receive = request.form["cc03jam7"]
            cc03jam8_receive = request.form["cc03jam8"]
            cc03jam9_receive = request.form["cc03jam9"]
            cc03jam10_receive = request.form["cc03jam10"]
            cc03jam11_receive = request.form["cc03jam11"]
            cc03jam12_receive = request.form["cc03jam12"]
            cc03jam13_receive = request.form["cc03jam13"]
            cc03jam14_receive = request.form["cc03jam14"]
            cc03jam15_receive = request.form["cc03jam15"]
            cc03jam16_receive = request.form["cc03jam16"]
            cc03jam17_receive = request.form["cc03jam17"]
            cc03jam18_receive = request.form["cc03jam18"]
            cc03jam19_receive = request.form["cc03jam19"]
            cc03jam20_receive = request.form["cc03jam20"]
            cc03jam21_receive = request.form["cc03jam21"]
            cc03jam22_receive = request.form["cc03jam22"]
            cc03jam23_receive = request.form["cc03jam23"]
            cc03jam24_receive = request.form["cc03jam24"]
            
            cc04jam1_receive = request.form["cc04jam1"]
            cc04jam2_receive = request.form["cc04jam2"]
            cc04jam3_receive = request.form["cc04jam3"]
            cc04jam4_receive = request.form["cc04jam4"]
            cc04jam5_receive = request.form["cc04jam5"]
            cc04jam6_receive = request.form["cc04jam6"]
            cc04jam7_receive = request.form["cc04jam7"]
            cc04jam8_receive = request.form["cc04jam8"]
            cc04jam9_receive = request.form["cc04jam9"]
            cc04jam10_receive = request.form["cc04jam10"]
            cc04jam11_receive = request.form["cc04jam11"]
            cc04jam12_receive = request.form["cc04jam12"]
            cc04jam13_receive = request.form["cc04jam13"]
            cc04jam14_receive = request.form["cc04jam14"]
            cc04jam15_receive = request.form["cc04jam15"]
            cc04jam16_receive = request.form["cc04jam16"]
            cc04jam17_receive = request.form["cc04jam17"]
            cc04jam18_receive = request.form["cc04jam18"]
            cc04jam19_receive = request.form["cc04jam19"]
            cc04jam20_receive = request.form["cc04jam20"]
            cc04jam21_receive = request.form["cc04jam21"]
            cc04jam22_receive = request.form["cc04jam22"]
            cc04jam23_receive = request.form["cc04jam23"]
            cc04jam24_receive = request.form["cc04jam24"]
            
            cc05jam1_receive = request.form["cc05jam1"]
            cc05jam2_receive = request.form["cc05jam2"]
            cc05jam3_receive = request.form["cc05jam3"]
            cc05jam4_receive = request.form["cc05jam4"]
            cc05jam5_receive = request.form["cc05jam5"]
            cc05jam6_receive = request.form["cc05jam6"]
            cc05jam7_receive = request.form["cc05jam7"]
            cc05jam8_receive = request.form["cc05jam8"]
            cc05jam9_receive = request.form["cc05jam9"]
            cc05jam10_receive = request.form["cc05jam10"]
            cc05jam11_receive = request.form["cc05jam11"]
            cc05jam12_receive = request.form["cc05jam12"]
            cc05jam13_receive = request.form["cc05jam13"]
            cc05jam14_receive = request.form["cc05jam14"]
            cc05jam15_receive = request.form["cc05jam15"]
            cc05jam16_receive = request.form["cc05jam16"]
            cc05jam17_receive = request.form["cc05jam17"]
            cc05jam18_receive = request.form["cc05jam18"]
            cc05jam19_receive = request.form["cc05jam19"]
            cc05jam20_receive = request.form["cc05jam20"]
            cc05jam21_receive = request.form["cc05jam21"]
            cc05jam22_receive = request.form["cc05jam22"]
            cc05jam23_receive = request.form["cc05jam23"]
            cc05jam24_receive = request.form["cc05jam24"]
            
            cc06jam1_receive = request.form["cc06jam1"]
            cc06jam2_receive = request.form["cc06jam2"]
            cc06jam3_receive = request.form["cc06jam3"]
            cc06jam4_receive = request.form["cc06jam4"]
            cc06jam5_receive = request.form["cc06jam5"]
            cc06jam6_receive = request.form["cc06jam6"]
            cc06jam7_receive = request.form["cc06jam7"]
            cc06jam8_receive = request.form["cc06jam8"]
            cc06jam9_receive = request.form["cc06jam9"]
            cc06jam10_receive = request.form["cc06jam10"]
            cc06jam11_receive = request.form["cc06jam11"]
            cc06jam12_receive = request.form["cc06jam12"]
            cc06jam13_receive = request.form["cc06jam13"]
            cc06jam14_receive = request.form["cc06jam14"]
            cc06jam15_receive = request.form["cc06jam15"]
            cc06jam16_receive = request.form["cc06jam16"]
            cc06jam17_receive = request.form["cc06jam17"]
            cc06jam18_receive = request.form["cc06jam18"]
            cc06jam19_receive = request.form["cc06jam19"]
            cc06jam20_receive = request.form["cc06jam20"]
            cc06jam21_receive = request.form["cc06jam21"]
            cc06jam22_receive = request.form["cc06jam22"]
            cc06jam23_receive = request.form["cc06jam23"]
            cc06jam24_receive = request.form["cc06jam24"]


            breakdown_receive = request.form.get('breakdown')
            corrective_receive = request.form.get('corrective')
            preventive_receive = request.form.get('preventive')
            accident_receive = request.form.get('accident')
            remark_receive = request.form.get('remark')

            doc = {
                'unit': unit_receive,
                'tanggal': tanggal_receive,

                'cc01jam1': cc01jam1_receive,
                'cc01jam2': cc01jam2_receive,
                'cc01jam3': cc01jam3_receive,
                'cc01jam4': cc01jam4_receive,
                'cc01jam5': cc01jam5_receive,
                'cc01jam6': cc01jam6_receive,
                'cc01jam7': cc01jam7_receive,
                'cc01jam8': cc01jam8_receive,
                'cc01jam9': cc01jam9_receive,
                'cc01jam10': cc01jam10_receive,
                'cc01jam11': cc01jam11_receive,
                'cc01jam12': cc01jam12_receive,
                'cc01jam13': cc01jam13_receive,
                'cc01jam14': cc01jam14_receive,
                'cc01jam15': cc01jam15_receive,
                'cc01jam16': cc01jam16_receive,
                'cc01jam17': cc01jam17_receive,
                'cc01jam18': cc01jam18_receive,
                'cc01jam19': cc01jam19_receive,
                'cc01jam20': cc01jam20_receive,
                'cc01jam21': cc01jam21_receive,
                'cc01jam22': cc01jam22_receive,
                'cc01jam23': cc01jam23_receive,
                'cc01jam24': cc01jam24_receive,
                
                'cc03jam1': cc03jam1_receive,
                'cc03jam2': cc03jam2_receive,
                'cc03jam3': cc03jam3_receive,
                'cc03jam4': cc03jam4_receive,
                'cc03jam5': cc03jam5_receive,
                'cc03jam6': cc03jam6_receive,
                'cc03jam7': cc03jam7_receive,
                'cc03jam8': cc03jam8_receive,
                'cc03jam9': cc03jam9_receive,
                'cc03jam10': cc03jam10_receive,
                'cc03jam11': cc03jam11_receive,
                'cc03jam12': cc03jam12_receive,
                'cc03jam13': cc03jam13_receive,
                'cc03jam14': cc03jam14_receive,
                'cc03jam15': cc03jam15_receive,
                'cc03jam16': cc03jam16_receive,
                'cc03jam17': cc03jam17_receive,
                'cc03jam18': cc03jam18_receive,
                'cc03jam19': cc03jam19_receive,
                'cc03jam20': cc03jam20_receive,
                'cc03jam21': cc03jam21_receive,
                'cc03jam22': cc03jam22_receive,
                'cc03jam23': cc03jam23_receive,
                'cc03jam24': cc03jam24_receive,
                
                'cc04jam1': cc04jam1_receive,
                'cc04jam2': cc04jam2_receive,
                'cc04jam3': cc04jam3_receive,
                'cc04jam4': cc04jam4_receive,
                'cc04jam5': cc04jam5_receive,
                'cc04jam6': cc04jam6_receive,
                'cc04jam7': cc04jam7_receive,
                'cc04jam8': cc04jam8_receive,
                'cc04jam9': cc04jam9_receive,
                'cc04jam10': cc04jam10_receive,
                'cc04jam11': cc04jam11_receive,
                'cc04jam12': cc04jam12_receive,
                'cc04jam13': cc04jam13_receive,
                'cc04jam14': cc04jam14_receive,
                'cc04jam15': cc04jam15_receive,
                'cc04jam16': cc04jam16_receive,
                'cc04jam17': cc04jam17_receive,
                'cc04jam18': cc04jam18_receive,
                'cc04jam19': cc04jam19_receive,
                'cc04jam20': cc04jam20_receive,
                'cc04jam21': cc04jam21_receive,
                'cc04jam22': cc04jam22_receive,
                'cc04jam23': cc04jam23_receive,
                'cc04jam24': cc04jam24_receive,
                
                'cc05jam1': cc05jam1_receive,
                'cc05jam2': cc05jam2_receive,
                'cc05jam3': cc05jam3_receive,
                'cc05jam4': cc05jam4_receive,
                'cc05jam5': cc05jam5_receive,
                'cc05jam6': cc05jam6_receive,
                'cc05jam7': cc05jam7_receive,
                'cc05jam8': cc05jam8_receive,
                'cc05jam9': cc05jam9_receive,
                'cc05jam10': cc05jam10_receive,
                'cc05jam11': cc05jam11_receive,
                'cc05jam12': cc05jam12_receive,
                'cc05jam13': cc05jam13_receive,
                'cc05jam14': cc05jam14_receive,
                'cc05jam15': cc05jam15_receive,
                'cc05jam16': cc05jam16_receive,
                'cc05jam17': cc05jam17_receive,
                'cc05jam18': cc05jam18_receive,
                'cc05jam19': cc05jam19_receive,
                'cc05jam20': cc05jam20_receive,
                'cc05jam21': cc05jam21_receive,
                'cc05jam22': cc05jam22_receive,
                'cc05jam23': cc05jam23_receive,
                'cc05jam24': cc05jam24_receive,
                
                'cc06jam1': cc06jam1_receive,
                'cc06jam2': cc06jam2_receive,
                'cc06jam3': cc06jam3_receive,
                'cc06jam4': cc06jam4_receive,
                'cc06jam5': cc06jam5_receive,
                'cc06jam6': cc06jam6_receive,
                'cc06jam7': cc06jam7_receive,
                'cc06jam8': cc06jam8_receive,
                'cc06jam9': cc06jam9_receive,
                'cc06jam10': cc06jam10_receive,
                'cc06jam11': cc06jam11_receive,
                'cc06jam12': cc06jam12_receive,
                'cc06jam13': cc06jam13_receive,
                'cc06jam14': cc06jam14_receive,
                'cc06jam15': cc06jam15_receive,
                'cc06jam16': cc06jam16_receive,
                'cc06jam17': cc06jam17_receive,
                'cc06jam18': cc06jam18_receive,
                'cc06jam19': cc06jam19_receive,
                'cc06jam20': cc06jam20_receive,
                'cc06jam21': cc06jam21_receive,
                'cc06jam22': cc06jam22_receive,
                'cc06jam23': cc06jam23_receive,
                'cc06jam24': cc06jam24_receive,

                'breakdown': breakdown_receive,
                'corrective': corrective_receive,
                'preventive': preventive_receive,
                'accident': accident_receive,
                'remark': remark_receive,
            }
            db.cc.update_one({"_id": ObjectId(id)}, {"$set": doc})
            return redirect('/')

@app.route('/dailyRTG', methods=['GET'])
def dailyRTG():
    token_receive = request.cookies.get(TOKEN_KEY)
    try:
        payload = jwt.decode(
            token_receive,
            SECRET_KEY,
            algorithms=['HS256']
        )
        user_info = db.teknisi.find_one({'username': payload.get('id')})
        return render_template('dailyRTG.html', user_info=user_info)
    except jwt.ExpiredSignatureError:
        msg = 'Token Anda sudah kadaluarsa'
        return redirect(url_for('home', msg=msg))
    except jwt.exceptions.DecodeError:
        msg = 'Terjadi masalah saat login'
        return redirect(url_for('home', msg=msg))


@app.route("/inputrtg", methods=["POST"])
def inputrtg():
    unit_receive = request.form.get('unit_give')
    tanggal_receive = request.form.get('tanggal_give')
    
    rtg01jam1_receive = request.form.get('rtg01jam1_give')
    rtg01jam2_receive = request.form.get('rtg01jam2_give')
    rtg01jam3_receive = request.form.get('rtg01jam3_give')
    rtg01jam4_receive = request.form.get('rtg01jam4_give')
    rtg01jam5_receive = request.form.get('rtg01jam5_give')
    rtg01jam6_receive = request.form.get('rtg01jam6_give')
    rtg01jam7_receive = request.form.get('rtg01jam7_give')
    rtg01jam8_receive = request.form.get('rtg01jam8_give')
    rtg01jam9_receive = request.form.get('rtg01jam9_give')
    rtg01jam10_receive = request.form.get('rtg01jam10_give')
    rtg01jam11_receive = request.form.get('rtg01jam11_give')
    rtg01jam12_receive = request.form.get('rtg01jam12_give')
    rtg01jam13_receive = request.form.get('rtg01jam13_give')
    rtg01jam14_receive = request.form.get('rtg01jam14_give')
    rtg01jam15_receive = request.form.get('rtg01jam15_give')
    rtg01jam16_receive = request.form.get('rtg01jam16_give')
    rtg01jam17_receive = request.form.get('rtg01jam17_give')
    rtg01jam18_receive = request.form.get('rtg01jam18_give')
    rtg01jam19_receive = request.form.get('rtg01jam19_give')
    rtg01jam20_receive = request.form.get('rtg01jam20_give')
    rtg01jam21_receive = request.form.get('rtg01jam21_give')
    rtg01jam22_receive = request.form.get('rtg01jam22_give')
    rtg01jam23_receive = request.form.get('rtg01jam23_give')
    rtg01jam24_receive = request.form.get('rtg01jam24_give')
    
    rtg02jam1_receive = request.form.get('rtg02jam1_give')
    rtg02jam2_receive = request.form.get('rtg02jam2_give')
    rtg02jam3_receive = request.form.get('rtg02jam3_give')
    rtg02jam4_receive = request.form.get('rtg02jam4_give')
    rtg02jam5_receive = request.form.get('rtg02jam5_give')
    rtg02jam6_receive = request.form.get('rtg02jam6_give')
    rtg02jam7_receive = request.form.get('rtg02jam7_give')
    rtg02jam8_receive = request.form.get('rtg02jam8_give')
    rtg02jam9_receive = request.form.get('rtg02jam9_give')
    rtg02jam10_receive = request.form.get('rtg02jam10_give')
    rtg02jam11_receive = request.form.get('rtg02jam11_give')
    rtg02jam12_receive = request.form.get('rtg02jam12_give')
    rtg02jam13_receive = request.form.get('rtg02jam13_give')
    rtg02jam14_receive = request.form.get('rtg02jam14_give')
    rtg02jam15_receive = request.form.get('rtg02jam15_give')
    rtg02jam16_receive = request.form.get('rtg02jam16_give')
    rtg02jam17_receive = request.form.get('rtg02jam17_give')
    rtg02jam18_receive = request.form.get('rtg02jam18_give')
    rtg02jam19_receive = request.form.get('rtg02jam19_give')
    rtg02jam20_receive = request.form.get('rtg02jam20_give')
    rtg02jam21_receive = request.form.get('rtg02jam21_give')
    rtg02jam22_receive = request.form.get('rtg02jam22_give')
    rtg02jam23_receive = request.form.get('rtg02jam23_give')
    rtg02jam24_receive = request.form.get('rtg02jam24_give')
    
    rtg03jam1_receive = request.form.get('rtg03jam1_give')
    rtg03jam2_receive = request.form.get('rtg03jam2_give')
    rtg03jam3_receive = request.form.get('rtg03jam3_give')
    rtg03jam4_receive = request.form.get('rtg03jam4_give')
    rtg03jam5_receive = request.form.get('rtg03jam5_give')
    rtg03jam6_receive = request.form.get('rtg03jam6_give')
    rtg03jam7_receive = request.form.get('rtg03jam7_give')
    rtg03jam8_receive = request.form.get('rtg03jam8_give')
    rtg03jam9_receive = request.form.get('rtg03jam9_give')
    rtg03jam10_receive = request.form.get('rtg03jam10_give')
    rtg03jam11_receive = request.form.get('rtg03jam11_give')
    rtg03jam12_receive = request.form.get('rtg03jam12_give')
    rtg03jam13_receive = request.form.get('rtg03jam13_give')
    rtg03jam14_receive = request.form.get('rtg03jam14_give')
    rtg03jam15_receive = request.form.get('rtg03jam15_give')
    rtg03jam16_receive = request.form.get('rtg03jam16_give')
    rtg03jam17_receive = request.form.get('rtg03jam17_give')
    rtg03jam18_receive = request.form.get('rtg03jam18_give')
    rtg03jam19_receive = request.form.get('rtg03jam19_give')
    rtg03jam20_receive = request.form.get('rtg03jam20_give')
    rtg03jam21_receive = request.form.get('rtg03jam21_give')
    rtg03jam22_receive = request.form.get('rtg03jam22_give')
    rtg03jam23_receive = request.form.get('rtg03jam23_give')
    rtg03jam24_receive = request.form.get('rtg03jam24_give')
    
    rtg04jam1_receive = request.form.get('rtg04jam1_give')
    rtg04jam2_receive = request.form.get('rtg04jam2_give')
    rtg04jam3_receive = request.form.get('rtg04jam3_give')
    rtg04jam4_receive = request.form.get('rtg04jam4_give')
    rtg04jam5_receive = request.form.get('rtg04jam5_give')
    rtg04jam6_receive = request.form.get('rtg04jam6_give')
    rtg04jam7_receive = request.form.get('rtg04jam7_give')
    rtg04jam8_receive = request.form.get('rtg04jam8_give')
    rtg04jam9_receive = request.form.get('rtg04jam9_give')
    rtg04jam10_receive = request.form.get('rtg04jam10_give')
    rtg04jam11_receive = request.form.get('rtg04jam11_give')
    rtg04jam12_receive = request.form.get('rtg04jam12_give')
    rtg04jam13_receive = request.form.get('rtg04jam13_give')
    rtg04jam14_receive = request.form.get('rtg04jam14_give')
    rtg04jam15_receive = request.form.get('rtg04jam15_give')
    rtg04jam16_receive = request.form.get('rtg04jam16_give')
    rtg04jam17_receive = request.form.get('rtg04jam17_give')
    rtg04jam18_receive = request.form.get('rtg04jam18_give')
    rtg04jam19_receive = request.form.get('rtg04jam19_give')
    rtg04jam20_receive = request.form.get('rtg04jam20_give')
    rtg04jam21_receive = request.form.get('rtg04jam21_give')
    rtg04jam22_receive = request.form.get('rtg04jam22_give')
    rtg04jam23_receive = request.form.get('rtg04jam23_give')
    rtg04jam24_receive = request.form.get('rtg04jam24_give')
    
    rtg05jam1_receive = request.form.get('rtg05jam1_give')
    rtg05jam2_receive = request.form.get('rtg05jam2_give')
    rtg05jam3_receive = request.form.get('rtg05jam3_give')
    rtg05jam4_receive = request.form.get('rtg05jam4_give')
    rtg05jam5_receive = request.form.get('rtg05jam5_give')
    rtg05jam6_receive = request.form.get('rtg05jam6_give')
    rtg05jam7_receive = request.form.get('rtg05jam7_give')
    rtg05jam8_receive = request.form.get('rtg05jam8_give')
    rtg05jam9_receive = request.form.get('rtg05jam9_give')
    rtg05jam10_receive = request.form.get('rtg05jam10_give')
    rtg05jam11_receive = request.form.get('rtg05jam11_give')
    rtg05jam12_receive = request.form.get('rtg05jam12_give')
    rtg05jam13_receive = request.form.get('rtg05jam13_give')
    rtg05jam14_receive = request.form.get('rtg05jam14_give')
    rtg05jam15_receive = request.form.get('rtg05jam15_give')
    rtg05jam16_receive = request.form.get('rtg05jam16_give')
    rtg05jam17_receive = request.form.get('rtg05jam17_give')
    rtg05jam18_receive = request.form.get('rtg05jam18_give')
    rtg05jam19_receive = request.form.get('rtg05jam19_give')
    rtg05jam20_receive = request.form.get('rtg05jam20_give')
    rtg05jam21_receive = request.form.get('rtg05jam21_give')
    rtg05jam22_receive = request.form.get('rtg05jam22_give')
    rtg05jam23_receive = request.form.get('rtg05jam23_give')
    rtg05jam24_receive = request.form.get('rtg05jam24_give')
    
    rtg06jam1_receive = request.form.get('rtg06jam1_give')
    rtg06jam2_receive = request.form.get('rtg06jam2_give')
    rtg06jam3_receive = request.form.get('rtg06jam3_give')
    rtg06jam4_receive = request.form.get('rtg06jam4_give')
    rtg06jam5_receive = request.form.get('rtg06jam5_give')
    rtg06jam6_receive = request.form.get('rtg06jam6_give')
    rtg06jam7_receive = request.form.get('rtg06jam7_give')
    rtg06jam8_receive = request.form.get('rtg06jam8_give')
    rtg06jam9_receive = request.form.get('rtg06jam9_give')
    rtg06jam10_receive = request.form.get('rtg06jam10_give')
    rtg06jam11_receive = request.form.get('rtg06jam11_give')
    rtg06jam12_receive = request.form.get('rtg06jam12_give')
    rtg06jam13_receive = request.form.get('rtg06jam13_give')
    rtg06jam14_receive = request.form.get('rtg06jam14_give')
    rtg06jam15_receive = request.form.get('rtg06jam15_give')
    rtg06jam16_receive = request.form.get('rtg06jam16_give')
    rtg06jam17_receive = request.form.get('rtg06jam17_give')
    rtg06jam18_receive = request.form.get('rtg06jam18_give')
    rtg06jam19_receive = request.form.get('rtg06jam19_give')
    rtg06jam20_receive = request.form.get('rtg06jam20_give')
    rtg06jam21_receive = request.form.get('rtg06jam21_give')
    rtg06jam22_receive = request.form.get('rtg06jam22_give')
    rtg06jam23_receive = request.form.get('rtg06jam23_give')
    rtg06jam24_receive = request.form.get('rtg06jam24_give')
    
    rtg08jam1_receive = request.form.get('rtg08jam1_give')
    rtg08jam2_receive = request.form.get('rtg08jam2_give')
    rtg08jam3_receive = request.form.get('rtg08jam3_give')
    rtg08jam4_receive = request.form.get('rtg08jam4_give')
    rtg08jam5_receive = request.form.get('rtg08jam5_give')
    rtg08jam6_receive = request.form.get('rtg08jam6_give')
    rtg08jam7_receive = request.form.get('rtg08jam7_give')
    rtg08jam8_receive = request.form.get('rtg08jam8_give')
    rtg08jam9_receive = request.form.get('rtg08jam9_give')
    rtg08jam10_receive = request.form.get('rtg08jam10_give')
    rtg08jam11_receive = request.form.get('rtg08jam11_give')
    rtg08jam12_receive = request.form.get('rtg08jam12_give')
    rtg08jam13_receive = request.form.get('rtg08jam13_give')
    rtg08jam14_receive = request.form.get('rtg08jam14_give')
    rtg08jam15_receive = request.form.get('rtg08jam15_give')
    rtg08jam16_receive = request.form.get('rtg08jam16_give')
    rtg08jam17_receive = request.form.get('rtg08jam17_give')
    rtg08jam18_receive = request.form.get('rtg08jam18_give')
    rtg08jam19_receive = request.form.get('rtg08jam19_give')
    rtg08jam20_receive = request.form.get('rtg08jam20_give')
    rtg08jam21_receive = request.form.get('rtg08jam21_give')
    rtg08jam22_receive = request.form.get('rtg08jam22_give')
    rtg08jam23_receive = request.form.get('rtg08jam23_give')
    rtg08jam24_receive = request.form.get('rtg08jam24_give')
    
    rtg09jam1_receive = request.form.get('rtg09jam1_give')
    rtg09jam2_receive = request.form.get('rtg09jam2_give')
    rtg09jam3_receive = request.form.get('rtg09jam3_give')
    rtg09jam4_receive = request.form.get('rtg09jam4_give')
    rtg09jam5_receive = request.form.get('rtg09jam5_give')
    rtg09jam6_receive = request.form.get('rtg09jam6_give')
    rtg09jam7_receive = request.form.get('rtg09jam7_give')
    rtg09jam8_receive = request.form.get('rtg09jam8_give')
    rtg09jam9_receive = request.form.get('rtg09jam9_give')
    rtg09jam10_receive = request.form.get('rtg09jam10_give')
    rtg09jam11_receive = request.form.get('rtg09jam11_give')
    rtg09jam12_receive = request.form.get('rtg09jam12_give')
    rtg09jam13_receive = request.form.get('rtg09jam13_give')
    rtg09jam14_receive = request.form.get('rtg09jam14_give')
    rtg09jam15_receive = request.form.get('rtg09jam15_give')
    rtg09jam16_receive = request.form.get('rtg09jam16_give')
    rtg09jam17_receive = request.form.get('rtg09jam17_give')
    rtg09jam18_receive = request.form.get('rtg09jam18_give')
    rtg09jam19_receive = request.form.get('rtg09jam19_give')
    rtg09jam20_receive = request.form.get('rtg09jam20_give')
    rtg09jam21_receive = request.form.get('rtg09jam21_give')
    rtg09jam22_receive = request.form.get('rtg09jam22_give')
    rtg09jam23_receive = request.form.get('rtg09jam23_give')
    rtg09jam24_receive = request.form.get('rtg09jam24_give')
    
    rtg10jam1_receive = request.form.get('rtg10jam1_give')
    rtg10jam2_receive = request.form.get('rtg10jam2_give')
    rtg10jam3_receive = request.form.get('rtg10jam3_give')
    rtg10jam4_receive = request.form.get('rtg10jam4_give')
    rtg10jam5_receive = request.form.get('rtg10jam5_give')
    rtg10jam6_receive = request.form.get('rtg10jam6_give')
    rtg10jam7_receive = request.form.get('rtg10jam7_give')
    rtg10jam8_receive = request.form.get('rtg10jam8_give')
    rtg10jam9_receive = request.form.get('rtg10jam9_give')
    rtg10jam10_receive = request.form.get('rtg10jam10_give')
    rtg10jam11_receive = request.form.get('rtg10jam11_give')
    rtg10jam12_receive = request.form.get('rtg10jam12_give')
    rtg10jam13_receive = request.form.get('rtg10jam13_give')
    rtg10jam14_receive = request.form.get('rtg10jam14_give')
    rtg10jam15_receive = request.form.get('rtg10jam15_give')
    rtg10jam16_receive = request.form.get('rtg10jam16_give')
    rtg10jam17_receive = request.form.get('rtg10jam17_give')
    rtg10jam18_receive = request.form.get('rtg10jam18_give')
    rtg10jam19_receive = request.form.get('rtg10jam19_give')
    rtg10jam20_receive = request.form.get('rtg10jam20_give')
    rtg10jam21_receive = request.form.get('rtg10jam21_give')
    rtg10jam22_receive = request.form.get('rtg10jam22_give')
    rtg10jam23_receive = request.form.get('rtg10jam23_give')
    rtg10jam24_receive = request.form.get('rtg10jam24_give')   
    
    rtg11jam1_receive = request.form.get('rtg11jam1_give')
    rtg11jam2_receive = request.form.get('rtg11jam2_give')
    rtg11jam3_receive = request.form.get('rtg11jam3_give')
    rtg11jam4_receive = request.form.get('rtg11jam4_give')
    rtg11jam5_receive = request.form.get('rtg11jam5_give')
    rtg11jam6_receive = request.form.get('rtg11jam6_give')
    rtg11jam7_receive = request.form.get('rtg11jam7_give')
    rtg11jam8_receive = request.form.get('rtg11jam8_give')
    rtg11jam9_receive = request.form.get('rtg11jam9_give')
    rtg11jam10_receive = request.form.get('rtg11jam10_give')
    rtg11jam11_receive = request.form.get('rtg11jam11_give')
    rtg11jam12_receive = request.form.get('rtg11jam12_give')
    rtg11jam13_receive = request.form.get('rtg11jam13_give')
    rtg11jam14_receive = request.form.get('rtg11jam14_give')
    rtg11jam15_receive = request.form.get('rtg11jam15_give')
    rtg11jam16_receive = request.form.get('rtg11jam16_give')
    rtg11jam17_receive = request.form.get('rtg11jam17_give')
    rtg11jam18_receive = request.form.get('rtg11jam18_give')
    rtg11jam19_receive = request.form.get('rtg11jam19_give')
    rtg11jam20_receive = request.form.get('rtg11jam20_give')
    rtg11jam21_receive = request.form.get('rtg11jam21_give')
    rtg11jam22_receive = request.form.get('rtg11jam22_give')
    rtg11jam23_receive = request.form.get('rtg11jam23_give')
    rtg11jam24_receive = request.form.get('rtg11jam24_give')  
    
    rtg12jam1_receive = request.form.get('rtg12jam1_give')
    rtg12jam2_receive = request.form.get('rtg12jam2_give')
    rtg12jam3_receive = request.form.get('rtg12jam3_give')
    rtg12jam4_receive = request.form.get('rtg12jam4_give')
    rtg12jam5_receive = request.form.get('rtg12jam5_give')
    rtg12jam6_receive = request.form.get('rtg12jam6_give')
    rtg12jam7_receive = request.form.get('rtg12jam7_give')
    rtg12jam8_receive = request.form.get('rtg12jam8_give')
    rtg12jam9_receive = request.form.get('rtg12jam9_give')
    rtg12jam10_receive = request.form.get('rtg12jam10_give')
    rtg12jam11_receive = request.form.get('rtg12jam11_give')
    rtg12jam12_receive = request.form.get('rtg12jam12_give')
    rtg12jam13_receive = request.form.get('rtg12jam13_give')
    rtg12jam14_receive = request.form.get('rtg12jam14_give')
    rtg12jam15_receive = request.form.get('rtg12jam15_give')
    rtg12jam16_receive = request.form.get('rtg12jam16_give')
    rtg12jam17_receive = request.form.get('rtg12jam17_give')
    rtg12jam18_receive = request.form.get('rtg12jam18_give')
    rtg12jam19_receive = request.form.get('rtg12jam19_give')
    rtg12jam20_receive = request.form.get('rtg12jam20_give')
    rtg12jam21_receive = request.form.get('rtg12jam21_give')
    rtg12jam22_receive = request.form.get('rtg12jam22_give')
    rtg12jam23_receive = request.form.get('rtg12jam23_give')
    rtg12jam24_receive = request.form.get('rtg12jam24_give')  
    
    rtg13jam1_receive = request.form.get('rtg13jam1_give')
    rtg13jam2_receive = request.form.get('rtg13jam2_give')
    rtg13jam3_receive = request.form.get('rtg13jam3_give')
    rtg13jam4_receive = request.form.get('rtg13jam4_give')
    rtg13jam5_receive = request.form.get('rtg13jam5_give')
    rtg13jam6_receive = request.form.get('rtg13jam6_give')
    rtg13jam7_receive = request.form.get('rtg13jam7_give')
    rtg13jam8_receive = request.form.get('rtg13jam8_give')
    rtg13jam9_receive = request.form.get('rtg13jam9_give')
    rtg13jam10_receive = request.form.get('rtg13jam10_give')
    rtg13jam11_receive = request.form.get('rtg13jam11_give')
    rtg13jam12_receive = request.form.get('rtg13jam12_give')
    rtg13jam13_receive = request.form.get('rtg13jam13_give')
    rtg13jam14_receive = request.form.get('rtg13jam14_give')
    rtg13jam15_receive = request.form.get('rtg13jam15_give')
    rtg13jam16_receive = request.form.get('rtg13jam16_give')
    rtg13jam17_receive = request.form.get('rtg13jam17_give')
    rtg13jam18_receive = request.form.get('rtg13jam18_give')
    rtg13jam19_receive = request.form.get('rtg13jam19_give')
    rtg13jam20_receive = request.form.get('rtg13jam20_give')
    rtg13jam21_receive = request.form.get('rtg13jam21_give')
    rtg13jam22_receive = request.form.get('rtg13jam22_give')
    rtg13jam23_receive = request.form.get('rtg13jam23_give')
    rtg13jam24_receive = request.form.get('rtg13jam24_give')    

    breakdown_receive = request.form.get('breakdown_give')
    corrective_receive = request.form.get('corrective_give')
    preventive_receive = request.form.get('preventive_give')
    accident_receive = request.form.get('accident_give')
    remark_receive = request.form.get('remark_give')

    doc = {
        'unit': unit_receive,
        'tanggal': tanggal_receive,

        'rtg01jam1': rtg01jam1_receive,
        'rtg01jam2': rtg01jam2_receive,
        'rtg01jam3': rtg01jam3_receive,
        'rtg01jam4': rtg01jam4_receive,
        'rtg01jam5': rtg01jam5_receive,
        'rtg01jam6': rtg01jam6_receive,
        'rtg01jam7': rtg01jam7_receive,
        'rtg01jam8': rtg01jam8_receive,
        'rtg01jam9': rtg01jam9_receive,
        'rtg01jam10': rtg01jam10_receive,
        'rtg01jam11': rtg01jam11_receive,
        'rtg01jam12': rtg01jam12_receive,
        'rtg01jam13': rtg01jam13_receive,
        'rtg01jam14': rtg01jam14_receive,
        'rtg01jam15': rtg01jam15_receive,
        'rtg01jam16': rtg01jam16_receive,
        'rtg01jam17': rtg01jam17_receive,
        'rtg01jam18': rtg01jam18_receive,
        'rtg01jam19': rtg01jam19_receive,
        'rtg01jam20': rtg01jam20_receive,
        'rtg01jam21': rtg01jam21_receive,
        'rtg01jam22': rtg01jam22_receive,
        'rtg01jam23': rtg01jam23_receive,
        'rtg01jam24': rtg01jam24_receive,
        
        'rtg02jam1': rtg02jam1_receive,
        'rtg02jam2': rtg02jam2_receive,
        'rtg02jam3': rtg02jam3_receive,
        'rtg02jam4': rtg02jam4_receive,
        'rtg02jam5': rtg02jam5_receive,
        'rtg02jam6': rtg02jam6_receive,
        'rtg02jam7': rtg02jam7_receive,
        'rtg02jam8': rtg02jam8_receive,
        'rtg02jam9': rtg02jam9_receive,
        'rtg02jam10': rtg02jam10_receive,
        'rtg02jam11': rtg02jam11_receive,
        'rtg02jam12': rtg02jam12_receive,
        'rtg02jam13': rtg02jam13_receive,
        'rtg02jam14': rtg02jam14_receive,
        'rtg02jam15': rtg02jam15_receive,
        'rtg02jam16': rtg02jam16_receive,
        'rtg02jam17': rtg02jam17_receive,
        'rtg02jam18': rtg02jam18_receive,
        'rtg02jam19': rtg02jam19_receive,
        'rtg02jam20': rtg02jam20_receive,
        'rtg02jam21': rtg02jam21_receive,
        'rtg02jam22': rtg02jam22_receive,
        'rtg02jam23': rtg02jam23_receive,
        'rtg02jam24': rtg02jam24_receive,
        
        'rtg03jam1': rtg03jam1_receive,
        'rtg03jam2': rtg03jam2_receive,
        'rtg03jam3': rtg03jam3_receive,
        'rtg03jam4': rtg03jam4_receive,
        'rtg03jam5': rtg03jam5_receive,
        'rtg03jam6': rtg03jam6_receive,
        'rtg03jam7': rtg03jam7_receive,
        'rtg03jam8': rtg03jam8_receive,
        'rtg03jam9': rtg03jam9_receive,
        'rtg03jam10': rtg03jam10_receive,
        'rtg03jam11': rtg03jam11_receive,
        'rtg03jam12': rtg03jam12_receive,
        'rtg03jam13': rtg03jam13_receive,
        'rtg03jam14': rtg03jam14_receive,
        'rtg03jam15': rtg03jam15_receive,
        'rtg03jam16': rtg03jam16_receive,
        'rtg03jam17': rtg03jam17_receive,
        'rtg03jam18': rtg03jam18_receive,
        'rtg03jam19': rtg03jam19_receive,
        'rtg03jam20': rtg03jam20_receive,
        'rtg03jam21': rtg03jam21_receive,
        'rtg03jam22': rtg03jam22_receive,
        'rtg03jam23': rtg03jam23_receive,
        'rtg03jam24': rtg03jam24_receive,
        
        'rtg04jam1': rtg04jam1_receive,
        'rtg04jam2': rtg04jam2_receive,
        'rtg04jam3': rtg04jam3_receive,
        'rtg04jam4': rtg04jam4_receive,
        'rtg04jam5': rtg04jam5_receive,
        'rtg04jam6': rtg04jam6_receive,
        'rtg04jam7': rtg04jam7_receive,
        'rtg04jam8': rtg04jam8_receive,
        'rtg04jam9': rtg04jam9_receive,
        'rtg04jam10': rtg04jam10_receive,
        'rtg04jam11': rtg04jam11_receive,
        'rtg04jam12': rtg04jam12_receive,
        'rtg04jam13': rtg04jam13_receive,
        'rtg04jam14': rtg04jam14_receive,
        'rtg04jam15': rtg04jam15_receive,
        'rtg04jam16': rtg04jam16_receive,
        'rtg04jam17': rtg04jam17_receive,
        'rtg04jam18': rtg04jam18_receive,
        'rtg04jam19': rtg04jam19_receive,
        'rtg04jam20': rtg04jam20_receive,
        'rtg04jam21': rtg04jam21_receive,
        'rtg04jam22': rtg04jam22_receive,
        'rtg04jam23': rtg04jam23_receive,
        'rtg04jam24': rtg04jam24_receive,
        
        'rtg05jam1': rtg05jam1_receive,
        'rtg05jam2': rtg05jam2_receive,
        'rtg05jam3': rtg05jam3_receive,
        'rtg05jam4': rtg05jam4_receive,
        'rtg05jam5': rtg05jam5_receive,
        'rtg05jam6': rtg05jam6_receive,
        'rtg05jam7': rtg05jam7_receive,
        'rtg05jam8': rtg05jam8_receive,
        'rtg05jam9': rtg05jam9_receive,
        'rtg05jam10': rtg05jam10_receive,
        'rtg05jam11': rtg05jam11_receive,
        'rtg05jam12': rtg05jam12_receive,
        'rtg05jam13': rtg05jam13_receive,
        'rtg05jam14': rtg05jam14_receive,
        'rtg05jam15': rtg05jam15_receive,
        'rtg05jam16': rtg05jam16_receive,
        'rtg05jam17': rtg05jam17_receive,
        'rtg05jam18': rtg05jam18_receive,
        'rtg05jam19': rtg05jam19_receive,
        'rtg05jam20': rtg05jam20_receive,
        'rtg05jam21': rtg05jam21_receive,
        'rtg05jam22': rtg05jam22_receive,
        'rtg05jam23': rtg05jam23_receive,
        'rtg05jam24': rtg05jam24_receive,
        
        'rtg06jam1': rtg06jam1_receive,
        'rtg06jam2': rtg06jam2_receive,
        'rtg06jam3': rtg06jam3_receive,
        'rtg06jam4': rtg06jam4_receive,
        'rtg06jam5': rtg06jam5_receive,
        'rtg06jam6': rtg06jam6_receive,
        'rtg06jam7': rtg06jam7_receive,
        'rtg06jam8': rtg06jam8_receive,
        'rtg06jam9': rtg06jam9_receive,
        'rtg06jam10': rtg06jam10_receive,
        'rtg06jam11': rtg06jam11_receive,
        'rtg06jam12': rtg06jam12_receive,
        'rtg06jam13': rtg06jam13_receive,
        'rtg06jam14': rtg06jam14_receive,
        'rtg06jam15': rtg06jam15_receive,
        'rtg06jam16': rtg06jam16_receive,
        'rtg06jam17': rtg06jam17_receive,
        'rtg06jam18': rtg06jam18_receive,
        'rtg06jam19': rtg06jam19_receive,
        'rtg06jam20': rtg06jam20_receive,
        'rtg06jam21': rtg06jam21_receive,
        'rtg06jam22': rtg06jam22_receive,
        'rtg06jam23': rtg06jam23_receive,
        'rtg06jam24': rtg06jam24_receive,
        
        'rtg08jam1': rtg08jam1_receive,
        'rtg08jam2': rtg08jam2_receive,
        'rtg08jam3': rtg08jam3_receive,
        'rtg08jam4': rtg08jam4_receive,
        'rtg08jam5': rtg08jam5_receive,
        'rtg08jam6': rtg08jam6_receive,
        'rtg08jam7': rtg08jam7_receive,
        'rtg08jam8': rtg08jam8_receive,
        'rtg08jam9': rtg08jam9_receive,
        'rtg08jam10': rtg08jam10_receive,
        'rtg08jam11': rtg08jam11_receive,
        'rtg08jam12': rtg08jam12_receive,
        'rtg08jam13': rtg08jam13_receive,
        'rtg08jam14': rtg08jam14_receive,
        'rtg08jam15': rtg08jam15_receive,
        'rtg08jam16': rtg08jam16_receive,
        'rtg08jam17': rtg08jam17_receive,
        'rtg08jam18': rtg08jam18_receive,
        'rtg08jam19': rtg08jam19_receive,
        'rtg08jam20': rtg08jam20_receive,
        'rtg08jam21': rtg08jam21_receive,
        'rtg08jam22': rtg08jam22_receive,
        'rtg08jam23': rtg08jam23_receive,
        'rtg08jam24': rtg08jam24_receive,
        
        'rtg09jam1': rtg09jam1_receive,
        'rtg09jam2': rtg09jam2_receive,
        'rtg09jam3': rtg09jam3_receive,
        'rtg09jam4': rtg09jam4_receive,
        'rtg09jam5': rtg09jam5_receive,
        'rtg09jam6': rtg09jam6_receive,
        'rtg09jam7': rtg09jam7_receive,
        'rtg09jam8': rtg09jam8_receive,
        'rtg09jam9': rtg09jam9_receive,
        'rtg09jam10': rtg09jam10_receive,
        'rtg09jam11': rtg09jam11_receive,
        'rtg09jam12': rtg09jam12_receive,
        'rtg09jam13': rtg09jam13_receive,
        'rtg09jam14': rtg09jam14_receive,
        'rtg09jam15': rtg09jam15_receive,
        'rtg09jam16': rtg09jam16_receive,
        'rtg09jam17': rtg09jam17_receive,
        'rtg09jam18': rtg09jam18_receive,
        'rtg09jam19': rtg09jam19_receive,
        'rtg09jam20': rtg09jam20_receive,
        'rtg09jam21': rtg09jam21_receive,
        'rtg09jam22': rtg09jam22_receive,
        'rtg09jam23': rtg09jam23_receive,
        'rtg09jam24': rtg09jam24_receive,
        
        'rtg10jam1': rtg10jam1_receive,
        'rtg10jam2': rtg10jam2_receive,
        'rtg10jam3': rtg10jam3_receive,
        'rtg10jam4': rtg10jam4_receive,
        'rtg10jam5': rtg10jam5_receive,
        'rtg10jam6': rtg10jam6_receive,
        'rtg10jam7': rtg10jam7_receive,
        'rtg10jam8': rtg10jam8_receive,
        'rtg10jam9': rtg10jam9_receive,
        'rtg10jam10': rtg10jam10_receive,
        'rtg10jam11': rtg10jam11_receive,
        'rtg10jam12': rtg10jam12_receive,
        'rtg10jam13': rtg10jam13_receive,
        'rtg10jam14': rtg10jam14_receive,
        'rtg10jam15': rtg10jam15_receive,
        'rtg10jam16': rtg10jam16_receive,
        'rtg10jam17': rtg10jam17_receive,
        'rtg10jam18': rtg10jam18_receive,
        'rtg10jam19': rtg10jam19_receive,
        'rtg10jam20': rtg10jam20_receive,
        'rtg10jam21': rtg10jam21_receive,
        'rtg10jam22': rtg10jam22_receive,
        'rtg10jam23': rtg10jam23_receive,
        'rtg10jam24': rtg10jam24_receive,
        
        'rtg11jam1': rtg11jam1_receive,
        'rtg11jam2': rtg11jam2_receive,
        'rtg11jam3': rtg11jam3_receive,
        'rtg11jam4': rtg11jam4_receive,
        'rtg11jam5': rtg11jam5_receive,
        'rtg11jam6': rtg11jam6_receive,
        'rtg11jam7': rtg11jam7_receive,
        'rtg11jam8': rtg11jam8_receive,
        'rtg11jam9': rtg11jam9_receive,
        'rtg11jam10': rtg11jam10_receive,
        'rtg11jam11': rtg11jam11_receive,
        'rtg11jam12': rtg11jam12_receive,
        'rtg11jam13': rtg11jam13_receive,
        'rtg11jam14': rtg11jam14_receive,
        'rtg11jam15': rtg11jam15_receive,
        'rtg11jam16': rtg11jam16_receive,
        'rtg11jam17': rtg11jam17_receive,
        'rtg11jam18': rtg11jam18_receive,
        'rtg11jam19': rtg11jam19_receive,
        'rtg11jam20': rtg11jam20_receive,
        'rtg11jam21': rtg11jam21_receive,
        'rtg11jam22': rtg11jam22_receive,
        'rtg11jam23': rtg11jam23_receive,
        'rtg11jam24': rtg11jam24_receive,
        
        'rtg12jam1': rtg12jam1_receive,
        'rtg12jam2': rtg12jam2_receive,
        'rtg12jam3': rtg12jam3_receive,
        'rtg12jam4': rtg12jam4_receive,
        'rtg12jam5': rtg12jam5_receive,
        'rtg12jam6': rtg12jam6_receive,
        'rtg12jam7': rtg12jam7_receive,
        'rtg12jam8': rtg12jam8_receive,
        'rtg12jam9': rtg12jam9_receive,
        'rtg12jam10': rtg12jam10_receive,
        'rtg12jam11': rtg12jam11_receive,
        'rtg12jam12': rtg12jam12_receive,
        'rtg12jam13': rtg12jam13_receive,
        'rtg12jam14': rtg12jam14_receive,
        'rtg12jam15': rtg12jam15_receive,
        'rtg12jam16': rtg12jam16_receive,
        'rtg12jam17': rtg12jam17_receive,
        'rtg12jam18': rtg12jam18_receive,
        'rtg12jam19': rtg12jam19_receive,
        'rtg12jam20': rtg12jam20_receive,
        'rtg12jam21': rtg12jam21_receive,
        'rtg12jam22': rtg12jam22_receive,
        'rtg12jam23': rtg12jam23_receive,
        'rtg12jam24': rtg12jam24_receive,
        
        'rtg13jam1': rtg13jam1_receive,
        'rtg13jam2': rtg13jam2_receive,
        'rtg13jam3': rtg13jam3_receive,
        'rtg13jam4': rtg13jam4_receive,
        'rtg13jam5': rtg13jam5_receive,
        'rtg13jam6': rtg13jam6_receive,
        'rtg13jam7': rtg13jam7_receive,
        'rtg13jam8': rtg13jam8_receive,
        'rtg13jam9': rtg13jam9_receive,
        'rtg13jam10': rtg13jam10_receive,
        'rtg13jam11': rtg13jam11_receive,
        'rtg13jam12': rtg13jam12_receive,
        'rtg13jam13': rtg13jam13_receive,
        'rtg13jam14': rtg13jam14_receive,
        'rtg13jam15': rtg13jam15_receive,
        'rtg13jam16': rtg13jam16_receive,
        'rtg13jam17': rtg13jam17_receive,
        'rtg13jam18': rtg13jam18_receive,
        'rtg13jam19': rtg13jam19_receive,
        'rtg13jam20': rtg13jam20_receive,
        'rtg13jam21': rtg13jam21_receive,
        'rtg13jam22': rtg13jam22_receive,
        'rtg13jam23': rtg13jam23_receive,
        'rtg13jam24': rtg13jam24_receive,

        'breakdown': breakdown_receive,
        'corrective': corrective_receive,
        'preventive': preventive_receive,
        'accident': accident_receive,
        'remark': remark_receive,
    }
    db.rtg.insert_one(doc)
    return jsonify({'msg': 'Data berhasil disimpan!'})


    
@app.route('/viewRTG', methods=['GET'])
def viewRTG():
    token_receive = request.cookies.get(TOKEN_KEY)
    try:
        payload = jwt.decode(
            token_receive,
            SECRET_KEY,
            algorithms=['HS256']
        )
        id = request.args.get("id")
        data = db.rtg.find_one({"_id": ObjectId(id)})
        data["_id"] = str(data["_id"])
        print(data)
        user_info = db.teknisi.find_one({'username': payload.get('id')})
        return render_template('viewRTG.html', user_info=user_info, data=data)
    except jwt.ExpiredSignatureError:
        msg = 'Token Anda sudah kadaluarsa'
        return redirect(url_for('home', msg=msg))
    except jwt.exceptions.DecodeError:
        msg = 'Terjadi masalah saat login'
        return redirect(url_for('home', msg=msg))


@app.route('/editRTG', methods=['GET', 'POST'])
def editRTG():
    if request.method == "GET":
        token_receive = request.cookies.get(TOKEN_KEY)
        try:
            payload = jwt.decode(
                token_receive,
                SECRET_KEY,
                algorithms=['HS256']
            )
            id = request.args.get("id")
            data = db.rtg.find_one({"_id": ObjectId(id)})
            data["_id"] = str(data["_id"])
            print(data)
            user_info = db.teknisi.find_one({'username': payload.get('id')})
            return render_template('editRTG.html', user_info=user_info, data=data)
        except jwt.ExpiredSignatureError:
            msg = 'Token Anda sudah kadaluarsa'
            return redirect(url_for('home', msg=msg))
        except jwt.exceptions.DecodeError:
            msg = 'Terjadi masalah saat login'
            return redirect(url_for('home', msg=msg))

    elif request.method == "POST":
            id = request.form["id"]
            unit_receive = request.form["unit"]
            tanggal_receive = request.form["tanggal"]
        
            rtg01jam1_receive = request.form["rtg01jam1"]
            rtg01jam2_receive = request.form["rtg01jam2"]
            rtg01jam3_receive = request.form["rtg01jam3"]
            rtg01jam4_receive = request.form["rtg01jam4"]
            rtg01jam5_receive = request.form["rtg01jam5"]
            rtg01jam6_receive = request.form["rtg01jam6"]
            rtg01jam7_receive = request.form["rtg01jam7"]
            rtg01jam8_receive = request.form["rtg01jam8"]
            rtg01jam9_receive = request.form["rtg01jam9"]
            rtg01jam10_receive = request.form["rtg01jam10"]
            rtg01jam11_receive = request.form["rtg01jam11"]
            rtg01jam12_receive = request.form["rtg01jam12"]
            rtg01jam13_receive = request.form["rtg01jam13"]
            rtg01jam14_receive = request.form["rtg01jam14"]
            rtg01jam15_receive = request.form["rtg01jam15"]
            rtg01jam16_receive = request.form["rtg01jam16"]
            rtg01jam17_receive = request.form["rtg01jam17"]
            rtg01jam18_receive = request.form["rtg01jam18"]
            rtg01jam19_receive = request.form["rtg01jam19"]
            rtg01jam20_receive = request.form["rtg01jam20"]
            rtg01jam21_receive = request.form["rtg01jam21"]
            rtg01jam22_receive = request.form["rtg01jam22"]
            rtg01jam23_receive = request.form["rtg01jam23"]
            rtg01jam24_receive = request.form["rtg01jam24"]
            
            rtg02jam1_receive = request.form["rtg02jam1"]
            rtg02jam2_receive = request.form["rtg02jam2"]
            rtg02jam3_receive = request.form["rtg02jam3"]
            rtg02jam4_receive = request.form["rtg02jam4"]
            rtg02jam5_receive = request.form["rtg02jam5"]
            rtg02jam6_receive = request.form["rtg02jam6"]
            rtg02jam7_receive = request.form["rtg02jam7"]
            rtg02jam8_receive = request.form["rtg02jam8"]
            rtg02jam9_receive = request.form["rtg02jam9"]
            rtg02jam10_receive = request.form["rtg02jam10"]
            rtg02jam11_receive = request.form["rtg02jam11"]
            rtg02jam12_receive = request.form["rtg02jam12"]
            rtg02jam13_receive = request.form["rtg02jam13"]
            rtg02jam14_receive = request.form["rtg02jam14"]
            rtg02jam15_receive = request.form["rtg02jam15"]
            rtg02jam16_receive = request.form["rtg02jam16"]
            rtg02jam17_receive = request.form["rtg02jam17"]
            rtg02jam18_receive = request.form["rtg02jam18"]
            rtg02jam19_receive = request.form["rtg02jam19"]
            rtg02jam20_receive = request.form["rtg02jam20"]
            rtg02jam21_receive = request.form["rtg02jam21"]
            rtg02jam22_receive = request.form["rtg02jam22"]
            rtg02jam23_receive = request.form["rtg02jam23"]
            rtg02jam24_receive = request.form["rtg02jam24"]
            
            rtg03jam1_receive = request.form["rtg03jam1"]
            rtg03jam2_receive = request.form["rtg03jam2"]
            rtg03jam3_receive = request.form["rtg03jam3"]
            rtg03jam4_receive = request.form["rtg03jam4"]
            rtg03jam5_receive = request.form["rtg03jam5"]
            rtg03jam6_receive = request.form["rtg03jam6"]
            rtg03jam7_receive = request.form["rtg03jam7"]
            rtg03jam8_receive = request.form["rtg03jam8"]
            rtg03jam9_receive = request.form["rtg03jam9"]
            rtg03jam10_receive = request.form["rtg03jam10"]
            rtg03jam11_receive = request.form["rtg03jam11"]
            rtg03jam12_receive = request.form["rtg03jam12"]
            rtg03jam13_receive = request.form["rtg03jam13"]
            rtg03jam14_receive = request.form["rtg03jam14"]
            rtg03jam15_receive = request.form["rtg03jam15"]
            rtg03jam16_receive = request.form["rtg03jam16"]
            rtg03jam17_receive = request.form["rtg03jam17"]
            rtg03jam18_receive = request.form["rtg03jam18"]
            rtg03jam19_receive = request.form["rtg03jam19"]
            rtg03jam20_receive = request.form["rtg03jam20"]
            rtg03jam21_receive = request.form["rtg03jam21"]
            rtg03jam22_receive = request.form["rtg03jam22"]
            rtg03jam23_receive = request.form["rtg03jam23"]
            rtg03jam24_receive = request.form["rtg03jam24"]
            
            rtg04jam1_receive = request.form["rtg04jam1"]
            rtg04jam2_receive = request.form["rtg04jam2"]
            rtg04jam3_receive = request.form["rtg04jam3"]
            rtg04jam4_receive = request.form["rtg04jam4"]
            rtg04jam5_receive = request.form["rtg04jam5"]
            rtg04jam6_receive = request.form["rtg04jam6"]
            rtg04jam7_receive = request.form["rtg04jam7"]
            rtg04jam8_receive = request.form["rtg04jam8"]
            rtg04jam9_receive = request.form["rtg04jam9"]
            rtg04jam10_receive = request.form["rtg04jam10"]
            rtg04jam11_receive = request.form["rtg04jam11"]
            rtg04jam12_receive = request.form["rtg04jam12"]
            rtg04jam13_receive = request.form["rtg04jam13"]
            rtg04jam14_receive = request.form["rtg04jam14"]
            rtg04jam15_receive = request.form["rtg04jam15"]
            rtg04jam16_receive = request.form["rtg04jam16"]
            rtg04jam17_receive = request.form["rtg04jam17"]
            rtg04jam18_receive = request.form["rtg04jam18"]
            rtg04jam19_receive = request.form["rtg04jam19"]
            rtg04jam20_receive = request.form["rtg04jam20"]
            rtg04jam21_receive = request.form["rtg04jam21"]
            rtg04jam22_receive = request.form["rtg04jam22"]
            rtg04jam23_receive = request.form["rtg04jam23"]
            rtg04jam24_receive = request.form["rtg04jam24"]
            
            rtg05jam1_receive = request.form["rtg05jam1"]
            rtg05jam2_receive = request.form["rtg05jam2"]
            rtg05jam3_receive = request.form["rtg05jam3"]
            rtg05jam4_receive = request.form["rtg05jam4"]
            rtg05jam5_receive = request.form["rtg05jam5"]
            rtg05jam6_receive = request.form["rtg05jam6"]
            rtg05jam7_receive = request.form["rtg05jam7"]
            rtg05jam8_receive = request.form["rtg05jam8"]
            rtg05jam9_receive = request.form["rtg05jam9"]
            rtg05jam10_receive = request.form["rtg05jam10"]
            rtg05jam11_receive = request.form["rtg05jam11"]
            rtg05jam12_receive = request.form["rtg05jam12"]
            rtg05jam13_receive = request.form["rtg05jam13"]
            rtg05jam14_receive = request.form["rtg05jam14"]
            rtg05jam15_receive = request.form["rtg05jam15"]
            rtg05jam16_receive = request.form["rtg05jam16"]
            rtg05jam17_receive = request.form["rtg05jam17"]
            rtg05jam18_receive = request.form["rtg05jam18"]
            rtg05jam19_receive = request.form["rtg05jam19"]
            rtg05jam20_receive = request.form["rtg05jam20"]
            rtg05jam21_receive = request.form["rtg05jam21"]
            rtg05jam22_receive = request.form["rtg05jam22"]
            rtg05jam23_receive = request.form["rtg05jam23"]
            rtg05jam24_receive = request.form["rtg05jam24"]
            
            rtg06jam1_receive = request.form["rtg06jam1"]
            rtg06jam2_receive = request.form["rtg06jam2"]
            rtg06jam3_receive = request.form["rtg06jam3"]
            rtg06jam4_receive = request.form["rtg06jam4"]
            rtg06jam5_receive = request.form["rtg06jam5"]
            rtg06jam6_receive = request.form["rtg06jam6"]
            rtg06jam7_receive = request.form["rtg06jam7"]
            rtg06jam8_receive = request.form["rtg06jam8"]
            rtg06jam9_receive = request.form["rtg06jam9"]
            rtg06jam10_receive = request.form["rtg06jam10"]
            rtg06jam11_receive = request.form["rtg06jam11"]
            rtg06jam12_receive = request.form["rtg06jam12"]
            rtg06jam13_receive = request.form["rtg06jam13"]
            rtg06jam14_receive = request.form["rtg06jam14"]
            rtg06jam15_receive = request.form["rtg06jam15"]
            rtg06jam16_receive = request.form["rtg06jam16"]
            rtg06jam17_receive = request.form["rtg06jam17"]
            rtg06jam18_receive = request.form["rtg06jam18"]
            rtg06jam19_receive = request.form["rtg06jam19"]
            rtg06jam20_receive = request.form["rtg06jam20"]
            rtg06jam21_receive = request.form["rtg06jam21"]
            rtg06jam22_receive = request.form["rtg06jam22"]
            rtg06jam23_receive = request.form["rtg06jam23"]
            rtg06jam24_receive = request.form["rtg06jam24"]
            
            rtg08jam1_receive = request.form["rtg08jam1"]
            rtg08jam2_receive = request.form["rtg08jam2"]
            rtg08jam3_receive = request.form["rtg08jam3"]
            rtg08jam4_receive = request.form["rtg08jam4"]
            rtg08jam5_receive = request.form["rtg08jam5"]
            rtg08jam6_receive = request.form["rtg08jam6"]
            rtg08jam7_receive = request.form["rtg08jam7"]
            rtg08jam8_receive = request.form["rtg08jam8"]
            rtg08jam9_receive = request.form["rtg08jam9"]
            rtg08jam10_receive = request.form["rtg08jam10"]
            rtg08jam11_receive = request.form["rtg08jam11"]
            rtg08jam12_receive = request.form["rtg08jam12"]
            rtg08jam13_receive = request.form["rtg08jam13"]
            rtg08jam14_receive = request.form["rtg08jam14"]
            rtg08jam15_receive = request.form["rtg08jam15"]
            rtg08jam16_receive = request.form["rtg08jam16"]
            rtg08jam17_receive = request.form["rtg08jam17"]
            rtg08jam18_receive = request.form["rtg08jam18"]
            rtg08jam19_receive = request.form["rtg08jam19"]
            rtg08jam20_receive = request.form["rtg08jam20"]
            rtg08jam21_receive = request.form["rtg08jam21"]
            rtg08jam22_receive = request.form["rtg08jam22"]
            rtg08jam23_receive = request.form["rtg08jam23"]
            rtg08jam24_receive = request.form["rtg08jam24"]
            
            rtg09jam1_receive = request.form["rtg09jam1"]
            rtg09jam2_receive = request.form["rtg09jam2"]
            rtg09jam3_receive = request.form["rtg09jam3"]
            rtg09jam4_receive = request.form["rtg09jam4"]
            rtg09jam5_receive = request.form["rtg09jam5"]
            rtg09jam6_receive = request.form["rtg09jam6"]
            rtg09jam7_receive = request.form["rtg09jam7"]
            rtg09jam8_receive = request.form["rtg09jam8"]
            rtg09jam9_receive = request.form["rtg09jam9"]
            rtg09jam10_receive = request.form["rtg09jam10"]
            rtg09jam11_receive = request.form["rtg09jam11"]
            rtg09jam12_receive = request.form["rtg09jam12"]
            rtg09jam13_receive = request.form["rtg09jam13"]
            rtg09jam14_receive = request.form["rtg09jam14"]
            rtg09jam15_receive = request.form["rtg09jam15"]
            rtg09jam16_receive = request.form["rtg09jam16"]
            rtg09jam17_receive = request.form["rtg09jam17"]
            rtg09jam18_receive = request.form["rtg09jam18"]
            rtg09jam19_receive = request.form["rtg09jam19"]
            rtg09jam20_receive = request.form["rtg09jam20"]
            rtg09jam21_receive = request.form["rtg09jam21"]
            rtg09jam22_receive = request.form["rtg09jam22"]
            rtg09jam23_receive = request.form["rtg09jam23"]
            rtg09jam24_receive = request.form["rtg09jam24"]
            
            rtg10jam1_receive = request.form["rtg10jam1"]
            rtg10jam2_receive = request.form["rtg10jam2"]
            rtg10jam3_receive = request.form["rtg10jam3"]
            rtg10jam4_receive = request.form["rtg10jam4"]
            rtg10jam5_receive = request.form["rtg10jam5"]
            rtg10jam6_receive = request.form["rtg10jam6"]
            rtg10jam7_receive = request.form["rtg10jam7"]
            rtg10jam8_receive = request.form["rtg10jam8"]
            rtg10jam9_receive = request.form["rtg10jam9"]
            rtg10jam10_receive = request.form["rtg10jam10"]
            rtg10jam11_receive = request.form["rtg10jam11"]
            rtg10jam12_receive = request.form["rtg10jam12"]
            rtg10jam13_receive = request.form["rtg10jam13"]
            rtg10jam14_receive = request.form["rtg10jam14"]
            rtg10jam15_receive = request.form["rtg10jam15"]
            rtg10jam16_receive = request.form["rtg10jam16"]
            rtg10jam17_receive = request.form["rtg10jam17"]
            rtg10jam18_receive = request.form["rtg10jam18"]
            rtg10jam19_receive = request.form["rtg10jam19"]
            rtg10jam20_receive = request.form["rtg10jam20"]
            rtg10jam21_receive = request.form["rtg10jam21"]
            rtg10jam22_receive = request.form["rtg10jam22"]
            rtg10jam23_receive = request.form["rtg10jam23"]
            rtg10jam24_receive = request.form["rtg10jam24"]
            
            rtg11jam1_receive = request.form["rtg11jam1"]
            rtg11jam2_receive = request.form["rtg11jam2"]
            rtg11jam3_receive = request.form["rtg11jam3"]
            rtg11jam4_receive = request.form["rtg11jam4"]
            rtg11jam5_receive = request.form["rtg11jam5"]
            rtg11jam6_receive = request.form["rtg11jam6"]
            rtg11jam7_receive = request.form["rtg11jam7"]
            rtg11jam8_receive = request.form["rtg11jam8"]
            rtg11jam9_receive = request.form["rtg11jam9"]
            rtg11jam10_receive = request.form["rtg11jam10"]
            rtg11jam11_receive = request.form["rtg11jam11"]
            rtg11jam12_receive = request.form["rtg11jam12"]
            rtg11jam13_receive = request.form["rtg11jam13"]
            rtg11jam14_receive = request.form["rtg11jam14"]
            rtg11jam15_receive = request.form["rtg11jam15"]
            rtg11jam16_receive = request.form["rtg11jam16"]
            rtg11jam17_receive = request.form["rtg11jam17"]
            rtg11jam18_receive = request.form["rtg11jam18"]
            rtg11jam19_receive = request.form["rtg11jam19"]
            rtg11jam20_receive = request.form["rtg11jam20"]
            rtg11jam21_receive = request.form["rtg11jam21"]
            rtg11jam22_receive = request.form["rtg11jam22"]
            rtg11jam23_receive = request.form["rtg11jam23"]
            rtg11jam24_receive = request.form["rtg11jam24"]
            
            rtg12jam1_receive = request.form["rtg12jam1"]
            rtg12jam2_receive = request.form["rtg12jam2"]
            rtg12jam3_receive = request.form["rtg12jam3"]
            rtg12jam4_receive = request.form["rtg12jam4"]
            rtg12jam5_receive = request.form["rtg12jam5"]
            rtg12jam6_receive = request.form["rtg12jam6"]
            rtg12jam7_receive = request.form["rtg12jam7"]
            rtg12jam8_receive = request.form["rtg12jam8"]
            rtg12jam9_receive = request.form["rtg12jam9"]
            rtg12jam10_receive = request.form["rtg12jam10"]
            rtg12jam11_receive = request.form["rtg12jam11"]
            rtg12jam12_receive = request.form["rtg12jam12"]
            rtg12jam13_receive = request.form["rtg12jam13"]
            rtg12jam14_receive = request.form["rtg12jam14"]
            rtg12jam15_receive = request.form["rtg12jam15"]
            rtg12jam16_receive = request.form["rtg12jam16"]
            rtg12jam17_receive = request.form["rtg12jam17"]
            rtg12jam18_receive = request.form["rtg12jam18"]
            rtg12jam19_receive = request.form["rtg12jam19"]
            rtg12jam20_receive = request.form["rtg12jam20"]
            rtg12jam21_receive = request.form["rtg12jam21"]
            rtg12jam22_receive = request.form["rtg12jam22"]
            rtg12jam23_receive = request.form["rtg12jam23"]
            rtg12jam24_receive = request.form["rtg12jam24"]

            rtg13jam1_receive = request.form["rtg13jam1"]
            rtg13jam2_receive = request.form["rtg13jam2"]
            rtg13jam3_receive = request.form["rtg13jam3"]
            rtg13jam4_receive = request.form["rtg13jam4"]
            rtg13jam5_receive = request.form["rtg13jam5"]
            rtg13jam6_receive = request.form["rtg13jam6"]
            rtg13jam7_receive = request.form["rtg13jam7"]
            rtg13jam8_receive = request.form["rtg13jam8"]
            rtg13jam9_receive = request.form["rtg13jam9"]
            rtg13jam10_receive = request.form["rtg13jam10"]
            rtg13jam11_receive = request.form["rtg13jam11"]
            rtg13jam12_receive = request.form["rtg13jam12"]
            rtg13jam13_receive = request.form["rtg13jam13"]
            rtg13jam14_receive = request.form["rtg13jam14"]
            rtg13jam15_receive = request.form["rtg13jam15"]
            rtg13jam16_receive = request.form["rtg13jam16"]
            rtg13jam17_receive = request.form["rtg13jam17"]
            rtg13jam18_receive = request.form["rtg13jam18"]
            rtg13jam19_receive = request.form["rtg13jam19"]
            rtg13jam20_receive = request.form["rtg13jam20"]
            rtg13jam21_receive = request.form["rtg13jam21"]
            rtg13jam22_receive = request.form["rtg13jam22"]
            rtg13jam23_receive = request.form["rtg13jam23"]
            rtg13jam24_receive = request.form["rtg13jam24"]

            breakdown_receive = request.form.get('breakdown')
            corrective_receive = request.form.get('corrective')
            preventive_receive = request.form.get('preventive')
            accident_receive = request.form.get('accident')
            remark_receive = request.form.get('remark')

            doc = {
                'unit': unit_receive,
                'tanggal': tanggal_receive,
                
                'rtg01jam1': rtg01jam1_receive,
                'rtg01jam2': rtg01jam2_receive,
                'rtg01jam3': rtg01jam3_receive,
                'rtg01jam4': rtg01jam4_receive,
                'rtg01jam5': rtg01jam5_receive,
                'rtg01jam6': rtg01jam6_receive,
                'rtg01jam7': rtg01jam7_receive,
                'rtg01jam8': rtg01jam8_receive,
                'rtg01jam9': rtg01jam9_receive,
                'rtg01jam10': rtg01jam10_receive,
                'rtg01jam11': rtg01jam11_receive,
                'rtg01jam12': rtg01jam12_receive,
                'rtg01jam13': rtg01jam13_receive,
                'rtg01jam14': rtg01jam14_receive,
                'rtg01jam15': rtg01jam15_receive,
                'rtg01jam16': rtg01jam16_receive,
                'rtg01jam17': rtg01jam17_receive,
                'rtg01jam18': rtg01jam18_receive,
                'rtg01jam19': rtg01jam19_receive,
                'rtg01jam20': rtg01jam20_receive,
                'rtg01jam21': rtg01jam21_receive,
                'rtg01jam22': rtg01jam22_receive,
                'rtg01jam23': rtg01jam23_receive,
                'rtg01jam24': rtg01jam24_receive,
                
                'rtg02jam1': rtg02jam1_receive,
                'rtg02jam2': rtg02jam2_receive,
                'rtg02jam3': rtg02jam3_receive,
                'rtg02jam4': rtg02jam4_receive,
                'rtg02jam5': rtg02jam5_receive,
                'rtg02jam6': rtg02jam6_receive,
                'rtg02jam7': rtg02jam7_receive,
                'rtg02jam8': rtg02jam8_receive,
                'rtg02jam9': rtg02jam9_receive,
                'rtg02jam10': rtg02jam10_receive,
                'rtg02jam11': rtg02jam11_receive,
                'rtg02jam12': rtg02jam12_receive,
                'rtg02jam13': rtg02jam13_receive,
                'rtg02jam14': rtg02jam14_receive,
                'rtg02jam15': rtg02jam15_receive,
                'rtg02jam16': rtg02jam16_receive,
                'rtg02jam17': rtg02jam17_receive,
                'rtg02jam18': rtg02jam18_receive,
                'rtg02jam19': rtg02jam19_receive,
                'rtg02jam20': rtg02jam20_receive,
                'rtg02jam21': rtg02jam21_receive,
                'rtg02jam22': rtg02jam22_receive,
                'rtg02jam23': rtg02jam23_receive,
                'rtg02jam24': rtg02jam24_receive,
                
                'rtg03jam1': rtg03jam1_receive,
                'rtg03jam2': rtg03jam2_receive,
                'rtg03jam3': rtg03jam3_receive,
                'rtg03jam4': rtg03jam4_receive,
                'rtg03jam5': rtg03jam5_receive,
                'rtg03jam6': rtg03jam6_receive,
                'rtg03jam7': rtg03jam7_receive,
                'rtg03jam8': rtg03jam8_receive,
                'rtg03jam9': rtg03jam9_receive,
                'rtg03jam10': rtg03jam10_receive,
                'rtg03jam11': rtg03jam11_receive,
                'rtg03jam12': rtg03jam12_receive,
                'rtg03jam13': rtg03jam13_receive,
                'rtg03jam14': rtg03jam14_receive,
                'rtg03jam15': rtg03jam15_receive,
                'rtg03jam16': rtg03jam16_receive,
                'rtg03jam17': rtg03jam17_receive,
                'rtg03jam18': rtg03jam18_receive,
                'rtg03jam19': rtg03jam19_receive,
                'rtg03jam20': rtg03jam20_receive,
                'rtg03jam21': rtg03jam21_receive,
                'rtg03jam22': rtg03jam22_receive,
                'rtg03jam23': rtg03jam23_receive,
                'rtg03jam24': rtg03jam24_receive,
                
                'rtg04jam1': rtg04jam1_receive,
                'rtg04jam2': rtg04jam2_receive,
                'rtg04jam3': rtg04jam3_receive,
                'rtg04jam4': rtg04jam4_receive,
                'rtg04jam5': rtg04jam5_receive,
                'rtg04jam6': rtg04jam6_receive,
                'rtg04jam7': rtg04jam7_receive,
                'rtg04jam8': rtg04jam8_receive,
                'rtg04jam9': rtg04jam9_receive,
                'rtg04jam10': rtg04jam10_receive,
                'rtg04jam11': rtg04jam11_receive,
                'rtg04jam12': rtg04jam12_receive,
                'rtg04jam13': rtg04jam13_receive,
                'rtg04jam14': rtg04jam14_receive,
                'rtg04jam15': rtg04jam15_receive,
                'rtg04jam16': rtg04jam16_receive,
                'rtg04jam17': rtg04jam17_receive,
                'rtg04jam18': rtg04jam18_receive,
                'rtg04jam19': rtg04jam19_receive,
                'rtg04jam20': rtg04jam20_receive,
                'rtg04jam21': rtg04jam21_receive,
                'rtg04jam22': rtg04jam22_receive,
                'rtg04jam23': rtg04jam23_receive,
                'rtg04jam24': rtg04jam24_receive,
                
                'rtg05jam1': rtg05jam1_receive,
                'rtg05jam2': rtg05jam2_receive,
                'rtg05jam3': rtg05jam3_receive,
                'rtg05jam4': rtg05jam4_receive,
                'rtg05jam5': rtg05jam5_receive,
                'rtg05jam6': rtg05jam6_receive,
                'rtg05jam7': rtg05jam7_receive,
                'rtg05jam8': rtg05jam8_receive,
                'rtg05jam9': rtg05jam9_receive,
                'rtg05jam10': rtg05jam10_receive,
                'rtg05jam11': rtg05jam11_receive,
                'rtg05jam12': rtg05jam12_receive,
                'rtg05jam13': rtg05jam13_receive,
                'rtg05jam14': rtg05jam14_receive,
                'rtg05jam15': rtg05jam15_receive,
                'rtg05jam16': rtg05jam16_receive,
                'rtg05jam17': rtg05jam17_receive,
                'rtg05jam18': rtg05jam18_receive,
                'rtg05jam19': rtg05jam19_receive,
                'rtg05jam20': rtg05jam20_receive,
                'rtg05jam21': rtg05jam21_receive,
                'rtg05jam22': rtg05jam22_receive,
                'rtg05jam23': rtg05jam23_receive,
                'rtg05jam24': rtg05jam24_receive,
                
                'rtg06jam1': rtg06jam1_receive,
                'rtg06jam2': rtg06jam2_receive,
                'rtg06jam3': rtg06jam3_receive,
                'rtg06jam4': rtg06jam4_receive,
                'rtg06jam5': rtg06jam5_receive,
                'rtg06jam6': rtg06jam6_receive,
                'rtg06jam7': rtg06jam7_receive,
                'rtg06jam8': rtg06jam8_receive,
                'rtg06jam9': rtg06jam9_receive,
                'rtg06jam10': rtg06jam10_receive,
                'rtg06jam11': rtg06jam11_receive,
                'rtg06jam12': rtg06jam12_receive,
                'rtg06jam13': rtg06jam13_receive,
                'rtg06jam14': rtg06jam14_receive,
                'rtg06jam15': rtg06jam15_receive,
                'rtg06jam16': rtg06jam16_receive,
                'rtg06jam17': rtg06jam17_receive,
                'rtg06jam18': rtg06jam18_receive,
                'rtg06jam19': rtg06jam19_receive,
                'rtg06jam20': rtg06jam20_receive,
                'rtg06jam21': rtg06jam21_receive,
                'rtg06jam22': rtg06jam22_receive,
                'rtg06jam23': rtg06jam23_receive,
                'rtg06jam24': rtg06jam24_receive,
                
                'rtg08jam1': rtg08jam1_receive,
                'rtg08jam2': rtg08jam2_receive,
                'rtg08jam3': rtg08jam3_receive,
                'rtg08jam4': rtg08jam4_receive,
                'rtg08jam5': rtg08jam5_receive,
                'rtg08jam6': rtg08jam6_receive,
                'rtg08jam7': rtg08jam7_receive,
                'rtg08jam8': rtg08jam8_receive,
                'rtg08jam9': rtg08jam9_receive,
                'rtg08jam10': rtg08jam10_receive,
                'rtg08jam11': rtg08jam11_receive,
                'rtg08jam12': rtg08jam12_receive,
                'rtg08jam13': rtg08jam13_receive,
                'rtg08jam14': rtg08jam14_receive,
                'rtg08jam15': rtg08jam15_receive,
                'rtg08jam16': rtg08jam16_receive,
                'rtg08jam17': rtg08jam17_receive,
                'rtg08jam18': rtg08jam18_receive,
                'rtg08jam19': rtg08jam19_receive,
                'rtg08jam20': rtg08jam20_receive,
                'rtg08jam21': rtg08jam21_receive,
                'rtg08jam22': rtg08jam22_receive,
                'rtg08jam23': rtg08jam23_receive,
                'rtg08jam24': rtg08jam24_receive,
                
                'rtg09jam1': rtg09jam1_receive,
                'rtg09jam2': rtg09jam2_receive,
                'rtg09jam3': rtg09jam3_receive,
                'rtg09jam4': rtg09jam4_receive,
                'rtg09jam5': rtg09jam5_receive,
                'rtg09jam6': rtg09jam6_receive,
                'rtg09jam7': rtg09jam7_receive,
                'rtg09jam8': rtg09jam8_receive,
                'rtg09jam9': rtg09jam9_receive,
                'rtg09jam10': rtg09jam10_receive,
                'rtg09jam11': rtg09jam11_receive,
                'rtg09jam12': rtg09jam12_receive,
                'rtg09jam13': rtg09jam13_receive,
                'rtg09jam14': rtg09jam14_receive,
                'rtg09jam15': rtg09jam15_receive,
                'rtg09jam16': rtg09jam16_receive,
                'rtg09jam17': rtg09jam17_receive,
                'rtg09jam18': rtg09jam18_receive,
                'rtg09jam19': rtg09jam19_receive,
                'rtg09jam20': rtg09jam20_receive,
                'rtg09jam21': rtg09jam21_receive,
                'rtg09jam22': rtg09jam22_receive,
                'rtg09jam23': rtg09jam23_receive,
                'rtg09jam24': rtg09jam24_receive,
                
                'rtg10jam1': rtg10jam1_receive,
                'rtg10jam2': rtg10jam2_receive,
                'rtg10jam3': rtg10jam3_receive,
                'rtg10jam4': rtg10jam4_receive,
                'rtg10jam5': rtg10jam5_receive,
                'rtg10jam6': rtg10jam6_receive,
                'rtg10jam7': rtg10jam7_receive,
                'rtg10jam8': rtg10jam8_receive,
                'rtg10jam9': rtg10jam9_receive,
                'rtg10jam10': rtg10jam10_receive,
                'rtg10jam11': rtg10jam11_receive,
                'rtg10jam12': rtg10jam12_receive,
                'rtg10jam13': rtg10jam13_receive,
                'rtg10jam14': rtg10jam14_receive,
                'rtg10jam15': rtg10jam15_receive,
                'rtg10jam16': rtg10jam16_receive,
                'rtg10jam17': rtg10jam17_receive,
                'rtg10jam18': rtg10jam18_receive,
                'rtg10jam19': rtg10jam19_receive,
                'rtg10jam20': rtg10jam20_receive,
                'rtg10jam21': rtg10jam21_receive,
                'rtg10jam22': rtg10jam22_receive,
                'rtg10jam23': rtg10jam23_receive,
                'rtg10jam24': rtg10jam24_receive,
                
                'rtg11jam1': rtg11jam1_receive,
                'rtg11jam2': rtg11jam2_receive,
                'rtg11jam3': rtg11jam3_receive,
                'rtg11jam4': rtg11jam4_receive,
                'rtg11jam5': rtg11jam5_receive,
                'rtg11jam6': rtg11jam6_receive,
                'rtg11jam7': rtg11jam7_receive,
                'rtg11jam8': rtg11jam8_receive,
                'rtg11jam9': rtg11jam9_receive,
                'rtg11jam10': rtg11jam10_receive,
                'rtg11jam11': rtg11jam11_receive,
                'rtg11jam12': rtg11jam12_receive,
                'rtg11jam13': rtg11jam13_receive,
                'rtg11jam14': rtg11jam14_receive,
                'rtg11jam15': rtg11jam15_receive,
                'rtg11jam16': rtg11jam16_receive,
                'rtg11jam17': rtg11jam17_receive,
                'rtg11jam18': rtg11jam18_receive,
                'rtg11jam19': rtg11jam19_receive,
                'rtg11jam20': rtg11jam20_receive,
                'rtg11jam21': rtg11jam21_receive,
                'rtg11jam22': rtg11jam22_receive,
                'rtg11jam23': rtg11jam23_receive,
                'rtg11jam24': rtg11jam24_receive,
                
                'rtg12jam1': rtg12jam1_receive,
                'rtg12jam2': rtg12jam2_receive,
                'rtg12jam3': rtg12jam3_receive,
                'rtg12jam4': rtg12jam4_receive,
                'rtg12jam5': rtg12jam5_receive,
                'rtg12jam6': rtg12jam6_receive,
                'rtg12jam7': rtg12jam7_receive,
                'rtg12jam8': rtg12jam8_receive,
                'rtg12jam9': rtg12jam9_receive,
                'rtg12jam10': rtg12jam10_receive,
                'rtg12jam11': rtg12jam11_receive,
                'rtg12jam12': rtg12jam12_receive,
                'rtg12jam13': rtg12jam13_receive,
                'rtg12jam14': rtg12jam14_receive,
                'rtg12jam15': rtg12jam15_receive,
                'rtg12jam16': rtg12jam16_receive,
                'rtg12jam17': rtg12jam17_receive,
                'rtg12jam18': rtg12jam18_receive,
                'rtg12jam19': rtg12jam19_receive,
                'rtg12jam20': rtg12jam20_receive,
                'rtg12jam21': rtg12jam21_receive,
                'rtg12jam22': rtg12jam22_receive,
                'rtg12jam23': rtg12jam23_receive,
                'rtg12jam24': rtg12jam24_receive,
                
                'rtg13jam1': rtg13jam1_receive,
                'rtg13jam2': rtg13jam2_receive,
                'rtg13jam3': rtg13jam3_receive,
                'rtg13jam4': rtg13jam4_receive,
                'rtg13jam5': rtg13jam5_receive,
                'rtg13jam6': rtg13jam6_receive,
                'rtg13jam7': rtg13jam7_receive,
                'rtg13jam8': rtg13jam8_receive,
                'rtg13jam9': rtg13jam9_receive,
                'rtg13jam10': rtg13jam10_receive,
                'rtg13jam11': rtg13jam11_receive,
                'rtg13jam12': rtg13jam12_receive,
                'rtg13jam13': rtg13jam13_receive,
                'rtg13jam14': rtg13jam14_receive,
                'rtg13jam15': rtg13jam15_receive,
                'rtg13jam16': rtg13jam16_receive,
                'rtg13jam17': rtg13jam17_receive,
                'rtg13jam18': rtg13jam18_receive,
                'rtg13jam19': rtg13jam19_receive,
                'rtg13jam20': rtg13jam20_receive,
                'rtg13jam21': rtg13jam21_receive,
                'rtg13jam22': rtg13jam22_receive,
                'rtg13jam23': rtg13jam23_receive,
                'rtg13jam24': rtg13jam24_receive,

                'breakdown': breakdown_receive,
                'corrective': corrective_receive,
                'preventive': preventive_receive,
                'accident': accident_receive,
                'remark': remark_receive,
            }
            db.rtg.update_one({"_id": ObjectId(id)}, {"$set": doc})
            return redirect('/')
        
@app.route('/dailyAB', methods=['GET'])
def dailyAB():
    token_receive = request.cookies.get(TOKEN_KEY)
    try:
        payload = jwt.decode(
            token_receive,
            SECRET_KEY,
            algorithms=['HS256']
        )
        user_info = db.teknisi.find_one({'username': payload.get('id')})
        return render_template('dailyAB.html', user_info=user_info)
    except jwt.ExpiredSignatureError:
        msg = 'Token Anda sudah kadaluarsa'
        return redirect(url_for('home', msg=msg))
    except jwt.exceptions.DecodeError:
        msg = 'Terjadi masalah saat login'
        return redirect(url_for('home', msg=msg))


@app.route("/inputab", methods=["POST"])
def inputab():
    unit_receive = request.form.get('unit_give')
    tanggal_receive = request.form.get('tanggal_give')
    
    rs01jam1_receive = request.form.get('rs01jam1_give')
    rs01jam2_receive = request.form.get('rs01jam2_give')
    rs01jam3_receive = request.form.get('rs01jam3_give')
    rs01jam4_receive = request.form.get('rs01jam4_give')
    rs01jam5_receive = request.form.get('rs01jam5_give')
    rs01jam6_receive = request.form.get('rs01jam6_give')
    rs01jam7_receive = request.form.get('rs01jam7_give')
    rs01jam8_receive = request.form.get('rs01jam8_give')
    rs01jam9_receive = request.form.get('rs01jam9_give')
    rs01jam10_receive = request.form.get('rs01jam10_give')
    rs01jam11_receive = request.form.get('rs01jam11_give')
    rs01jam12_receive = request.form.get('rs01jam12_give')
    rs01jam13_receive = request.form.get('rs01jam13_give')
    rs01jam14_receive = request.form.get('rs01jam14_give')
    rs01jam15_receive = request.form.get('rs01jam15_give')
    rs01jam16_receive = request.form.get('rs01jam16_give')
    rs01jam17_receive = request.form.get('rs01jam17_give')
    rs01jam18_receive = request.form.get('rs01jam18_give')
    rs01jam19_receive = request.form.get('rs01jam19_give')
    rs01jam20_receive = request.form.get('rs01jam20_give')
    rs01jam21_receive = request.form.get('rs01jam21_give')
    rs01jam22_receive = request.form.get('rs01jam22_give')
    rs01jam23_receive = request.form.get('rs01jam23_give')
    rs01jam24_receive = request.form.get('rs01jam24_give')
    
    rs02jam1_receive = request.form.get('rs02jam1_give')
    rs02jam2_receive = request.form.get('rs02jam2_give')
    rs02jam3_receive = request.form.get('rs02jam3_give')
    rs02jam4_receive = request.form.get('rs02jam4_give')
    rs02jam5_receive = request.form.get('rs02jam5_give')
    rs02jam6_receive = request.form.get('rs02jam6_give')
    rs02jam7_receive = request.form.get('rs02jam7_give')
    rs02jam8_receive = request.form.get('rs02jam8_give')
    rs02jam9_receive = request.form.get('rs02jam9_give')
    rs02jam10_receive = request.form.get('rs02jam10_give')
    rs02jam11_receive = request.form.get('rs02jam11_give')
    rs02jam12_receive = request.form.get('rs02jam12_give')
    rs02jam13_receive = request.form.get('rs02jam13_give')
    rs02jam14_receive = request.form.get('rs02jam14_give')
    rs02jam15_receive = request.form.get('rs02jam15_give')
    rs02jam16_receive = request.form.get('rs02jam16_give')
    rs02jam17_receive = request.form.get('rs02jam17_give')
    rs02jam18_receive = request.form.get('rs02jam18_give')
    rs02jam19_receive = request.form.get('rs02jam19_give')
    rs02jam20_receive = request.form.get('rs02jam20_give')
    rs02jam21_receive = request.form.get('rs02jam21_give')
    rs02jam22_receive = request.form.get('rs02jam22_give')
    rs02jam23_receive = request.form.get('rs02jam23_give')
    rs02jam24_receive = request.form.get('rs02jam24_give')
    
    sljam1_receive = request.form.get('sljam1_give')
    sljam2_receive = request.form.get('sljam2_give')
    sljam3_receive = request.form.get('sljam3_give')
    sljam4_receive = request.form.get('sljam4_give')
    sljam5_receive = request.form.get('sljam5_give')
    sljam6_receive = request.form.get('sljam6_give')
    sljam7_receive = request.form.get('sljam7_give')
    sljam8_receive = request.form.get('sljam8_give')
    sljam9_receive = request.form.get('sljam9_give')
    sljam10_receive = request.form.get('sljam10_give')
    sljam11_receive = request.form.get('sljam11_give')
    sljam12_receive = request.form.get('sljam12_give')
    sljam13_receive = request.form.get('sljam13_give')
    sljam14_receive = request.form.get('sljam14_give')
    sljam15_receive = request.form.get('sljam15_give')
    sljam16_receive = request.form.get('sljam16_give')
    sljam17_receive = request.form.get('sljam17_give')
    sljam18_receive = request.form.get('sljam18_give')
    sljam19_receive = request.form.get('sljam19_give')
    sljam20_receive = request.form.get('sljam20_give')
    sljam21_receive = request.form.get('sljam21_give')
    sljam22_receive = request.form.get('sljam22_give')
    sljam23_receive = request.form.get('sljam23_give')
    sljam24_receive = request.form.get('sljam24_give')
    
    fl03jam1_receive = request.form.get('fl03jam1_give')
    fl03jam2_receive = request.form.get('fl03jam2_give')
    fl03jam3_receive = request.form.get('fl03jam3_give')
    fl03jam4_receive = request.form.get('fl03jam4_give')
    fl03jam5_receive = request.form.get('fl03jam5_give')
    fl03jam6_receive = request.form.get('fl03jam6_give')
    fl03jam7_receive = request.form.get('fl03jam7_give')
    fl03jam8_receive = request.form.get('fl03jam8_give')
    fl03jam9_receive = request.form.get('fl03jam9_give')
    fl03jam10_receive = request.form.get('fl03jam10_give')
    fl03jam11_receive = request.form.get('fl03jam11_give')
    fl03jam12_receive = request.form.get('fl03jam12_give')
    fl03jam13_receive = request.form.get('fl03jam13_give')
    fl03jam14_receive = request.form.get('fl03jam14_give')
    fl03jam15_receive = request.form.get('fl03jam15_give')
    fl03jam16_receive = request.form.get('fl03jam16_give')
    fl03jam17_receive = request.form.get('fl03jam17_give')
    fl03jam18_receive = request.form.get('fl03jam18_give')
    fl03jam19_receive = request.form.get('fl03jam19_give')
    fl03jam20_receive = request.form.get('fl03jam20_give')
    fl03jam21_receive = request.form.get('fl03jam21_give')
    fl03jam22_receive = request.form.get('fl03jam22_give')
    fl03jam23_receive = request.form.get('fl03jam23_give')
    fl03jam24_receive = request.form.get('fl03jam24_give')
    
    fl05jam1_receive = request.form.get('fl05jam1_give')
    fl05jam2_receive = request.form.get('fl05jam2_give')
    fl05jam3_receive = request.form.get('fl05jam3_give')
    fl05jam4_receive = request.form.get('fl05jam4_give')
    fl05jam5_receive = request.form.get('fl05jam5_give')
    fl05jam6_receive = request.form.get('fl05jam6_give')
    fl05jam7_receive = request.form.get('fl05jam7_give')
    fl05jam8_receive = request.form.get('fl05jam8_give')
    fl05jam9_receive = request.form.get('fl05jam9_give')
    fl05jam10_receive = request.form.get('fl05jam10_give')
    fl05jam11_receive = request.form.get('fl05jam11_give')
    fl05jam12_receive = request.form.get('fl05jam12_give')
    fl05jam13_receive = request.form.get('fl05jam13_give')
    fl05jam14_receive = request.form.get('fl05jam14_give')
    fl05jam15_receive = request.form.get('fl05jam15_give')
    fl05jam16_receive = request.form.get('fl05jam16_give')
    fl05jam17_receive = request.form.get('fl05jam17_give')
    fl05jam18_receive = request.form.get('fl05jam18_give')
    fl05jam19_receive = request.form.get('fl05jam19_give')
    fl05jam20_receive = request.form.get('fl05jam20_give')
    fl05jam21_receive = request.form.get('fl05jam21_give')
    fl05jam22_receive = request.form.get('fl05jam22_give')
    fl05jam23_receive = request.form.get('fl05jam23_give')
    fl05jam24_receive = request.form.get('fl05jam24_give')
    
    fl06jam1_receive = request.form.get('fl06jam1_give')
    fl06jam2_receive = request.form.get('fl06jam2_give')
    fl06jam3_receive = request.form.get('fl06jam3_give')
    fl06jam4_receive = request.form.get('fl06jam4_give')
    fl06jam5_receive = request.form.get('fl06jam5_give')
    fl06jam6_receive = request.form.get('fl06jam6_give')
    fl06jam7_receive = request.form.get('fl06jam7_give')
    fl06jam8_receive = request.form.get('fl06jam8_give')
    fl06jam9_receive = request.form.get('fl06jam9_give')
    fl06jam10_receive = request.form.get('fl06jam10_give')
    fl06jam11_receive = request.form.get('fl06jam11_give')
    fl06jam12_receive = request.form.get('fl06jam12_give')
    fl06jam13_receive = request.form.get('fl06jam13_give')
    fl06jam14_receive = request.form.get('fl06jam14_give')
    fl06jam15_receive = request.form.get('fl06jam15_give')
    fl06jam16_receive = request.form.get('fl06jam16_give')
    fl06jam17_receive = request.form.get('fl06jam17_give')
    fl06jam18_receive = request.form.get('fl06jam18_give')
    fl06jam19_receive = request.form.get('fl06jam19_give')
    fl06jam20_receive = request.form.get('fl06jam20_give')
    fl06jam21_receive = request.form.get('fl06jam21_give')
    fl06jam22_receive = request.form.get('fl06jam22_give')
    fl06jam23_receive = request.form.get('fl06jam23_give')
    fl06jam24_receive = request.form.get('fl06jam24_give')

    breakdown_receive = request.form.get('breakdown_give')
    corrective_receive = request.form.get('corrective_give')
    preventive_receive = request.form.get('preventive_give')
    accident_receive = request.form.get('accident_give')
    remark_receive = request.form.get('remark_give')

    doc = {
        'unit': unit_receive,
        'tanggal': tanggal_receive,

        'rs01jam1': rs01jam1_receive,
        'rs01jam2': rs01jam2_receive,
        'rs01jam3': rs01jam3_receive,
        'rs01jam4': rs01jam4_receive,
        'rs01jam5': rs01jam5_receive,
        'rs01jam6': rs01jam6_receive,
        'rs01jam7': rs01jam7_receive,
        'rs01jam8': rs01jam8_receive,
        'rs01jam9': rs01jam9_receive,
        'rs01jam10': rs01jam10_receive,
        'rs01jam11': rs01jam11_receive,
        'rs01jam12': rs01jam12_receive,
        'rs01jam13': rs01jam13_receive,
        'rs01jam14': rs01jam14_receive,
        'rs01jam15': rs01jam15_receive,
        'rs01jam16': rs01jam16_receive,
        'rs01jam17': rs01jam17_receive,
        'rs01jam18': rs01jam18_receive,
        'rs01jam19': rs01jam19_receive,
        'rs01jam20': rs01jam20_receive,
        'rs01jam21': rs01jam21_receive,
        'rs01jam22': rs01jam22_receive,
        'rs01jam23': rs01jam23_receive,
        'rs01jam24': rs01jam24_receive,
        
        'rs02jam1': rs02jam1_receive,
        'rs02jam2': rs02jam2_receive,
        'rs02jam3': rs02jam3_receive,
        'rs02jam4': rs02jam4_receive,
        'rs02jam5': rs02jam5_receive,
        'rs02jam6': rs02jam6_receive,
        'rs02jam7': rs02jam7_receive,
        'rs02jam8': rs02jam8_receive,
        'rs02jam9': rs02jam9_receive,
        'rs02jam10': rs02jam10_receive,
        'rs02jam11': rs02jam11_receive,
        'rs02jam12': rs02jam12_receive,
        'rs02jam13': rs02jam13_receive,
        'rs02jam14': rs02jam14_receive,
        'rs02jam15': rs02jam15_receive,
        'rs02jam16': rs02jam16_receive,
        'rs02jam17': rs02jam17_receive,
        'rs02jam18': rs02jam18_receive,
        'rs02jam19': rs02jam19_receive,
        'rs02jam20': rs02jam20_receive,
        'rs02jam21': rs02jam21_receive,
        'rs02jam22': rs02jam22_receive,
        'rs02jam23': rs02jam23_receive,
        'rs02jam24': rs02jam24_receive,

        'sljam1': sljam1_receive,
        'sljam2': sljam2_receive,
        'sljam3': sljam3_receive,
        'sljam4': sljam4_receive,
        'sljam5': sljam5_receive,
        'sljam6': sljam6_receive,
        'sljam7': sljam7_receive,
        'sljam8': sljam8_receive,
        'sljam9': sljam9_receive,
        'sljam10': sljam10_receive,
        'sljam11': sljam11_receive,
        'sljam12': sljam12_receive,
        'sljam13': sljam13_receive,
        'sljam14': sljam14_receive,
        'sljam15': sljam15_receive,
        'sljam16': sljam16_receive,
        'sljam17': sljam17_receive,
        'sljam18': sljam18_receive,
        'sljam19': sljam19_receive,
        'sljam20': sljam20_receive,
        'sljam21': sljam21_receive,
        'sljam22': sljam22_receive,
        'sljam23': sljam23_receive,
        'sljam24': sljam24_receive,
        
        'fl03jam1': fl03jam1_receive,
        'fl03jam2': fl03jam2_receive,
        'fl03jam3': fl03jam3_receive,
        'fl03jam4': fl03jam4_receive,
        'fl03jam5': fl03jam5_receive,
        'fl03jam6': fl03jam6_receive,
        'fl03jam7': fl03jam7_receive,
        'fl03jam8': fl03jam8_receive,
        'fl03jam9': fl03jam9_receive,
        'fl03jam10': fl03jam10_receive,
        'fl03jam11': fl03jam11_receive,
        'fl03jam12': fl03jam12_receive,
        'fl03jam13': fl03jam13_receive,
        'fl03jam14': fl03jam14_receive,
        'fl03jam15': fl03jam15_receive,
        'fl03jam16': fl03jam16_receive,
        'fl03jam17': fl03jam17_receive,
        'fl03jam18': fl03jam18_receive,
        'fl03jam19': fl03jam19_receive,
        'fl03jam20': fl03jam20_receive,
        'fl03jam21': fl03jam21_receive,
        'fl03jam22': fl03jam22_receive,
        'fl03jam23': fl03jam23_receive,
        'fl03jam24': fl03jam24_receive,
        
        'fl05jam1': fl05jam1_receive,
        'fl05jam2': fl05jam2_receive,
        'fl05jam3': fl05jam3_receive,
        'fl05jam4': fl05jam4_receive,
        'fl05jam5': fl05jam5_receive,
        'fl05jam6': fl05jam6_receive,
        'fl05jam7': fl05jam7_receive,
        'fl05jam8': fl05jam8_receive,
        'fl05jam9': fl05jam9_receive,
        'fl05jam10': fl05jam10_receive,
        'fl05jam11': fl05jam11_receive,
        'fl05jam12': fl05jam12_receive,
        'fl05jam13': fl05jam13_receive,
        'fl05jam14': fl05jam14_receive,
        'fl05jam15': fl05jam15_receive,
        'fl05jam16': fl05jam16_receive,
        'fl05jam17': fl05jam17_receive,
        'fl05jam18': fl05jam18_receive,
        'fl05jam19': fl05jam19_receive,
        'fl05jam20': fl05jam20_receive,
        'fl05jam21': fl05jam21_receive,
        'fl05jam22': fl05jam22_receive,
        'fl05jam23': fl05jam23_receive,
        'fl05jam24': fl05jam24_receive,
        
        'fl06jam1': fl06jam1_receive,
        'fl06jam2': fl06jam2_receive,
        'fl06jam3': fl06jam3_receive,
        'fl06jam4': fl06jam4_receive,
        'fl06jam5': fl06jam5_receive,
        'fl06jam6': fl06jam6_receive,
        'fl06jam7': fl06jam7_receive,
        'fl06jam8': fl06jam8_receive,
        'fl06jam9': fl06jam9_receive,
        'fl06jam10': fl06jam10_receive,
        'fl06jam11': fl06jam11_receive,
        'fl06jam12': fl06jam12_receive,
        'fl06jam13': fl06jam13_receive,
        'fl06jam14': fl06jam14_receive,
        'fl06jam15': fl06jam15_receive,
        'fl06jam16': fl06jam16_receive,
        'fl06jam17': fl06jam17_receive,
        'fl06jam18': fl06jam18_receive,
        'fl06jam19': fl06jam19_receive,
        'fl06jam20': fl06jam20_receive,
        'fl06jam21': fl06jam21_receive,
        'fl06jam22': fl06jam22_receive,
        'fl06jam23': fl06jam23_receive,
        'fl06jam24': fl06jam24_receive,

        'breakdown': breakdown_receive,
        'corrective': corrective_receive,
        'preventive': preventive_receive,
        'accident': accident_receive,
        'remark': remark_receive,
    }
    db.ab.insert_one(doc)
    return jsonify({'msg': 'Data berhasil disimpan!'})


    
@app.route('/viewAB', methods=['GET'])
def viewAB():
    token_receive = request.cookies.get(TOKEN_KEY)
    try:
        payload = jwt.decode(
            token_receive,
            SECRET_KEY,
            algorithms=['HS256']
        )
        id = request.args.get("id")
        data = db.ab.find_one({"_id": ObjectId(id)})
        data["_id"] = str(data["_id"])
        print(data)
        user_info = db.teknisi.find_one({'username': payload.get('id')})
        return render_template('viewAB.html', user_info=user_info, data=data)
    except jwt.ExpiredSignatureError:
        msg = 'Token Anda sudah kadaluarsa'
        return redirect(url_for('home', msg=msg))
    except jwt.exceptions.DecodeError:
        msg = 'Terjadi masalah saat login'
        return redirect(url_for('home', msg=msg))



    

@app.route('/editAB', methods=['GET', 'POST'])
def editAB():
    if request.method == "GET":
        token_receive = request.cookies.get(TOKEN_KEY)
        try:
            payload = jwt.decode(
                token_receive,
                SECRET_KEY,
                algorithms=['HS256']
            )
            id = request.args.get("id")
            data = db.ab.find_one({"_id": ObjectId(id)})
            data["_id"] = str(data["_id"])
            print(data)
            user_info = db.teknisi.find_one({'username': payload.get('id')})
            return render_template('editAB.html', user_info=user_info, data=data)
        except jwt.ExpiredSignatureError:
            msg = 'Token Anda sudah kadaluarsa'
            return redirect(url_for('home', msg=msg))
        except jwt.exceptions.DecodeError:
            msg = 'Terjadi masalah saat login'
            return redirect(url_for('home', msg=msg))

    elif request.method == "POST":
            id = request.form["id"]
            unit_receive = request.form["unit"]
            tanggal_receive = request.form["tanggal"]
        
            rs01jam1_receive = request.form["rs01jam1"]
            rs01jam2_receive = request.form["rs01jam2"]
            rs01jam3_receive = request.form["rs01jam3"]
            rs01jam4_receive = request.form["rs01jam4"]
            rs01jam5_receive = request.form["rs01jam5"]
            rs01jam6_receive = request.form["rs01jam6"]
            rs01jam7_receive = request.form["rs01jam7"]
            rs01jam8_receive = request.form["rs01jam8"]
            rs01jam9_receive = request.form["rs01jam9"]
            rs01jam10_receive = request.form["rs01jam10"]
            rs01jam11_receive = request.form["rs01jam11"]
            rs01jam12_receive = request.form["rs01jam12"]
            rs01jam13_receive = request.form["rs01jam13"]
            rs01jam14_receive = request.form["rs01jam14"]
            rs01jam15_receive = request.form["rs01jam15"]
            rs01jam16_receive = request.form["rs01jam16"]
            rs01jam17_receive = request.form["rs01jam17"]
            rs01jam18_receive = request.form["rs01jam18"]
            rs01jam19_receive = request.form["rs01jam19"]
            rs01jam20_receive = request.form["rs01jam20"]
            rs01jam21_receive = request.form["rs01jam21"]
            rs01jam22_receive = request.form["rs01jam22"]
            rs01jam23_receive = request.form["rs01jam23"]
            rs01jam24_receive = request.form["rs01jam24"]
            
            rs02jam1_receive = request.form["rs02jam1"]
            rs02jam2_receive = request.form["rs02jam2"]
            rs02jam3_receive = request.form["rs02jam3"]
            rs02jam4_receive = request.form["rs02jam4"]
            rs02jam5_receive = request.form["rs02jam5"]
            rs02jam6_receive = request.form["rs02jam6"]
            rs02jam7_receive = request.form["rs02jam7"]
            rs02jam8_receive = request.form["rs02jam8"]
            rs02jam9_receive = request.form["rs02jam9"]
            rs02jam10_receive = request.form["rs02jam10"]
            rs02jam11_receive = request.form["rs02jam11"]
            rs02jam12_receive = request.form["rs02jam12"]
            rs02jam13_receive = request.form["rs02jam13"]
            rs02jam14_receive = request.form["rs02jam14"]
            rs02jam15_receive = request.form["rs02jam15"]
            rs02jam16_receive = request.form["rs02jam16"]
            rs02jam17_receive = request.form["rs02jam17"]
            rs02jam18_receive = request.form["rs02jam18"]
            rs02jam19_receive = request.form["rs02jam19"]
            rs02jam20_receive = request.form["rs02jam20"]
            rs02jam21_receive = request.form["rs02jam21"]
            rs02jam22_receive = request.form["rs02jam22"]
            rs02jam23_receive = request.form["rs02jam23"]
            rs02jam24_receive = request.form["rs02jam24"]
            
            sljam1_receive = request.form["sljam1"]
            sljam2_receive = request.form["sljam2"]
            sljam3_receive = request.form["sljam3"]
            sljam4_receive = request.form["sljam4"]
            sljam5_receive = request.form["sljam5"]
            sljam6_receive = request.form["sljam6"]
            sljam7_receive = request.form["sljam7"]
            sljam8_receive = request.form["sljam8"]
            sljam9_receive = request.form["sljam9"]
            sljam10_receive = request.form["sljam10"]
            sljam11_receive = request.form["sljam11"]
            sljam12_receive = request.form["sljam12"]
            sljam13_receive = request.form["sljam13"]
            sljam14_receive = request.form["sljam14"]
            sljam15_receive = request.form["sljam15"]
            sljam16_receive = request.form["sljam16"]
            sljam17_receive = request.form["sljam17"]
            sljam18_receive = request.form["sljam18"]
            sljam19_receive = request.form["sljam19"]
            sljam20_receive = request.form["sljam20"]
            sljam21_receive = request.form["sljam21"]
            sljam22_receive = request.form["sljam22"]
            sljam23_receive = request.form["sljam23"]
            sljam24_receive = request.form["sljam24"]
            
            fl03jam1_receive = request.form["fl03jam1"]
            fl03jam2_receive = request.form["fl03jam2"]
            fl03jam3_receive = request.form["fl03jam3"]
            fl03jam4_receive = request.form["fl03jam4"]
            fl03jam5_receive = request.form["fl03jam5"]
            fl03jam6_receive = request.form["fl03jam6"]
            fl03jam7_receive = request.form["fl03jam7"]
            fl03jam8_receive = request.form["fl03jam8"]
            fl03jam9_receive = request.form["fl03jam9"]
            fl03jam10_receive = request.form["fl03jam10"]
            fl03jam11_receive = request.form["fl03jam11"]
            fl03jam12_receive = request.form["fl03jam12"]
            fl03jam13_receive = request.form["fl03jam13"]
            fl03jam14_receive = request.form["fl03jam14"]
            fl03jam15_receive = request.form["fl03jam15"]
            fl03jam16_receive = request.form["fl03jam16"]
            fl03jam17_receive = request.form["fl03jam17"]
            fl03jam18_receive = request.form["fl03jam18"]
            fl03jam19_receive = request.form["fl03jam19"]
            fl03jam20_receive = request.form["fl03jam20"]
            fl03jam21_receive = request.form["fl03jam21"]
            fl03jam22_receive = request.form["fl03jam22"]
            fl03jam23_receive = request.form["fl03jam23"]
            fl03jam24_receive = request.form["fl03jam24"]
            
            fl05jam1_receive = request.form["fl05jam1"]
            fl05jam2_receive = request.form["fl05jam2"]
            fl05jam3_receive = request.form["fl05jam3"]
            fl05jam4_receive = request.form["fl05jam4"]
            fl05jam5_receive = request.form["fl05jam5"]
            fl05jam6_receive = request.form["fl05jam6"]
            fl05jam7_receive = request.form["fl05jam7"]
            fl05jam8_receive = request.form["fl05jam8"]
            fl05jam9_receive = request.form["fl05jam9"]
            fl05jam10_receive = request.form["fl05jam10"]
            fl05jam11_receive = request.form["fl05jam11"]
            fl05jam12_receive = request.form["fl05jam12"]
            fl05jam13_receive = request.form["fl05jam13"]
            fl05jam14_receive = request.form["fl05jam14"]
            fl05jam15_receive = request.form["fl05jam15"]
            fl05jam16_receive = request.form["fl05jam16"]
            fl05jam17_receive = request.form["fl05jam17"]
            fl05jam18_receive = request.form["fl05jam18"]
            fl05jam19_receive = request.form["fl05jam19"]
            fl05jam20_receive = request.form["fl05jam20"]
            fl05jam21_receive = request.form["fl05jam21"]
            fl05jam22_receive = request.form["fl05jam22"]
            fl05jam23_receive = request.form["fl05jam23"]
            fl05jam24_receive = request.form["fl05jam24"]
            
            fl06jam1_receive = request.form["fl06jam1"]
            fl06jam2_receive = request.form["fl06jam2"]
            fl06jam3_receive = request.form["fl06jam3"]
            fl06jam4_receive = request.form["fl06jam4"]
            fl06jam5_receive = request.form["fl06jam5"]
            fl06jam6_receive = request.form["fl06jam6"]
            fl06jam7_receive = request.form["fl06jam7"]
            fl06jam8_receive = request.form["fl06jam8"]
            fl06jam9_receive = request.form["fl06jam9"]
            fl06jam10_receive = request.form["fl06jam10"]
            fl06jam11_receive = request.form["fl06jam11"]
            fl06jam12_receive = request.form["fl06jam12"]
            fl06jam13_receive = request.form["fl06jam13"]
            fl06jam14_receive = request.form["fl06jam14"]
            fl06jam15_receive = request.form["fl06jam15"]
            fl06jam16_receive = request.form["fl06jam16"]
            fl06jam17_receive = request.form["fl06jam17"]
            fl06jam18_receive = request.form["fl06jam18"]
            fl06jam19_receive = request.form["fl06jam19"]
            fl06jam20_receive = request.form["fl06jam20"]
            fl06jam21_receive = request.form["fl06jam21"]
            fl06jam22_receive = request.form["fl06jam22"]
            fl06jam23_receive = request.form["fl06jam23"]
            fl06jam24_receive = request.form["fl06jam24"]

            breakdown_receive = request.form.get('breakdown')
            corrective_receive = request.form.get('corrective')
            preventive_receive = request.form.get('preventive')
            accident_receive = request.form.get('accident')
            remark_receive = request.form.get('remark')

            doc = {
                'unit': unit_receive,
                'tanggal': tanggal_receive,

                'rs01jam1': rs01jam1_receive,
                'rs01jam2': rs01jam2_receive,
                'rs01jam3': rs01jam3_receive,
                'rs01jam4': rs01jam4_receive,
                'rs01jam5': rs01jam5_receive,
                'rs01jam6': rs01jam6_receive,
                'rs01jam7': rs01jam7_receive,
                'rs01jam8': rs01jam8_receive,
                'rs01jam9': rs01jam9_receive,
                'rs01jam10': rs01jam10_receive,
                'rs01jam11': rs01jam11_receive,
                'rs01jam12': rs01jam12_receive,
                'rs01jam13': rs01jam13_receive,
                'rs01jam14': rs01jam14_receive,
                'rs01jam15': rs01jam15_receive,
                'rs01jam16': rs01jam16_receive,
                'rs01jam17': rs01jam17_receive,
                'rs01jam18': rs01jam18_receive,
                'rs01jam19': rs01jam19_receive,
                'rs01jam20': rs01jam20_receive,
                'rs01jam21': rs01jam21_receive,
                'rs01jam22': rs01jam22_receive,
                'rs01jam23': rs01jam23_receive,
                'rs01jam24': rs01jam24_receive,
                
                'rs02jam1': rs02jam1_receive,
                'rs02jam2': rs02jam2_receive,
                'rs02jam3': rs02jam3_receive,
                'rs02jam4': rs02jam4_receive,
                'rs02jam5': rs02jam5_receive,
                'rs02jam6': rs02jam6_receive,
                'rs02jam7': rs02jam7_receive,
                'rs02jam8': rs02jam8_receive,
                'rs02jam9': rs02jam9_receive,
                'rs02jam10': rs02jam10_receive,
                'rs02jam11': rs02jam11_receive,
                'rs02jam12': rs02jam12_receive,
                'rs02jam13': rs02jam13_receive,
                'rs02jam14': rs02jam14_receive,
                'rs02jam15': rs02jam15_receive,
                'rs02jam16': rs02jam16_receive,
                'rs02jam17': rs02jam17_receive,
                'rs02jam18': rs02jam18_receive,
                'rs02jam19': rs02jam19_receive,
                'rs02jam20': rs02jam20_receive,
                'rs02jam21': rs02jam21_receive,
                'rs02jam22': rs02jam22_receive,
                'rs02jam23': rs02jam23_receive,
                'rs02jam24': rs02jam24_receive,

                'sljam1': sljam1_receive,
                'sljam2': sljam2_receive,
                'sljam3': sljam3_receive,
                'sljam4': sljam4_receive,
                'sljam5': sljam5_receive,
                'sljam6': sljam6_receive,
                'sljam7': sljam7_receive,
                'sljam8': sljam8_receive,
                'sljam9': sljam9_receive,
                'sljam10': sljam10_receive,
                'sljam11': sljam11_receive,
                'sljam12': sljam12_receive,
                'sljam13': sljam13_receive,
                'sljam14': sljam14_receive,
                'sljam15': sljam15_receive,
                'sljam16': sljam16_receive,
                'sljam17': sljam17_receive,
                'sljam18': sljam18_receive,
                'sljam19': sljam19_receive,
                'sljam20': sljam20_receive,
                'sljam21': sljam21_receive,
                'sljam22': sljam22_receive,
                'sljam23': sljam23_receive,
                'sljam24': sljam24_receive,
                
                'fl03jam1': fl03jam1_receive,
                'fl03jam2': fl03jam2_receive,
                'fl03jam3': fl03jam3_receive,
                'fl03jam4': fl03jam4_receive,
                'fl03jam5': fl03jam5_receive,
                'fl03jam6': fl03jam6_receive,
                'fl03jam7': fl03jam7_receive,
                'fl03jam8': fl03jam8_receive,
                'fl03jam9': fl03jam9_receive,
                'fl03jam10': fl03jam10_receive,
                'fl03jam11': fl03jam11_receive,
                'fl03jam12': fl03jam12_receive,
                'fl03jam13': fl03jam13_receive,
                'fl03jam14': fl03jam14_receive,
                'fl03jam15': fl03jam15_receive,
                'fl03jam16': fl03jam16_receive,
                'fl03jam17': fl03jam17_receive,
                'fl03jam18': fl03jam18_receive,
                'fl03jam19': fl03jam19_receive,
                'fl03jam20': fl03jam20_receive,
                'fl03jam21': fl03jam21_receive,
                'fl03jam22': fl03jam22_receive,
                'fl03jam23': fl03jam23_receive,
                'fl03jam24': fl03jam24_receive,
                
                'fl05jam1': fl05jam1_receive,
                'fl05jam2': fl05jam2_receive,
                'fl05jam3': fl05jam3_receive,
                'fl05jam4': fl05jam4_receive,
                'fl05jam5': fl05jam5_receive,
                'fl05jam6': fl05jam6_receive,
                'fl05jam7': fl05jam7_receive,
                'fl05jam8': fl05jam8_receive,
                'fl05jam9': fl05jam9_receive,
                'fl05jam10': fl05jam10_receive,
                'fl05jam11': fl05jam11_receive,
                'fl05jam12': fl05jam12_receive,
                'fl05jam13': fl05jam13_receive,
                'fl05jam14': fl05jam14_receive,
                'fl05jam15': fl05jam15_receive,
                'fl05jam16': fl05jam16_receive,
                'fl05jam17': fl05jam17_receive,
                'fl05jam18': fl05jam18_receive,
                'fl05jam19': fl05jam19_receive,
                'fl05jam20': fl05jam20_receive,
                'fl05jam21': fl05jam21_receive,
                'fl05jam22': fl05jam22_receive,
                'fl05jam23': fl05jam23_receive,
                'fl05jam24': fl05jam24_receive,
                
                'fl06jam1': fl06jam1_receive,
                'fl06jam2': fl06jam2_receive,
                'fl06jam3': fl06jam3_receive,
                'fl06jam4': fl06jam4_receive,
                'fl06jam5': fl06jam5_receive,
                'fl06jam6': fl06jam6_receive,
                'fl06jam7': fl06jam7_receive,
                'fl06jam8': fl06jam8_receive,
                'fl06jam9': fl06jam9_receive,
                'fl06jam10': fl06jam10_receive,
                'fl06jam11': fl06jam11_receive,
                'fl06jam12': fl06jam12_receive,
                'fl06jam13': fl06jam13_receive,
                'fl06jam14': fl06jam14_receive,
                'fl06jam15': fl06jam15_receive,
                'fl06jam16': fl06jam16_receive,
                'fl06jam17': fl06jam17_receive,
                'fl06jam18': fl06jam18_receive,
                'fl06jam19': fl06jam19_receive,
                'fl06jam20': fl06jam20_receive,
                'fl06jam21': fl06jam21_receive,
                'fl06jam22': fl06jam22_receive,
                'fl06jam23': fl06jam23_receive,
                'fl06jam24': fl06jam24_receive,

                'breakdown': breakdown_receive,
                'corrective': corrective_receive,
                'preventive': preventive_receive,
                'accident': accident_receive,
                'remark': remark_receive,
            }
            db.ab.update_one({"_id": ObjectId(id)}, {"$set": doc})
            return redirect('/')
        
@app.route('/dailyHT', methods=['GET'])
def dailyHT():
    token_receive = request.cookies.get(TOKEN_KEY)
    try:
        payload = jwt.decode(
            token_receive,
            SECRET_KEY,
            algorithms=['HS256']
        )
        user_info = db.teknisi.find_one({'username': payload.get('id')})
        return render_template('dailyHT.html', user_info=user_info)
    except jwt.ExpiredSignatureError:
        msg = 'Token Anda sudah kadaluarsa'
        return redirect(url_for('home', msg=msg))
    except jwt.exceptions.DecodeError:
        msg = 'Terjadi masalah saat login'
        return redirect(url_for('home', msg=msg))


@app.route("/inputht", methods=["POST"])
def inputht():
    unit_receive = request.form.get('unit_give')
    tanggal_receive = request.form.get('tanggal_give')
    
    ht01jam1_receive = request.form.get('ht01jam1_give')
    ht01jam2_receive = request.form.get('ht01jam2_give')
    ht01jam3_receive = request.form.get('ht01jam3_give')
    ht01jam4_receive = request.form.get('ht01jam4_give')
    ht01jam5_receive = request.form.get('ht01jam5_give')
    ht01jam6_receive = request.form.get('ht01jam6_give')
    ht01jam7_receive = request.form.get('ht01jam7_give')
    ht01jam8_receive = request.form.get('ht01jam8_give')
    ht01jam9_receive = request.form.get('ht01jam9_give')
    ht01jam10_receive = request.form.get('ht01jam10_give')
    ht01jam11_receive = request.form.get('ht01jam11_give')
    ht01jam12_receive = request.form.get('ht01jam12_give')
    ht01jam13_receive = request.form.get('ht01jam13_give')
    ht01jam14_receive = request.form.get('ht01jam14_give')
    ht01jam15_receive = request.form.get('ht01jam15_give')
    ht01jam16_receive = request.form.get('ht01jam16_give')
    ht01jam17_receive = request.form.get('ht01jam17_give')
    ht01jam18_receive = request.form.get('ht01jam18_give')
    ht01jam19_receive = request.form.get('ht01jam19_give')
    ht01jam20_receive = request.form.get('ht01jam20_give')
    ht01jam21_receive = request.form.get('ht01jam21_give')
    ht01jam22_receive = request.form.get('ht01jam22_give')
    ht01jam23_receive = request.form.get('ht01jam23_give')
    ht01jam24_receive = request.form.get('ht01jam24_give')
    
    ht02jam1_receive = request.form.get('ht02jam1_give')
    ht02jam2_receive = request.form.get('ht02jam2_give')
    ht02jam3_receive = request.form.get('ht02jam3_give')
    ht02jam4_receive = request.form.get('ht02jam4_give')
    ht02jam5_receive = request.form.get('ht02jam5_give')
    ht02jam6_receive = request.form.get('ht02jam6_give')
    ht02jam7_receive = request.form.get('ht02jam7_give')
    ht02jam8_receive = request.form.get('ht02jam8_give')
    ht02jam9_receive = request.form.get('ht02jam9_give')
    ht02jam10_receive = request.form.get('ht02jam10_give')
    ht02jam11_receive = request.form.get('ht02jam11_give')
    ht02jam12_receive = request.form.get('ht02jam12_give')
    ht02jam13_receive = request.form.get('ht02jam13_give')
    ht02jam14_receive = request.form.get('ht02jam14_give')
    ht02jam15_receive = request.form.get('ht02jam15_give')
    ht02jam16_receive = request.form.get('ht02jam16_give')
    ht02jam17_receive = request.form.get('ht02jam17_give')
    ht02jam18_receive = request.form.get('ht02jam18_give')
    ht02jam19_receive = request.form.get('ht02jam19_give')
    ht02jam20_receive = request.form.get('ht02jam20_give')
    ht02jam21_receive = request.form.get('ht02jam21_give')
    ht02jam22_receive = request.form.get('ht02jam22_give')
    ht02jam23_receive = request.form.get('ht02jam23_give')
    ht02jam24_receive = request.form.get('ht02jam24_give')
    
    ht03jam1_receive = request.form.get('ht03jam1_give')
    ht03jam2_receive = request.form.get('ht03jam2_give')
    ht03jam3_receive = request.form.get('ht03jam3_give')
    ht03jam4_receive = request.form.get('ht03jam4_give')
    ht03jam5_receive = request.form.get('ht03jam5_give')
    ht03jam6_receive = request.form.get('ht03jam6_give')
    ht03jam7_receive = request.form.get('ht03jam7_give')
    ht03jam8_receive = request.form.get('ht03jam8_give')
    ht03jam9_receive = request.form.get('ht03jam9_give')
    ht03jam10_receive = request.form.get('ht03jam10_give')
    ht03jam11_receive = request.form.get('ht03jam11_give')
    ht03jam12_receive = request.form.get('ht03jam12_give')
    ht03jam13_receive = request.form.get('ht03jam13_give')
    ht03jam14_receive = request.form.get('ht03jam14_give')
    ht03jam15_receive = request.form.get('ht03jam15_give')
    ht03jam16_receive = request.form.get('ht03jam16_give')
    ht03jam17_receive = request.form.get('ht03jam17_give')
    ht03jam18_receive = request.form.get('ht03jam18_give')
    ht03jam19_receive = request.form.get('ht03jam19_give')
    ht03jam20_receive = request.form.get('ht03jam20_give')
    ht03jam21_receive = request.form.get('ht03jam21_give')
    ht03jam22_receive = request.form.get('ht03jam22_give')
    ht03jam23_receive = request.form.get('ht03jam23_give')
    ht03jam24_receive = request.form.get('ht03jam24_give')
    
    ht04jam1_receive = request.form.get('ht04jam1_give')
    ht04jam2_receive = request.form.get('ht04jam2_give')
    ht04jam3_receive = request.form.get('ht04jam3_give')
    ht04jam4_receive = request.form.get('ht04jam4_give')
    ht04jam5_receive = request.form.get('ht04jam5_give')
    ht04jam6_receive = request.form.get('ht04jam6_give')
    ht04jam7_receive = request.form.get('ht04jam7_give')
    ht04jam8_receive = request.form.get('ht04jam8_give')
    ht04jam9_receive = request.form.get('ht04jam9_give')
    ht04jam10_receive = request.form.get('ht04jam10_give')
    ht04jam11_receive = request.form.get('ht04jam11_give')
    ht04jam12_receive = request.form.get('ht04jam12_give')
    ht04jam13_receive = request.form.get('ht04jam13_give')
    ht04jam14_receive = request.form.get('ht04jam14_give')
    ht04jam15_receive = request.form.get('ht04jam15_give')
    ht04jam16_receive = request.form.get('ht04jam16_give')
    ht04jam17_receive = request.form.get('ht04jam17_give')
    ht04jam18_receive = request.form.get('ht04jam18_give')
    ht04jam19_receive = request.form.get('ht04jam19_give')
    ht04jam20_receive = request.form.get('ht04jam20_give')
    ht04jam21_receive = request.form.get('ht04jam21_give')
    ht04jam22_receive = request.form.get('ht04jam22_give')
    ht04jam23_receive = request.form.get('ht04jam23_give')
    ht04jam24_receive = request.form.get('ht04jam24_give')
    
    ht05jam1_receive = request.form.get('ht05jam1_give')
    ht05jam2_receive = request.form.get('ht05jam2_give')
    ht05jam3_receive = request.form.get('ht05jam3_give')
    ht05jam4_receive = request.form.get('ht05jam4_give')
    ht05jam5_receive = request.form.get('ht05jam5_give')
    ht05jam6_receive = request.form.get('ht05jam6_give')
    ht05jam7_receive = request.form.get('ht05jam7_give')
    ht05jam8_receive = request.form.get('ht05jam8_give')
    ht05jam9_receive = request.form.get('ht05jam9_give')
    ht05jam10_receive = request.form.get('ht05jam10_give')
    ht05jam11_receive = request.form.get('ht05jam11_give')
    ht05jam12_receive = request.form.get('ht05jam12_give')
    ht05jam13_receive = request.form.get('ht05jam13_give')
    ht05jam14_receive = request.form.get('ht05jam14_give')
    ht05jam15_receive = request.form.get('ht05jam15_give')
    ht05jam16_receive = request.form.get('ht05jam16_give')
    ht05jam17_receive = request.form.get('ht05jam17_give')
    ht05jam18_receive = request.form.get('ht05jam18_give')
    ht05jam19_receive = request.form.get('ht05jam19_give')
    ht05jam20_receive = request.form.get('ht05jam20_give')
    ht05jam21_receive = request.form.get('ht05jam21_give')
    ht05jam22_receive = request.form.get('ht05jam22_give')
    ht05jam23_receive = request.form.get('ht05jam23_give')
    ht05jam24_receive = request.form.get('ht05jam24_give')
    
    ht06jam1_receive = request.form.get('ht06jam1_give')
    ht06jam2_receive = request.form.get('ht06jam2_give')
    ht06jam3_receive = request.form.get('ht06jam3_give')
    ht06jam4_receive = request.form.get('ht06jam4_give')
    ht06jam5_receive = request.form.get('ht06jam5_give')
    ht06jam6_receive = request.form.get('ht06jam6_give')
    ht06jam7_receive = request.form.get('ht06jam7_give')
    ht06jam8_receive = request.form.get('ht06jam8_give')
    ht06jam9_receive = request.form.get('ht06jam9_give')
    ht06jam10_receive = request.form.get('ht06jam10_give')
    ht06jam11_receive = request.form.get('ht06jam11_give')
    ht06jam12_receive = request.form.get('ht06jam12_give')
    ht06jam13_receive = request.form.get('ht06jam13_give')
    ht06jam14_receive = request.form.get('ht06jam14_give')
    ht06jam15_receive = request.form.get('ht06jam15_give')
    ht06jam16_receive = request.form.get('ht06jam16_give')
    ht06jam17_receive = request.form.get('ht06jam17_give')
    ht06jam18_receive = request.form.get('ht06jam18_give')
    ht06jam19_receive = request.form.get('ht06jam19_give')
    ht06jam20_receive = request.form.get('ht06jam20_give')
    ht06jam21_receive = request.form.get('ht06jam21_give')
    ht06jam22_receive = request.form.get('ht06jam22_give')
    ht06jam23_receive = request.form.get('ht06jam23_give')
    ht06jam24_receive = request.form.get('ht06jam24_give')
    
    ht07jam1_receive = request.form.get('ht07jam1_give')
    ht07jam2_receive = request.form.get('ht07jam2_give')
    ht07jam3_receive = request.form.get('ht07jam3_give')
    ht07jam4_receive = request.form.get('ht07jam4_give')
    ht07jam5_receive = request.form.get('ht07jam5_give')
    ht07jam6_receive = request.form.get('ht07jam6_give')
    ht07jam7_receive = request.form.get('ht07jam7_give')
    ht07jam8_receive = request.form.get('ht07jam8_give')
    ht07jam9_receive = request.form.get('ht07jam9_give')
    ht07jam10_receive = request.form.get('ht07jam10_give')
    ht07jam11_receive = request.form.get('ht07jam11_give')
    ht07jam12_receive = request.form.get('ht07jam12_give')
    ht07jam13_receive = request.form.get('ht07jam13_give')
    ht07jam14_receive = request.form.get('ht07jam14_give')
    ht07jam15_receive = request.form.get('ht07jam15_give')
    ht07jam16_receive = request.form.get('ht07jam16_give')
    ht07jam17_receive = request.form.get('ht07jam17_give')
    ht07jam18_receive = request.form.get('ht07jam18_give')
    ht07jam19_receive = request.form.get('ht07jam19_give')
    ht07jam20_receive = request.form.get('ht07jam20_give')
    ht07jam21_receive = request.form.get('ht07jam21_give')
    ht07jam22_receive = request.form.get('ht07jam22_give')
    ht07jam23_receive = request.form.get('ht07jam23_give')
    ht07jam24_receive = request.form.get('ht07jam24_give')
    
    ht08jam1_receive = request.form.get('ht08jam1_give')
    ht08jam2_receive = request.form.get('ht08jam2_give')
    ht08jam3_receive = request.form.get('ht08jam3_give')
    ht08jam4_receive = request.form.get('ht08jam4_give')
    ht08jam5_receive = request.form.get('ht08jam5_give')
    ht08jam6_receive = request.form.get('ht08jam6_give')
    ht08jam7_receive = request.form.get('ht08jam7_give')
    ht08jam8_receive = request.form.get('ht08jam8_give')
    ht08jam9_receive = request.form.get('ht08jam9_give')
    ht08jam10_receive = request.form.get('ht08jam10_give')
    ht08jam11_receive = request.form.get('ht08jam11_give')
    ht08jam12_receive = request.form.get('ht08jam12_give')
    ht08jam13_receive = request.form.get('ht08jam13_give')
    ht08jam14_receive = request.form.get('ht08jam14_give')
    ht08jam15_receive = request.form.get('ht08jam15_give')
    ht08jam16_receive = request.form.get('ht08jam16_give')
    ht08jam17_receive = request.form.get('ht08jam17_give')
    ht08jam18_receive = request.form.get('ht08jam18_give')
    ht08jam19_receive = request.form.get('ht08jam19_give')
    ht08jam20_receive = request.form.get('ht08jam20_give')
    ht08jam21_receive = request.form.get('ht08jam21_give')
    ht08jam22_receive = request.form.get('ht08jam22_give')
    ht08jam23_receive = request.form.get('ht08jam23_give')
    ht08jam24_receive = request.form.get('ht08jam24_give')
    
    ht09jam1_receive = request.form.get('ht09jam1_give')
    ht09jam2_receive = request.form.get('ht09jam2_give')
    ht09jam3_receive = request.form.get('ht09jam3_give')
    ht09jam4_receive = request.form.get('ht09jam4_give')
    ht09jam5_receive = request.form.get('ht09jam5_give')
    ht09jam6_receive = request.form.get('ht09jam6_give')
    ht09jam7_receive = request.form.get('ht09jam7_give')
    ht09jam8_receive = request.form.get('ht09jam8_give')
    ht09jam9_receive = request.form.get('ht09jam9_give')
    ht09jam10_receive = request.form.get('ht09jam10_give')
    ht09jam11_receive = request.form.get('ht09jam11_give')
    ht09jam12_receive = request.form.get('ht09jam12_give')
    ht09jam13_receive = request.form.get('ht09jam13_give')
    ht09jam14_receive = request.form.get('ht09jam14_give')
    ht09jam15_receive = request.form.get('ht09jam15_give')
    ht09jam16_receive = request.form.get('ht09jam16_give')
    ht09jam17_receive = request.form.get('ht09jam17_give')
    ht09jam18_receive = request.form.get('ht09jam18_give')
    ht09jam19_receive = request.form.get('ht09jam19_give')
    ht09jam20_receive = request.form.get('ht09jam20_give')
    ht09jam21_receive = request.form.get('ht09jam21_give')
    ht09jam22_receive = request.form.get('ht09jam22_give')
    ht09jam23_receive = request.form.get('ht09jam23_give')
    ht09jam24_receive = request.form.get('ht09jam24_give')
    
    ht10jam1_receive = request.form.get('ht10jam1_give')
    ht10jam2_receive = request.form.get('ht10jam2_give')
    ht10jam3_receive = request.form.get('ht10jam3_give')
    ht10jam4_receive = request.form.get('ht10jam4_give')
    ht10jam5_receive = request.form.get('ht10jam5_give')
    ht10jam6_receive = request.form.get('ht10jam6_give')
    ht10jam7_receive = request.form.get('ht10jam7_give')
    ht10jam8_receive = request.form.get('ht10jam8_give')
    ht10jam9_receive = request.form.get('ht10jam9_give')
    ht10jam10_receive = request.form.get('ht10jam10_give')
    ht10jam11_receive = request.form.get('ht10jam11_give')
    ht10jam12_receive = request.form.get('ht10jam12_give')
    ht10jam13_receive = request.form.get('ht10jam13_give')
    ht10jam14_receive = request.form.get('ht10jam14_give')
    ht10jam15_receive = request.form.get('ht10jam15_give')
    ht10jam16_receive = request.form.get('ht10jam16_give')
    ht10jam17_receive = request.form.get('ht10jam17_give')
    ht10jam18_receive = request.form.get('ht10jam18_give')
    ht10jam19_receive = request.form.get('ht10jam19_give')
    ht10jam20_receive = request.form.get('ht10jam20_give')
    ht10jam21_receive = request.form.get('ht10jam21_give')
    ht10jam22_receive = request.form.get('ht10jam22_give')
    ht10jam23_receive = request.form.get('ht10jam23_give')
    ht10jam24_receive = request.form.get('ht10jam24_give')
    
    ht11jam1_receive = request.form.get('ht11jam1_give')
    ht11jam2_receive = request.form.get('ht11jam2_give')
    ht11jam3_receive = request.form.get('ht11jam3_give')
    ht11jam4_receive = request.form.get('ht11jam4_give')
    ht11jam5_receive = request.form.get('ht11jam5_give')
    ht11jam6_receive = request.form.get('ht11jam6_give')
    ht11jam7_receive = request.form.get('ht11jam7_give')
    ht11jam8_receive = request.form.get('ht11jam8_give')
    ht11jam9_receive = request.form.get('ht11jam9_give')
    ht11jam10_receive = request.form.get('ht11jam10_give')
    ht11jam11_receive = request.form.get('ht11jam11_give')
    ht11jam12_receive = request.form.get('ht11jam12_give')
    ht11jam13_receive = request.form.get('ht11jam13_give')
    ht11jam14_receive = request.form.get('ht11jam14_give')
    ht11jam15_receive = request.form.get('ht11jam15_give')
    ht11jam16_receive = request.form.get('ht11jam16_give')
    ht11jam17_receive = request.form.get('ht11jam17_give')
    ht11jam18_receive = request.form.get('ht11jam18_give')
    ht11jam19_receive = request.form.get('ht11jam19_give')
    ht11jam20_receive = request.form.get('ht11jam20_give')
    ht11jam21_receive = request.form.get('ht11jam21_give')
    ht11jam22_receive = request.form.get('ht11jam22_give')
    ht11jam23_receive = request.form.get('ht11jam23_give')
    ht11jam24_receive = request.form.get('ht11jam24_give')
    
    ht12jam1_receive = request.form.get('ht12jam1_give')
    ht12jam2_receive = request.form.get('ht12jam2_give')
    ht12jam3_receive = request.form.get('ht12jam3_give')
    ht12jam4_receive = request.form.get('ht12jam4_give')
    ht12jam5_receive = request.form.get('ht12jam5_give')
    ht12jam6_receive = request.form.get('ht12jam6_give')
    ht12jam7_receive = request.form.get('ht12jam7_give')
    ht12jam8_receive = request.form.get('ht12jam8_give')
    ht12jam9_receive = request.form.get('ht12jam9_give')
    ht12jam10_receive = request.form.get('ht12jam10_give')
    ht12jam11_receive = request.form.get('ht12jam11_give')
    ht12jam12_receive = request.form.get('ht12jam12_give')
    ht12jam13_receive = request.form.get('ht12jam13_give')
    ht12jam14_receive = request.form.get('ht12jam14_give')
    ht12jam15_receive = request.form.get('ht12jam15_give')
    ht12jam16_receive = request.form.get('ht12jam16_give')
    ht12jam17_receive = request.form.get('ht12jam17_give')
    ht12jam18_receive = request.form.get('ht12jam18_give')
    ht12jam19_receive = request.form.get('ht12jam19_give')
    ht12jam20_receive = request.form.get('ht12jam20_give')
    ht12jam21_receive = request.form.get('ht12jam21_give')
    ht12jam22_receive = request.form.get('ht12jam22_give')
    ht12jam23_receive = request.form.get('ht12jam23_give')
    ht12jam24_receive = request.form.get('ht12jam24_give')
    
    ht13jam1_receive = request.form.get('ht13jam1_give')
    ht13jam2_receive = request.form.get('ht13jam2_give')
    ht13jam3_receive = request.form.get('ht13jam3_give')
    ht13jam4_receive = request.form.get('ht13jam4_give')
    ht13jam5_receive = request.form.get('ht13jam5_give')
    ht13jam6_receive = request.form.get('ht13jam6_give')
    ht13jam7_receive = request.form.get('ht13jam7_give')
    ht13jam8_receive = request.form.get('ht13jam8_give')
    ht13jam9_receive = request.form.get('ht13jam9_give')
    ht13jam10_receive = request.form.get('ht13jam10_give')
    ht13jam11_receive = request.form.get('ht13jam11_give')
    ht13jam12_receive = request.form.get('ht13jam12_give')
    ht13jam13_receive = request.form.get('ht13jam13_give')
    ht13jam14_receive = request.form.get('ht13jam14_give')
    ht13jam15_receive = request.form.get('ht13jam15_give')
    ht13jam16_receive = request.form.get('ht13jam16_give')
    ht13jam17_receive = request.form.get('ht13jam17_give')
    ht13jam18_receive = request.form.get('ht13jam18_give')
    ht13jam19_receive = request.form.get('ht13jam19_give')
    ht13jam20_receive = request.form.get('ht13jam20_give')
    ht13jam21_receive = request.form.get('ht13jam21_give')
    ht13jam22_receive = request.form.get('ht13jam22_give')
    ht13jam23_receive = request.form.get('ht13jam23_give')
    ht13jam24_receive = request.form.get('ht13jam24_give')
    
    ht14jam1_receive = request.form.get('ht14jam1_give')
    ht14jam2_receive = request.form.get('ht14jam2_give')
    ht14jam3_receive = request.form.get('ht14jam3_give')
    ht14jam4_receive = request.form.get('ht14jam4_give')
    ht14jam5_receive = request.form.get('ht14jam5_give')
    ht14jam6_receive = request.form.get('ht14jam6_give')
    ht14jam7_receive = request.form.get('ht14jam7_give')
    ht14jam8_receive = request.form.get('ht14jam8_give')
    ht14jam9_receive = request.form.get('ht14jam9_give')
    ht14jam10_receive = request.form.get('ht14jam10_give')
    ht14jam11_receive = request.form.get('ht14jam11_give')
    ht14jam12_receive = request.form.get('ht14jam12_give')
    ht14jam13_receive = request.form.get('ht14jam13_give')
    ht14jam14_receive = request.form.get('ht14jam14_give')
    ht14jam15_receive = request.form.get('ht14jam15_give')
    ht14jam16_receive = request.form.get('ht14jam16_give')
    ht14jam17_receive = request.form.get('ht14jam17_give')
    ht14jam18_receive = request.form.get('ht14jam18_give')
    ht14jam19_receive = request.form.get('ht14jam19_give')
    ht14jam20_receive = request.form.get('ht14jam20_give')
    ht14jam21_receive = request.form.get('ht14jam21_give')
    ht14jam22_receive = request.form.get('ht14jam22_give')
    ht14jam23_receive = request.form.get('ht14jam23_give')
    ht14jam24_receive = request.form.get('ht14jam24_give')
    
    ht15jam1_receive = request.form.get('ht15jam1_give')
    ht15jam2_receive = request.form.get('ht15jam2_give')
    ht15jam3_receive = request.form.get('ht15jam3_give')
    ht15jam4_receive = request.form.get('ht15jam4_give')
    ht15jam5_receive = request.form.get('ht15jam5_give')
    ht15jam6_receive = request.form.get('ht15jam6_give')
    ht15jam7_receive = request.form.get('ht15jam7_give')
    ht15jam8_receive = request.form.get('ht15jam8_give')
    ht15jam9_receive = request.form.get('ht15jam9_give')
    ht15jam10_receive = request.form.get('ht15jam10_give')
    ht15jam11_receive = request.form.get('ht15jam11_give')
    ht15jam12_receive = request.form.get('ht15jam12_give')
    ht15jam13_receive = request.form.get('ht15jam13_give')
    ht15jam14_receive = request.form.get('ht15jam14_give')
    ht15jam15_receive = request.form.get('ht15jam15_give')
    ht15jam16_receive = request.form.get('ht15jam16_give')
    ht15jam17_receive = request.form.get('ht15jam17_give')
    ht15jam18_receive = request.form.get('ht15jam18_give')
    ht15jam19_receive = request.form.get('ht15jam19_give')
    ht15jam20_receive = request.form.get('ht15jam20_give')
    ht15jam21_receive = request.form.get('ht15jam21_give')
    ht15jam22_receive = request.form.get('ht15jam22_give')
    ht15jam23_receive = request.form.get('ht15jam23_give')
    ht15jam24_receive = request.form.get('ht15jam24_give')
    
    ht16jam1_receive = request.form.get('ht16jam1_give')
    ht16jam2_receive = request.form.get('ht16jam2_give')
    ht16jam3_receive = request.form.get('ht16jam3_give')
    ht16jam4_receive = request.form.get('ht16jam4_give')
    ht16jam5_receive = request.form.get('ht16jam5_give')
    ht16jam6_receive = request.form.get('ht16jam6_give')
    ht16jam7_receive = request.form.get('ht16jam7_give')
    ht16jam8_receive = request.form.get('ht16jam8_give')
    ht16jam9_receive = request.form.get('ht16jam9_give')
    ht16jam10_receive = request.form.get('ht16jam10_give')
    ht16jam11_receive = request.form.get('ht16jam11_give')
    ht16jam12_receive = request.form.get('ht16jam12_give')
    ht16jam13_receive = request.form.get('ht16jam13_give')
    ht16jam14_receive = request.form.get('ht16jam14_give')
    ht16jam15_receive = request.form.get('ht16jam15_give')
    ht16jam16_receive = request.form.get('ht16jam16_give')
    ht16jam17_receive = request.form.get('ht16jam17_give')
    ht16jam18_receive = request.form.get('ht16jam18_give')
    ht16jam19_receive = request.form.get('ht16jam19_give')
    ht16jam20_receive = request.form.get('ht16jam20_give')
    ht16jam21_receive = request.form.get('ht16jam21_give')
    ht16jam22_receive = request.form.get('ht16jam22_give')
    ht16jam23_receive = request.form.get('ht16jam23_give')
    ht16jam24_receive = request.form.get('ht16jam24_give')
    
    ht17jam1_receive = request.form.get('ht17jam1_give')
    ht17jam2_receive = request.form.get('ht17jam2_give')
    ht17jam3_receive = request.form.get('ht17jam3_give')
    ht17jam4_receive = request.form.get('ht17jam4_give')
    ht17jam5_receive = request.form.get('ht17jam5_give')
    ht17jam6_receive = request.form.get('ht17jam6_give')
    ht17jam7_receive = request.form.get('ht17jam7_give')
    ht17jam8_receive = request.form.get('ht17jam8_give')
    ht17jam9_receive = request.form.get('ht17jam9_give')
    ht17jam10_receive = request.form.get('ht17jam10_give')
    ht17jam11_receive = request.form.get('ht17jam11_give')
    ht17jam12_receive = request.form.get('ht17jam12_give')
    ht17jam13_receive = request.form.get('ht17jam13_give')
    ht17jam14_receive = request.form.get('ht17jam14_give')
    ht17jam15_receive = request.form.get('ht17jam15_give')
    ht17jam16_receive = request.form.get('ht17jam16_give')
    ht17jam17_receive = request.form.get('ht17jam17_give')
    ht17jam18_receive = request.form.get('ht17jam18_give')
    ht17jam19_receive = request.form.get('ht17jam19_give')
    ht17jam20_receive = request.form.get('ht17jam20_give')
    ht17jam21_receive = request.form.get('ht17jam21_give')
    ht17jam22_receive = request.form.get('ht17jam22_give')
    ht17jam23_receive = request.form.get('ht17jam23_give')
    ht17jam24_receive = request.form.get('ht17jam24_give')
    
    ht18jam1_receive = request.form.get('ht18jam1_give')
    ht18jam2_receive = request.form.get('ht18jam2_give')
    ht18jam3_receive = request.form.get('ht18jam3_give')
    ht18jam4_receive = request.form.get('ht18jam4_give')
    ht18jam5_receive = request.form.get('ht18jam5_give')
    ht18jam6_receive = request.form.get('ht18jam6_give')
    ht18jam7_receive = request.form.get('ht18jam7_give')
    ht18jam8_receive = request.form.get('ht18jam8_give')
    ht18jam9_receive = request.form.get('ht18jam9_give')
    ht18jam10_receive = request.form.get('ht18jam10_give')
    ht18jam11_receive = request.form.get('ht18jam11_give')
    ht18jam12_receive = request.form.get('ht18jam12_give')
    ht18jam13_receive = request.form.get('ht18jam13_give')
    ht18jam14_receive = request.form.get('ht18jam14_give')
    ht18jam15_receive = request.form.get('ht18jam15_give')
    ht18jam16_receive = request.form.get('ht18jam16_give')
    ht18jam17_receive = request.form.get('ht18jam17_give')
    ht18jam18_receive = request.form.get('ht18jam18_give')
    ht18jam19_receive = request.form.get('ht18jam19_give')
    ht18jam20_receive = request.form.get('ht18jam20_give')
    ht18jam21_receive = request.form.get('ht18jam21_give')
    ht18jam22_receive = request.form.get('ht18jam22_give')
    ht18jam23_receive = request.form.get('ht18jam23_give')
    ht18jam24_receive = request.form.get('ht18jam24_give')
    
    ht19jam1_receive = request.form.get('ht19jam1_give')
    ht19jam2_receive = request.form.get('ht19jam2_give')
    ht19jam3_receive = request.form.get('ht19jam3_give')
    ht19jam4_receive = request.form.get('ht19jam4_give')
    ht19jam5_receive = request.form.get('ht19jam5_give')
    ht19jam6_receive = request.form.get('ht19jam6_give')
    ht19jam7_receive = request.form.get('ht19jam7_give')
    ht19jam8_receive = request.form.get('ht19jam8_give')
    ht19jam9_receive = request.form.get('ht19jam9_give')
    ht19jam10_receive = request.form.get('ht19jam10_give')
    ht19jam11_receive = request.form.get('ht19jam11_give')
    ht19jam12_receive = request.form.get('ht19jam12_give')
    ht19jam13_receive = request.form.get('ht19jam13_give')
    ht19jam14_receive = request.form.get('ht19jam14_give')
    ht19jam15_receive = request.form.get('ht19jam15_give')
    ht19jam16_receive = request.form.get('ht19jam16_give')
    ht19jam17_receive = request.form.get('ht19jam17_give')
    ht19jam18_receive = request.form.get('ht19jam18_give')
    ht19jam19_receive = request.form.get('ht19jam19_give')
    ht19jam20_receive = request.form.get('ht19jam20_give')
    ht19jam21_receive = request.form.get('ht19jam21_give')
    ht19jam22_receive = request.form.get('ht19jam22_give')
    ht19jam23_receive = request.form.get('ht19jam23_give')
    ht19jam24_receive = request.form.get('ht19jam24_give')
    
    ht20jam1_receive = request.form.get('ht20jam1_give')
    ht20jam2_receive = request.form.get('ht20jam2_give')
    ht20jam3_receive = request.form.get('ht20jam3_give')
    ht20jam4_receive = request.form.get('ht20jam4_give')
    ht20jam5_receive = request.form.get('ht20jam5_give')
    ht20jam6_receive = request.form.get('ht20jam6_give')
    ht20jam7_receive = request.form.get('ht20jam7_give')
    ht20jam8_receive = request.form.get('ht20jam8_give')
    ht20jam9_receive = request.form.get('ht20jam9_give')
    ht20jam10_receive = request.form.get('ht20jam10_give')
    ht20jam11_receive = request.form.get('ht20jam11_give')
    ht20jam12_receive = request.form.get('ht20jam12_give')
    ht20jam13_receive = request.form.get('ht20jam13_give')
    ht20jam14_receive = request.form.get('ht20jam14_give')
    ht20jam15_receive = request.form.get('ht20jam15_give')
    ht20jam16_receive = request.form.get('ht20jam16_give')
    ht20jam17_receive = request.form.get('ht20jam17_give')
    ht20jam18_receive = request.form.get('ht20jam18_give')
    ht20jam19_receive = request.form.get('ht20jam19_give')
    ht20jam20_receive = request.form.get('ht20jam20_give')
    ht20jam21_receive = request.form.get('ht20jam21_give')
    ht20jam22_receive = request.form.get('ht20jam22_give')
    ht20jam23_receive = request.form.get('ht20jam23_give')
    ht20jam24_receive = request.form.get('ht20jam24_give')
    
    ht21jam1_receive = request.form.get('ht21jam1_give')
    ht21jam2_receive = request.form.get('ht21jam2_give')
    ht21jam3_receive = request.form.get('ht21jam3_give')
    ht21jam4_receive = request.form.get('ht21jam4_give')
    ht21jam5_receive = request.form.get('ht21jam5_give')
    ht21jam6_receive = request.form.get('ht21jam6_give')
    ht21jam7_receive = request.form.get('ht21jam7_give')
    ht21jam8_receive = request.form.get('ht21jam8_give')
    ht21jam9_receive = request.form.get('ht21jam9_give')
    ht21jam10_receive = request.form.get('ht21jam10_give')
    ht21jam11_receive = request.form.get('ht21jam11_give')
    ht21jam12_receive = request.form.get('ht21jam12_give')
    ht21jam13_receive = request.form.get('ht21jam13_give')
    ht21jam14_receive = request.form.get('ht21jam14_give')
    ht21jam15_receive = request.form.get('ht21jam15_give')
    ht21jam16_receive = request.form.get('ht21jam16_give')
    ht21jam17_receive = request.form.get('ht21jam17_give')
    ht21jam18_receive = request.form.get('ht21jam18_give')
    ht21jam19_receive = request.form.get('ht21jam19_give')
    ht21jam20_receive = request.form.get('ht21jam20_give')
    ht21jam21_receive = request.form.get('ht21jam21_give')
    ht21jam22_receive = request.form.get('ht21jam22_give')
    ht21jam23_receive = request.form.get('ht21jam23_give')
    ht21jam24_receive = request.form.get('ht21jam24_give')
    
    ht22jam1_receive = request.form.get('ht22jam1_give')
    ht22jam2_receive = request.form.get('ht22jam2_give')
    ht22jam3_receive = request.form.get('ht22jam3_give')
    ht22jam4_receive = request.form.get('ht22jam4_give')
    ht22jam5_receive = request.form.get('ht22jam5_give')
    ht22jam6_receive = request.form.get('ht22jam6_give')
    ht22jam7_receive = request.form.get('ht22jam7_give')
    ht22jam8_receive = request.form.get('ht22jam8_give')
    ht22jam9_receive = request.form.get('ht22jam9_give')
    ht22jam10_receive = request.form.get('ht22jam10_give')
    ht22jam11_receive = request.form.get('ht22jam11_give')
    ht22jam12_receive = request.form.get('ht22jam12_give')
    ht22jam13_receive = request.form.get('ht22jam13_give')
    ht22jam14_receive = request.form.get('ht22jam14_give')
    ht22jam15_receive = request.form.get('ht22jam15_give')
    ht22jam16_receive = request.form.get('ht22jam16_give')
    ht22jam17_receive = request.form.get('ht22jam17_give')
    ht22jam18_receive = request.form.get('ht22jam18_give')
    ht22jam19_receive = request.form.get('ht22jam19_give')
    ht22jam20_receive = request.form.get('ht22jam20_give')
    ht22jam21_receive = request.form.get('ht22jam21_give')
    ht22jam22_receive = request.form.get('ht22jam22_give')
    ht22jam23_receive = request.form.get('ht22jam23_give')
    ht22jam24_receive = request.form.get('ht22jam24_give')
    
    ht23jam1_receive = request.form.get('ht23jam1_give')
    ht23jam2_receive = request.form.get('ht23jam2_give')
    ht23jam3_receive = request.form.get('ht23jam3_give')
    ht23jam4_receive = request.form.get('ht23jam4_give')
    ht23jam5_receive = request.form.get('ht23jam5_give')
    ht23jam6_receive = request.form.get('ht23jam6_give')
    ht23jam7_receive = request.form.get('ht23jam7_give')
    ht23jam8_receive = request.form.get('ht23jam8_give')
    ht23jam9_receive = request.form.get('ht23jam9_give')
    ht23jam10_receive = request.form.get('ht23jam10_give')
    ht23jam11_receive = request.form.get('ht23jam11_give')
    ht23jam12_receive = request.form.get('ht23jam12_give')
    ht23jam13_receive = request.form.get('ht23jam13_give')
    ht23jam14_receive = request.form.get('ht23jam14_give')
    ht23jam15_receive = request.form.get('ht23jam15_give')
    ht23jam16_receive = request.form.get('ht23jam16_give')
    ht23jam17_receive = request.form.get('ht23jam17_give')
    ht23jam18_receive = request.form.get('ht23jam18_give')
    ht23jam19_receive = request.form.get('ht23jam19_give')
    ht23jam20_receive = request.form.get('ht23jam20_give')
    ht23jam21_receive = request.form.get('ht23jam21_give')
    ht23jam22_receive = request.form.get('ht23jam22_give')
    ht23jam23_receive = request.form.get('ht23jam23_give')
    ht23jam24_receive = request.form.get('ht23jam24_give')
    
    ht24jam1_receive = request.form.get('ht24jam1_give')
    ht24jam2_receive = request.form.get('ht24jam2_give')
    ht24jam3_receive = request.form.get('ht24jam3_give')
    ht24jam4_receive = request.form.get('ht24jam4_give')
    ht24jam5_receive = request.form.get('ht24jam5_give')
    ht24jam6_receive = request.form.get('ht24jam6_give')
    ht24jam7_receive = request.form.get('ht24jam7_give')
    ht24jam8_receive = request.form.get('ht24jam8_give')
    ht24jam9_receive = request.form.get('ht24jam9_give')
    ht24jam10_receive = request.form.get('ht24jam10_give')
    ht24jam11_receive = request.form.get('ht24jam11_give')
    ht24jam12_receive = request.form.get('ht24jam12_give')
    ht24jam13_receive = request.form.get('ht24jam13_give')
    ht24jam14_receive = request.form.get('ht24jam14_give')
    ht24jam15_receive = request.form.get('ht24jam15_give')
    ht24jam16_receive = request.form.get('ht24jam16_give')
    ht24jam17_receive = request.form.get('ht24jam17_give')
    ht24jam18_receive = request.form.get('ht24jam18_give')
    ht24jam19_receive = request.form.get('ht24jam19_give')
    ht24jam20_receive = request.form.get('ht24jam20_give')
    ht24jam21_receive = request.form.get('ht24jam21_give')
    ht24jam22_receive = request.form.get('ht24jam22_give')
    ht24jam23_receive = request.form.get('ht24jam23_give')
    ht24jam24_receive = request.form.get('ht24jam24_give')
    
    ht25jam1_receive = request.form.get('ht25jam1_give')
    ht25jam2_receive = request.form.get('ht25jam2_give')
    ht25jam3_receive = request.form.get('ht25jam3_give')
    ht25jam4_receive = request.form.get('ht25jam4_give')
    ht25jam5_receive = request.form.get('ht25jam5_give')
    ht25jam6_receive = request.form.get('ht25jam6_give')
    ht25jam7_receive = request.form.get('ht25jam7_give')
    ht25jam8_receive = request.form.get('ht25jam8_give')
    ht25jam9_receive = request.form.get('ht25jam9_give')
    ht25jam10_receive = request.form.get('ht25jam10_give')
    ht25jam11_receive = request.form.get('ht25jam11_give')
    ht25jam12_receive = request.form.get('ht25jam12_give')
    ht25jam13_receive = request.form.get('ht25jam13_give')
    ht25jam14_receive = request.form.get('ht25jam14_give')
    ht25jam15_receive = request.form.get('ht25jam15_give')
    ht25jam16_receive = request.form.get('ht25jam16_give')
    ht25jam17_receive = request.form.get('ht25jam17_give')
    ht25jam18_receive = request.form.get('ht25jam18_give')
    ht25jam19_receive = request.form.get('ht25jam19_give')
    ht25jam20_receive = request.form.get('ht25jam20_give')
    ht25jam21_receive = request.form.get('ht25jam21_give')
    ht25jam22_receive = request.form.get('ht25jam22_give')
    ht25jam23_receive = request.form.get('ht25jam23_give')
    ht25jam24_receive = request.form.get('ht25jam24_give')
    
    ht26jam1_receive = request.form.get('ht26jam1_give')
    ht26jam2_receive = request.form.get('ht26jam2_give')
    ht26jam3_receive = request.form.get('ht26jam3_give')
    ht26jam4_receive = request.form.get('ht26jam4_give')
    ht26jam5_receive = request.form.get('ht26jam5_give')
    ht26jam6_receive = request.form.get('ht26jam6_give')
    ht26jam7_receive = request.form.get('ht26jam7_give')
    ht26jam8_receive = request.form.get('ht26jam8_give')
    ht26jam9_receive = request.form.get('ht26jam9_give')
    ht26jam10_receive = request.form.get('ht26jam10_give')
    ht26jam11_receive = request.form.get('ht26jam11_give')
    ht26jam12_receive = request.form.get('ht26jam12_give')
    ht26jam13_receive = request.form.get('ht26jam13_give')
    ht26jam14_receive = request.form.get('ht26jam14_give')
    ht26jam15_receive = request.form.get('ht26jam15_give')
    ht26jam16_receive = request.form.get('ht26jam16_give')
    ht26jam17_receive = request.form.get('ht26jam17_give')
    ht26jam18_receive = request.form.get('ht26jam18_give')
    ht26jam19_receive = request.form.get('ht26jam19_give')
    ht26jam20_receive = request.form.get('ht26jam20_give')
    ht26jam21_receive = request.form.get('ht26jam21_give')
    ht26jam22_receive = request.form.get('ht26jam22_give')
    ht26jam23_receive = request.form.get('ht26jam23_give')
    ht26jam24_receive = request.form.get('ht26jam24_give')
    
    ht27jam1_receive = request.form.get('ht27jam1_give')
    ht27jam2_receive = request.form.get('ht27jam2_give')
    ht27jam3_receive = request.form.get('ht27jam3_give')
    ht27jam4_receive = request.form.get('ht27jam4_give')
    ht27jam5_receive = request.form.get('ht27jam5_give')
    ht27jam6_receive = request.form.get('ht27jam6_give')
    ht27jam7_receive = request.form.get('ht27jam7_give')
    ht27jam8_receive = request.form.get('ht27jam8_give')
    ht27jam9_receive = request.form.get('ht27jam9_give')
    ht27jam10_receive = request.form.get('ht27jam10_give')
    ht27jam11_receive = request.form.get('ht27jam11_give')
    ht27jam12_receive = request.form.get('ht27jam12_give')
    ht27jam13_receive = request.form.get('ht27jam13_give')
    ht27jam14_receive = request.form.get('ht27jam14_give')
    ht27jam15_receive = request.form.get('ht27jam15_give')
    ht27jam16_receive = request.form.get('ht27jam16_give')
    ht27jam17_receive = request.form.get('ht27jam17_give')
    ht27jam18_receive = request.form.get('ht27jam18_give')
    ht27jam19_receive = request.form.get('ht27jam19_give')
    ht27jam20_receive = request.form.get('ht27jam20_give')
    ht27jam21_receive = request.form.get('ht27jam21_give')
    ht27jam22_receive = request.form.get('ht27jam22_give')
    ht27jam23_receive = request.form.get('ht27jam23_give')
    ht27jam24_receive = request.form.get('ht27jam24_give')

    breakdown_receive = request.form.get('breakdown_give')
    corrective_receive = request.form.get('corrective_give')
    preventive_receive = request.form.get('preventive_give')
    accident_receive = request.form.get('accident_give')
    remark_receive = request.form.get('remark_give')

    doc = {
        'unit': unit_receive,
        'tanggal': tanggal_receive,

        'ht01jam1': ht01jam1_receive,
        'ht01jam2': ht01jam2_receive,
        'ht01jam3': ht01jam3_receive,
        'ht01jam4': ht01jam4_receive,
        'ht01jam5': ht01jam5_receive,
        'ht01jam6': ht01jam6_receive,
        'ht01jam7': ht01jam7_receive,
        'ht01jam8': ht01jam8_receive,
        'ht01jam9': ht01jam9_receive,
        'ht01jam10': ht01jam10_receive,
        'ht01jam11': ht01jam11_receive,
        'ht01jam12': ht01jam12_receive,
        'ht01jam13': ht01jam13_receive,
        'ht01jam14': ht01jam14_receive,
        'ht01jam15': ht01jam15_receive,
        'ht01jam16': ht01jam16_receive,
        'ht01jam17': ht01jam17_receive,
        'ht01jam18': ht01jam18_receive,
        'ht01jam19': ht01jam19_receive,
        'ht01jam20': ht01jam20_receive,
        'ht01jam21': ht01jam21_receive,
        'ht01jam22': ht01jam22_receive,
        'ht01jam23': ht01jam23_receive,
        'ht01jam24': ht01jam24_receive,
        
        'ht02jam1': ht02jam1_receive,
        'ht02jam2': ht02jam2_receive,
        'ht02jam3': ht02jam3_receive,
        'ht02jam4': ht02jam4_receive,
        'ht02jam5': ht02jam5_receive,
        'ht02jam6': ht02jam6_receive,
        'ht02jam7': ht02jam7_receive,
        'ht02jam8': ht02jam8_receive,
        'ht02jam9': ht02jam9_receive,
        'ht02jam10': ht02jam10_receive,
        'ht02jam11': ht02jam11_receive,
        'ht02jam12': ht02jam12_receive,
        'ht02jam13': ht02jam13_receive,
        'ht02jam14': ht02jam14_receive,
        'ht02jam15': ht02jam15_receive,
        'ht02jam16': ht02jam16_receive,
        'ht02jam17': ht02jam17_receive,
        'ht02jam18': ht02jam18_receive,
        'ht02jam19': ht02jam19_receive,
        'ht02jam20': ht02jam20_receive,
        'ht02jam21': ht02jam21_receive,
        'ht02jam22': ht02jam22_receive,
        'ht02jam23': ht02jam23_receive,
        'ht02jam24': ht02jam24_receive,
        
        'ht03jam1': ht03jam1_receive,
        'ht03jam2': ht03jam2_receive,
        'ht03jam3': ht03jam3_receive,
        'ht03jam4': ht03jam4_receive,
        'ht03jam5': ht03jam5_receive,
        'ht03jam6': ht03jam6_receive,
        'ht03jam7': ht03jam7_receive,
        'ht03jam8': ht03jam8_receive,
        'ht03jam9': ht03jam9_receive,
        'ht03jam10': ht03jam10_receive,
        'ht03jam11': ht03jam11_receive,
        'ht03jam12': ht03jam12_receive,
        'ht03jam13': ht03jam13_receive,
        'ht03jam14': ht03jam14_receive,
        'ht03jam15': ht03jam15_receive,
        'ht03jam16': ht03jam16_receive,
        'ht03jam17': ht03jam17_receive,
        'ht03jam18': ht03jam18_receive,
        'ht03jam19': ht03jam19_receive,
        'ht03jam20': ht03jam20_receive,
        'ht03jam21': ht03jam21_receive,
        'ht03jam22': ht03jam22_receive,
        'ht03jam23': ht03jam23_receive,
        'ht03jam24': ht03jam24_receive,
        
        'ht04jam1': ht04jam1_receive,
        'ht04jam2': ht04jam2_receive,
        'ht04jam3': ht04jam3_receive,
        'ht04jam4': ht04jam4_receive,
        'ht04jam5': ht04jam5_receive,
        'ht04jam6': ht04jam6_receive,
        'ht04jam7': ht04jam7_receive,
        'ht04jam8': ht04jam8_receive,
        'ht04jam9': ht04jam9_receive,
        'ht04jam10': ht04jam10_receive,
        'ht04jam11': ht04jam11_receive,
        'ht04jam12': ht04jam12_receive,
        'ht04jam13': ht04jam13_receive,
        'ht04jam14': ht04jam14_receive,
        'ht04jam15': ht04jam15_receive,
        'ht04jam16': ht04jam16_receive,
        'ht04jam17': ht04jam17_receive,
        'ht04jam18': ht04jam18_receive,
        'ht04jam19': ht04jam19_receive,
        'ht04jam20': ht04jam20_receive,
        'ht04jam21': ht04jam21_receive,
        'ht04jam22': ht04jam22_receive,
        'ht04jam23': ht04jam23_receive,
        'ht04jam24': ht04jam24_receive,
        
        'ht05jam1': ht05jam1_receive,
        'ht05jam2': ht05jam2_receive,
        'ht05jam3': ht05jam3_receive,
        'ht05jam4': ht05jam4_receive,
        'ht05jam5': ht05jam5_receive,
        'ht05jam6': ht05jam6_receive,
        'ht05jam7': ht05jam7_receive,
        'ht05jam8': ht05jam8_receive,
        'ht05jam9': ht05jam9_receive,
        'ht05jam10': ht05jam10_receive,
        'ht05jam11': ht05jam11_receive,
        'ht05jam12': ht05jam12_receive,
        'ht05jam13': ht05jam13_receive,
        'ht05jam14': ht05jam14_receive,
        'ht05jam15': ht05jam15_receive,
        'ht05jam16': ht05jam16_receive,
        'ht05jam17': ht05jam17_receive,
        'ht05jam18': ht05jam18_receive,
        'ht05jam19': ht05jam19_receive,
        'ht05jam20': ht05jam20_receive,
        'ht05jam21': ht05jam21_receive,
        'ht05jam22': ht05jam22_receive,
        'ht05jam23': ht05jam23_receive,
        'ht05jam24': ht05jam24_receive,
        
        'ht06jam1': ht06jam1_receive,
        'ht06jam2': ht06jam2_receive,
        'ht06jam3': ht06jam3_receive,
        'ht06jam4': ht06jam4_receive,
        'ht06jam5': ht06jam5_receive,
        'ht06jam6': ht06jam6_receive,
        'ht06jam7': ht06jam7_receive,
        'ht06jam8': ht06jam8_receive,
        'ht06jam9': ht06jam9_receive,
        'ht06jam10': ht06jam10_receive,
        'ht06jam11': ht06jam11_receive,
        'ht06jam12': ht06jam12_receive,
        'ht06jam13': ht06jam13_receive,
        'ht06jam14': ht06jam14_receive,
        'ht06jam15': ht06jam15_receive,
        'ht06jam16': ht06jam16_receive,
        'ht06jam17': ht06jam17_receive,
        'ht06jam18': ht06jam18_receive,
        'ht06jam19': ht06jam19_receive,
        'ht06jam20': ht06jam20_receive,
        'ht06jam21': ht06jam21_receive,
        'ht06jam22': ht06jam22_receive,
        'ht06jam23': ht06jam23_receive,
        'ht06jam24': ht06jam24_receive,
        
        'ht07jam1': ht07jam1_receive,
        'ht07jam2': ht07jam2_receive,
        'ht07jam3': ht07jam3_receive,
        'ht07jam4': ht07jam4_receive,
        'ht07jam5': ht07jam5_receive,
        'ht07jam6': ht07jam6_receive,
        'ht07jam7': ht07jam7_receive,
        'ht07jam8': ht07jam8_receive,
        'ht07jam9': ht07jam9_receive,
        'ht07jam10': ht07jam10_receive,
        'ht07jam11': ht07jam11_receive,
        'ht07jam12': ht07jam12_receive,
        'ht07jam13': ht07jam13_receive,
        'ht07jam14': ht07jam14_receive,
        'ht07jam15': ht07jam15_receive,
        'ht07jam16': ht07jam16_receive,
        'ht07jam17': ht07jam17_receive,
        'ht07jam18': ht07jam18_receive,
        'ht07jam19': ht07jam19_receive,
        'ht07jam20': ht07jam20_receive,
        'ht07jam21': ht07jam21_receive,
        'ht07jam22': ht07jam22_receive,
        'ht07jam23': ht07jam23_receive,
        'ht07jam24': ht07jam24_receive,
        
        'ht08jam1': ht08jam1_receive,
        'ht08jam2': ht08jam2_receive,
        'ht08jam3': ht08jam3_receive,
        'ht08jam4': ht08jam4_receive,
        'ht08jam5': ht08jam5_receive,
        'ht08jam6': ht08jam6_receive,
        'ht08jam7': ht08jam7_receive,
        'ht08jam8': ht08jam8_receive,
        'ht08jam9': ht08jam9_receive,
        'ht08jam10': ht08jam10_receive,
        'ht08jam11': ht08jam11_receive,
        'ht08jam12': ht08jam12_receive,
        'ht08jam13': ht08jam13_receive,
        'ht08jam14': ht08jam14_receive,
        'ht08jam15': ht08jam15_receive,
        'ht08jam16': ht08jam16_receive,
        'ht08jam17': ht08jam17_receive,
        'ht08jam18': ht08jam18_receive,
        'ht08jam19': ht08jam19_receive,
        'ht08jam20': ht08jam20_receive,
        'ht08jam21': ht08jam21_receive,
        'ht08jam22': ht08jam22_receive,
        'ht08jam23': ht08jam23_receive,
        'ht08jam24': ht08jam24_receive,
        
        'ht09jam1': ht09jam1_receive,
        'ht09jam2': ht09jam2_receive,
        'ht09jam3': ht09jam3_receive,
        'ht09jam4': ht09jam4_receive,
        'ht09jam5': ht09jam5_receive,
        'ht09jam6': ht09jam6_receive,
        'ht09jam7': ht09jam7_receive,
        'ht09jam8': ht09jam8_receive,
        'ht09jam9': ht09jam9_receive,
        'ht09jam10': ht09jam10_receive,
        'ht09jam11': ht09jam11_receive,
        'ht09jam12': ht09jam12_receive,
        'ht09jam13': ht09jam13_receive,
        'ht09jam14': ht09jam14_receive,
        'ht09jam15': ht09jam15_receive,
        'ht09jam16': ht09jam16_receive,
        'ht09jam17': ht09jam17_receive,
        'ht09jam18': ht09jam18_receive,
        'ht09jam19': ht09jam19_receive,
        'ht09jam20': ht09jam20_receive,
        'ht09jam21': ht09jam21_receive,
        'ht09jam22': ht09jam22_receive,
        'ht09jam23': ht09jam23_receive,
        'ht09jam24': ht09jam24_receive,
        
        'ht10jam1': ht10jam1_receive,
        'ht10jam2': ht10jam2_receive,
        'ht10jam3': ht10jam3_receive,
        'ht10jam4': ht10jam4_receive,
        'ht10jam5': ht10jam5_receive,
        'ht10jam6': ht10jam6_receive,
        'ht10jam7': ht10jam7_receive,
        'ht10jam8': ht10jam8_receive,
        'ht10jam9': ht10jam9_receive,
        'ht10jam10': ht10jam10_receive,
        'ht10jam11': ht10jam11_receive,
        'ht10jam12': ht10jam12_receive,
        'ht10jam13': ht10jam13_receive,
        'ht10jam14': ht10jam14_receive,
        'ht10jam15': ht10jam15_receive,
        'ht10jam16': ht10jam16_receive,
        'ht10jam17': ht10jam17_receive,
        'ht10jam18': ht10jam18_receive,
        'ht10jam19': ht10jam19_receive,
        'ht10jam20': ht10jam20_receive,
        'ht10jam21': ht10jam21_receive,
        'ht10jam22': ht10jam22_receive,
        'ht10jam23': ht10jam23_receive,
        'ht10jam24': ht10jam24_receive,
        
        'ht11jam1': ht11jam1_receive,
        'ht11jam2': ht11jam2_receive,
        'ht11jam3': ht11jam3_receive,
        'ht11jam4': ht11jam4_receive,
        'ht11jam5': ht11jam5_receive,
        'ht11jam6': ht11jam6_receive,
        'ht11jam7': ht11jam7_receive,
        'ht11jam8': ht11jam8_receive,
        'ht11jam9': ht11jam9_receive,
        'ht11jam10': ht11jam10_receive,
        'ht11jam11': ht11jam11_receive,
        'ht11jam12': ht11jam12_receive,
        'ht11jam13': ht11jam13_receive,
        'ht11jam14': ht11jam14_receive,
        'ht11jam15': ht11jam15_receive,
        'ht11jam16': ht11jam16_receive,
        'ht11jam17': ht11jam17_receive,
        'ht11jam18': ht11jam18_receive,
        'ht11jam19': ht11jam19_receive,
        'ht11jam20': ht11jam20_receive,
        'ht11jam21': ht11jam21_receive,
        'ht11jam22': ht11jam22_receive,
        'ht11jam23': ht11jam23_receive,
        'ht11jam24': ht11jam24_receive,
        
        'ht12jam1': ht12jam1_receive,
        'ht12jam2': ht12jam2_receive,
        'ht12jam3': ht12jam3_receive,
        'ht12jam4': ht12jam4_receive,
        'ht12jam5': ht12jam5_receive,
        'ht12jam6': ht12jam6_receive,
        'ht12jam7': ht12jam7_receive,
        'ht12jam8': ht12jam8_receive,
        'ht12jam9': ht12jam9_receive,
        'ht12jam10': ht12jam10_receive,
        'ht12jam11': ht12jam11_receive,
        'ht12jam12': ht12jam12_receive,
        'ht12jam13': ht12jam13_receive,
        'ht12jam14': ht12jam14_receive,
        'ht12jam15': ht12jam15_receive,
        'ht12jam16': ht12jam16_receive,
        'ht12jam17': ht12jam17_receive,
        'ht12jam18': ht12jam18_receive,
        'ht12jam19': ht12jam19_receive,
        'ht12jam20': ht12jam20_receive,
        'ht12jam21': ht12jam21_receive,
        'ht12jam22': ht12jam22_receive,
        'ht12jam23': ht12jam23_receive,
        'ht12jam24': ht12jam24_receive,
        
        'ht13jam1': ht13jam1_receive,
        'ht13jam2': ht13jam2_receive,
        'ht13jam3': ht13jam3_receive,
        'ht13jam4': ht13jam4_receive,
        'ht13jam5': ht13jam5_receive,
        'ht13jam6': ht13jam6_receive,
        'ht13jam7': ht13jam7_receive,
        'ht13jam8': ht13jam8_receive,
        'ht13jam9': ht13jam9_receive,
        'ht13jam10': ht13jam10_receive,
        'ht13jam11': ht13jam11_receive,
        'ht13jam12': ht13jam12_receive,
        'ht13jam13': ht13jam13_receive,
        'ht13jam14': ht13jam14_receive,
        'ht13jam15': ht13jam15_receive,
        'ht13jam16': ht13jam16_receive,
        'ht13jam17': ht13jam17_receive,
        'ht13jam18': ht13jam18_receive,
        'ht13jam19': ht13jam19_receive,
        'ht13jam20': ht13jam20_receive,
        'ht13jam21': ht13jam21_receive,
        'ht13jam22': ht13jam22_receive,
        'ht13jam23': ht13jam23_receive,
        'ht13jam24': ht13jam24_receive,
        
        'ht14jam1': ht14jam1_receive,
        'ht14jam2': ht14jam2_receive,
        'ht14jam3': ht14jam3_receive,
        'ht14jam4': ht14jam4_receive,
        'ht14jam5': ht14jam5_receive,
        'ht14jam6': ht14jam6_receive,
        'ht14jam7': ht14jam7_receive,
        'ht14jam8': ht14jam8_receive,
        'ht14jam9': ht14jam9_receive,
        'ht14jam10': ht14jam10_receive,
        'ht14jam11': ht14jam11_receive,
        'ht14jam12': ht14jam12_receive,
        'ht14jam13': ht14jam13_receive,
        'ht14jam14': ht14jam14_receive,
        'ht14jam15': ht14jam15_receive,
        'ht14jam16': ht14jam16_receive,
        'ht14jam17': ht14jam17_receive,
        'ht14jam18': ht14jam18_receive,
        'ht14jam19': ht14jam19_receive,
        'ht14jam20': ht14jam20_receive,
        'ht14jam21': ht14jam21_receive,
        'ht14jam22': ht14jam22_receive,
        'ht14jam23': ht14jam23_receive,
        'ht14jam24': ht14jam24_receive,
        
        'ht15jam1': ht15jam1_receive,
        'ht15jam2': ht15jam2_receive,
        'ht15jam3': ht15jam3_receive,
        'ht15jam4': ht15jam4_receive,
        'ht15jam5': ht15jam5_receive,
        'ht15jam6': ht15jam6_receive,
        'ht15jam7': ht15jam7_receive,
        'ht15jam8': ht15jam8_receive,
        'ht15jam9': ht15jam9_receive,
        'ht15jam10': ht15jam10_receive,
        'ht15jam11': ht15jam11_receive,
        'ht15jam12': ht15jam12_receive,
        'ht15jam13': ht15jam13_receive,
        'ht15jam14': ht15jam14_receive,
        'ht15jam15': ht15jam15_receive,
        'ht15jam16': ht15jam16_receive,
        'ht15jam17': ht15jam17_receive,
        'ht15jam18': ht15jam18_receive,
        'ht15jam19': ht15jam19_receive,
        'ht15jam20': ht15jam20_receive,
        'ht15jam21': ht15jam21_receive,
        'ht15jam22': ht15jam22_receive,
        'ht15jam23': ht15jam23_receive,
        'ht15jam24': ht15jam24_receive,
        
        'ht16jam1': ht16jam1_receive,
        'ht16jam2': ht16jam2_receive,
        'ht16jam3': ht16jam3_receive,
        'ht16jam4': ht16jam4_receive,
        'ht16jam5': ht16jam5_receive,
        'ht16jam6': ht16jam6_receive,
        'ht16jam7': ht16jam7_receive,
        'ht16jam8': ht16jam8_receive,
        'ht16jam9': ht16jam9_receive,
        'ht16jam10': ht16jam10_receive,
        'ht16jam11': ht16jam11_receive,
        'ht16jam12': ht16jam12_receive,
        'ht16jam13': ht16jam13_receive,
        'ht16jam14': ht16jam14_receive,
        'ht16jam15': ht16jam15_receive,
        'ht16jam16': ht16jam16_receive,
        'ht16jam17': ht16jam17_receive,
        'ht16jam18': ht16jam18_receive,
        'ht16jam19': ht16jam19_receive,
        'ht16jam20': ht16jam20_receive,
        'ht16jam21': ht16jam21_receive,
        'ht16jam22': ht16jam22_receive,
        'ht16jam23': ht16jam23_receive,
        'ht16jam24': ht16jam24_receive,
        
        'ht17jam1': ht17jam1_receive,
        'ht17jam2': ht17jam2_receive,
        'ht17jam3': ht17jam3_receive,
        'ht17jam4': ht17jam4_receive,
        'ht17jam5': ht17jam5_receive,
        'ht17jam6': ht17jam6_receive,
        'ht17jam7': ht17jam7_receive,
        'ht17jam8': ht17jam8_receive,
        'ht17jam9': ht17jam9_receive,
        'ht17jam10': ht17jam10_receive,
        'ht17jam11': ht17jam11_receive,
        'ht17jam12': ht17jam12_receive,
        'ht17jam13': ht17jam13_receive,
        'ht17jam14': ht17jam14_receive,
        'ht17jam15': ht17jam15_receive,
        'ht17jam16': ht17jam16_receive,
        'ht17jam17': ht17jam17_receive,
        'ht17jam18': ht17jam18_receive,
        'ht17jam19': ht17jam19_receive,
        'ht17jam20': ht17jam20_receive,
        'ht17jam21': ht17jam21_receive,
        'ht17jam22': ht17jam22_receive,
        'ht17jam23': ht17jam23_receive,
        'ht17jam24': ht17jam24_receive,
        
        'ht18jam1': ht18jam1_receive,
        'ht18jam2': ht18jam2_receive,
        'ht18jam3': ht18jam3_receive,
        'ht18jam4': ht18jam4_receive,
        'ht18jam5': ht18jam5_receive,
        'ht18jam6': ht18jam6_receive,
        'ht18jam7': ht18jam7_receive,
        'ht18jam8': ht18jam8_receive,
        'ht18jam9': ht18jam9_receive,
        'ht18jam10': ht18jam10_receive,
        'ht18jam11': ht18jam11_receive,
        'ht18jam12': ht18jam12_receive,
        'ht18jam13': ht18jam13_receive,
        'ht18jam14': ht18jam14_receive,
        'ht18jam15': ht18jam15_receive,
        'ht18jam16': ht18jam16_receive,
        'ht18jam17': ht18jam17_receive,
        'ht18jam18': ht18jam18_receive,
        'ht18jam19': ht18jam19_receive,
        'ht18jam20': ht18jam20_receive,
        'ht18jam21': ht18jam21_receive,
        'ht18jam22': ht18jam22_receive,
        'ht18jam23': ht18jam23_receive,
        'ht18jam24': ht18jam24_receive,
        
        'ht19jam1': ht19jam1_receive,
        'ht19jam2': ht19jam2_receive,
        'ht19jam3': ht19jam3_receive,
        'ht19jam4': ht19jam4_receive,
        'ht19jam5': ht19jam5_receive,
        'ht19jam6': ht19jam6_receive,
        'ht19jam7': ht19jam7_receive,
        'ht19jam8': ht19jam8_receive,
        'ht19jam9': ht19jam9_receive,
        'ht19jam10': ht19jam10_receive,
        'ht19jam11': ht19jam11_receive,
        'ht19jam12': ht19jam12_receive,
        'ht19jam13': ht19jam13_receive,
        'ht19jam14': ht19jam14_receive,
        'ht19jam15': ht19jam15_receive,
        'ht19jam16': ht19jam16_receive,
        'ht19jam17': ht19jam17_receive,
        'ht19jam18': ht19jam18_receive,
        'ht19jam19': ht19jam19_receive,
        'ht19jam20': ht19jam20_receive,
        'ht19jam21': ht19jam21_receive,
        'ht19jam22': ht19jam22_receive,
        'ht19jam23': ht19jam23_receive,
        'ht19jam24': ht19jam24_receive,
        
        'ht20jam1': ht20jam1_receive,
        'ht20jam2': ht20jam2_receive,
        'ht20jam3': ht20jam3_receive,
        'ht20jam4': ht20jam4_receive,
        'ht20jam5': ht20jam5_receive,
        'ht20jam6': ht20jam6_receive,
        'ht20jam7': ht20jam7_receive,
        'ht20jam8': ht20jam8_receive,
        'ht20jam9': ht20jam9_receive,
        'ht20jam10': ht20jam10_receive,
        'ht20jam11': ht20jam11_receive,
        'ht20jam12': ht20jam12_receive,
        'ht20jam13': ht20jam13_receive,
        'ht20jam14': ht20jam14_receive,
        'ht20jam15': ht20jam15_receive,
        'ht20jam16': ht20jam16_receive,
        'ht20jam17': ht20jam17_receive,
        'ht20jam18': ht20jam18_receive,
        'ht20jam19': ht20jam19_receive,
        'ht20jam20': ht20jam20_receive,
        'ht20jam21': ht20jam21_receive,
        'ht20jam22': ht20jam22_receive,
        'ht20jam23': ht20jam23_receive,
        'ht20jam24': ht20jam24_receive,
        
        'ht21jam1': ht21jam1_receive,
        'ht21jam2': ht21jam2_receive,
        'ht21jam3': ht21jam3_receive,
        'ht21jam4': ht21jam4_receive,
        'ht21jam5': ht21jam5_receive,
        'ht21jam6': ht21jam6_receive,
        'ht21jam7': ht21jam7_receive,
        'ht21jam8': ht21jam8_receive,
        'ht21jam9': ht21jam9_receive,
        'ht21jam10': ht21jam10_receive,
        'ht21jam11': ht21jam11_receive,
        'ht21jam12': ht21jam12_receive,
        'ht21jam13': ht21jam13_receive,
        'ht21jam14': ht21jam14_receive,
        'ht21jam15': ht21jam15_receive,
        'ht21jam16': ht21jam16_receive,
        'ht21jam17': ht21jam17_receive,
        'ht21jam18': ht21jam18_receive,
        'ht21jam19': ht21jam19_receive,
        'ht21jam20': ht21jam20_receive,
        'ht21jam21': ht21jam21_receive,
        'ht21jam22': ht21jam22_receive,
        'ht21jam23': ht21jam23_receive,
        'ht21jam24': ht21jam24_receive,
        
        'ht22jam1': ht22jam1_receive,
        'ht22jam2': ht22jam2_receive,
        'ht22jam3': ht22jam3_receive,
        'ht22jam4': ht22jam4_receive,
        'ht22jam5': ht22jam5_receive,
        'ht22jam6': ht22jam6_receive,
        'ht22jam7': ht22jam7_receive,
        'ht22jam8': ht22jam8_receive,
        'ht22jam9': ht22jam9_receive,
        'ht22jam10': ht22jam10_receive,
        'ht22jam11': ht22jam11_receive,
        'ht22jam12': ht22jam12_receive,
        'ht22jam13': ht22jam13_receive,
        'ht22jam14': ht22jam14_receive,
        'ht22jam15': ht22jam15_receive,
        'ht22jam16': ht22jam16_receive,
        'ht22jam17': ht22jam17_receive,
        'ht22jam18': ht22jam18_receive,
        'ht22jam19': ht22jam19_receive,
        'ht22jam20': ht22jam20_receive,
        'ht22jam21': ht22jam21_receive,
        'ht22jam22': ht22jam22_receive,
        'ht22jam23': ht22jam23_receive,
        'ht22jam24': ht22jam24_receive,
        
        'ht23jam1': ht23jam1_receive,
        'ht23jam2': ht23jam2_receive,
        'ht23jam3': ht23jam3_receive,
        'ht23jam4': ht23jam4_receive,
        'ht23jam5': ht23jam5_receive,
        'ht23jam6': ht23jam6_receive,
        'ht23jam7': ht23jam7_receive,
        'ht23jam8': ht23jam8_receive,
        'ht23jam9': ht23jam9_receive,
        'ht23jam10': ht23jam10_receive,
        'ht23jam11': ht23jam11_receive,
        'ht23jam12': ht23jam12_receive,
        'ht23jam13': ht23jam13_receive,
        'ht23jam14': ht23jam14_receive,
        'ht23jam15': ht23jam15_receive,
        'ht23jam16': ht23jam16_receive,
        'ht23jam17': ht23jam17_receive,
        'ht23jam18': ht23jam18_receive,
        'ht23jam19': ht23jam19_receive,
        'ht23jam20': ht23jam20_receive,
        'ht23jam21': ht23jam21_receive,
        'ht23jam22': ht23jam22_receive,
        'ht23jam23': ht23jam23_receive,
        'ht23jam24': ht23jam24_receive,
        
        'ht24jam1': ht24jam1_receive,
        'ht24jam2': ht24jam2_receive,
        'ht24jam3': ht24jam3_receive,
        'ht24jam4': ht24jam4_receive,
        'ht24jam5': ht24jam5_receive,
        'ht24jam6': ht24jam6_receive,
        'ht24jam7': ht24jam7_receive,
        'ht24jam8': ht24jam8_receive,
        'ht24jam9': ht24jam9_receive,
        'ht24jam10': ht24jam10_receive,
        'ht24jam11': ht24jam11_receive,
        'ht24jam12': ht24jam12_receive,
        'ht24jam13': ht24jam13_receive,
        'ht24jam14': ht24jam14_receive,
        'ht24jam15': ht24jam15_receive,
        'ht24jam16': ht24jam16_receive,
        'ht24jam17': ht24jam17_receive,
        'ht24jam18': ht24jam18_receive,
        'ht24jam19': ht24jam19_receive,
        'ht24jam20': ht24jam20_receive,
        'ht24jam21': ht24jam21_receive,
        'ht24jam22': ht24jam22_receive,
        'ht24jam23': ht24jam23_receive,
        'ht24jam24': ht24jam24_receive,
        
        'ht25jam1': ht25jam1_receive,
        'ht25jam2': ht25jam2_receive,
        'ht25jam3': ht25jam3_receive,
        'ht25jam4': ht25jam4_receive,
        'ht25jam5': ht25jam5_receive,
        'ht25jam6': ht25jam6_receive,
        'ht25jam7': ht25jam7_receive,
        'ht25jam8': ht25jam8_receive,
        'ht25jam9': ht25jam9_receive,
        'ht25jam10': ht25jam10_receive,
        'ht25jam11': ht25jam11_receive,
        'ht25jam12': ht25jam12_receive,
        'ht25jam13': ht25jam13_receive,
        'ht25jam14': ht25jam14_receive,
        'ht25jam15': ht25jam15_receive,
        'ht25jam16': ht25jam16_receive,
        'ht25jam17': ht25jam17_receive,
        'ht25jam18': ht25jam18_receive,
        'ht25jam19': ht25jam19_receive,
        'ht25jam20': ht25jam20_receive,
        'ht25jam21': ht25jam21_receive,
        'ht25jam22': ht25jam22_receive,
        'ht25jam23': ht25jam23_receive,
        'ht25jam24': ht25jam24_receive,
        
        'ht26jam1': ht26jam1_receive,
        'ht26jam2': ht26jam2_receive,
        'ht26jam3': ht26jam3_receive,
        'ht26jam4': ht26jam4_receive,
        'ht26jam5': ht26jam5_receive,
        'ht26jam6': ht26jam6_receive,
        'ht26jam7': ht26jam7_receive,
        'ht26jam8': ht26jam8_receive,
        'ht26jam9': ht26jam9_receive,
        'ht26jam10': ht26jam10_receive,
        'ht26jam11': ht26jam11_receive,
        'ht26jam12': ht26jam12_receive,
        'ht26jam13': ht26jam13_receive,
        'ht26jam14': ht26jam14_receive,
        'ht26jam15': ht26jam15_receive,
        'ht26jam16': ht26jam16_receive,
        'ht26jam17': ht26jam17_receive,
        'ht26jam18': ht26jam18_receive,
        'ht26jam19': ht26jam19_receive,
        'ht26jam20': ht26jam20_receive,
        'ht26jam21': ht26jam21_receive,
        'ht26jam22': ht26jam22_receive,
        'ht26jam23': ht26jam23_receive,
        'ht26jam24': ht26jam24_receive,
        
        'ht27jam1': ht27jam1_receive,
        'ht27jam2': ht27jam2_receive,
        'ht27jam3': ht27jam3_receive,
        'ht27jam4': ht27jam4_receive,
        'ht27jam5': ht27jam5_receive,
        'ht27jam6': ht27jam6_receive,
        'ht27jam7': ht27jam7_receive,
        'ht27jam8': ht27jam8_receive,
        'ht27jam9': ht27jam9_receive,
        'ht27jam10': ht27jam10_receive,
        'ht27jam11': ht27jam11_receive,
        'ht27jam12': ht27jam12_receive,
        'ht27jam13': ht27jam13_receive,
        'ht27jam14': ht27jam14_receive,
        'ht27jam15': ht27jam15_receive,
        'ht27jam16': ht27jam16_receive,
        'ht27jam17': ht27jam17_receive,
        'ht27jam18': ht27jam18_receive,
        'ht27jam19': ht27jam19_receive,
        'ht27jam20': ht27jam20_receive,
        'ht27jam21': ht27jam21_receive,
        'ht27jam22': ht27jam22_receive,
        'ht27jam23': ht27jam23_receive,
        'ht27jam24': ht27jam24_receive,

        'breakdown': breakdown_receive,
        'corrective': corrective_receive,
        'preventive': preventive_receive,
        'accident': accident_receive,
        'remark': remark_receive,
    }
    db.ht.insert_one(doc)
    return jsonify({'msg': 'Data berhasil disimpan!'})

    
@app.route('/viewHT', methods=['GET'])
def viewHT():
    token_receive = request.cookies.get(TOKEN_KEY)
    try:
        payload = jwt.decode(
            token_receive,
            SECRET_KEY,
            algorithms=['HS256']
        )
        id = request.args.get("id")
        data = db.ht.find_one({"_id": ObjectId(id)})
        data["_id"] = str(data["_id"])
        print(data)
        user_info = db.teknisi.find_one({'username': payload.get('id')})
        return render_template('viewHT.html', user_info=user_info, data=data)
    except jwt.ExpiredSignatureError:
        msg = 'Token Anda sudah kadaluarsa'
        return redirect(url_for('home', msg=msg))
    except jwt.exceptions.DecodeError:
        msg = 'Terjadi masalah saat login'
        return redirect(url_for('home', msg=msg))


@app.route('/editHT', methods=['GET', 'POST'])
def editHT():
    if request.method == "GET":
        token_receive = request.cookies.get(TOKEN_KEY)
        try:
            payload = jwt.decode(
                token_receive,
                SECRET_KEY,
                algorithms=['HS256']
            )
            id = request.args.get("id")
            data = db.ht.find_one({"_id": ObjectId(id)})
            data["_id"] = str(data["_id"])
            print(data)
            user_info = db.teknisi.find_one({'username': payload.get('id')})
            return render_template('editHT.html', user_info=user_info, data=data)
        except jwt.ExpiredSignatureError:
            msg = 'Token Anda sudah kadaluarsa'
            return redirect(url_for('home', msg=msg))
        except jwt.exceptions.DecodeError:
            msg = 'Terjadi masalah saat login'
            return redirect(url_for('home', msg=msg))

    elif request.method == "POST":
            id = request.form["id"]
            unit_receive = request.form["unit"]
            tanggal_receive = request.form["tanggal"]
        
            ht01jam1_receive = request.form["ht01jam1"]
            ht01jam2_receive = request.form["ht01jam2"]
            ht01jam3_receive = request.form["ht01jam3"]
            ht01jam4_receive = request.form["ht01jam4"]
            ht01jam5_receive = request.form["ht01jam5"]
            ht01jam6_receive = request.form["ht01jam6"]
            ht01jam7_receive = request.form["ht01jam7"]
            ht01jam8_receive = request.form["ht01jam8"]
            ht01jam9_receive = request.form["ht01jam9"]
            ht01jam10_receive = request.form["ht01jam10"]
            ht01jam11_receive = request.form["ht01jam11"]
            ht01jam12_receive = request.form["ht01jam12"]
            ht01jam13_receive = request.form["ht01jam13"]
            ht01jam14_receive = request.form["ht01jam14"]
            ht01jam15_receive = request.form["ht01jam15"]
            ht01jam16_receive = request.form["ht01jam16"]
            ht01jam17_receive = request.form["ht01jam17"]
            ht01jam18_receive = request.form["ht01jam18"]
            ht01jam19_receive = request.form["ht01jam19"]
            ht01jam20_receive = request.form["ht01jam20"]
            ht01jam21_receive = request.form["ht01jam21"]
            ht01jam22_receive = request.form["ht01jam22"]
            ht01jam23_receive = request.form["ht01jam23"]
            ht01jam24_receive = request.form["ht01jam24"]
            
            ht02jam1_receive = request.form["ht02jam1"]
            ht02jam2_receive = request.form["ht02jam2"]
            ht02jam3_receive = request.form["ht02jam3"]
            ht02jam4_receive = request.form["ht02jam4"]
            ht02jam5_receive = request.form["ht02jam5"]
            ht02jam6_receive = request.form["ht02jam6"]
            ht02jam7_receive = request.form["ht02jam7"]
            ht02jam8_receive = request.form["ht02jam8"]
            ht02jam9_receive = request.form["ht02jam9"]
            ht02jam10_receive = request.form["ht02jam10"]
            ht02jam11_receive = request.form["ht02jam11"]
            ht02jam12_receive = request.form["ht02jam12"]
            ht02jam13_receive = request.form["ht02jam13"]
            ht02jam14_receive = request.form["ht02jam14"]
            ht02jam15_receive = request.form["ht02jam15"]
            ht02jam16_receive = request.form["ht02jam16"]
            ht02jam17_receive = request.form["ht02jam17"]
            ht02jam18_receive = request.form["ht02jam18"]
            ht02jam19_receive = request.form["ht02jam19"]
            ht02jam20_receive = request.form["ht02jam20"]
            ht02jam21_receive = request.form["ht02jam21"]
            ht02jam22_receive = request.form["ht02jam22"]
            ht02jam23_receive = request.form["ht02jam23"]
            ht02jam24_receive = request.form["ht02jam24"]
            
            ht03jam1_receive = request.form["ht03jam1"]
            ht03jam2_receive = request.form["ht03jam2"]
            ht03jam3_receive = request.form["ht03jam3"]
            ht03jam4_receive = request.form["ht03jam4"]
            ht03jam5_receive = request.form["ht03jam5"]
            ht03jam6_receive = request.form["ht03jam6"]
            ht03jam7_receive = request.form["ht03jam7"]
            ht03jam8_receive = request.form["ht03jam8"]
            ht03jam9_receive = request.form["ht03jam9"]
            ht03jam10_receive = request.form["ht03jam10"]
            ht03jam11_receive = request.form["ht03jam11"]
            ht03jam12_receive = request.form["ht03jam12"]
            ht03jam13_receive = request.form["ht03jam13"]
            ht03jam14_receive = request.form["ht03jam14"]
            ht03jam15_receive = request.form["ht03jam15"]
            ht03jam16_receive = request.form["ht03jam16"]
            ht03jam17_receive = request.form["ht03jam17"]
            ht03jam18_receive = request.form["ht03jam18"]
            ht03jam19_receive = request.form["ht03jam19"]
            ht03jam20_receive = request.form["ht03jam20"]
            ht03jam21_receive = request.form["ht03jam21"]
            ht03jam22_receive = request.form["ht03jam22"]
            ht03jam23_receive = request.form["ht03jam23"]
            ht03jam24_receive = request.form["ht03jam24"]


            ht04jam1_receive = request.form["ht04jam1"]
            ht04jam2_receive = request.form["ht04jam2"]
            ht04jam3_receive = request.form["ht04jam3"]
            ht04jam4_receive = request.form["ht04jam4"]
            ht04jam5_receive = request.form["ht04jam5"]
            ht04jam6_receive = request.form["ht04jam6"]
            ht04jam7_receive = request.form["ht04jam7"]
            ht04jam8_receive = request.form["ht04jam8"]
            ht04jam9_receive = request.form["ht04jam9"]
            ht04jam10_receive = request.form["ht04jam10"]
            ht04jam11_receive = request.form["ht04jam11"]
            ht04jam12_receive = request.form["ht04jam12"]
            ht04jam13_receive = request.form["ht04jam13"]
            ht04jam14_receive = request.form["ht04jam14"]
            ht04jam15_receive = request.form["ht04jam15"]
            ht04jam16_receive = request.form["ht04jam16"]
            ht04jam17_receive = request.form["ht04jam17"]
            ht04jam18_receive = request.form["ht04jam18"]
            ht04jam19_receive = request.form["ht04jam19"]
            ht04jam20_receive = request.form["ht04jam20"]
            ht04jam21_receive = request.form["ht04jam21"]
            ht04jam22_receive = request.form["ht04jam22"]
            ht04jam23_receive = request.form["ht04jam23"]
            ht04jam24_receive = request.form["ht04jam24"]
            
            ht05jam1_receive = request.form["ht05jam1"]
            ht05jam2_receive = request.form["ht05jam2"]
            ht05jam3_receive = request.form["ht05jam3"]
            ht05jam4_receive = request.form["ht05jam4"]
            ht05jam5_receive = request.form["ht05jam5"]
            ht05jam6_receive = request.form["ht05jam6"]
            ht05jam7_receive = request.form["ht05jam7"]
            ht05jam8_receive = request.form["ht05jam8"]
            ht05jam9_receive = request.form["ht05jam9"]
            ht05jam10_receive = request.form["ht05jam10"]
            ht05jam11_receive = request.form["ht05jam11"]
            ht05jam12_receive = request.form["ht05jam12"]
            ht05jam13_receive = request.form["ht05jam13"]
            ht05jam14_receive = request.form["ht05jam14"]
            ht05jam15_receive = request.form["ht05jam15"]
            ht05jam16_receive = request.form["ht05jam16"]
            ht05jam17_receive = request.form["ht05jam17"]
            ht05jam18_receive = request.form["ht05jam18"]
            ht05jam19_receive = request.form["ht05jam19"]
            ht05jam20_receive = request.form["ht05jam20"]
            ht05jam21_receive = request.form["ht05jam21"]
            ht05jam22_receive = request.form["ht05jam22"]
            ht05jam23_receive = request.form["ht05jam23"]
            ht05jam24_receive = request.form["ht05jam24"]
            
            ht06jam1_receive = request.form["ht06jam1"]
            ht06jam2_receive = request.form["ht06jam2"]
            ht06jam3_receive = request.form["ht06jam3"]
            ht06jam4_receive = request.form["ht06jam4"]
            ht06jam5_receive = request.form["ht06jam5"]
            ht06jam6_receive = request.form["ht06jam6"]
            ht06jam7_receive = request.form["ht06jam7"]
            ht06jam8_receive = request.form["ht06jam8"]
            ht06jam9_receive = request.form["ht06jam9"]
            ht06jam10_receive = request.form["ht06jam10"]
            ht06jam11_receive = request.form["ht06jam11"]
            ht06jam12_receive = request.form["ht06jam12"]
            ht06jam13_receive = request.form["ht06jam13"]
            ht06jam14_receive = request.form["ht06jam14"]
            ht06jam15_receive = request.form["ht06jam15"]
            ht06jam16_receive = request.form["ht06jam16"]
            ht06jam17_receive = request.form["ht06jam17"]
            ht06jam18_receive = request.form["ht06jam18"]
            ht06jam19_receive = request.form["ht06jam19"]
            ht06jam20_receive = request.form["ht06jam20"]
            ht06jam21_receive = request.form["ht06jam21"]
            ht06jam22_receive = request.form["ht06jam22"]
            ht06jam23_receive = request.form["ht06jam23"]
            ht06jam24_receive = request.form["ht06jam24"]
            
            ht07jam1_receive = request.form["ht07jam1"]
            ht07jam2_receive = request.form["ht07jam2"]
            ht07jam3_receive = request.form["ht07jam3"]
            ht07jam4_receive = request.form["ht07jam4"]
            ht07jam5_receive = request.form["ht07jam5"]
            ht07jam6_receive = request.form["ht07jam6"]
            ht07jam7_receive = request.form["ht07jam7"]
            ht07jam8_receive = request.form["ht07jam8"]
            ht07jam9_receive = request.form["ht07jam9"]
            ht07jam10_receive = request.form["ht07jam10"]
            ht07jam11_receive = request.form["ht07jam11"]
            ht07jam12_receive = request.form["ht07jam12"]
            ht07jam13_receive = request.form["ht07jam13"]
            ht07jam14_receive = request.form["ht07jam14"]
            ht07jam15_receive = request.form["ht07jam15"]
            ht07jam16_receive = request.form["ht07jam16"]
            ht07jam17_receive = request.form["ht07jam17"]
            ht07jam18_receive = request.form["ht07jam18"]
            ht07jam19_receive = request.form["ht07jam19"]
            ht07jam20_receive = request.form["ht07jam20"]
            ht07jam21_receive = request.form["ht07jam21"]
            ht07jam22_receive = request.form["ht07jam22"]
            ht07jam23_receive = request.form["ht07jam23"]
            ht07jam24_receive = request.form["ht07jam24"]
            
            ht08jam1_receive = request.form["ht08jam1"]
            ht08jam2_receive = request.form["ht08jam2"]
            ht08jam3_receive = request.form["ht08jam3"]
            ht08jam4_receive = request.form["ht08jam4"]
            ht08jam5_receive = request.form["ht08jam5"]
            ht08jam6_receive = request.form["ht08jam6"]
            ht08jam7_receive = request.form["ht08jam7"]
            ht08jam8_receive = request.form["ht08jam8"]
            ht08jam9_receive = request.form["ht08jam9"]
            ht08jam10_receive = request.form["ht08jam10"]
            ht08jam11_receive = request.form["ht08jam11"]
            ht08jam12_receive = request.form["ht08jam12"]
            ht08jam13_receive = request.form["ht08jam13"]
            ht08jam14_receive = request.form["ht08jam14"]
            ht08jam15_receive = request.form["ht08jam15"]
            ht08jam16_receive = request.form["ht08jam16"]
            ht08jam17_receive = request.form["ht08jam17"]
            ht08jam18_receive = request.form["ht08jam18"]
            ht08jam19_receive = request.form["ht08jam19"]
            ht08jam20_receive = request.form["ht08jam20"]
            ht08jam21_receive = request.form["ht08jam21"]
            ht08jam22_receive = request.form["ht08jam22"]
            ht08jam23_receive = request.form["ht08jam23"]
            ht08jam24_receive = request.form["ht08jam24"]
            
            ht09jam1_receive = request.form["ht09jam1"]
            ht09jam2_receive = request.form["ht09jam2"]
            ht09jam3_receive = request.form["ht09jam3"]
            ht09jam4_receive = request.form["ht09jam4"]
            ht09jam5_receive = request.form["ht09jam5"]
            ht09jam6_receive = request.form["ht09jam6"]
            ht09jam7_receive = request.form["ht09jam7"]
            ht09jam8_receive = request.form["ht09jam8"]
            ht09jam9_receive = request.form["ht09jam9"]
            ht09jam10_receive = request.form["ht09jam10"]
            ht09jam11_receive = request.form["ht09jam11"]
            ht09jam12_receive = request.form["ht09jam12"]
            ht09jam13_receive = request.form["ht09jam13"]
            ht09jam14_receive = request.form["ht09jam14"]
            ht09jam15_receive = request.form["ht09jam15"]
            ht09jam16_receive = request.form["ht09jam16"]
            ht09jam17_receive = request.form["ht09jam17"]
            ht09jam18_receive = request.form["ht09jam18"]
            ht09jam19_receive = request.form["ht09jam19"]
            ht09jam20_receive = request.form["ht09jam20"]
            ht09jam21_receive = request.form["ht09jam21"]
            ht09jam22_receive = request.form["ht09jam22"]
            ht09jam23_receive = request.form["ht09jam23"]
            ht09jam24_receive = request.form["ht09jam24"]
            
            ht10jam1_receive = request.form["ht10jam1"]
            ht10jam2_receive = request.form["ht10jam2"]
            ht10jam3_receive = request.form["ht10jam3"]
            ht10jam4_receive = request.form["ht10jam4"]
            ht10jam5_receive = request.form["ht10jam5"]
            ht10jam6_receive = request.form["ht10jam6"]
            ht10jam7_receive = request.form["ht10jam7"]
            ht10jam8_receive = request.form["ht10jam8"]
            ht10jam9_receive = request.form["ht10jam9"]
            ht10jam10_receive = request.form["ht10jam10"]
            ht10jam11_receive = request.form["ht10jam11"]
            ht10jam12_receive = request.form["ht10jam12"]
            ht10jam13_receive = request.form["ht10jam13"]
            ht10jam14_receive = request.form["ht10jam14"]
            ht10jam15_receive = request.form["ht10jam15"]
            ht10jam16_receive = request.form["ht10jam16"]
            ht10jam17_receive = request.form["ht10jam17"]
            ht10jam18_receive = request.form["ht10jam18"]
            ht10jam19_receive = request.form["ht10jam19"]
            ht10jam20_receive = request.form["ht10jam20"]
            ht10jam21_receive = request.form["ht10jam21"]
            ht10jam22_receive = request.form["ht10jam22"]
            ht10jam23_receive = request.form["ht10jam23"]
            ht10jam24_receive = request.form["ht10jam24"]
            
            ht11jam1_receive = request.form["ht11jam1"]
            ht11jam2_receive = request.form["ht11jam2"]
            ht11jam3_receive = request.form["ht11jam3"]
            ht11jam4_receive = request.form["ht11jam4"]
            ht11jam5_receive = request.form["ht11jam5"]
            ht11jam6_receive = request.form["ht11jam6"]
            ht11jam7_receive = request.form["ht11jam7"]
            ht11jam8_receive = request.form["ht11jam8"]
            ht11jam9_receive = request.form["ht11jam9"]
            ht11jam10_receive = request.form["ht11jam10"]
            ht11jam11_receive = request.form["ht11jam11"]
            ht11jam12_receive = request.form["ht11jam12"]
            ht11jam13_receive = request.form["ht11jam13"]
            ht11jam14_receive = request.form["ht11jam14"]
            ht11jam15_receive = request.form["ht11jam15"]
            ht11jam16_receive = request.form["ht11jam16"]
            ht11jam17_receive = request.form["ht11jam17"]
            ht11jam18_receive = request.form["ht11jam18"]
            ht11jam19_receive = request.form["ht11jam19"]
            ht11jam20_receive = request.form["ht11jam20"]
            ht11jam21_receive = request.form["ht11jam21"]
            ht11jam22_receive = request.form["ht11jam22"]
            ht11jam23_receive = request.form["ht11jam23"]
            ht11jam24_receive = request.form["ht11jam24"]
            
            ht12jam1_receive = request.form["ht12jam1"]
            ht12jam2_receive = request.form["ht12jam2"]
            ht12jam3_receive = request.form["ht12jam3"]
            ht12jam4_receive = request.form["ht12jam4"]
            ht12jam5_receive = request.form["ht12jam5"]
            ht12jam6_receive = request.form["ht12jam6"]
            ht12jam7_receive = request.form["ht12jam7"]
            ht12jam8_receive = request.form["ht12jam8"]
            ht12jam9_receive = request.form["ht12jam9"]
            ht12jam10_receive = request.form["ht12jam10"]
            ht12jam11_receive = request.form["ht12jam11"]
            ht12jam12_receive = request.form["ht12jam12"]
            ht12jam13_receive = request.form["ht12jam13"]
            ht12jam14_receive = request.form["ht12jam14"]
            ht12jam15_receive = request.form["ht12jam15"]
            ht12jam16_receive = request.form["ht12jam16"]
            ht12jam17_receive = request.form["ht12jam17"]
            ht12jam18_receive = request.form["ht12jam18"]
            ht12jam19_receive = request.form["ht12jam19"]
            ht12jam20_receive = request.form["ht12jam20"]
            ht12jam21_receive = request.form["ht12jam21"]
            ht12jam22_receive = request.form["ht12jam22"]
            ht12jam23_receive = request.form["ht12jam23"]
            ht12jam24_receive = request.form["ht12jam24"]
            
            ht13jam1_receive = request.form["ht13jam1"]
            ht13jam2_receive = request.form["ht13jam2"]
            ht13jam3_receive = request.form["ht13jam3"]
            ht13jam4_receive = request.form["ht13jam4"]
            ht13jam5_receive = request.form["ht13jam5"]
            ht13jam6_receive = request.form["ht13jam6"]
            ht13jam7_receive = request.form["ht13jam7"]
            ht13jam8_receive = request.form["ht13jam8"]
            ht13jam9_receive = request.form["ht13jam9"]
            ht13jam10_receive = request.form["ht13jam10"]
            ht13jam11_receive = request.form["ht13jam11"]
            ht13jam12_receive = request.form["ht13jam12"]
            ht13jam13_receive = request.form["ht13jam13"]
            ht13jam14_receive = request.form["ht13jam14"]
            ht13jam15_receive = request.form["ht13jam15"]
            ht13jam16_receive = request.form["ht13jam16"]
            ht13jam17_receive = request.form["ht13jam17"]
            ht13jam18_receive = request.form["ht13jam18"]
            ht13jam19_receive = request.form["ht13jam19"]
            ht13jam20_receive = request.form["ht13jam20"]
            ht13jam21_receive = request.form["ht13jam21"]
            ht13jam22_receive = request.form["ht13jam22"]
            ht13jam23_receive = request.form["ht13jam23"]
            ht13jam24_receive = request.form["ht13jam24"]
            
            ht14jam1_receive = request.form["ht14jam1"]
            ht14jam2_receive = request.form["ht14jam2"]
            ht14jam3_receive = request.form["ht14jam3"]
            ht14jam4_receive = request.form["ht14jam4"]
            ht14jam5_receive = request.form["ht14jam5"]
            ht14jam6_receive = request.form["ht14jam6"]
            ht14jam7_receive = request.form["ht14jam7"]
            ht14jam8_receive = request.form["ht14jam8"]
            ht14jam9_receive = request.form["ht14jam9"]
            ht14jam10_receive = request.form["ht14jam10"]
            ht14jam11_receive = request.form["ht14jam11"]
            ht14jam12_receive = request.form["ht14jam12"]
            ht14jam13_receive = request.form["ht14jam13"]
            ht14jam14_receive = request.form["ht14jam14"]
            ht14jam15_receive = request.form["ht14jam15"]
            ht14jam16_receive = request.form["ht14jam16"]
            ht14jam17_receive = request.form["ht14jam17"]
            ht14jam18_receive = request.form["ht14jam18"]
            ht14jam19_receive = request.form["ht14jam19"]
            ht14jam20_receive = request.form["ht14jam20"]
            ht14jam21_receive = request.form["ht14jam21"]
            ht14jam22_receive = request.form["ht14jam22"]
            ht14jam23_receive = request.form["ht14jam23"]
            ht14jam24_receive = request.form["ht14jam24"]
            
            ht15jam1_receive = request.form["ht15jam1"]
            ht15jam2_receive = request.form["ht15jam2"]
            ht15jam3_receive = request.form["ht15jam3"]
            ht15jam4_receive = request.form["ht15jam4"]
            ht15jam5_receive = request.form["ht15jam5"]
            ht15jam6_receive = request.form["ht15jam6"]
            ht15jam7_receive = request.form["ht15jam7"]
            ht15jam8_receive = request.form["ht15jam8"]
            ht15jam9_receive = request.form["ht15jam9"]
            ht15jam10_receive = request.form["ht15jam10"]
            ht15jam11_receive = request.form["ht15jam11"]
            ht15jam12_receive = request.form["ht15jam12"]
            ht15jam13_receive = request.form["ht15jam13"]
            ht15jam14_receive = request.form["ht15jam14"]
            ht15jam15_receive = request.form["ht15jam15"]
            ht15jam16_receive = request.form["ht15jam16"]
            ht15jam17_receive = request.form["ht15jam17"]
            ht15jam18_receive = request.form["ht15jam18"]
            ht15jam19_receive = request.form["ht15jam19"]
            ht15jam20_receive = request.form["ht15jam20"]
            ht15jam21_receive = request.form["ht15jam21"]
            ht15jam22_receive = request.form["ht15jam22"]
            ht15jam23_receive = request.form["ht15jam23"]
            ht15jam24_receive = request.form["ht15jam24"]
            
            ht16jam1_receive = request.form["ht16jam1"]
            ht16jam2_receive = request.form["ht16jam2"]
            ht16jam3_receive = request.form["ht16jam3"]
            ht16jam4_receive = request.form["ht16jam4"]
            ht16jam5_receive = request.form["ht16jam5"]
            ht16jam6_receive = request.form["ht16jam6"]
            ht16jam7_receive = request.form["ht16jam7"]
            ht16jam8_receive = request.form["ht16jam8"]
            ht16jam9_receive = request.form["ht16jam9"]
            ht16jam10_receive = request.form["ht16jam10"]
            ht16jam11_receive = request.form["ht16jam11"]
            ht16jam12_receive = request.form["ht16jam12"]
            ht16jam13_receive = request.form["ht16jam13"]
            ht16jam14_receive = request.form["ht16jam14"]
            ht16jam15_receive = request.form["ht16jam15"]
            ht16jam16_receive = request.form["ht16jam16"]
            ht16jam17_receive = request.form["ht16jam17"]
            ht16jam18_receive = request.form["ht16jam18"]
            ht16jam19_receive = request.form["ht16jam19"]
            ht16jam20_receive = request.form["ht16jam20"]
            ht16jam21_receive = request.form["ht16jam21"]
            ht16jam22_receive = request.form["ht16jam22"]
            ht16jam23_receive = request.form["ht16jam23"]
            ht16jam24_receive = request.form["ht16jam24"]
            
            ht17jam1_receive = request.form["ht17jam1"]
            ht17jam2_receive = request.form["ht17jam2"]
            ht17jam3_receive = request.form["ht17jam3"]
            ht17jam4_receive = request.form["ht17jam4"]
            ht17jam5_receive = request.form["ht17jam5"]
            ht17jam6_receive = request.form["ht17jam6"]
            ht17jam7_receive = request.form["ht17jam7"]
            ht17jam8_receive = request.form["ht17jam8"]
            ht17jam9_receive = request.form["ht17jam9"]
            ht17jam10_receive = request.form["ht17jam10"]
            ht17jam11_receive = request.form["ht17jam11"]
            ht17jam12_receive = request.form["ht17jam12"]
            ht17jam13_receive = request.form["ht17jam13"]
            ht17jam14_receive = request.form["ht17jam14"]
            ht17jam15_receive = request.form["ht17jam15"]
            ht17jam16_receive = request.form["ht17jam16"]
            ht17jam17_receive = request.form["ht17jam17"]
            ht17jam18_receive = request.form["ht17jam18"]
            ht17jam19_receive = request.form["ht17jam19"]
            ht17jam20_receive = request.form["ht17jam20"]
            ht17jam21_receive = request.form["ht17jam21"]
            ht17jam22_receive = request.form["ht17jam22"]
            ht17jam23_receive = request.form["ht17jam23"]
            ht17jam24_receive = request.form["ht17jam24"]
            
            ht18jam1_receive = request.form["ht18jam1"]
            ht18jam2_receive = request.form["ht18jam2"]
            ht18jam3_receive = request.form["ht18jam3"]
            ht18jam4_receive = request.form["ht18jam4"]
            ht18jam5_receive = request.form["ht18jam5"]
            ht18jam6_receive = request.form["ht18jam6"]
            ht18jam7_receive = request.form["ht18jam7"]
            ht18jam8_receive = request.form["ht18jam8"]
            ht18jam9_receive = request.form["ht18jam9"]
            ht18jam10_receive = request.form["ht18jam10"]
            ht18jam11_receive = request.form["ht18jam11"]
            ht18jam12_receive = request.form["ht18jam12"]
            ht18jam13_receive = request.form["ht18jam13"]
            ht18jam14_receive = request.form["ht18jam14"]
            ht18jam15_receive = request.form["ht18jam15"]
            ht18jam16_receive = request.form["ht18jam16"]
            ht18jam17_receive = request.form["ht18jam17"]
            ht18jam18_receive = request.form["ht18jam18"]
            ht18jam19_receive = request.form["ht18jam19"]
            ht18jam20_receive = request.form["ht18jam20"]
            ht18jam21_receive = request.form["ht18jam21"]
            ht18jam22_receive = request.form["ht18jam22"]
            ht18jam23_receive = request.form["ht18jam23"]
            ht18jam24_receive = request.form["ht18jam24"]
            
            ht19jam1_receive = request.form["ht19jam1"]
            ht19jam2_receive = request.form["ht19jam2"]
            ht19jam3_receive = request.form["ht19jam3"]
            ht19jam4_receive = request.form["ht19jam4"]
            ht19jam5_receive = request.form["ht19jam5"]
            ht19jam6_receive = request.form["ht19jam6"]
            ht19jam7_receive = request.form["ht19jam7"]
            ht19jam8_receive = request.form["ht19jam8"]
            ht19jam9_receive = request.form["ht19jam9"]
            ht19jam10_receive = request.form["ht19jam10"]
            ht19jam11_receive = request.form["ht19jam11"]
            ht19jam12_receive = request.form["ht19jam12"]
            ht19jam13_receive = request.form["ht19jam13"]
            ht19jam14_receive = request.form["ht19jam14"]
            ht19jam15_receive = request.form["ht19jam15"]
            ht19jam16_receive = request.form["ht19jam16"]
            ht19jam17_receive = request.form["ht19jam17"]
            ht19jam18_receive = request.form["ht19jam18"]
            ht19jam19_receive = request.form["ht19jam19"]
            ht19jam20_receive = request.form["ht19jam20"]
            ht19jam21_receive = request.form["ht19jam21"]
            ht19jam22_receive = request.form["ht19jam22"]
            ht19jam23_receive = request.form["ht19jam23"]
            ht19jam24_receive = request.form["ht19jam24"]
            
            ht20jam1_receive = request.form["ht20jam1"]
            ht20jam2_receive = request.form["ht20jam2"]
            ht20jam3_receive = request.form["ht20jam3"]
            ht20jam4_receive = request.form["ht20jam4"]
            ht20jam5_receive = request.form["ht20jam5"]
            ht20jam6_receive = request.form["ht20jam6"]
            ht20jam7_receive = request.form["ht20jam7"]
            ht20jam8_receive = request.form["ht20jam8"]
            ht20jam9_receive = request.form["ht20jam9"]
            ht20jam10_receive = request.form["ht20jam10"]
            ht20jam11_receive = request.form["ht20jam11"]
            ht20jam12_receive = request.form["ht20jam12"]
            ht20jam13_receive = request.form["ht20jam13"]
            ht20jam14_receive = request.form["ht20jam14"]
            ht20jam15_receive = request.form["ht20jam15"]
            ht20jam16_receive = request.form["ht20jam16"]
            ht20jam17_receive = request.form["ht20jam17"]
            ht20jam18_receive = request.form["ht20jam18"]
            ht20jam19_receive = request.form["ht20jam19"]
            ht20jam20_receive = request.form["ht20jam20"]
            ht20jam21_receive = request.form["ht20jam21"]
            ht20jam22_receive = request.form["ht20jam22"]
            ht20jam23_receive = request.form["ht20jam23"]
            ht20jam24_receive = request.form["ht20jam24"]
            
            ht21jam1_receive = request.form["ht21jam1"]
            ht21jam2_receive = request.form["ht21jam2"]
            ht21jam3_receive = request.form["ht21jam3"]
            ht21jam4_receive = request.form["ht21jam4"]
            ht21jam5_receive = request.form["ht21jam5"]
            ht21jam6_receive = request.form["ht21jam6"]
            ht21jam7_receive = request.form["ht21jam7"]
            ht21jam8_receive = request.form["ht21jam8"]
            ht21jam9_receive = request.form["ht21jam9"]
            ht21jam10_receive = request.form["ht21jam10"]
            ht21jam11_receive = request.form["ht21jam11"]
            ht21jam12_receive = request.form["ht21jam12"]
            ht21jam13_receive = request.form["ht21jam13"]
            ht21jam14_receive = request.form["ht21jam14"]
            ht21jam15_receive = request.form["ht21jam15"]
            ht21jam16_receive = request.form["ht21jam16"]
            ht21jam17_receive = request.form["ht21jam17"]
            ht21jam18_receive = request.form["ht21jam18"]
            ht21jam19_receive = request.form["ht21jam19"]
            ht21jam20_receive = request.form["ht21jam20"]
            ht21jam21_receive = request.form["ht21jam21"]
            ht21jam22_receive = request.form["ht21jam22"]
            ht21jam23_receive = request.form["ht21jam23"]
            ht21jam24_receive = request.form["ht21jam24"]
            
            ht22jam1_receive = request.form["ht22jam1"]
            ht22jam2_receive = request.form["ht22jam2"]
            ht22jam3_receive = request.form["ht22jam3"]
            ht22jam4_receive = request.form["ht22jam4"]
            ht22jam5_receive = request.form["ht22jam5"]
            ht22jam6_receive = request.form["ht22jam6"]
            ht22jam7_receive = request.form["ht22jam7"]
            ht22jam8_receive = request.form["ht22jam8"]
            ht22jam9_receive = request.form["ht22jam9"]
            ht22jam10_receive = request.form["ht22jam10"]
            ht22jam11_receive = request.form["ht22jam11"]
            ht22jam12_receive = request.form["ht22jam12"]
            ht22jam13_receive = request.form["ht22jam13"]
            ht22jam14_receive = request.form["ht22jam14"]
            ht22jam15_receive = request.form["ht22jam15"]
            ht22jam16_receive = request.form["ht22jam16"]
            ht22jam17_receive = request.form["ht22jam17"]
            ht22jam18_receive = request.form["ht22jam18"]
            ht22jam19_receive = request.form["ht22jam19"]
            ht22jam20_receive = request.form["ht22jam20"]
            ht22jam21_receive = request.form["ht22jam21"]
            ht22jam22_receive = request.form["ht22jam22"]
            ht22jam23_receive = request.form["ht22jam23"]
            ht22jam24_receive = request.form["ht22jam24"]
            
            ht23jam1_receive = request.form["ht23jam1"]
            ht23jam2_receive = request.form["ht23jam2"]
            ht23jam3_receive = request.form["ht23jam3"]
            ht23jam4_receive = request.form["ht23jam4"]
            ht23jam5_receive = request.form["ht23jam5"]
            ht23jam6_receive = request.form["ht23jam6"]
            ht23jam7_receive = request.form["ht23jam7"]
            ht23jam8_receive = request.form["ht23jam8"]
            ht23jam9_receive = request.form["ht23jam9"]
            ht23jam10_receive = request.form["ht23jam10"]
            ht23jam11_receive = request.form["ht23jam11"]
            ht23jam12_receive = request.form["ht23jam12"]
            ht23jam13_receive = request.form["ht23jam13"]
            ht23jam14_receive = request.form["ht23jam14"]
            ht23jam15_receive = request.form["ht23jam15"]
            ht23jam16_receive = request.form["ht23jam16"]
            ht23jam17_receive = request.form["ht23jam17"]
            ht23jam18_receive = request.form["ht23jam18"]
            ht23jam19_receive = request.form["ht23jam19"]
            ht23jam20_receive = request.form["ht23jam20"]
            ht23jam21_receive = request.form["ht23jam21"]
            ht23jam22_receive = request.form["ht23jam22"]
            ht23jam23_receive = request.form["ht23jam23"]
            ht23jam24_receive = request.form["ht23jam24"]
            
            ht24jam1_receive = request.form["ht24jam1"]
            ht24jam2_receive = request.form["ht24jam2"]
            ht24jam3_receive = request.form["ht24jam3"]
            ht24jam4_receive = request.form["ht24jam4"]
            ht24jam5_receive = request.form["ht24jam5"]
            ht24jam6_receive = request.form["ht24jam6"]
            ht24jam7_receive = request.form["ht24jam7"]
            ht24jam8_receive = request.form["ht24jam8"]
            ht24jam9_receive = request.form["ht24jam9"]
            ht24jam10_receive = request.form["ht24jam10"]
            ht24jam11_receive = request.form["ht24jam11"]
            ht24jam12_receive = request.form["ht24jam12"]
            ht24jam13_receive = request.form["ht24jam13"]
            ht24jam14_receive = request.form["ht24jam14"]
            ht24jam15_receive = request.form["ht24jam15"]
            ht24jam16_receive = request.form["ht24jam16"]
            ht24jam17_receive = request.form["ht24jam17"]
            ht24jam18_receive = request.form["ht24jam18"]
            ht24jam19_receive = request.form["ht24jam19"]
            ht24jam20_receive = request.form["ht24jam20"]
            ht24jam21_receive = request.form["ht24jam21"]
            ht24jam22_receive = request.form["ht24jam22"]
            ht24jam23_receive = request.form["ht24jam23"]
            ht24jam24_receive = request.form["ht24jam24"]
            
            ht25jam1_receive = request.form["ht25jam1"]
            ht25jam2_receive = request.form["ht25jam2"]
            ht25jam3_receive = request.form["ht25jam3"]
            ht25jam4_receive = request.form["ht25jam4"]
            ht25jam5_receive = request.form["ht25jam5"]
            ht25jam6_receive = request.form["ht25jam6"]
            ht25jam7_receive = request.form["ht25jam7"]
            ht25jam8_receive = request.form["ht25jam8"]
            ht25jam9_receive = request.form["ht25jam9"]
            ht25jam10_receive = request.form["ht25jam10"]
            ht25jam11_receive = request.form["ht25jam11"]
            ht25jam12_receive = request.form["ht25jam12"]
            ht25jam13_receive = request.form["ht25jam13"]
            ht25jam14_receive = request.form["ht25jam14"]
            ht25jam15_receive = request.form["ht25jam15"]
            ht25jam16_receive = request.form["ht25jam16"]
            ht25jam17_receive = request.form["ht25jam17"]
            ht25jam18_receive = request.form["ht25jam18"]
            ht25jam19_receive = request.form["ht25jam19"]
            ht25jam20_receive = request.form["ht25jam20"]
            ht25jam21_receive = request.form["ht25jam21"]
            ht25jam22_receive = request.form["ht25jam22"]
            ht25jam23_receive = request.form["ht25jam23"]
            ht25jam24_receive = request.form["ht25jam24"]
            
            ht26jam1_receive = request.form["ht26jam1"]
            ht26jam2_receive = request.form["ht26jam2"]
            ht26jam3_receive = request.form["ht26jam3"]
            ht26jam4_receive = request.form["ht26jam4"]
            ht26jam5_receive = request.form["ht26jam5"]
            ht26jam6_receive = request.form["ht26jam6"]
            ht26jam7_receive = request.form["ht26jam7"]
            ht26jam8_receive = request.form["ht26jam8"]
            ht26jam9_receive = request.form["ht26jam9"]
            ht26jam10_receive = request.form["ht26jam10"]
            ht26jam11_receive = request.form["ht26jam11"]
            ht26jam12_receive = request.form["ht26jam12"]
            ht26jam13_receive = request.form["ht26jam13"]
            ht26jam14_receive = request.form["ht26jam14"]
            ht26jam15_receive = request.form["ht26jam15"]
            ht26jam16_receive = request.form["ht26jam16"]
            ht26jam17_receive = request.form["ht26jam17"]
            ht26jam18_receive = request.form["ht26jam18"]
            ht26jam19_receive = request.form["ht26jam19"]
            ht26jam20_receive = request.form["ht26jam20"]
            ht26jam21_receive = request.form["ht26jam21"]
            ht26jam22_receive = request.form["ht26jam22"]
            ht26jam23_receive = request.form["ht26jam23"]
            ht26jam24_receive = request.form["ht26jam24"]
            
            ht27jam1_receive = request.form["ht27jam1"]
            ht27jam2_receive = request.form["ht27jam2"]
            ht27jam3_receive = request.form["ht27jam3"]
            ht27jam4_receive = request.form["ht27jam4"]
            ht27jam5_receive = request.form["ht27jam5"]
            ht27jam6_receive = request.form["ht27jam6"]
            ht27jam7_receive = request.form["ht27jam7"]
            ht27jam8_receive = request.form["ht27jam8"]
            ht27jam9_receive = request.form["ht27jam9"]
            ht27jam10_receive = request.form["ht27jam10"]
            ht27jam11_receive = request.form["ht27jam11"]
            ht27jam12_receive = request.form["ht27jam12"]
            ht27jam13_receive = request.form["ht27jam13"]
            ht27jam14_receive = request.form["ht27jam14"]
            ht27jam15_receive = request.form["ht27jam15"]
            ht27jam16_receive = request.form["ht27jam16"]
            ht27jam17_receive = request.form["ht27jam17"]
            ht27jam18_receive = request.form["ht27jam18"]
            ht27jam19_receive = request.form["ht27jam19"]
            ht27jam20_receive = request.form["ht27jam20"]
            ht27jam21_receive = request.form["ht27jam21"]
            ht27jam22_receive = request.form["ht27jam22"]
            ht27jam23_receive = request.form["ht27jam23"]
            ht27jam24_receive = request.form["ht27jam24"]

            breakdown_receive = request.form.get('breakdown')
            corrective_receive = request.form.get('corrective')
            preventive_receive = request.form.get('preventive')
            accident_receive = request.form.get('accident')
            remark_receive = request.form.get('remark')

            doc = {
                'unit': unit_receive,
                'tanggal': tanggal_receive,

                'ht01jam1': ht01jam1_receive,
                'ht01jam2': ht01jam2_receive,
                'ht01jam3': ht01jam3_receive,
                'ht01jam4': ht01jam4_receive,
                'ht01jam5': ht01jam5_receive,
                'ht01jam6': ht01jam6_receive,
                'ht01jam7': ht01jam7_receive,
                'ht01jam8': ht01jam8_receive,
                'ht01jam9': ht01jam9_receive,
                'ht01jam10': ht01jam10_receive,
                'ht01jam11': ht01jam11_receive,
                'ht01jam12': ht01jam12_receive,
                'ht01jam13': ht01jam13_receive,
                'ht01jam14': ht01jam14_receive,
                'ht01jam15': ht01jam15_receive,
                'ht01jam16': ht01jam16_receive,
                'ht01jam17': ht01jam17_receive,
                'ht01jam18': ht01jam18_receive,
                'ht01jam19': ht01jam19_receive,
                'ht01jam20': ht01jam20_receive,
                'ht01jam21': ht01jam21_receive,
                'ht01jam22': ht01jam22_receive,
                'ht01jam23': ht01jam23_receive,
                'ht01jam24': ht01jam24_receive,
                
                'ht02jam1': ht02jam1_receive,
                'ht02jam2': ht02jam2_receive,
                'ht02jam3': ht02jam3_receive,
                'ht02jam4': ht02jam4_receive,
                'ht02jam5': ht02jam5_receive,
                'ht02jam6': ht02jam6_receive,
                'ht02jam7': ht02jam7_receive,
                'ht02jam8': ht02jam8_receive,
                'ht02jam9': ht02jam9_receive,
                'ht02jam10': ht02jam10_receive,
                'ht02jam11': ht02jam11_receive,
                'ht02jam12': ht02jam12_receive,
                'ht02jam13': ht02jam13_receive,
                'ht02jam14': ht02jam14_receive,
                'ht02jam15': ht02jam15_receive,
                'ht02jam16': ht02jam16_receive,
                'ht02jam17': ht02jam17_receive,
                'ht02jam18': ht02jam18_receive,
                'ht02jam19': ht02jam19_receive,
                'ht02jam20': ht02jam20_receive,
                'ht02jam21': ht02jam21_receive,
                'ht02jam22': ht02jam22_receive,
                'ht02jam23': ht02jam23_receive,
                'ht02jam24': ht02jam24_receive,
                
                'ht03jam1': ht03jam1_receive,
                'ht03jam2': ht03jam2_receive,
                'ht03jam3': ht03jam3_receive,
                'ht03jam4': ht03jam4_receive,
                'ht03jam5': ht03jam5_receive,
                'ht03jam6': ht03jam6_receive,
                'ht03jam7': ht03jam7_receive,
                'ht03jam8': ht03jam8_receive,
                'ht03jam9': ht03jam9_receive,
                'ht03jam10': ht03jam10_receive,
                'ht03jam11': ht03jam11_receive,
                'ht03jam12': ht03jam12_receive,
                'ht03jam13': ht03jam13_receive,
                'ht03jam14': ht03jam14_receive,
                'ht03jam15': ht03jam15_receive,
                'ht03jam16': ht03jam16_receive,
                'ht03jam17': ht03jam17_receive,
                'ht03jam18': ht03jam18_receive,
                'ht03jam19': ht03jam19_receive,
                'ht03jam20': ht03jam20_receive,
                'ht03jam21': ht03jam21_receive,
                'ht03jam22': ht03jam22_receive,
                'ht03jam23': ht03jam23_receive,
                'ht03jam24': ht03jam24_receive,
                
                'ht04jam1': ht04jam1_receive,
                'ht04jam2': ht04jam2_receive,
                'ht04jam3': ht04jam3_receive,
                'ht04jam4': ht04jam4_receive,
                'ht04jam5': ht04jam5_receive,
                'ht04jam6': ht04jam6_receive,
                'ht04jam7': ht04jam7_receive,
                'ht04jam8': ht04jam8_receive,
                'ht04jam9': ht04jam9_receive,
                'ht04jam10': ht04jam10_receive,
                'ht04jam11': ht04jam11_receive,
                'ht04jam12': ht04jam12_receive,
                'ht04jam13': ht04jam13_receive,
                'ht04jam14': ht04jam14_receive,
                'ht04jam15': ht04jam15_receive,
                'ht04jam16': ht04jam16_receive,
                'ht04jam17': ht04jam17_receive,
                'ht04jam18': ht04jam18_receive,
                'ht04jam19': ht04jam19_receive,
                'ht04jam20': ht04jam20_receive,
                'ht04jam21': ht04jam21_receive,
                'ht04jam22': ht04jam22_receive,
                'ht04jam23': ht04jam23_receive,
                'ht04jam24': ht04jam24_receive,
                
                'ht05jam1': ht05jam1_receive,
                'ht05jam2': ht05jam2_receive,
                'ht05jam3': ht05jam3_receive,
                'ht05jam4': ht05jam4_receive,
                'ht05jam5': ht05jam5_receive,
                'ht05jam6': ht05jam6_receive,
                'ht05jam7': ht05jam7_receive,
                'ht05jam8': ht05jam8_receive,
                'ht05jam9': ht05jam9_receive,
                'ht05jam10': ht05jam10_receive,
                'ht05jam11': ht05jam11_receive,
                'ht05jam12': ht05jam12_receive,
                'ht05jam13': ht05jam13_receive,
                'ht05jam14': ht05jam14_receive,
                'ht05jam15': ht05jam15_receive,
                'ht05jam16': ht05jam16_receive,
                'ht05jam17': ht05jam17_receive,
                'ht05jam18': ht05jam18_receive,
                'ht05jam19': ht05jam19_receive,
                'ht05jam20': ht05jam20_receive,
                'ht05jam21': ht05jam21_receive,
                'ht05jam22': ht05jam22_receive,
                'ht05jam23': ht05jam23_receive,
                'ht05jam24': ht05jam24_receive,
                
                'ht06jam1': ht06jam1_receive,
                'ht06jam2': ht06jam2_receive,
                'ht06jam3': ht06jam3_receive,
                'ht06jam4': ht06jam4_receive,
                'ht06jam5': ht06jam5_receive,
                'ht06jam6': ht06jam6_receive,
                'ht06jam7': ht06jam7_receive,
                'ht06jam8': ht06jam8_receive,
                'ht06jam9': ht06jam9_receive,
                'ht06jam10': ht06jam10_receive,
                'ht06jam11': ht06jam11_receive,
                'ht06jam12': ht06jam12_receive,
                'ht06jam13': ht06jam13_receive,
                'ht06jam14': ht06jam14_receive,
                'ht06jam15': ht06jam15_receive,
                'ht06jam16': ht06jam16_receive,
                'ht06jam17': ht06jam17_receive,
                'ht06jam18': ht06jam18_receive,
                'ht06jam19': ht06jam19_receive,
                'ht06jam20': ht06jam20_receive,
                'ht06jam21': ht06jam21_receive,
                'ht06jam22': ht06jam22_receive,
                'ht06jam23': ht06jam23_receive,
                'ht06jam24': ht06jam24_receive,
                
                'ht07jam1': ht07jam1_receive,
                'ht07jam2': ht07jam2_receive,
                'ht07jam3': ht07jam3_receive,
                'ht07jam4': ht07jam4_receive,
                'ht07jam5': ht07jam5_receive,
                'ht07jam6': ht07jam6_receive,
                'ht07jam7': ht07jam7_receive,
                'ht07jam8': ht07jam8_receive,
                'ht07jam9': ht07jam9_receive,
                'ht07jam10': ht07jam10_receive,
                'ht07jam11': ht07jam11_receive,
                'ht07jam12': ht07jam12_receive,
                'ht07jam13': ht07jam13_receive,
                'ht07jam14': ht07jam14_receive,
                'ht07jam15': ht07jam15_receive,
                'ht07jam16': ht07jam16_receive,
                'ht07jam17': ht07jam17_receive,
                'ht07jam18': ht07jam18_receive,
                'ht07jam19': ht07jam19_receive,
                'ht07jam20': ht07jam20_receive,
                'ht07jam21': ht07jam21_receive,
                'ht07jam22': ht07jam22_receive,
                'ht07jam23': ht07jam23_receive,
                'ht07jam24': ht07jam24_receive,
                
                'ht08jam1': ht08jam1_receive,
                'ht08jam2': ht08jam2_receive,
                'ht08jam3': ht08jam3_receive,
                'ht08jam4': ht08jam4_receive,
                'ht08jam5': ht08jam5_receive,
                'ht08jam6': ht08jam6_receive,
                'ht08jam7': ht08jam7_receive,
                'ht08jam8': ht08jam8_receive,
                'ht08jam9': ht08jam9_receive,
                'ht08jam10': ht08jam10_receive,
                'ht08jam11': ht08jam11_receive,
                'ht08jam12': ht08jam12_receive,
                'ht08jam13': ht08jam13_receive,
                'ht08jam14': ht08jam14_receive,
                'ht08jam15': ht08jam15_receive,
                'ht08jam16': ht08jam16_receive,
                'ht08jam17': ht08jam17_receive,
                'ht08jam18': ht08jam18_receive,
                'ht08jam19': ht08jam19_receive,
                'ht08jam20': ht08jam20_receive,
                'ht08jam21': ht08jam21_receive,
                'ht08jam22': ht08jam22_receive,
                'ht08jam23': ht08jam23_receive,
                'ht08jam24': ht08jam24_receive,
                
                'ht09jam1': ht09jam1_receive,
                'ht09jam2': ht09jam2_receive,
                'ht09jam3': ht09jam3_receive,
                'ht09jam4': ht09jam4_receive,
                'ht09jam5': ht09jam5_receive,
                'ht09jam6': ht09jam6_receive,
                'ht09jam7': ht09jam7_receive,
                'ht09jam8': ht09jam8_receive,
                'ht09jam9': ht09jam9_receive,
                'ht09jam10': ht09jam10_receive,
                'ht09jam11': ht09jam11_receive,
                'ht09jam12': ht09jam12_receive,
                'ht09jam13': ht09jam13_receive,
                'ht09jam14': ht09jam14_receive,
                'ht09jam15': ht09jam15_receive,
                'ht09jam16': ht09jam16_receive,
                'ht09jam17': ht09jam17_receive,
                'ht09jam18': ht09jam18_receive,
                'ht09jam19': ht09jam19_receive,
                'ht09jam20': ht09jam20_receive,
                'ht09jam21': ht09jam21_receive,
                'ht09jam22': ht09jam22_receive,
                'ht09jam23': ht09jam23_receive,
                'ht09jam24': ht09jam24_receive,
                
                'ht10jam1': ht10jam1_receive,
                'ht10jam2': ht10jam2_receive,
                'ht10jam3': ht10jam3_receive,
                'ht10jam4': ht10jam4_receive,
                'ht10jam5': ht10jam5_receive,
                'ht10jam6': ht10jam6_receive,
                'ht10jam7': ht10jam7_receive,
                'ht10jam8': ht10jam8_receive,
                'ht10jam9': ht10jam9_receive,
                'ht10jam10': ht10jam10_receive,
                'ht10jam11': ht10jam11_receive,
                'ht10jam12': ht10jam12_receive,
                'ht10jam13': ht10jam13_receive,
                'ht10jam14': ht10jam14_receive,
                'ht10jam15': ht10jam15_receive,
                'ht10jam16': ht10jam16_receive,
                'ht10jam17': ht10jam17_receive,
                'ht10jam18': ht10jam18_receive,
                'ht10jam19': ht10jam19_receive,
                'ht10jam20': ht10jam20_receive,
                'ht10jam21': ht10jam21_receive,
                'ht10jam22': ht10jam22_receive,
                'ht10jam23': ht10jam23_receive,
                'ht10jam24': ht10jam24_receive,
                
                'ht11jam1': ht11jam1_receive,
                'ht11jam2': ht11jam2_receive,
                'ht11jam3': ht11jam3_receive,
                'ht11jam4': ht11jam4_receive,
                'ht11jam5': ht11jam5_receive,
                'ht11jam6': ht11jam6_receive,
                'ht11jam7': ht11jam7_receive,
                'ht11jam8': ht11jam8_receive,
                'ht11jam9': ht11jam9_receive,
                'ht11jam10': ht11jam10_receive,
                'ht11jam11': ht11jam11_receive,
                'ht11jam12': ht11jam12_receive,
                'ht11jam13': ht11jam13_receive,
                'ht11jam14': ht11jam14_receive,
                'ht11jam15': ht11jam15_receive,
                'ht11jam16': ht11jam16_receive,
                'ht11jam17': ht11jam17_receive,
                'ht11jam18': ht11jam18_receive,
                'ht11jam19': ht11jam19_receive,
                'ht11jam20': ht11jam20_receive,
                'ht11jam21': ht11jam21_receive,
                'ht11jam22': ht11jam22_receive,
                'ht11jam23': ht11jam23_receive,
                'ht11jam24': ht11jam24_receive,
                
                'ht12jam1': ht12jam1_receive,
                'ht12jam2': ht12jam2_receive,
                'ht12jam3': ht12jam3_receive,
                'ht12jam4': ht12jam4_receive,
                'ht12jam5': ht12jam5_receive,
                'ht12jam6': ht12jam6_receive,
                'ht12jam7': ht12jam7_receive,
                'ht12jam8': ht12jam8_receive,
                'ht12jam9': ht12jam9_receive,
                'ht12jam10': ht12jam10_receive,
                'ht12jam11': ht12jam11_receive,
                'ht12jam12': ht12jam12_receive,
                'ht12jam13': ht12jam13_receive,
                'ht12jam14': ht12jam14_receive,
                'ht12jam15': ht12jam15_receive,
                'ht12jam16': ht12jam16_receive,
                'ht12jam17': ht12jam17_receive,
                'ht12jam18': ht12jam18_receive,
                'ht12jam19': ht12jam19_receive,
                'ht12jam20': ht12jam20_receive,
                'ht12jam21': ht12jam21_receive,
                'ht12jam22': ht12jam22_receive,
                'ht12jam23': ht12jam23_receive,
                'ht12jam24': ht12jam24_receive,
                
                'ht13jam1': ht13jam1_receive,
                'ht13jam2': ht13jam2_receive,
                'ht13jam3': ht13jam3_receive,
                'ht13jam4': ht13jam4_receive,
                'ht13jam5': ht13jam5_receive,
                'ht13jam6': ht13jam6_receive,
                'ht13jam7': ht13jam7_receive,
                'ht13jam8': ht13jam8_receive,
                'ht13jam9': ht13jam9_receive,
                'ht13jam10': ht13jam10_receive,
                'ht13jam11': ht13jam11_receive,
                'ht13jam12': ht13jam12_receive,
                'ht13jam13': ht13jam13_receive,
                'ht13jam14': ht13jam14_receive,
                'ht13jam15': ht13jam15_receive,
                'ht13jam16': ht13jam16_receive,
                'ht13jam17': ht13jam17_receive,
                'ht13jam18': ht13jam18_receive,
                'ht13jam19': ht13jam19_receive,
                'ht13jam20': ht13jam20_receive,
                'ht13jam21': ht13jam21_receive,
                'ht13jam22': ht13jam22_receive,
                'ht13jam23': ht13jam23_receive,
                'ht13jam24': ht13jam24_receive,
                
                'ht14jam1': ht14jam1_receive,
                'ht14jam2': ht14jam2_receive,
                'ht14jam3': ht14jam3_receive,
                'ht14jam4': ht14jam4_receive,
                'ht14jam5': ht14jam5_receive,
                'ht14jam6': ht14jam6_receive,
                'ht14jam7': ht14jam7_receive,
                'ht14jam8': ht14jam8_receive,
                'ht14jam9': ht14jam9_receive,
                'ht14jam10': ht14jam10_receive,
                'ht14jam11': ht14jam11_receive,
                'ht14jam12': ht14jam12_receive,
                'ht14jam13': ht14jam13_receive,
                'ht14jam14': ht14jam14_receive,
                'ht14jam15': ht14jam15_receive,
                'ht14jam16': ht14jam16_receive,
                'ht14jam17': ht14jam17_receive,
                'ht14jam18': ht14jam18_receive,
                'ht14jam19': ht14jam19_receive,
                'ht14jam20': ht14jam20_receive,
                'ht14jam21': ht14jam21_receive,
                'ht14jam22': ht14jam22_receive,
                'ht14jam23': ht14jam23_receive,
                'ht14jam24': ht14jam24_receive,
                
                'ht15jam1': ht15jam1_receive,
                'ht15jam2': ht15jam2_receive,
                'ht15jam3': ht15jam3_receive,
                'ht15jam4': ht15jam4_receive,
                'ht15jam5': ht15jam5_receive,
                'ht15jam6': ht15jam6_receive,
                'ht15jam7': ht15jam7_receive,
                'ht15jam8': ht15jam8_receive,
                'ht15jam9': ht15jam9_receive,
                'ht15jam10': ht15jam10_receive,
                'ht15jam11': ht15jam11_receive,
                'ht15jam12': ht15jam12_receive,
                'ht15jam13': ht15jam13_receive,
                'ht15jam14': ht15jam14_receive,
                'ht15jam15': ht15jam15_receive,
                'ht15jam16': ht15jam16_receive,
                'ht15jam17': ht15jam17_receive,
                'ht15jam18': ht15jam18_receive,
                'ht15jam19': ht15jam19_receive,
                'ht15jam20': ht15jam20_receive,
                'ht15jam21': ht15jam21_receive,
                'ht15jam22': ht15jam22_receive,
                'ht15jam23': ht15jam23_receive,
                'ht15jam24': ht15jam24_receive,
                
                 'ht16jam1': ht16jam1_receive,
                'ht16jam2': ht16jam2_receive,
                'ht16jam3': ht16jam3_receive,
                'ht16jam4': ht16jam4_receive,
                'ht16jam5': ht16jam5_receive,
                'ht16jam6': ht16jam6_receive,
                'ht16jam7': ht16jam7_receive,
                'ht16jam8': ht16jam8_receive,
                'ht16jam9': ht16jam9_receive,
                'ht16jam10': ht16jam10_receive,
                'ht16jam11': ht16jam11_receive,
                'ht16jam12': ht16jam12_receive,
                'ht16jam13': ht16jam13_receive,
                'ht16jam14': ht16jam14_receive,
                'ht16jam15': ht16jam15_receive,
                'ht16jam16': ht16jam16_receive,
                'ht16jam17': ht16jam17_receive,
                'ht16jam18': ht16jam18_receive,
                'ht16jam19': ht16jam19_receive,
                'ht16jam20': ht16jam20_receive,
                'ht16jam21': ht16jam21_receive,
                'ht16jam22': ht16jam22_receive,
                'ht16jam23': ht16jam23_receive,
                'ht16jam24': ht16jam24_receive,
                
                'ht17jam1': ht17jam1_receive,
                'ht17jam2': ht17jam2_receive,
                'ht17jam3': ht17jam3_receive,
                'ht17jam4': ht17jam4_receive,
                'ht17jam5': ht17jam5_receive,
                'ht17jam6': ht17jam6_receive,
                'ht17jam7': ht17jam7_receive,
                'ht17jam8': ht17jam8_receive,
                'ht17jam9': ht17jam9_receive,
                'ht17jam10': ht17jam10_receive,
                'ht17jam11': ht17jam11_receive,
                'ht17jam12': ht17jam12_receive,
                'ht17jam13': ht17jam13_receive,
                'ht17jam14': ht17jam14_receive,
                'ht17jam15': ht17jam15_receive,
                'ht17jam16': ht17jam16_receive,
                'ht17jam17': ht17jam17_receive,
                'ht17jam18': ht17jam18_receive,
                'ht17jam19': ht17jam19_receive,
                'ht17jam20': ht17jam20_receive,
                'ht17jam21': ht17jam21_receive,
                'ht17jam22': ht17jam22_receive,
                'ht17jam23': ht17jam23_receive,
                'ht17jam24': ht17jam24_receive,
                
                'ht18jam1': ht18jam1_receive,
                'ht18jam2': ht18jam2_receive,
                'ht18jam3': ht18jam3_receive,
                'ht18jam4': ht18jam4_receive,
                'ht18jam5': ht18jam5_receive,
                'ht18jam6': ht18jam6_receive,
                'ht18jam7': ht18jam7_receive,
                'ht18jam8': ht18jam8_receive,
                'ht18jam9': ht18jam9_receive,
                'ht18jam10': ht18jam10_receive,
                'ht18jam11': ht18jam11_receive,
                'ht18jam12': ht18jam12_receive,
                'ht18jam13': ht18jam13_receive,
                'ht18jam14': ht18jam14_receive,
                'ht18jam15': ht18jam15_receive,
                'ht18jam16': ht18jam16_receive,
                'ht18jam17': ht18jam17_receive,
                'ht18jam18': ht18jam18_receive,
                'ht18jam19': ht18jam19_receive,
                'ht18jam20': ht18jam20_receive,
                'ht18jam21': ht18jam21_receive,
                'ht18jam22': ht18jam22_receive,
                'ht18jam23': ht18jam23_receive,
                'ht18jam24': ht18jam24_receive,
                
                'ht19jam1': ht19jam1_receive,
                'ht19jam2': ht19jam2_receive,
                'ht19jam3': ht19jam3_receive,
                'ht19jam4': ht19jam4_receive,
                'ht19jam5': ht19jam5_receive,
                'ht19jam6': ht19jam6_receive,
                'ht19jam7': ht19jam7_receive,
                'ht19jam8': ht19jam8_receive,
                'ht19jam9': ht19jam9_receive,
                'ht19jam10': ht19jam10_receive,
                'ht19jam11': ht19jam11_receive,
                'ht19jam12': ht19jam12_receive,
                'ht19jam13': ht19jam13_receive,
                'ht19jam14': ht19jam14_receive,
                'ht19jam15': ht19jam15_receive,
                'ht19jam16': ht19jam16_receive,
                'ht19jam17': ht19jam17_receive,
                'ht19jam18': ht19jam18_receive,
                'ht19jam19': ht19jam19_receive,
                'ht19jam20': ht19jam20_receive,
                'ht19jam21': ht19jam21_receive,
                'ht19jam22': ht19jam22_receive,
                'ht19jam23': ht19jam23_receive,
                'ht19jam24': ht19jam24_receive,
                
                'ht20jam1': ht20jam1_receive,
                'ht20jam2': ht20jam2_receive,
                'ht20jam3': ht20jam3_receive,
                'ht20jam4': ht20jam4_receive,
                'ht20jam5': ht20jam5_receive,
                'ht20jam6': ht20jam6_receive,
                'ht20jam7': ht20jam7_receive,
                'ht20jam8': ht20jam8_receive,
                'ht20jam9': ht20jam9_receive,
                'ht20jam10': ht20jam10_receive,
                'ht20jam11': ht20jam11_receive,
                'ht20jam12': ht20jam12_receive,
                'ht20jam13': ht20jam13_receive,
                'ht20jam14': ht20jam14_receive,
                'ht20jam15': ht20jam15_receive,
                'ht20jam16': ht20jam16_receive,
                'ht20jam17': ht20jam17_receive,
                'ht20jam18': ht20jam18_receive,
                'ht20jam19': ht20jam19_receive,
                'ht20jam20': ht20jam20_receive,
                'ht20jam21': ht20jam21_receive,
                'ht20jam22': ht20jam22_receive,
                'ht20jam23': ht20jam23_receive,
                'ht20jam24': ht20jam24_receive,
                
                'ht21jam1': ht21jam1_receive,
                'ht21jam2': ht21jam2_receive,
                'ht21jam3': ht21jam3_receive,
                'ht21jam4': ht21jam4_receive,
                'ht21jam5': ht21jam5_receive,
                'ht21jam6': ht21jam6_receive,
                'ht21jam7': ht21jam7_receive,
                'ht21jam8': ht21jam8_receive,
                'ht21jam9': ht21jam9_receive,
                'ht21jam10': ht21jam10_receive,
                'ht21jam11': ht21jam11_receive,
                'ht21jam12': ht21jam12_receive,
                'ht21jam13': ht21jam13_receive,
                'ht21jam14': ht21jam14_receive,
                'ht21jam15': ht21jam15_receive,
                'ht21jam16': ht21jam16_receive,
                'ht21jam17': ht21jam17_receive,
                'ht21jam18': ht21jam18_receive,
                'ht21jam19': ht21jam19_receive,
                'ht21jam20': ht21jam20_receive,
                'ht21jam21': ht21jam21_receive,
                'ht21jam22': ht21jam22_receive,
                'ht21jam23': ht21jam23_receive,
                'ht21jam24': ht21jam24_receive,
                
                'ht22jam1': ht22jam1_receive,
                'ht22jam2': ht22jam2_receive,
                'ht22jam3': ht22jam3_receive,
                'ht22jam4': ht22jam4_receive,
                'ht22jam5': ht22jam5_receive,
                'ht22jam6': ht22jam6_receive,
                'ht22jam7': ht22jam7_receive,
                'ht22jam8': ht22jam8_receive,
                'ht22jam9': ht22jam9_receive,
                'ht22jam10': ht22jam10_receive,
                'ht22jam11': ht22jam11_receive,
                'ht22jam12': ht22jam12_receive,
                'ht22jam13': ht22jam13_receive,
                'ht22jam14': ht22jam14_receive,
                'ht22jam15': ht22jam15_receive,
                'ht22jam16': ht22jam16_receive,
                'ht22jam17': ht22jam17_receive,
                'ht22jam18': ht22jam18_receive,
                'ht22jam19': ht22jam19_receive,
                'ht22jam20': ht22jam20_receive,
                'ht22jam21': ht22jam21_receive,
                'ht22jam22': ht22jam22_receive,
                'ht22jam23': ht22jam23_receive,
                'ht22jam24': ht22jam24_receive,
                
                'ht23jam1': ht23jam1_receive,
                'ht23jam2': ht23jam2_receive,
                'ht23jam3': ht23jam3_receive,
                'ht23jam4': ht23jam4_receive,
                'ht23jam5': ht23jam5_receive,
                'ht23jam6': ht23jam6_receive,
                'ht23jam7': ht23jam7_receive,
                'ht23jam8': ht23jam8_receive,
                'ht23jam9': ht23jam9_receive,
                'ht23jam10': ht23jam10_receive,
                'ht23jam11': ht23jam11_receive,
                'ht23jam12': ht23jam12_receive,
                'ht23jam13': ht23jam13_receive,
                'ht23jam14': ht23jam14_receive,
                'ht23jam15': ht23jam15_receive,
                'ht23jam16': ht23jam16_receive,
                'ht23jam17': ht23jam17_receive,
                'ht23jam18': ht23jam18_receive,
                'ht23jam19': ht23jam19_receive,
                'ht23jam20': ht23jam20_receive,
                'ht23jam21': ht23jam21_receive,
                'ht23jam22': ht23jam22_receive,
                'ht23jam23': ht23jam23_receive,
                'ht23jam24': ht23jam24_receive,
                
                'ht24jam1': ht24jam1_receive,
                'ht24jam2': ht24jam2_receive,
                'ht24jam3': ht24jam3_receive,
                'ht24jam4': ht24jam4_receive,
                'ht24jam5': ht24jam5_receive,
                'ht24jam6': ht24jam6_receive,
                'ht24jam7': ht24jam7_receive,
                'ht24jam8': ht24jam8_receive,
                'ht24jam9': ht24jam9_receive,
                'ht24jam10': ht24jam10_receive,
                'ht24jam11': ht24jam11_receive,
                'ht24jam12': ht24jam12_receive,
                'ht24jam13': ht24jam13_receive,
                'ht24jam14': ht24jam14_receive,
                'ht24jam15': ht24jam15_receive,
                'ht24jam16': ht24jam16_receive,
                'ht24jam17': ht24jam17_receive,
                'ht24jam18': ht24jam18_receive,
                'ht24jam19': ht24jam19_receive,
                'ht24jam20': ht24jam20_receive,
                'ht24jam21': ht24jam21_receive,
                'ht24jam22': ht24jam22_receive,
                'ht24jam23': ht24jam23_receive,
                'ht24jam24': ht24jam24_receive,
                
                'ht25jam1': ht25jam1_receive,
                'ht25jam2': ht25jam2_receive,
                'ht25jam3': ht25jam3_receive,
                'ht25jam4': ht25jam4_receive,
                'ht25jam5': ht25jam5_receive,
                'ht25jam6': ht25jam6_receive,
                'ht25jam7': ht25jam7_receive,
                'ht25jam8': ht25jam8_receive,
                'ht25jam9': ht25jam9_receive,
                'ht25jam10': ht25jam10_receive,
                'ht25jam11': ht25jam11_receive,
                'ht25jam12': ht25jam12_receive,
                'ht25jam13': ht25jam13_receive,
                'ht25jam14': ht25jam14_receive,
                'ht25jam15': ht25jam15_receive,
                'ht25jam16': ht25jam16_receive,
                'ht25jam17': ht25jam17_receive,
                'ht25jam18': ht25jam18_receive,
                'ht25jam19': ht25jam19_receive,
                'ht25jam20': ht25jam20_receive,
                'ht25jam21': ht25jam21_receive,
                'ht25jam22': ht25jam22_receive,
                'ht25jam23': ht25jam23_receive,
                'ht25jam24': ht25jam24_receive,
                
                'ht26jam1': ht26jam1_receive,
                'ht26jam2': ht26jam2_receive,
                'ht26jam3': ht26jam3_receive,
                'ht26jam4': ht26jam4_receive,
                'ht26jam5': ht26jam5_receive,
                'ht26jam6': ht26jam6_receive,
                'ht26jam7': ht26jam7_receive,
                'ht26jam8': ht26jam8_receive,
                'ht26jam9': ht26jam9_receive,
                'ht26jam10': ht26jam10_receive,
                'ht26jam11': ht26jam11_receive,
                'ht26jam12': ht26jam12_receive,
                'ht26jam13': ht26jam13_receive,
                'ht26jam14': ht26jam14_receive,
                'ht26jam15': ht26jam15_receive,
                'ht26jam16': ht26jam16_receive,
                'ht26jam17': ht26jam17_receive,
                'ht26jam18': ht26jam18_receive,
                'ht26jam19': ht26jam19_receive,
                'ht26jam20': ht26jam20_receive,
                'ht26jam21': ht26jam21_receive,
                'ht26jam22': ht26jam22_receive,
                'ht26jam23': ht26jam23_receive,
                'ht26jam24': ht26jam24_receive,
                
                'ht27jam1': ht27jam1_receive,
                'ht27jam2': ht27jam2_receive,
                'ht27jam3': ht27jam3_receive,
                'ht27jam4': ht27jam4_receive,
                'ht27jam5': ht27jam5_receive,
                'ht27jam6': ht27jam6_receive,
                'ht27jam7': ht27jam7_receive,
                'ht27jam8': ht27jam8_receive,
                'ht27jam9': ht27jam9_receive,
                'ht27jam10': ht27jam10_receive,
                'ht27jam11': ht27jam11_receive,
                'ht27jam12': ht27jam12_receive,
                'ht27jam13': ht27jam13_receive,
                'ht27jam14': ht27jam14_receive,
                'ht27jam15': ht27jam15_receive,
                'ht27jam16': ht27jam16_receive,
                'ht27jam17': ht27jam17_receive,
                'ht27jam18': ht27jam18_receive,
                'ht27jam19': ht27jam19_receive,
                'ht27jam20': ht27jam20_receive,
                'ht27jam21': ht27jam21_receive,
                'ht27jam22': ht27jam22_receive,
                'ht27jam23': ht27jam23_receive,
                'ht27jam24': ht27jam24_receive,

                'breakdown': breakdown_receive,
                'corrective': corrective_receive,
                'preventive': preventive_receive,
                'accident': accident_receive,
                'remark': remark_receive,
            }
            db.ht.update_one({"_id": ObjectId(id)}, {"$set": doc})
            return redirect('/')
    
@app.route('/delete_rep', methods=['GET', 'POST'])
def delete():
    id = request.form["id"]
    
    # Hapus data dari db.cc
    db.cc.delete_one({'_id': ObjectId(id)})
    
    # Hapus data dari db.rtg
    db.rtg.delete_one({'_id': ObjectId(id)})
    
    # Hapus data dari db.ab
    db.ab.delete_one({'_id': ObjectId(id)})
    
    # Hapus data dari db.ht
    db.ht.delete_one({'_id': ObjectId(id)})
    
    return redirect('/')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)