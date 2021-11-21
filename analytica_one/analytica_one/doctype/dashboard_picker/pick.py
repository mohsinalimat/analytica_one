# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import frappe
import jwt
import time


@frappe.whitelist()
def get_url(dashboard):
	# get metabase info
	metabase_config = frappe.get_single('Metabase Settings')
	# get dashboard info
	dashboard = frappe.get_doc('Dashboard Picker', dashboard)
	# config token
	payload = {
		'resource': {'dashboard': int(dashboard.dashboard_id)},
		'params': {},
		"exp": round(time.time()) + (60 * 20) # 10 minute expiration
	}
	# set expiration time
	#exp_time = metabase_config.metabase_exp_time
	#frappe.msgprint('EXP TIME '+str(exp_time))
	#if exp_time:
	#	frappe.msgprint('IN IF '+str(round(time.time()))
	#	frappe.msgprint('MU '+str((60 * exp_time)))
	#	payload['exp'] = (round(time.time()) + (60 * exp_time))  # 60 second * minute
	#	frappe.msgprint('PDDD '+str(payload['exp']))
	# gen token
	token = jwt.encode(
		payload,
		metabase_config.metabase_secret,
		algorithm='HS256'
	)

	# prepare config
	config = []
	if dashboard.show_border:
		config.append('bordered=true')
	else:
		config.append('bordered=false')
	if dashboard.show_title:
		config.append('titled=true')
	else:
		config.append('titled=false')
	if dashboard.theme == 'Dark':
		config.append('theme=night')
	config_param = '&'.join(config)

	# prepare url
	resizer = ''.join([
		metabase_config.metabase_url,
		'/app/iframeResizer.js',
	])

	iframeUrl = ''.join([
		metabase_config.metabase_url,
		'/embed/dashboard/',
		token.decode('utf8'),
		'#',
		config_param,
	])

	return {
		'name': dashboard.dashboard_name,
		'resizer': resizer,
		'iframeUrl': iframeUrl
	}