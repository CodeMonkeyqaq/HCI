#!flask/bin/python
######################################################################################################################
# ---------------------------------------------------------------------------------------------------------------------
# This file implements the REST layer.
# It uses flask micro framework for server implementation. Calls from front end reaches
# here as json and being branched out to each projects. Basic level of validation is also being done in this file.
# ---------------------------------------------------------------------------------------------------------------------
######################################################################################################################
from flask import Flask, jsonify, abort, request, make_response, url_for,redirect, render_template
from flask_httpauth import HTTPBasicAuth
from werkzeug.utils import secure_filename
import os
import shutil 
import numpy as np
import json
from search import recommend
from tensorflow.python.platform import gfile
import tarfile
from datetime import datetime
from scipy import ndimage
from scipy.misc import imsave 
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app = Flask(__name__, static_url_path="")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
auth = HTTPBasicAuth()
number = 9

# ====================================================================================================================
#                                                                                                                              
#    Loading the extracted feature vectors for image retrieval                                                                 
#                                                                          						        
#                                                                                                                              
# ====================================================================================================================
extracted_features = np.zeros((10000, 2048), dtype=np.float32)
with open('saved_features_recom.txt') as f:
			for i, line in enumerate(f):
				extracted_features[i, :] = line.split()
print("loaded extracted_features") 


# ======================================================================================================================
#                                                                                                                              
#  This function is used to do the image search/image retrieval
#                                                                                                                              
# ======================================================================================================================
@app.route('/imgUpload', methods=['GET', 'POST'])
# def allowed_file(filename):
#    return '.' in filename and \
#           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_img():
	print("image upload")
	result = 'static/result'
	if not gfile.Exists(result):
		  os.mkdir(result)
	shutil.rmtree(result)
	if request.method == 'POST' or request.method == 'GET':
		print(request.method)
		# check if the post request has the file part
		if 'file' not in request.files:
			print('No file part')
			return redirect(request.url)

		file = request.files['file']
		print(file.filename)
		# if user does not select file, browser also
		# submit a empty part without filename
		if file.filename == '':

			print('No selected file')
			return redirect(request.url)
		if file:# and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			inputloc = os.path.join(app.config['UPLOAD_FOLDER'], filename)
			recommend(inputloc, extracted_features)
			os.remove(inputloc)
			image_path = "/result"
			image_list = [os.path.join(image_path, file) for file in os.listdir(result)
							  if not file.startswith('.')]
			images = {
			'image0': image_list[0],
			'image1': image_list[1],
			'image2': image_list[2],
			'image3': image_list[3],
			'image4': image_list[4],
			'image5': image_list[5],
			'image6': image_list[6],
			'image7': image_list[7],
			'image8': image_list[8]
			  }
			return jsonify(images)


@app.route('/imgUpload1', methods=['GET', 'POST'])
# def allowed_file(filename):
#    return '.' in filename and \
#           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_img1():
	print("image upload")
	result = 'static/result'
	if not gfile.Exists(result):
		os.mkdir(result)
	shutil.rmtree(result)
	if request.method == 'POST' or request.method == 'GET':
		print(request.method)
		# check if the post request has the file part
		if 'file' not in request.files:
			print('No file part')
			return redirect(request.url)

		file = request.files['file']
		print(file.filename)
		# if user does not select file, browser also
		# submit a empty part without filename
		if file.filename == '':
			print('No selected file')
			return redirect(request.url)
		if file:  # and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			inputloc = os.path.join(app.config['UPLOAD_FOLDER'], filename)
			recommend(inputloc, extracted_features)
			os.remove(inputloc)
			image_path = "/result"
			image_list = [os.path.join(image_path, file) for file in os.listdir(result)
						  if not file.startswith('.')]
			images = {
				'image0': image_list[0],
				'image1': image_list[1],
				'image2': image_list[2],
				'image3': image_list[3],
				'image4': image_list[4],
				'image5': image_list[5],
				'image6': image_list[6],
				'image7': image_list[7],
				'image8': image_list[8]
			}
			return jsonify(images)


@app.route('/imgUpload2', methods=['GET', 'POST'])
# def allowed_file(filename):
#    return '.' in filename and \
#           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_img2():
	print("image upload")
	result = 'static/result'
	if not gfile.Exists(result):
		  os.mkdir(result)
	shutil.rmtree(result)
	if request.method == 'POST' or request.method == 'GET':
		print(request.method)
		# check if the post request has the file part
		if 'file' not in request.files:
			print('No file part')
			return redirect(request.url)

		file = request.files['file']
		print(file.filename)
		# if user does not select file, browser also
		# submit a empty part without filename
		if file.filename == '':

			print('No selected file')
			return redirect(request.url)
		if file:# and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			inputloc = os.path.join(app.config['UPLOAD_FOLDER'], filename)
			recommend(inputloc, extracted_features)
			os.remove(inputloc)
			image_path = "/result"
			image_list = [os.path.join(image_path, file) for file in os.listdir(result)
							  if not file.startswith('.')]
			images = {
			'image0': image_list[0],
			'image1': image_list[1],
			'image2': image_list[2],
			'image3': image_list[3],
			'image4': image_list[4],
			'image5': image_list[5],
			'image6': image_list[6],
			'image7': image_list[7],
			'image8': image_list[8]
			  }
			return jsonify(images)
# =========================================================================================================
#                                                                                                                              
#                                           Main function
#  				                                                                                                
# =========================================================================================================


@app.route('/checkAnimal', methods=['GET', 'POST'])
def check():
	print("checkAnimals");
	if request.method == 'POST':
		a = request.get_data()
		dict1 = json.loads(a)
		arr = dict1["arrayAA"]
		result = []
		f = open("./database/tags/dog.txt")
		line = f.readline()
		while line:
			line = f.readline()
			line = line.split('\n')[0]
			if line in arr:
				print(line)
				result.append(line)
		f.close()

	print(result)

	res = {
		"result": result
	}
	return jsonify(res)


@app.route('/checkHuman', methods=['GET', 'POST'])
def check1():
	print("checkHuman");
	if request.method == 'POST':
		a = request.get_data()
		dict1 = json.loads(a)
		arr = dict1["arrayAA"]
		result = []
		f = open("./database/tags/people.txt")
		line = f.readline()
		while line:
			line = f.readline()
			line = line.split('\n')[0]
			if line in arr:
				print(line)
				result.append(line)
		f.close()

	print(result)

	res = {
		"result": result
	}
	return jsonify(res)


@app.route("/")
def main():
	value = str(number)
	return render_template("main.html", number=value)


@app.route("/animal")
def animal():
	return render_template("animal.html")


@app.route("/human")
def human():
	return render_template("human.html")


if __name__ == '__main__':
	app.run(debug=True, host='127.0.0.1')