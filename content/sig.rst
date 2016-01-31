What is "signature.asc"?
########################

:Date:		12-08-2014
:Category:	Security
:slug:      sig
:Summary: 	Explanation of the "signature.asc attachment" on all emails I send. 

The "signature.asc" attachment on my emails is my digital PGP signature. It allows people to verify that the email they recieved came from me and was not modified by a third party. Most people can completely ignore it and continue reading my email.

Where can I get your PGP keys?
------------------------------
A list of my `PGP keys are avalible here`__

__ {filename}/pages/pgp.md

Aren't PGP signatures usually big blocks of gibberish at the bottom of the email?
---------------------------------------------------------------------------------
There are two types of PGP signatures: inline armor (big block of gibberish) and PGP/MIME attachment (signature.asc). Inline PGP signatures ahave been around longer, but they don't play nicely with attachments or HTML formatted emails. Also, the big block of gibberish tends to confuse people more than an attachment. 

Still have Questions?
---------------------
If PGP interests you or you want to know more about PGP read `my article on PGP.`__ 

__ {filename}/pgp.rst
