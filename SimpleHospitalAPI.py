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
def fulltim():
	return jsonify({'fulltime':fulltime})

@app.route("/fulltime/<string:specified>", methods=['GET'])
def fulltime_specific(specified):
	dec=[h for h in fulltime if h['allday']== specified]
	return jsonify({'you have selected':dec[0]})


@app.route("/approvednurses", methods=['GET'])
def nurseesapproved():
	return jsonify({'approvednurses':approvednurses})


@app.route("/approvednurses/<string:specified>", methods=['GET'])
def approvednurses_specific(specified):
	dec=[h for h in approvednurses if h['nurse']== specified]
	return jsonify({'you have selected':dec[0]})


@app.route("/specialists", methods=['GET'])
def specialists_function():
	return jsonify({'specialists':specialists})


@app.route("/specialists/<string:specified>", methods=['GET'])
def specialists_specific(specified):
	dec=[h for h in specialists if h['spec']== specified]
	return jsonify({'you have selected':dec[0]})

'''=================the following code are for the POST METHOD================== '''
# fulltime=[{'allday':'Dentist-Mike'},{'allday':'Gynaecologist-Duke'},{'allday':'Occulist-Greg'}]
# approvednurses=[{'nurse':'Dental-Mia'},{'nurse':'Gynal-Dian'},{'nurse':'Skin-Greggory'}]
# specialists=[{'spec':'Dental-Kyle'},{'spec':'Nerval-Pyke'},{'spec':'Bones-Dreg'}]

'''this endpoing is for addding staffmembers '''
@app.route("/staff", methods=['POST'])
def staff_addingmore():
	addstaff= {'hospitalstaff':request.json['hospitalstaff']}
	databank.append(addstaff)
	return jsonify({'Messgae ':'Successfully Posted'})


'''this endpoing is for addding staffmembers who are specialists'''
@app.route("/specialists", methods=['POST'])
def specialists_function_addingmore():
	sp={'spec':request.json['spec']}
	specialists.append(sp)
	return jsonify({'Messgae ':'Successfully Posted'})

'''this endpoing is for addding staffmembers who are fulltime workers'''
@app.route("/fulltime", methods=['POST'])
def fulltim_addingmore():
	ft={'allday':request.json['allday']}
	fulltime.append(ft)
	return jsonify({'Messgae ':'Successfully Posted'})


'''this endpoing is for addding staffmembers who are approved nurses'''
@app.route("/approvednurses", methods=['POST'])
def nurseesapproved_addingmore():
	an={'nurse':request.json['nurse']}
	approvednurses.append(an)
	return jsonify({'Messgae ':'Successfully Posted'})


'''=================the following code are for the PUT METHOD================== '''
# fulltime=[{'allday':'Dentist-Mike'},{'allday':'Gynaecologist-Duke'},{'allday':'Occulist-Greg'}]
# approvednurses=[{'nurse':'Dental-Mia'},{'nurse':'Gynal-Dian'},{'nurse':'Skin-Greggory'}]
# specialists=[{'spec':'Dental-Kyle'},{'spec':'Nerval-Pyke'},{'spec':'Bones-Dreg'}]
# databank=[{'hospitalstaff':'fulltime'},{'hospitalstaff':'approvednurses'},{'hospitalstaff':'specialists'}]


'''this endpoint modify the staffcategory of the hospital'''
@app.route("/staff/<string:hospitalstaff>", methods=['PUT'])
def staff_specifiedto_be_changed(hospitalstaff):
	grp=[ k for k in databank if k['hospitalstaff']== hospitalstaff]
	grp[0]['hospitalstaff']= request.json['hospitalstaff']
	return jsonify({'Messgae ':'Successfully Posted'})
	

'''this endpoint modifythe staffcategory particularly nurses of the hospital'''
@app.route("/approvednurses/<string:specified>", methods=['PUT'])
def approvednurses_specific_to_be_changed(specified):
	dec=[h for h in approvednurses if h['nurse']== specified]
	dec[0]['nurse']=request.json['nurse']
	return jsonify({'you have selected':dec[0]})

'''this endpoint modifythe staffcategory particularly specialists of the hospital'''
@app.route("/specialists/<string:specified>", methods=['PUT'])
def specialists_specific_to_be_changed(specified):
	dec=[h for h in specialists if h['spec']== specified]
	dec[0]['spec']=request.json['spec']
	return jsonify({'you have selected':dec[0]})


'''=================the following code are for the DELETE METHOD================== '''
# fulltime=[{'allday':'Dentist-Mike'},{'allday':'Gynaecologist-Duke'},{'allday':'Occulist-Greg'}]
# approvednurses=[{'nurse':'Dental-Mia'},{'nurse':'Gynal-Dian'},{'nurse':'Skin-Greggory'}]
# specialists=[{'spec':'Dental-Kyle'},{'spec':'Nerval-Pyke'},{'spec':'Bones-Dreg'}]
# databank=[{'hospitalstaff':'fulltime'},{'hospitalstaff':'approvednurses'},{'hospitalstaff':'specialists'}]


'''this endpoint modify the staffcategory of the hospital'''
@app.route("/staff/<string:hospitalstaff>", methods=['DELETE'])
def staff_specifiedto_be_deleted(hospitalstaff):
	grp=[ k for k in databank if k['hospitalstaff']== hospitalstaff]
	databank.remove(grp[0])
	return jsonify({'Messgae ':'Successfully deleted'})
	

'''this endpoint modifythe staffcategory particularly nurses of the hospital'''
@app.route("/approvednurses/<string:specified>", methods=['DELETE'])
def approvednurses_specific_to_be_deleted(specified):
	dec=[h for h in approvednurses if h['nurse']== specified]
	databank.remove(dec[0])
	return jsonify({'Messgae ':'Successfully deleted'})

'''this endpoint modifythe staffcategory particularly specialists of the hospital'''
@app.route("/specialists/<string:specified>", methods=['DELETE'])
def specialists_specific_to_be_deleted(specified):
	dec=[h for h in specialists if h['spec']== specified]
	databank.remove(dec[0])
	return jsonify({'Messgae ':'Successfully deleted'})

if __name__ =='__main__':
	app.run(debug=True)