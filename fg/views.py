from flask import Blueprint, render_template, request, make_response
from flask_login import login_required, current_user

views = Blueprint('views',__name__)


@views.route('/')
def home():
    username = request.cookies.get('username')
    resp = make_response(render_template('index.html'))
    resp.set_cookie('username', 'the username')
    return resp
    #return render_template ("index.html")


@views.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@views.route('/telecommunication-engineering')
@login_required
def tc():
    return render_template ('Telecommunication-engineering.md')

@views.route('/programming')
@login_required
def progrmming ():
    return render_template('programming.md')



@views.route('/digital-circuit')
@login_required
def digital_circuit():
    return render_template('/note_views/digital-circuit.md')



@views.route('/energy-conversion')
@login_required
def energy():
    return render_template('note_views/energy.md')



@views.route('/engineering-materials')
@login_required
def materials():
    return render_template('note_views/engineering-materials.md')


@views.route('/advanced-electronics')
@login_required
def adv_electronic():
    return render_template('note_views/advanced-electronics.md')



@views.route('/english-for-pro-purpose')
@login_required
def english():
    return render_template('note_views/english-for-pro-purpose.md')


@login_required
@views.route('/digital-circuit/universal-gate')
def digital_circuit_universal_gate():
    return render_template('note_views/digital_circuit/ການປະຍຸກໃຊ້ເກດທົດແທນ(Universal Gate).md')


















@views.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404