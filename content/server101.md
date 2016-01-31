Title:		Server 101
Date:		2014-11-02
Category:	Server
Summary: 	A brief overview of making a GNU/Linux box into a web-facing server. Covers domain names, sshd config, iptables, basic Apache, and SSL certificates.


## Before you begin
This guide is meant to be a set of suggestions to help point you in the right direction. I do provide some example config files but they are __only examples__.
I also mention several services that I have used and found helpful. I am not endorsing these services and encourage you to find if there is a service that suits your needs better.

This guide also makes a few assumptions:

 - You have a machine or VPS with some sort of linux already installed
 - You can figure out how to [forward ports](http://portforward.com/)
 - You understand that different distributions put config files in different places (This guide is based on Debian)
 - You know how to get around a linux system

## Domain Name

*If you don't understand what domain names are and how DNS works I suggest skimming the wikipedia article on [the Domain Name System](http://en.wikipedia.org/wiki/Domain_Name_System)*

There are two ways of getting a domain name. You can buy your own domain name for a website like [NameCheap](https://namecheap.com) or [gandi.net](https://gandi.net) or you can get a subdomain for free from websites like [duckDNS](https://duckdns.org) or [No-IP](noip.com) (You will not be able to use SSL or HTTPS with a verified SSL certificate if you are on a subdomain).

## SSH Daemon Config

The ssh config file is usually located in /etc/ssh/sshd_config on Debian based systems.  The main thing to worry about is disabling root login. This is important to do, because logging in as root is bad practice and, more importantly, everyone will try to bruteforce into your server as user "root" (take a look at /var/log/auth.log if you don't believe me). Other ways to secure SSH are to only allow [SSH key login](https://help.ubuntu.com/community/SSH/OpenSSH/Keys) and only allow certain users to login with ssh. The relevant options are below.

<pre>
PermitRootLogin no
AllowUser USER
PasswordAuthentication no # Make sure you have public key authentication set up if you do this
</pre>

Another way to secure ssh is by using [fail2ban](https://en.wikipedia.org/wiki/Fail2ban), a service that ssh login attempts and will block an IP address of someone who has failed to log into you server after a set amount of times. In Debian based systems if you install it it will set itself up and start automatically. The config files for fail2ban are usually in /etc/fail2ban/ the default options are usually fine, but it would be a good idea to read through the fil2ban man page to see if there are any other options you want to set.

## Firewall with iptables
For some reason most Linux distributions (Debian and Ubuntu server included) ship with all ports open. Having all your ports open is pretty risky, especially if your computer if facing the open internet. The sample iptables rules below are based on [this Arch Linux wiki article](https://wiki.archlinux.org/index.php/Simple_stateful_firewall) but was modified to work with fail2ban.

<pre>
# Sample iptables rules.
*filter
:INPUT DROP [0:0]
:FORWARD DROP [0:0]
:OUTPUT ACCEPT [0:0]
:fail2ban-ssh - [0:0]
:TCP - [0:0]
:UDP - [0:0]
-A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
-A INPUT -i lo -j ACCEPT
-A INPUT -p icmp -m icmp --icmp-type 8 -m conntrack --ctstate NEW -j ACCEPT
-A INPUT -p udp -m conntrack --ctstate NEW -j UDP
-A INPUT -p tcp -m tcp --tcp-flags FIN,SYN,RST,ACK SYN -m conntrack --ctstate NEW -j TCP
-A INPUT -p udp -j DROP
-A INPUT -p tcp -j DROP
## SSH rules
-A TCP -p tcp -m multiport --dports 22 -j fail2ban-ssh
-A fail2ban-ssh -j RETURN
-A TCP -p tcp -m tcp --dport 22 -j ACCEPT
## HTTP(s) rules
-A TCP -p tcp -m tcp --dport 80 -j ACCEPT
-A TCP -p tcp -m tcp --dport 443 -j ACCEPT 
COMMIT
</pre>

To open additional ports just add them to the UPD or TCP chain depending on what type of traffic you want to allow. Any IP addresses that fail2ban blocks will be added to the fail2ban-ssh chain. To use this set of rules save it in a file and use iptables-restore to load it. Depending on your system, you might need to write a script to reload the rules on boot.

## Apache and Virtual Hosts

Apache defaults to serving content form /var/www in Debian based systems. If you want to serve different content on different domains on the same server, you will want to take a look into Apache virtual hosts. The sample vhost below will server content out of /home/apache/sites/www.sample.com/ when someone is visiting the server with the domain name sample.com or www.sample.com

<pre>
&ltVirtualHost *:80&gt
    ServerName www.sample.com
    ServerAlias sample.com
    DocumentRoot /home/apache/sites/www.sample.com
&lt/VirtualHost&gt
</pre>

## SSL Certificates and Related Apache config

*There is an excellent article on how to use generate SSL certificates with StartSSL [here](http://wiki.stocksy.co.uk/wiki/Using_StartCom_%28StartSSL%29_to_Generate_valid_SSL_Certificates#Generate_a_CSR_and_Private_Key).*

Before you use ssl with Apache, you will need to make sure you have port 443 open for tcp connections and you will have to enable mod_ssl in Apache. On this site, I redirect all standard http requests to https requests with the following config that I placed on /etc/apache2/conf.d/force_ssl.conf

<pre>
&ltVirtualHost *:80&gt
    ServerAlias *
    RewriteEngine On
    RewriteRule ^(.*)$ https://%{HTTP_HOST}$1 [redirect=301]
&lt/VirtualHost&gt
</pre>

Another good idea to protect the people who use you server is to prefer [Perfect Forward Secrecy (PFS)](https://en.wikipedia.org/wiki/Forward_secrecy#Perfect_forward_secrecy) with the following config.

<pre>
SSLProtocol +TLSv1.2 +TLSv1.1 +TLSv1
SSLCompression off
SSLHonorCipherOrder on
SSLCipherSuite ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-RC4-SHA:ECDHE-RSA-AES256-SHA:DHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES256-SHA256:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA:RC4-SHA:AES256-GCM-SHA384:AES256-SHA256:CAMELLIA256-SHA:ECDHE-RSA-AES128-SHA:AES128-GCM-SHA256:AES128-SHA256:AES128-SHA:CAMELLIA128-SHA
Header add Strict-Transport-Security "max-age=15768000;includeSubDomains"
</pre>

After you set this option, you will have enable mod_rewrite and to modify your virtual hosts to use your SSL certificates. An example virtual host is below:

<pre>
&ltVirtualHost *:443&gt
    ServerName sample.com
    ServerAlias www.sample.com
    DocumentRoot /home/apache/sites/www.sample.com
    SSLEngine On
    SSLCertificateFile /CA/certs/www.sample.com-startssl-cert-YYY.pem
        SSLCertificateKeyFile /CA/keys/www.sample.com-startssl-key-YYYY-MM-DDTHH:MM:SS.pem
        SSLCertificateChainFile /CA/startssl/sub.class1.server.ca.pem
        SSLCACertificateFile /CA/startssl/ca.pem
&lt/VirtualHost&gt
</pre>

Once you have SSL all set up on your server you can check your server with [Qualys SSL test](https://www.ssllabs.com/ssltest/). It will probably say something about having a weak signature algorithm if you use StartSSL because of the way StartSSL signs certificates for now. Hopefully StartSSL will start signing certificates with SHA256 soon.

## Conclusion

Once you have your basic webserver setup working, it is relatively easy to set up other web-based services. If you are looking for an easy way to generate a website with static content check out [pelican](http://blog.getpelican.com/). I use pelican with [my custom theme](https://github.com/kd8zev/pelican-theme-zev) to generate this site. Hope this helped to get your server set up! If you have any questions about this guide shoot an email to stephen at this domain.
