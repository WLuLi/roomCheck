from flask import Blueprint, jsonify, request

manager_bp = Blueprint('manager', __name__)

# 用于存储房间数据的简单数据结构
rooms = [
    {"id": "2120", "description": "理科咨询:计算机大类(张泽宇、王麒杰、罗雨琪)", "status": "空闲"},
    {"id": "1909", "description": "理科咨询:电子大类(陈子安、杨思琪[下午到])", "status": "空闲"},
    {"id": "2106", "description": "理科咨询:自动化大类(饶启杭)", "status": "空闲"},
    {"id": "1921", "description": "理科咨询:数理(黄昱烁、邱昱翰)", "status": "空闲"},
    {"id": "2023", "description": "咨询:新雅(童宇轩、胡一臻、郑哲宇)", "status": "空闲"},
    {"id": "2020", "description": "咨询:经管(林枫、吴悠、熊珂、童宇轩)", "status": "空闲"},
    {"id": "2220", "description": "文科咨询:法学(程程、袁思佳、肖维怡)", "status": "空闲"},
    {"id": "2006", "description": "文科咨询:社科(刘志鹏)", "status": "空闲"},
    {"id": "2206", "description": "文科咨询:马院(胡铭杨)", "status": "空闲"},
    # 添加更多房间数据
]

# 获取房间占用情况
@manager_bp.route('/api/rooms', methods=['GET'])
def get_rooms():
    return jsonify({"rooms": rooms})

# 更改房间占用情况
@manager_bp.route('/api/rooms', methods=['POST'])
def change_room_status():
    data = request.get_json()
    room_id = data.get('roomId')
    new_status = data.get('status')

    # 根据roomId查找对应的房间
    room = next((room for room in rooms if room["id"] == room_id), None)

    if room:
        # 更新房间占用情况
        room["status"] = new_status
        return jsonify({"message": "房间占用情况已更新", "room": room}), 200
    else:
        return jsonify({"error": "找不到指定的房间"}), 404
