Shadowrun-Attribute-Generator-Project
=====================================

This is my Attribute Generator Project.

This is a combinatorics problem. 

In Shadowrun, the players have priorities for their starting resources.

One of those is their attributes, or mental or physical scores that represent them.

In the game also, are limits, derived from these scores. 

The function limit_maker shows the algebra behind how these are derived.

These limits are the number of dice rolled(attribute + skill) that can be applied to the total success pool.

This process can often take time with new players, and I was thinking how to help new players out and be efficiant.

So the computer scientiest in me thought: "whats the best combination of attributes, for the highest combination of limits?"

Then I thought: "What is 'best'?" For now that answer is:

the sum of any such set of attributes that is greater than any other, that also has a sum of it's limits for each priority

Now there is bound to be many different kinds of maximums, and there are a lot of ways to consider approaching this problem.

Writing the list comprehensions alone was a blast..now on to taking out the lesser choices. 

More to come as I continue this project.

UPDATE 09/07/2014
---------------------
So, I changed the implementation around. Now it creates a database file with my attributes and limits

Next step: create a sample file to do some basic testing of queries to ensure it's as I want it for this project.

Also, consider changing structure of database if queries taking too long.

UPDATE 01/04/2015
---------------------
I came back to this project and switched from using a db for this, to just a csv since it's a highly structured
data set.

Right now I am aiming to visualize the dataset with some rudimentary graphs, then a short bit of statistics on
the data set.

Finally a Output csv of the data set that answers the question I originally posited: "whats the best combination of attributes, for the highest combination of limits?"

Although, I feel the visualization supports revising this question to: 

"For any such combination of attributes, which have at least 1 maximum limit (which is 8)?"
