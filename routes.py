from app import app
from flask import request, jsonify, redirect
import random, string
from models import db, Url

@app.route('/api/shorten', methods=['POST'])
def shorten():
    body = request.json
    original_url = body.get('url')
    short_id = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

    if original_url is None:
        return jsonify({"error":"bad request"}), 401 
    
    url = Url(short_id=short_id, original_url=original_url)
    db.session.add(url)
    db.session.commit()

    return jsonify(shortUrl=f'http://127.0.0.1:5000/{short_id}')

@app.route('/<short_id>')
def redirect_to_oringal(short_id):
    url = Url.query.filter_by(short_id=short_id).one_or_none()
    url.access_count += 1
    db.session.commit()
    return redirect(url.original_url)


