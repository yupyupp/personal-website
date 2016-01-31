Title:		MeeBee
Date:		2016-01-27
parent:		projects.md
parents:	projects.md
children:	None
page_order:	3
Meebee is a data storage back-end that aims to honor user privacy while maintaining compatibility with standardized protocols. This project has been in the back of my mind for quite some time and I finally started working on it at OHI/O 2015 with my friend [Daniel Gratz](https://github.com/gratzdhg). While we weren't even able to get a working prototype finished by the end of the hack-a-thon, we were able to lay a good groundwork that we are continuing to develop.

## Technical details
 - User only needs username & password to authenticate
 - Every user gets her own public/private key pair
 - Public key is stored in plain text
 - Private key is encrypted with a salt of the user password
 - User data is encrypted to the user's key before it is stored

## Why is this project important?
 - Data on the server cannot be accessed by anyone without the user's credentials
 - Encryption is transparent to the end user. They don't need to enter a secondary password.
 - Using asymmetric encryption allows for data to be encrypted to the user when the user is not logged in (e.g. Incoming mail)
