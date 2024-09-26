from flask import Blueprint, jsonify
from models.target_model import Target


target_bp = Blueprint('target_bp', __name__)


@target_bp.route('/get_all', methods=['GET'])
def get_all_bp():
    result = Target.query.all()
    if len(result) == 0:
        return jsonify({"result": f"Target table is empty"}), 200
    return jsonify({"result": [target.to_dict() for target in result]}), 200

@target_bp.route('/get_by_id/<int:id>', methods=['GET'])
def get_by_id_bp(id):
    result = Target.query.get(id)
    if result is None:
        return jsonify({"error": f"Target with id = {id} not found"}), 404
    return jsonify({"result": result.to_dict()}), 200




