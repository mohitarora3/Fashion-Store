from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(404)
def error_404(error):
	return render_template('errors/404.html'), 404
	#in flask we can return a static code which has default value 200 so we did not need to do with other routes

@errors.app_errorhandler(403)
def error_404(error):
	return render_template('errors/403.html'), 403

@errors.app_errorhandler(500)
def error_404(error):
	return render_template('errors/500.html'), 500
