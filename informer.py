import aiohttp
import aiohttp.web
import json as Json
import os
import time
import sys
import psutil
import platform

import config

routes = aiohttp.web.RouteTableDef()

@routes.get('/')
async def main(request: aiohttp.web.Request):
    return aiohttp.web.json_response({'status': 'success', 'message': 'server is online and api ready'}, status=200)

@routes.get('/sys/info/all')
async def all_sys_info(request: aiohttp.web.Request):
    auth_header = str(request.headers.get('Authorization'))
    if not auth_header:
        return aiohttp.web.json_response({'status': 'error', 'message': 'The token is misseng in the request!'}, status=401)
    
    if not auth_header in config.json['tokens']:
        return aiohttp.web.json_response({'status': 'error', 'message': 'Your token has no access to this ressourche!'}, status=401)

    ram_byte = psutil.virtual_memory().total
    used_ram_byte = psutil.virtual_memory().used
    return aiohttp.web.json_response({'status': 'success', 'message': 'data was called', 'data': {
        'ram': {
            'total': {'b': ram_byte, 'kb': round(ram_byte/1024, 1), 'mb': round(ram_byte/1048576, 1), 'gb': round(ram_byte/1073741824, 1)}, 
            'used': {'b': used_ram_byte, 'kb': round(used_ram_byte/1024, 1), 'mb': round(used_ram_byte/1048576, 1), 'gb': round(used_ram_byte/1073741824, 1), 'percent': round(100/ram_byte*used_ram_byte, 1)}
        },
        'cpu': {
            'freq': psutil.cpu_freq(), 'count': psutil.cpu_count(), 'percent': psutil.cpu_percent()
        },
        'os': {
            'name': platform.system().lower(), 'release': platform.release(), 'version': platform.version(), 'architecture': platform.architecture()
        }
    }}, status=200)

@routes.get('/sys/info/small')
async def small_sys_info(request: aiohttp.web.Request):
    auth_header = str(request.headers.get('Authorization'))
    if not auth_header:
        return aiohttp.web.json_response({'status': 'error', 'message': 'The token is misseng in the request!'}, status=401)
    
    if not auth_header in config.json['tokens']:
        return aiohttp.web.json_response({'status': 'error', 'message': 'Your token has no access to this ressourche!'}, status=401)

    return aiohttp.web.json_response({'status': 'success', 'message': 'data was called', 'data': {
        'ram': {'total': psutil.virtual_memory().total, 'used': psutil.virtual_memory().used},
        'cpu': {'percent': psutil.cpu_percent()},
        'os': {'name': platform.system().lower(), 'release': platform.release()}
    }}, status=200)

@routes.get('/sys/info/ram')
async def ram_sys_info(request: aiohttp.web.Request):
    auth_header = str(request.headers.get('Authorization'))
    if not auth_header:
        return aiohttp.web.json_response({'status': 'error', 'message': 'The token is misseng in the request!'}, status=401)
    
    if not auth_header in config.json['tokens']:
        return aiohttp.web.json_response({'status': 'error', 'message': 'Your token has no access to this ressourche!'}, status=401)
    
    ram_byte = psutil.virtual_memory().total
    used_ram_byte = psutil.virtual_memory().used
    return aiohttp.web.json_response({'status': 'success', 'message': 'data was called', 'data': {
        'total': {'b': ram_byte, 'kb': round(ram_byte/1024, 1), 'mb': round(ram_byte/1048576, 1), 'gb': round(ram_byte/1073741824, 1)}, 
        'used': {'b': used_ram_byte, 'kb': round(used_ram_byte/1024, 1), 'mb': round(used_ram_byte/1048576, 1), 'gb': round(used_ram_byte/1073741824, 1), 'percent': round(100/ram_byte*used_ram_byte, 1)}
        }}, status=200)

@routes.get('/sys/info/cpu')
async def cpu_sys_info(request: aiohttp.web.Request):
    auth_header = str(request.headers.get('Authorization'))
    if not auth_header:
        return aiohttp.web.json_response({'status': 'error', 'message': 'The token is misseng in the request!'}, status=401)
    
    if not auth_header in config.json['tokens']:
        return aiohttp.web.json_response({'status': 'error', 'message': 'Your token has no access to this ressourche!'}, status=401)
    
    return aiohttp.web.json_response({'status': 'success', 'message': 'data was called', 'data': {
        'freq': psutil.cpu_freq(), 'count': psutil.cpu_count(), 'percent': psutil.cpu_percent()
    }}, status=200)

@routes.get('/sys/info/os')
async def os_sys_info(request: aiohttp.web.Request):
    auth_header = str(request.headers.get('Authorization'))
    if not auth_header:
        return aiohttp.web.json_response({'status': 'error', 'message': 'The token is misseng in the request!'}, status=401)
    
    if not auth_header in config.json['tokens']:
        return aiohttp.web.json_response({'status': 'error', 'message': 'Your token has no access to this ressourche!'}, status=401)

    return aiohttp.web.json_response({'status': 'success', 'message': 'data was called', 'data': {
        'name': platform.system().lower(), 'release': platform.release(), 'version': platform.version(), 'architecture': platform.architecture()
    }}, status=200)

app = aiohttp.web.Application()
app.add_routes(routes)

aiohttp.web.run_app(app, port=8080)