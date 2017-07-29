#!/usr/bin/python

import smtplib
import email.mime.text
import configparser
import os
import sys

class ReleaseManager:
    def __init__(self):
        self.debug=False
        self.config=ConfigParser.ConfigParser()
        self.name='releasemanager'
        self.config.read([self.name+'.cfg', os.path.expanduser('~/.'+self.name+'.cfg')])
        self.section='release'
        self.p_subject=self.config.get(self.section,'subject')
        self.p_from=self.config.get(self.section,'from')
        self.p_to=self.config.get(self.section,'to').split(',')
        self.p_smtp_host=self.config.get(self.section,'smtp_host')
        self.p_content=self.config.get(self.section,'content')
        self.p_mail_user=self.config.get(self.section,'mail_user')
        self.p_mail_password=self.config.get(self.section,'mail_password')
        self.p_twitter_user=self.config.get(self.section,'twitter_user')
        self.p_twitter_password=self.config.get(self.section,'twitter_password')
        self.p_debug=bool(self.config.get(self.section,'debug'))
        self.p_usetls=bool(self.config.get(self.section,'usetls'))

        self.p_email=bool(self.config.get(self.section,'email'))
        self.p_tweet=bool(self.config.get(self.section,'tweet'))
        #p_nonexist=config.get(section,'nonexist')
        if(self.debug):
            #print the entire config
            self.config.write(sys.stdout)
            self.p_debug=True
    def send_email():
        # build the message...
        msg=email.mime.text.MIMEText(self.p_content)
        msg['Subject']=self.p_subject
        msg['From']=self.p_from
        # Send the message via our own SMTP server, but don't include the # envelope header.
        server=smtplib.SMTP(self.p_smtp_host)
        if(self.p_debug):
            server.set_debuglevel(1)
        if(self.p_usetls):
            server.starttls()
        server.login(self.p_mail_user,self.p_mail_password)
        server.sendmail(self.p_from,self.p_to,msg.as_string())
        server.quit()
    def send_tweet():
        pass
    def release():
        if(p_email):
            send_email()
        if(p_tweet):
            send_tweet()
