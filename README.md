## ShareLife A Homesharing Project

Our project accomplished an online home-sharing platform where people can post their home, search for a destination accommodation, chat with like-minded people, save travel expense and make friends all over the world. Making a perfect journey plan based on the search, share engine and online chat-system we have provided.

Initially, our application is inspired by the real-life scenario that when holiday comes, travelers leave their home empty, and pay for accommodation at the destination. An idea just comes to us that why can’t people share homes with others who want to travel to their place. Specifically, when people make their holiday plans, they can come to our website and find someone who also wants to travel to their base cities, then the two groups exchange their homes and set foot on the journey with excitement, but without paying anything.


## The data in the database

Our data include two parts mainly, the first part is basic user information including the user-name, password and relevant record. The second is home post data which is divided into several relation schema including house, city, post information.
To make sure our data is accurate and reliable. We have create a python crawling program using request and lxml package to collect data from some well-known home sharing website such as Airbnb and Homestay, and parse the html file with XQuery and extract the data we need. As a result, 700 real data in-total around 7 major US cities including NYC, LA, Chicago, etc., are collected to empower our project. Then 667 valid data are imported into our database after cleaning and processing to ensure data validation.


## Functionality of the application 
1) Allows users to login, for personal post management and recommendations.
2) Insert/delete/update house post in our database.
3) Search the items in the database, including posts that meets only partial requirement
4) Our application allows user to leave comments under a post.
5) Our application allows user to chat with another user.


## List and brief explaination about the dataflow

1) the user clicks "More Post" button on index.html
2)  The frontend changes the URL and user enters the form interface
3) User fill in the form and click submit. Server get the post request and create a new record in Django interface
4) Then the Django engine will trigger the python codes, including the MyItems functions
5) After Django engine decides what data to query, it asks the database for the data, then wraps the data into JSON field through a serializer, then returns it to the server.  6) After the frontend engine receives the server's response, it renders the page and shows the queried data to the user.

## Explaination about the two advanced functions.

### Advanced function A: Smart Search
Search for places at a given destination is a crucial function for our website. Our search function is advanced because it shows result beyond users’ restrictions and also visualized the search result. Specifically, the search system not only tells user which posts fit exactly with user’s requirement, it also shows some post which satisfies most requirements.  Also, we provide a visualization for the searched results and use different markers indicating the level of matching in Google Map. This function is considered as advanced for the complex queries it used for a single search. The challenging part is to use sql to evaluate how many requirements a post satisfies and speed up the whole process to a satisfying level.



### Advanced function A: Chat System
To facilitate successful exchanges, our website provides two places where users can communicate.
1) under each post, we provide our users a platform to ask availability, query details and post feedbacks, making the transactions more flexible.
2) We provide a chat system for private conversations. The chat system is considered as advanced for its usefulness and technique challenges it involve.


