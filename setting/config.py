from flask import Flask, jsonify, request, Blueprint, make_response, url_for, render_template, session, redirect
from flask_cors import CORS
import requests, json, bson
import calendar
from datetime import datetime, timedelta
from jsondiff import diff
import random
from hashlib import sha256
import base64
from datetime import datetime, timedelta, date
from time import gmtime, strftime, localtime
import pyodbc
import pymysql
import jwt
from functools import wraps


apps = Flask(__name__, static_folder='../static', template_folder='../templates')

apps.config['SECRET_KEY'] = '33ea2029167f8abca5f0e95869860a93c74385b8'


