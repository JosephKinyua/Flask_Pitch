from flask import render_template, redirect, url_for, flash, request
from . import auth
from . forms import LoginForm, Registration
from ..models import User
from .. import db
from flask_login import login_user, login_required, logout_user, current_user
from ..email import mail_message