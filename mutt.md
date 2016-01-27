Title:		Mutt CLI email client
Date:		2014-09-19
Category:	CLI Tools
Summary:	Mutt is an awesome CLI email client but it can be a pain to set up. I added config file templates for mutt and its supporting programs to my [dotfile git repo](https://git.kd8zev.net/?p=dotfiles.git). Download the templates and follow the directions below to get it all working.

Mutt is an awesome CLI email client but it can be a pain to set up. I added config file templates for mutt and its supporting programs to my [dotfile git repo](https://git.kd8zev.net/?p=dotfiles.git). Download the templates and follow the directions below to get it all working.

## Before you begin
This setup downloads all the mail to your computer, so do not use this method if you have limited disk space!

I have this setup on my server at home and I ssh into it from a tmux session from my desktop and laptop to check and send mail. This makes handling attachments very difficult. I am currently testing different methods of sending attachments back and forth without having to manually scp everything.

I also assume you only have one address book/CardDav account that you use for all your contacts

## Required Programs
 - mutt - Duh
 - vim - To write mail
 - offlineIMAP - To sync all your messages with the mail servers
 - msmtp - To sent the mail using smtp
 - python-pycard - To syncronize contacts with a CardDav server
 - links - To view HTML formatted emails

## Directions
 - Grab the config file templates from [my git repository](https://git.kd8zev.net/?p=dotfiles.git)
 - All the "DOT.*" files are supposed to be hidden files/folders.  Rename them to ".*"
 - Move these files into your home directory
 - Edit .offlineimaprc
   - Replace "ACCOUNT_#" with whatever names you want
   - Replace "imap.domain.com", "user@domain.com", "email@domain.com", and "****" with the correct information
     - (NOTE: Unless you are setting up aliases, "user@domain.com" and "email@domain.com" are usually the same thing
   - Run "offlineimap" to create the folders and do an initial mail sync (This may take a very long time)
 - Edit .msmtprc
   - Replace "ACCOUNT_#" with the same names you used in .offlineimaprc 
   - Replace "smtp.domain.com", "user@domain.com", "email@domain.com", and "****" with the correct information
 - Edit .muttrc
   - Replace "ACCOUNT_#" with the same names you used in .offlineimaprc 
   - Replace "KEY_ID" with the key you want to use for signing
 - Edit .mutt/ACCOUNT_#
   - Rename ".mutt/ACCOUNT_#" with the same names you used in .offlineimaprc 
   - Replace "ACCOUNT_#" in each of the files with the same names you used in .offlineimaprc
 - Edit .mutt/macros
   - Replace "ACCOUNT_#" with the same names you used in .offlineimaprc 
 - Edit .mutt/sigs/ACCOUNT_#
   - Rename ".mutt/sigs/ACCOUNT_#" with the same names you used in .offlineimaprc
   - Replace the contents of each with your signature
 - Edit .config/pycard/pycard.conf
   - Replace "userneme", "****", and "https://carddavurl.com" with the proper information
   - Run "pycardsyncer" to so an initial address book sync
 - Add a cron job to run offlineimap and pycardsyncer regularly
	- (NOTE: Instead of syncing every account's whole mailbox every minute, you might want to just sync the INBOX forlders every minute with "offlineimap -f INBOX" and do a full sync once or twice a day)

## TODO
 - Find a good way to handle attachments (Reverse port forwards and scp?)
 - Find a good way to not store the passwords in plain text
 - Create a auto-setup script
