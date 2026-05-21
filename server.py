# from flask import Flask, request, jsonify, Response
# from flask_cors import CORS
# import sqlite3
# import os

# app = Flask(__name__)
# CORS(app)

# DB = 'abap_vault.db'

# def get_db():
#     conn = sqlite3.connect(DB)
#     conn.row_factory = sqlite3.Row
#     return conn

# def init_db():
#     conn = get_db()
#     conn.execute('''
#         CREATE TABLE IF NOT EXISTS programs (
#             id          INTEGER PRIMARY KEY AUTOINCREMENT,
#             name        TEXT NOT NULL,
#             description TEXT NOT NULL,
#             tcode       TEXT,
#             tags        TEXT,
#             code        TEXT NOT NULL,
#             date        TEXT NOT NULL
#         )
#     ''')
#     conn.commit()
#     conn.close()

# @app.route('/programs', methods=['GET'])
# def get_programs():
#     conn = get_db()
#     rows = conn.execute('SELECT * FROM programs ORDER BY id DESC').fetchall()
#     conn.close()
#     return jsonify([dict(r) for r in rows])

# @app.route('/programs', methods=['POST'])
# def add_program():
#     data = request.json
#     if not data.get('name') or not data.get('description') or not data.get('code'):
#         return jsonify({'error': 'Name, description and code are required.'}), 400
#     conn = get_db()
#     conn.execute(
#         'INSERT INTO programs (name, description, tcode, tags, code, date) VALUES (?, ?, ?, ?, ?, ?)',
#         (data['name'].strip(), data['description'].strip(), data.get('tcode', '').strip(),
#          data.get('tags', '').strip(), data['code'].strip(), data['date'])
#     )
#     conn.commit()
#     conn.close()
#     return jsonify({'message': 'Program saved'}), 201

# @app.route('/programs/<int:id>', methods=['PUT'])
# def update_program(id):
#     data = request.json
#     if not data.get('name') or not data.get('description') or not data.get('code'):
#         return jsonify({'error': 'Name, description and code are required.'}), 400
#     conn = get_db()
#     conn.execute(
#         '''UPDATE programs
#            SET name=?, description=?, tcode=?, tags=?, code=?
#            WHERE id=?''',
#         (data['name'].strip(), data['description'].strip(), data.get('tcode', '').strip(),
#          data.get('tags', '').strip(), data['code'].strip(), id)
#     )
#     conn.commit()
#     conn.close()
#     return jsonify({'message': 'Program updated'})

# @app.route('/programs/<int:id>', methods=['DELETE'])
# def delete_program(id):
#     conn = get_db()
#     conn.execute('DELETE FROM programs WHERE id=?', (id,))
#     conn.commit()
#     conn.close()
#     return jsonify({'message': 'Program deleted'})

# # Export as .abap file
# @app.route('/programs/<int:id>/export/abap', methods=['GET'])
# def export_abap(id):
#     conn = get_db()
#     row = conn.execute('SELECT * FROM programs WHERE id=?', (id,)).fetchone()
#     conn.close()
#     if not row:
#         return jsonify({'error': 'Program not found.'}), 404
#     p = dict(row)
#     content = f"""*&---------------------------------------------------------------------*
# *& Program    : {p['name']}
# *& Description: {p['description']}
# *& T-Code     : {p['tcode'] or 'N/A'}
# *& Tags       : {p['tags'] or 'N/A'}
# *& Created    : {p['date']}
# *&---------------------------------------------------------------------*

# {p['code']}
# """
#     filename = f"{p['name']}.abap"
#     return Response(
#         content,
#         mimetype='text/plain',
#         headers={
#             'Content-Disposition': f'attachment; filename="{filename}"',
#             'Content-Type': 'text/plain; charset=utf-8'
#         }
#     )

# # Export as JSON
# @app.route('/programs/<int:id>/export/json', methods=['GET'])
# def export_json(id):
#     conn = get_db()
#     row = conn.execute('SELECT * FROM programs WHERE id=?', (id,)).fetchone()
#     conn.close()
#     if not row:
#         return jsonify({'error': 'Program not found.'}), 404
#     p = dict(row)
#     filename = f"{p['name']}.json"
#     return Response(
#         jsonify(p).get_data(as_text=True),
#         mimetype='application/json',
#         headers={'Content-Disposition': f'attachment; filename="{filename}"'}
#     )

# if __name__ == '__main__':
#     init_db()
#     print('\n  ABAP Vault Server')
#     print('  Running at http://localhost:5500\n')
#     app.run(debug=True, port=5500)







#-----------------------------------------------------------------------------------------------------------------------------

from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)

DB = 'abap_vault.db'

def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS programs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            tcode TEXT,
            tags TEXT,
            code TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/programs', methods=['GET'])
def get_programs():
    conn = get_db()
    rows = conn.execute('SELECT * FROM programs ORDER BY id DESC').fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])

@app.route('/programs', methods=['POST'])
def add_program():
    data = request.json
    conn = get_db()
    conn.execute(
        'INSERT INTO programs (name, description, tcode, tags, code, created_at) VALUES (?, ?, ?, ?, ?, ?)',
        (data['name'], data['description'], data.get('tcode', ''), data.get('tags', ''), data['code'], data['created_at'])
    )
    conn.commit()
    conn.close()
    return jsonify({'message': 'Program saved'}), 201

@app.route('/programs/<int:id>', methods=['PUT'])
def update_program(id):
    data = request.json
    conn = get_db()
    conn.execute(
        'UPDATE programs SET name=?, description=?, tcode=?, tags=?, code=?, created_at=? WHERE id=?',
        (data['name'], data['description'], data.get('tcode', ''), data.get('tags', ''), data['code'], data['created_at'], id)
    )
    conn.commit()
    conn.close()
    return jsonify({'message': 'Program updated'})

@app.route('/programs/<int:id>', methods=['DELETE'])
def delete_program(id):
    conn = get_db()
    conn.execute('DELETE FROM programs WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Program deleted'})

if __name__ == '__main__':
    init_db()
    print('ABAP Vault server running at http://localhost:5000')
    app.run(debug=True, port=5000)
    app.run(host='192.168.1.6', debug=True, port=5000)
