Title: Magento, GoDaddy Fun
Date: 2008-06-07 10:34:16
Category: Archive
Tags: Magento, WebDev

So I'm starting to work with e-Commerce systems, and picked Magento because it has a very robust feature set (I still 
want to check out Zen Cart, for it also looks promising) .  I've about got my current customer's store up, just waiting 
on their host to setup the MySQL database to finish the install.  Since I've got a bit of time to kill before that's 
complete, I figured I'd do a small writeup on how much fun GoDaddy brought to me lol.

Okay, so all you really need to download is the Magento version that you want to use.  Fortunately, GoDaddy finally 
caught up with the times and now provides PHP 5.2 with it's hosting packages.  Otherwise, you get to have fun with the 
[CGI last resort fix](http://www.magentocommerce.com/wiki/welcome_to_the_magento_user_s_guide/chapter_2).

So I also found out that because GoDaddy hosts both PHP 4 AND PHP 5, developers have to change the file extensions from 
.php to .php5 (what fun, right?).

So, hunting around the Internet brought me a quick solution for this.

In your Magento folder/setup, there should already be a .htaccess file.  Open that file up and add the following line:

AddHandler x-httpd-php5 .php

Now when you go to the Magento index page, you should see a 'No Input File Specified' error.  This is another easy fix.

If you do not already have a php.ini file in your main folder, you need to create one.  This will only work if you have 
selected the option of using Hosting Connection 2.0 .  This will allow you to modify server settings for your site.

I had to name my file 'php5.ini' for it to recognize.  I then added the following line:

cgi.fix_pathinfo = 1

GoDaddy decided to behave at this point and allowed me to see the installation wizard. Do not despair if it doesn't work
- there's a few more things that can be done, just check out the official posting about this issue [here](http://www.magentocommerce.com/wiki/groups/227/error/no_input_file_specified)

So I only had one more error to pop up after this.  It came in the form of a nice long text box.  Apparently when I 
FTP'd the Magento software, one file didn't transfer over.  If this happens, just place the file where it belongs based 
off of the error message you may receive.

So once that's all done, you should also have Magento hosted on a GoDaddy account.

As I explore the features of Magento, I'll post my thoughts and ideas/tips up here.