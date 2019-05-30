from flask import Flask, jsonify, request

app = Flask(__name__)

kpboard = [
    {
        'id': 1,
        'name': 'Victor',
        'office': 'Front-End'
    },
    {
        'id': 2,
        'name': 'Gabriel',
        'office': 'Fullstack'
    },
    {
        'id': 3,
        'name': 'Vincenzo',
        'office': 'Fullstack'
    }
]

@app.route('/kpboard', methods=['GET'])
def officers():
    return jsonify(kpboard), 200

@app.route('/kpboard/<string:office>', methods=['GET'])
def officers_by_position(office):
    # List Comprehension
    officers_by_position = [officer for officer in kpboard if officer['office'] == office]
    return jsonify(officers_by_position), 200

@app.route('/kpboard', methods=['POST'])
def create():
    data = request.get_json()
    kpboard.append(data)
    return 'Created successfully!', 201

@app.route('/kpboard/<int:id>', methods=['PUT'])
def edit(id):
    for office in kpboard:
        if kpboard['id'] == id:
            kpboard['office'] = request.get_json().get('office')
            return jsonify(office), 200
    return jsonify({'error': 'Officer not found!'}), 404

@app.route('/kpboard/<int:id>', methods=['DELETE'])
def delete(id):
    del kpboard[id - 1]
    return 'Deleted successfully!', 200

if __name__ == '__main__':
    app.run(debug=True)