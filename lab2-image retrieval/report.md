# Lab 2: Information Retrieval

Author:王星洲

StudentID:1652977

brief: This file is the report of lab2, please make sure you have read the `readme` file before and have successfully run this project.



## Project implementation

### Formulation

I use `bootstrp2` to build the template. To make a beautiful website, I use carousel, navigation bar, tabbable and many other components to build this page. 

I have the input box to upload an image,:

![1558018221030](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1558018221030.png)

User can choose the picture and upload it.

### Initiation

I have the search button, when you press that search button, the website will post an ajax request to the back-end, and accept the value it return. Then it can be changed into pictures and give user the result.

This part of code is like this:

```javascript
			function fun() {

				$('#load').show();

				$("form").submit(function(evt) {
					//$('#loader-icon').show();

					evt.preventDefault();

					//$('#loader-icon').show();
					var formData = new FormData($(this)[0]);

					$.ajax({
						url: 'imgUpload',
						type: 'POST',
						data: formData,
						//async: false,
						cache: false,
						contentType: false,
						enctype: 'multipart/form-data',
						processData: false,

						success: function(response) {
							$('#load').hide();
							$('#row1').show();
							//console.log(response[1]);
							//document.getElementById("predictedResult").innerHTML= response;
							document.getElementById("img0").src = response.image0;
							document.getElementById("img1").src = response.image1;
							document.getElementById("img2").src = response.image2;
							document.getElementById("img3").src = response.image3;
							document.getElementById("img4").src = response.image4;
							document.getElementById("img5").src = response.image5;
							document.getElementById("img6").src = response.image6;
							document.getElementById("img7").src = response.image7;
							document.getElementById("img8").src = response.image8;
							$('#table').show();
							$('#clear').show();
							$('#searchResult').show();
						}
					});
					return false;
				})
			};
```

### Review

The return value will be shown in the form table, the code is also above.

### Refinement

​	I make tags to filter the result. (dog and human), you can also add other tags if you have understood my codes. If you press `dog` tag, It will show you the pictures in the original result in `dog.txt`and "No result!" elsewhere. It’s the same when you press `human` tag, the difference is that it will give you the pictures in `people.txt`.

​	Its implement is a little difficult. First from the front-end, it post a requirement:

```javascript
var num0 = response.image0.replace(/[^\d]/g, '');
						var num1 = response.image1.replace(/[^\d]/g, '');
						var num2 = response.image2.replace(/[^\d]/g, '');
						var num3 = response.image3.replace(/[^\d]/g, '');
						var num4 = response.image4.replace(/[^\d]/g, '');
						var num5 = response.image5.replace(/[^\d]/g, '');
						var num6 = response.image6.replace(/[^\d]/g, '');
						var num7 = response.image7.replace(/[^\d]/g, '');
						var num8 = response.image8.replace(/[^\d]/g, '');

						var arrayA = [num0, num1, num2, num3, num4, num5, num6, num7, num8]

						$.ajax({
							url: 'checkAnimal',
							type: 'POST',
							async: false,
							data: JSON.stringify({
								arrayAA: arrayA
							}),
							contentType: "application/json; charset=utf-8",
							dataType: "json",
```

Then the back-end accept the json file and judge whether it’s in  corresponding text file:

```python
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
```

And the front-end will deal with the result json and make sure whether the image is shown or not:

```javascript
success: function(res) {
    console.log(res);
    var a = res["result"];
    a.forEach(ele => {
        if(a.indexOf(ele) == 0) {
        	document.getElementById("img10").src = response.image0;
        } else if(a.indexOf(ele) == 1) {
       	 	document.getElementById("img11").src = response.image1;
        } else if(a.indexOf(ele) == 2) {
        	document.getElementById("img12").src = response.image2;
        } else if(a.indexOf(ele) == 3) {
        	document.getElementById("img13").src = response.image3;
        } else if(a.indexOf(ele) == 4) {
        	document.getElementById("img14").src = response.image4;
        } else if(a.indexOf(ele) == 5) {
        	document.getElementById("img15").src = response.image5;
        } else if(a.indexOf(ele) == 6) {
        	document.getElementById("img16").src = response.image6;
        } else if(a.indexOf(ele) == 7) {
        	document.getElementById("img17").src = response.image7;
        } else if(a.indexOf(ele) == 8) {
        	document.getElementById("img18").src = response.image8;
        }
	}
}
```

Then we will get the final result.

### Use

users will see how many results have returned:

```html
<td id="searchResult" style="display: none;">共查询到结果<b>{{ number }}</b>条。</td>
```

And use clear button to clean the pictures.

They can also use screenshot to save any of the pictures.



## Requirements

The requirements of image search task should be:

#### High similarity

your result should be like the original image of searching.

#### Know the user’s  requirement

If user search the image to find similar pictures, just show them. But most users use searching engine for other reasons: one may search it for recognizing what the picture is, others may search for downloading big   pictures. If you don’t know the users’ requirement, it will be a big trouble.

#### Guidance and interaction

Your searching engine should be easy to use, never let users guess how to use it.

#### Beautiful UI

If the image-searching engine has an ugly form, who will use it?