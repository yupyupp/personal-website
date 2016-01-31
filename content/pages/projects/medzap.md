Title:		MedZap
Date:		2013-09-15
parent:		projects.md
parents:	projects.md
children:	None
page_order:	6
The was my team's project for the 2014 Cardinal Health Codefest. None of us had much experience with anything at the time, so it was largely a learning experience. 

Check out the code [here](https://github.com/yupyupp/cardinalCodefest2014). Below is the README we wrote. 

## MedZapp - Data Centralization and Client Communication

MedZapp is a comprehensive healthcare database that efficiently handles who can access a patient's data and optionally allows the patient to connect anonymously with other people with similar conditions.

Database
-----
Contains the following tables:
- loginData
    username, password, uID (user ID number), anon (boolean), doctor (boolean)
- permissions
    uID, category (type of contition), pID (patient ID number)
- medicalHistory
    uID, category, name (name of condition), date, description
- messages
    postCount, threadID, uID, content (of the message)
- threads 
    threadID, uID, partnerID

Notes
-----
This is NOT ready for deployment. It currently does not utilize data sanitation or encryption of any kind (aside from SSL). These and other security measures will be incorporated later.
