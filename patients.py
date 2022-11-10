from flask import Flask , request , jsonify 
app =Flask(__name__)


'''=================the following code are for the GET METHOD================== '''
fulltime=[{'allday':'Dentist-Mike'},{'allday':'Gynaecologist-Duke'},{'allday':'Occulist-Greg'}]
approvednurses=[{'nurse':'Dental-Mia'},{'nurse':'Gynal-Dian'},{'nurse':'Skin-Greggory'}]
specialists=[{'spec':'Dental-Kyle'},{'spec':'Nerval-Pyke'},{'spec':'Bones-Dreg'}]
databank=[{'hospitalstaff':'fulltime'},{'hospitalstaff':'approvednurses'},{'hospitalstaff':'specialists'}]

@app.route("/staff", methods=['GET'])
def staff():
	return jsonify({'databank':databank})

@app.route("/staff/<string:hospitalstaff>", methods=['GET'])
def staff_specified(hospitalstaff):
	grp=[ k for k in databank if k['hospitalstaff']== hospitalstaff]
	return jsonify({'hospital workers include':grp[0]})

@app.route("/fulltime", methods=['GET'])
def fulltime():
	return jsonify({'fulltime':fulltime})

@app.route("/fulltime/<string:specified>", methods=['GET'])
def fulltime_specific(specified):
	dec=[h for h in fulltime if h['allday']== specified]
	return jsonify({'you have selected':dec[0]})

if __name__ =='__main__':
	app.run(debug=True)
