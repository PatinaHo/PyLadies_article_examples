# Python3.5
# -*- coding: utf-8 -*-
# OS: OS 10
# IDE: Sublime Text
# facebook-sdk version 1.0.0

import facebook
import requests
import json
import csv

def get_all_posts(fanpageID):
	"""Get all posts in fanpage and write each column in dicts.
	   Returns:
			postID_list:
			fanpageName_list:
			content_list:
			createTime_list:
	"""
	all_posts = graph.get_connections(id = fanpageID, connection_name = 'posts', summary='true', limit = 25)
	fanpageName = graph.get_object(id = fanpageID, fields = 'name')['name']
	postID_list = []
	fanpageName_list = []
	content_list = []
	createTime_list = []

	for i in range(0,24):
		postID_list.append(all_posts['data'][i]['id'])
		fanpageName_list.append(fanpageName)
		try:
			content_list.append(all_posts['data'][i]['message'])
		except:
			content_list.append(0)
		createTime_list.append(all_posts['data'][i]['created_time'])

	return postID_list, fanpageName_list, content_list, createTime_list

def get_activation(postID_list):
	"""Get likes and comments in each post and write total counts in dicts.
	   Returns:
	   		postLikesCount_list:
	   		postCommentsCount_list:
	"""
	url = 'https://graph.facebook.com/v2.12/'+ fanpageID +'?fields=posts.limits(25){likes,comments,shares}&access_token=' + token
	response = requests.get(url)
	html = json.loads(response.text)

	postLikesCount_list = []
	postCommentsCount_list = []
	postSharesCount_list = []
	for i in postID_list:
		postLikesCount = graph.get_connections(id = i, connection_name = 'likes', summary='true')
		postCommentsCount = graph.get_connections(id = i, connection_name = 'comments', summary='true')
		postLikesCount_list.append(postLikesCount['summary']['total_count'])
		postCommentsCount_list.append(postCommentsCount['summary']['total_count'])
		
	for i in range(25):
		postSharesCount = html['posts']['data'][i]['shares']['count']
		postSharesCount_list.append(postSharesCount)

	return postLikesCount_list, postCommentsCount_list, postSharesCount_list


def write_file(filename, write_list_1, write_list_2, write_list_3, write_list_4, write_list_5, write_list_6, write_list_7):
	"""Write file for list.
	Args:
		filename(str): write out file name.
		write_list(list): list to write out.
	"""
	with open(filename, 'w', newline="") as ofile:
		writer = csv.writer(ofile, delimiter=',')
		lists = write_list_1, write_list_2, write_list_3, write_list_4, write_list_5, write_list_6, write_list_7
		for i in range(24):
			write_out = [li[i] for li in lists]
			writer.writerow(write_out)


if __name__	== '__main__':
	token = '' #貼上token
	graph = facebook.GraphAPI(access_token = token)
	fanpageID = '1759525920983198'

	postID_list, fanpageName_list, content_list, createTime_list = get_all_posts(fanpageID)
	postLikesCount_list, postCommentsCount_list, postSharesCount_list = get_activation(postID_list)
	write_file('PyLadiesTW.csv', postID_list, fanpageName_list, content_list, createTime_list, postLikesCount_list, postCommentsCount_list, postSharesCount_list)