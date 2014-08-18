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
