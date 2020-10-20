Title: Sparklines - the Cheetah of Line Charts
Date:  2008-04-27 10:38:29
Category: Data Visualization

So a large chunk of my daily job consists of finding better ways of viewing  and obtaining data.  Being the geeky 
individual I am, I do my best to push Open Source initiatives (as a real quick aside, anyone else had the extreme fun of
having to prove over and over again that Open Source can be high quality, enterprise-grade stuff?  I'm pretty sure that 
is the case in a lot of places, but it's good to hear the horror stories lol).

So over the last two years I've come across many programs ([Pentaho Business Intelligence](http://www.pentaho.com\) and
[Open Flash Chart](http://teethgrinder.co.uk/open-flash-chart/) to name a couple...) and have recently come across a 
really neat little php app over at [Sparkline PHP Graphing Library](http://sparkline.org\)):  an open source application
to build sparklines from databases/array data.

## What are these sparklines anyway?

I was first introduced to the concept of sparklines by reading Information Dashboard Design:  The Effective Visual 
Communication of Data by Stephen Few ([Stephen Few's company site](http://www.perceptualedge.com/).  If you're looking 
for a good overview on how to design information dashboards, I highly recommend picking it up.

Sparklines were developed by Edward Tufte, who describes them as "data-intense, design-simple, word-sized graphics" 
([here is](http://www.edwardtufte.com/bboard/q-and-a-fetch-msg?msg_id=0001OR&amp;topic_id=1)  a post Tufte made about 
them).

Basically, they are a way to show a large chunk of data in a relatively small space.  Here's a few examples from 
sparkline.org:

<a href=\"http://www.bluefiredatasolutions.com/blog/wp-content/uploads/2008/04/sparkline_examples.png\"><img class=\"aligncenter size-medium wp-image-10\" title=\"sparkline_examples\" src=\"http://www.bluefiredatasolutions.com/blog/wp-content/uploads/2008/04/sparkline_examples.png\" alt=\"Large sparkline example\" width=\"200\" height=\"50\" /></a>

<a href=\"http://www.bluefiredatasolutions.com/blog/wp-content/uploads/2008/04/deficit_sparkline.png\"><img class=\"aligncenter size-medium wp-image-11\" title=\"deficit_sparkline\" src=\"http://www.bluefiredatasolutions.com/blog/wp-content/uploads/2008/04/deficit_sparkline.png\" alt=\"bar style sparkline\" width=\"62\" height=\"16\" /></a>

Notice there are two types - a line chart and a bar chart.  Both types can be embedded within a section of text to give 
quick, relevant data without breaking the stride of the writing.  As the first example also shows, you can also have 
sparklines be any size depending on what information you want to display.   I've been using them for On Time In Full 
calculations by customer - basically an overview page showing all customers on file with three sparklines beside them:  
one for On Time, In Full, and On Time In Full respectfully.  This way everyone (and I do mean everyone - I'm all about 
keeping data open to all those involved with the process) within the facility can see how well we are at shipping to our
 customers on time.
 
 I've gotten a tutorial about halfway finished on how to use the sparkline package with a mysql database (quick hint - 
 since OTIF is a hit/miss calculation, use a MySQL case statement to transform your data into a hit/miss total....).  
 Look for it soon.
 
 EDIT - Now here's some irony.  While looking through the WordPress widget repository, I came across this:  
 [Sparkstats Widget](http://widgets.wordpress.com/2006/08/14/sparkstats-widget/).  
 It even uses the Sparkline PHP Graphing Library.  Check it out.