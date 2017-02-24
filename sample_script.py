#!/usr/bin/python

import json
import sqlite3
import sys

'''
Requirements:
You must use a scripting language (i.e., Perl, Python, Ruby, Go, Java, Node)
Shell scripting is not allowed for the assignment (i.e., Bash, Ksh, Zsh)
Your solution must be easily deployable and include a well documented process 
to do so.
Your solution must be checked into Github. Do not submit a pull request to this
repository. Send us a link to your repository.
Please show your work. We want to see multiple commits and see how you 
approached the problem.
API Implementation

You will need to implement 2 API endpoints for this assignment.

An endpoint for POSTing a single blog post
Endpoint must be /post
Method must be POST
Content of the POST must be the title and body of the post
An endpoint for GETing all blog posts
Endpoint must be /posts
Method must be GET
There should be no content sent (this is a GET request)
Content received must be the post_id, title, and body of all posts in an array
All data exchanged with the API must be in JSON format.

'''

''' 
Thought process. 

I'm going to need to import the sqlite3 and json modules, first thing.

I need to create functions to generate posts, and retrieve posts from a db file. db is a SQLlite flat file.

Part 1 = post to the db. I need to put two arg's, title_id and body, both strings, into the db.
Part 2 = get all posts in the db. 

Part one requires 2 args, part 2 requires zero.


Flow: check input for args supplied. If 2 args are supplied, and both are transmuted to strings, and posted. If there are zero args, get the posts, and output them. If any numbers other than 0 or 2, output an error.


Note: I've only popped in here to look at this when I have a few minutes, and haven't really put the time into it yet to do it properly. I'm commiting wht I have now, and will try my best to finish it tomorrow. It's been open for a week, and I've only coded for a good 15 minutes in that span, lol.

'''

# Args supplied

	
#Global declarations
db_read = "blog.db"
#table_name = "posts"
#id_column = "post_id"
#title_in = "title"
#body_in = "body"
#test_id = 1234
#conn = sqlite3.connect(db_read)
#mark = conn.cursor()

def connect_db():
    conn = sqlite3.connect(db_read)
    mark = conn.cursor()
    return conn, mark

def number_posts():
    conn = sqlite3.connect(db_read) 
    mark = conn.cursor()
    mark.execute('SELECT * FROM posts')
    count = len(mark.fetchall()) 	
    return count


def submit_post(title_in,body_in):
	conn = sqlite3.connect(db_read)
	mark = conn.cursor()
	table_name = "posts"
	print table_name
	next_id = number_posts() + 1
	print next_id
	id_column = "post_id"
	print id_column
	print title_in
	print body_in
	try:
	    mark.execute("INSERT INTO {tn} ({idf}, {c2n}, {c3n}) VALUES (post_id, 'test', 'test 2')".\
	        format(tn=table_name, idf="post_id", c2n="title", c3n="body"))
	    return True
	except sqlite3.IntegrityError:
	    print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))
            return False


#mark.execute('SELECT * FROM posts')
#all_rows= mark.fetchall()
#print all_rows



	
submit_post("Test title","I have no idea what to put here. Maybe Lorem Ipsum")
