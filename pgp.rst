Intro to PGP
############

:Date:		12-09-2014
:Category:	Security
:Summary:    High-level explanation of public key cryptography

Public and Private Keys
-----------------------
When someone uses PGP they generate a pair of keys; one private key and one public key. The private key is kept by the person who made it and the public key is given to anyone she/he wants to communicate with.

Signing vs Encryption
---------------------
PGP can accomplish two things, encryption and signing. **Signing** is used to verify that a message or file came from a certain person and has not been tampered with. **Encryption** is used to make the contents of a message or file private so it is unreadable to anyone but the desired recipient. 

Signing does NOT provide privacy and encryption does NOT provide verification! To achieve both privacy and validation, a message or file must be both signed and encrypted. The following examples attempt to illustrate this.

No PGP
``````
Alice sends Bob an email but Eve intercepts the email. Not only is Eve able to read Alice's message, she is also able to change the message before Bob reads it and neither Eve nor Bob know that the message was read and modified by Eve.

Eve poses as Alice and sends Bob a message. Since Bob and Alice do not use PGP, Bob has no way of knowing that the message did not come from Alice.

Just Signing
`````````````
Alice signs a message with her private key and emails it to Bob. Eve intercepts the email and is able to read it, but she notices that is has been signed by Alice. If Eve modifies the message Bob will know when he tries to use Alice's public key to verify the signature.

Eve poses as Alice and sends Bob a message. Since Bob expects all of Alice's messages to be signed with her private key he is suspicious of the message and contacts Alice to check if she actually sent him the message.

Just Encryption
```````````````
Alice encrypts a message to Bob using Bob's public key. Eve intercepts the email but can not read the contents of the message since it is encrypted. Eve has no good way to modify the message because she doesn't know what the message contained. Bob receives the message and is able to decrypt and read it.

Eve poses as Alice and encrypts a message to Bob using Bob's public key. Bob receives the message and is able to decrypt and read it but has no way to know that Alice did not send it to him.

Signing and Encryption
``````````````````````
Alice encrypts a message to Bob using Bob's public key and signs it using her private key. Even intercepts the message but cannot read or modify it since it is encrypted and signed. Bob receives the message, uses Alice's public key to verify that the message came from Alice, and uses his private key to decrypt the message so he can read it.

Eve poses as Alice and encrypts a message to Bob using his public key. Bob receives the message and is able to decrypt it using his private key. 


Multiple Recipients
```````````````````
Alice signs a message with her private key and sends it to Bob and Charlie. Bob and Charlie are both able to use Alice's public key to verify that it came from Alice.

Alice encrypts a message using both Bob's and Charlie's public keys. Both Bob and Charlie are able to decrypt the message with their own private keys.

Signing Software
----------------
All of the examples in this article have been about signing and encrypting messages. PGP is often used to sign releases of certain software. For example, the developers of Debian publish a PGP signature for each version ISO so you can verify that the ISO was not corrupted or modified while you were downloading it.

Key signing (Web of Trust)
--------------------------
In additions to signing files and messages, PGP keys can also be signed. For example:

Alice knows that Bob's key belongs to Bob, so she signs Bob's public key. Bob knows that Charlie's key belongs to Charlie so Bob signs Charlie's public key. Since Alice's key trusts Bob's key and Bob's key trusts Charlie's key, Alice can be fairly confident that Charlie's key is trustworthy so she can trust anything signed with Charlie's key.
