

Our project accomplished an online home-sharing platform where people can post their home, search for a destination accommodation, chat with like-minded people, save travel expense and make friends all over the world. Making a perfect journey plan based on the search, share engine and online chat-system we have provided.

Initially, our application is inspired by the real-life scenario that when holiday comes, travelers leave their home empty, and pay for accommodation at the destination. An idea just comes to us that why can’t people share homes with others who want to travel to their place. Specifically, when people make their holiday plans, they can come to our website and find someone who also wants to travel to their base cities, then the two groups exchange their homes and set foot on the journey with excitement, but without paying anything.


## The data in your database

Our data include two parts mainly, the first part is basic user information including the user-name, password and relevant record. The second is home post data which is divided into several relation schema including house, city, post information.
To make sure our data is accurate and reliable. We have create a python crawling program using request and lxml package to collect data from some well-known home sharing website such as Airbnb and Homestay, and parse the html file with XQuery and extract the data we need. As a result, 700 real data in-total around 7 major US cities including NYC, LA, Chicago, etc., are collected to empower our project. Then 667 valid data are imported into our database after cleaning and processing to ensure data validation.


The functionality of your application (feature specs)
1) Allows users to login, for personal post management and recommendations.
2) Insert/delete/update house post in our database.
3) Search the items in the database, including posts that meets only partial requirement
4) Our application allows user to leave comments under a post.
5) Our application allows user to chat with another user.



7.   Explain one basic function

We will show the basic insert function here.

1) User click ‘post’ to make a new post





2)User fill in informations





3) The new post is added.



           



8.   Show the actual SQL code snippet

 

 

 



 9.   List and briefly explain the dataflow, i.e. the steps that occur between a user entering the data on the screen and the output that occurs (you can insert a set of screenshots)

1) the user clicks "More Post" button on index.html





2)  The frontend changes the URL and user enters the form interface





3) User fill in the form and click submit. Server get the post request and create a new record in Django interface



4) Then the Django engine will trigger the python codes, including the MyItems functions



5) After Django engine decides what data to query, it asks the database for the data, then wraps the data into JSON field through a serializer, then returns it to the server.  6) After the frontend engine receives the server's response, it re­renders the page and shows the queried data to the user.





10.  Explain your two advanced functions and why they are considered as advanced. Being able to do it is very important both in the report and final presentation.

Advanced function A: Smart Search

Search for places at a given destination is a crucial function for our website. Our search function is advanced because it shows result beyond users’ restrictions and also visualized the search result. Specifically, the search system not only tells user which posts fit exactly with user’s requirement, it also shows some post which satisfies most requirements.  Also, we provide a visualization for the searched results and use different markers indicating the level of matching in Google Map. This function is considered as advanced for the complex queries it used for a single search. The challenging part is to use sql to evaluate how many requirements a post satisfies and speed up the whole process to a satisfying level.



Advanced function A: Chat System

To facilitate successful exchanges, our website provides two places where users can communicate.

1) under each post, we provide our users a platform to ask availability, query details and post feedbacks, making the transactions more flexible.

2) We provide a chat system for private conversations. The chat system is considered as advanced for its usefulness and technique challenges it involve.



The implementation includes new UI design, multiple new models and new functions and joining queries from existing data sets. The new data models involve joining of two previous tables since a chat message are between two users over a post.



11.   Describe one technical challenge that the team encountered.  This should be sufficiently detailed such that another future team could use this as helpful advice if they were to start a similar project or were to maintain your project. Say you created a very robust crawler - share your knowledge. You learnt how to visualize a graph and make an interactive interface for it - teach all! Know how to minimize time building a mobile app - describe!



Unfamiliar with the CSS. The first challenge is to show the content properly, for example, the position of the slider and the number of pictures displaying on it. The picture we got from Airbnb is fixed size, most of them are smaller than the slider size we set, so the slider looks ugly when we use the original pic, so we changed the number of pictures from one to two, and changed the style of the slider by reading CSS document.

The second one is saving changes of the database in Django, as we changed some of the database schema, we found it always had some errors when we run manage.py, such as the datatype can’t be changed, or can’t import data from the csv file, so at first, we could only delete all of our code in model.py and did it again, then after so many times of trying, we found whenever we changed the database, it added an additional migration file, so we changed the migration file directly and de-apply some of the migration file by using this command: migrate yourprojectName migrationFile_number, such as migrate shareLife 0001 to apply the file we want to apply.



12.   State if everything went according to the initial development plan and proposed specifications, if not - why?!

No, not everything is going on according to the plan.

The first thing is our chat room. At first, we just plan to build a message board to display the message between two users, but it just lists all the messages in the post detail page, so we decided to change it to a live chat room, because displaying the message on the right of the page is not beautiful with the increase of the messages, and it’s not convenient for users to get in touch with each other.

The second one is the google map, we supposed to add a link to the marker, so that the user can get detailed information about the house when he or she click the marker, but it need some time to figure out how to add a link on the map, and we need to change our message board to chat room at that time, so we decided to improve one of our advanced function and just let it go.



13.   Describe the final division of labor and how did you manage team work.

Data crawler and database maintenance: Xuefeng Qin

Back-end development, smart search function and chat room: Yangyang Dai

Front-end development and web-page design: Bo Zhao

All: model construction, web framework design, function testing and UI design.

