#DeltaSysadTask3

A chat room using python socket programming for delta inductions

##User manual

1. Ensure python of version more than 3.6 is installed in your computer.
2. Install pip
3. Run ```pip install pymongo``` and ```pip install passlib``` to install pymongo and passlib packages.
4. Ensure that mongodb is installed on your local machine and is listening on port 27017
5. By running ``` python addUser.py ``` you can add users to the database
6. Open the terminal inside your cloned folder and run ```python server.py```
7. Now,the server will be listening on connections in port 3000
8. Then, run ```python client.py``` to create a memeber of the chat room.
9. Any message sent by the client is sent to all other members of the rooms
10. To get chat history send the message **chat_history** through any client and a file with the name of the client containing chat history is created.
