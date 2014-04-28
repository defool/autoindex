#!/usr/bin/env python
#-*- coding: UTF-8 -*-
"""
    Author:  defool@outlook.com
    License:    MIT
"""

import os
import template

def listfiles(dir, path):
	result = []
	for d in os.listdir(dir):
		p = os.path.join(dir, d)
		if os.path.isdir(p):
			ftype = 'directory'
		elif os.path.isfile(p):
			_, ftype = os.path.splitext(d)
			ftype = len(ftype) > 0 and ftype[1:] or 'file'
		else:
			ftype = 'unknown'

		info = os.stat(p)
		result.append({'name':d, 'type': ftype, 'href': os.path.join(path, d), \
				'size': info.st_size, 'mtime': info.st_mtime})
	return result
	
def application(env, start_response):
	document_root = env.get('DOCUMENT_ROOT', '/')
	path = env.get('PATH_INFO', '.')
	document_root = os.path.join(document_root, '.'+path)
	if os.path.isdir(document_root):
		try:
			result = listfiles(document_root, path)
		except OSError as e:
			result = []
		start_response('200 OK', [('Content-Type','text/html')])
		return [template.format_data({'title': path}, result)] #
	else:
		start_response('404 Not Found', [])
		return [template.format_data({'title': 'Unknown directory'}, [])]