Title: Magento Update:  Backend Fun/Frustration
Date: 2008-08-24 08:48:49
Category: Archive
Tags: Magento

Seeing that there's been interest with Magento, I figured I would write up my experiences since the last time I 
published about it.

First off, Magento does a fairly good job about documenting the basics about the program.  As I found out last time, it
will take a bit of digging to get into super-specific problems - mine just happened to be a host issue that had to be 
worked around. 

So basically, to access the administration side of the system, you need to go to the root directory of where you placed 
Magento and add /admin to the end of the address.  In my case, I actually created a store folder to keep it separate 
from the rest of the website so the address would look similar to:  http://somesite.com/store/admin.

Now during the installation process, you created an administrator account.  Using that will get you access to the 
backend - which happens to be a nice sales dashboard (one of the features that really sold me on Magento is the 
reporting capabilities build in, not sure if other OSS e-commerce solutions do something similar.  Feel free to post a 
comment and let me know what's up with the other solutions.  Heck, if you have a good review of any of them, send it to 
me too =p).

One of my big quips about Magento at this point is that even with my broadband connection, Magento seems to take it's 
time loading initially, which I sincerely hope they work on in future releases.  Also at first brush, it seems a bit 
complex to build addon modules for Magento, which I have also seen comments about elsewhere when reading reviews about 
php|architect\'s Magento guide.

I do like how the menu is organized, with the ability to create promotions for a particular date range, newsletter 
creation, and the ability to create personalized themes for stores (haven't worked on creating one yet, but I do like 
that they give the option).

Anywho, I'll keep playing around with Magento (when I'm not delving into symfony =p) and see what else I can come up 
with.