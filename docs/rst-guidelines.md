# RST Guidelines
This page describes practices to be adopted in RST projects. The goal of these practices is to ensure that we are able to deliver high-quality, usable, reproducible results in every project.

## Core practices

### Version control
Using version control is essential. In our case, we will use Github since it is the established home of a large majority of open-source science work. 

### Documentation
In most cases, we don't want to produce one-off scripts, but toolkits containing functions that can be adapted and reused. This is only useful, however, if the code is documented. There are three main kinds of documentation to think about:

* Inline documentation: These are comments interspersed with the code that are mainly intended to give help to someone reading or editing the code about what things are doing and why - probably the most important audience for this type of documentation is the code author's future self!
* Function documentation: These comments, often referred to as "docstrings", are associated with each function or class in the code and describe what it does, the required inputs, and expected outputs. These are intended for users of the code who are applying the method implemented in the function in a new context.
* Project documentation: Somewhat more nebulous, this is documentation that describes how the pieces fit together, and how someone should use the tools provided by the code. It can range from a simple readme document to something with multiple pages including examples, tutorials, etc...

In RST projects, documentation is important because it ensures that whatever we develop can be handed off to collaborators and is easier to pick up again.

## Optional practices

Some things that could be useful to do:

* Establish a data repository - it's very useful to have a single location that's internet accessible to store data. That way code can download missing data automatically, making it much easier to get collaborators up and running.
