
from flask import Blueprint, render_template, jsonify

from App.models import Area, Facility
from utils import status_code

house_blueprint = Blueprint('house', __name__)


# 我的房源页面
@house_blueprint.route('/myhouse/', methods=['GET'])
def my_house():
    return render_template('myhouse.html')


# 访问发布房源的页面
@house_blueprint.route('/newhouse/')
def new_house():
    return render_template('newhouse.html')


# 获取区域和设备的信息（查询接口）
@house_blueprint.route('/area_facility/')
def area_facility():
    # 拿到地区和设备的列表
    areas = Area.query.all()
    facilitys = Facility.query.all()

    # 序列化处理每一个地区和设备
    area_list = [area.to_dict() for area in areas]
    facilitys_list = [facility.to_dict() for facility in facilitys]

    # 返回状态码，地区列表和设备列表
    return jsonify(code=status_code.ok,
                   areas=area_list,
                   facilitys=facilitys_list
                   )
