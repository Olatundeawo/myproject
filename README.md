# Connecta

Project Description
# Connecta is a social media web app designed to bring people together in a digital world.
Connecta aims to foster a sense of community among users by facilitating meaningful discussions, promoting intellectual growth, and encouraging collaboration.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.txt.

```bash
pip install -r requirements.txt
```


## Why I choosed to work on this project
I used social media app so much, the experience i got from using the social media app got me captivated, 
 I love the way people can freely bear out their mind, engage in a lot of forum, meet alot of new friends sometimes awful(LOL). 
 I hope to give people good sense of comfort from using socia media web app.

## Technologies used

1. Front-end Technologies:
	HTML5: Markup language for structuring the web app's content.
	CSS3: Styling language used to design and format the app's user interface. I choosed 	to used bootsrap has a framework so has to assist in making the site more responsive.
	JavaScript: Programming language for implementing interactive features and client-	side functionality.
2. Back-end Technologies:
	Python:
	Web frameworks: Flask (Python),  for efficient development and handling server-side 	logic.
	Uses Object Relational Mapper(ORM): SQLAlchemy. I used SQLAlchemy cause it 	makes me switch between different databases without changing my application code 	significantly  
3. Authentication and Security:
	Encryption and hashing algorithms: To secure sensitive user data, such as passwords.
	SSL/TLS: To ensure secure communication between the web app and users' devices.

## Some of the challenges faced

While developing the project I planned on making the password the users enter safe and secure, 
this led me to search on how to secure a password, in my search I got to learn of encryption and hashing algorithms, 
I went along with bcrypt, which incorporates a salt and a cost factor. After incorporating bcrypt, 
It turned out to produce a bug in code, a bug which makes the password entered while signing up incorect while login, 
this led to alot of stresses and searches. It was later discovered that the hashing was not rightly incorporated because I didn't decode the password.

## Features I planned to implement in future

1. Incorporate Google login has an additional login features.
2. Design a messaging features where users can message each other.
3. Use a feature that will flag users if post some words known to be foul


## Credits

1. digitaloceans.com
2. w3schools.com
3. freecodecamp.com
4. stack overflow
5. geeksforgeeks



## Contact
1. [Twitter](https://twitter.com/bokinsin)
2. [LinkedIn](https://www.linkedin.com/in/babatunde-awotimilehin-284a25180/)
3. [project landingpage](https://olatundeawo.github.io/olatundewo.github.io/)
4. [Project website](https://intranet.alxswe.com/projects/www.realbabatundeawotimilehin.tech)

## License

[MIT](https://choosealicense.com/licenses/mit/)
