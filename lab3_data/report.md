# Lab 3: Data Visualization

Author:王星洲

StudentID:1652977

brief: This file is the report for the program.



## Purpose

​	As a Android developer, Google play store data means a lot to me. I need to find out the currently popular apps, find out their features, analyze the content of the apps, find out the types of various apps and the market share, so as to judge what kind of app I should make to seize the market.



## Executive Summary

​	I analyzed the data from Google play store, visualized the data and searched for the needed data, and analyzed based on it. This will affect the direction of my next app. I've been struggling lately not knowing which app model to emulate. I decided to analyze the visualization data carefully, and this report discusses my findings.



## Dataset

​	I was given 10,840 pieces of data about apps on the Google play store. The data contains App name, Category, Rating, Reviews, Size, Installs, Type, Price, Content Rating, Genres, Updated Time and Version. This data is consolidated in `googleplaystore.csv` and included in my submission, which you can view at any time to confirm its contents.



## Software

​	The dataset is based on `.csv` file and needed support by `Microsoft Excel`.  And in order to achieve **data visualization**, I adopted `python+dash+plotly` to display the data graphically and deploy it to the browser for display. 



## Analysis

### Using of Bar Graph

​	Firstly, it is necessary to obtain various data of a particular app. For example, the popularity of an app can be judged by its rating or the number of reviews, and then some or several successful apps can be selected for learning. I chose to do this with a bar chart, which is intuitive and useful.

![1559819751046](F:\CourseData\interact\Project\lab3_data\1559819751046.png)

​	For example, we can see instagram and facebook perfect very well in Reviews. We can learn the method of these app.



### Using of Scatter Graph

​	The number of reviews often reflects the popularity of the application, which is more important than the number of downloads. At the same time, we can get the rating of the application in the application market. There are also topical apps that are hot but annoying to consumers, and we can learn as needed.

​	To achieve this goal, it is a good idea to use a scatter plot. We use the application ratings and comments as horizontal and vertical coordinates, and look at the scatter plot to get the results.

![1559820163300](F:\CourseData\interact\Project\lab3_data\1559820163300.png)

​	`F.r Mike Audio Teachings` ... So poor app. It get 5 points but really low reviews. If you want your app to be hot, don’t learn to it. However, facebook, just 4.1 rating but really hot, a good teacher.



### Using of Pie Graph

​	Sometimes blind study facebook application is not a good idea, because they already dominate the market, it's hard to go to you a piece of cake, this needs us to market share to have certain understanding, when the number of a class of the app is not high, we can seize the opportunity to market, this needs us to analyze the classification of the app.

​	The best way to solve this kind of analysis is the pie chart. We can easily see the types of apps, downloads, and even the total distribution of the age group. In this way, we can choose some unpopular or user-required types for design and implementation.

![1559820558329](F:\CourseData\interact\Project\lab3_data\1559820558329.png)

![1559820581591](F:\CourseData\interact\Project\lab3_data\1559820581591.png)

​	We can easily get the point. But which category to choose is still a big problem to think deeply.



## Conclusion

​	I get a lot of inspiration through the analysis of google play store data, we've found some very the fire application nowadays, there are also some useful but unpopular application, we understand the types of individual application, convenient our own choice, the next app data visualization can do far more than these, but the developers have enough for us, hope every developer can develop a valuable and high-level application!