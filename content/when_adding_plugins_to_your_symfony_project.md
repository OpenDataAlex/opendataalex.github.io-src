Title:  When Adding Plugins To Your Symfony Project
Date: 2008-09-16 20:09:26
Category:  symfony, WebDev, Archive

Had the roughest time getting this one going - so therefore I'm posting just in case anyone else gets stuck.

Today, I started adding user security to the training database I've been developing in Symfony 1.1.  One of the great 
things about a strong framework like Symfony is the ability to create/distribute plugins to increase the core 
framework's functionality.  A very popular plugin, that I decided to use for my project, is [sfGuardPlugin](http://www.symfony-project.org/plugins/sfGuardPlugin).  
This plugin handles security with groups and a bunch of other features that I haven't played with yet.

There's a real good instruction set for installation/configuration with the plugin.  However, one thing not mentioned in
 the instructions is the fact that you _have_ to update your schema.xml file.  Otherwise, propel will throw this nice 
error:

> No package found for database "propel" in schema.xml.  The propel.packageObjectModel property requires the package 
> attribute to be set for each database.

So you'll need to update your schema file from this:
> <?xml version="1.0" encoding="utf-8">
>     <database name="propel" defaultIdMethod="native" noxsd="true">

to this:

>  <?xml version="1.0" encoding="utf-8">
>    <database name="propel" defaultIdMethod="native" noxsd="true" **package="lib.model"**>

The reason why is due to when a plugin has a schema of it's own.  Symfony/Propel will attempt to merge the plugin schema
with your application schema.  Your application schema though is not initially setup to handle this kind of merger.  
Adding that one variable should take care of that!

Edit:  I originally had the change to be:

> **package="model"**

This was incorrect and will result in your forms and models being stored in the primay folder for your symfony project - 
which will result in you wondering what the hell happened (as has been my problem for the last two days =S).