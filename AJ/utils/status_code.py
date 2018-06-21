ok = 200
success = {'code': 200, 'msg': '请求成功'}

USER_REGISTER_DATA_NOT_NULL = {'code': '1001', 'msg': '请填写完整的参数'}
USER_REGISTER_MOBILE_ERROR = {'code': '1002', 'msg': '手机号码不正确'}
USER_REGISTER_PASSWORD_IS_NOT_VALID = {'code': '1003', 'msg': '请输入一致密码'}
USER_REGISTER_MOBILE_EXISTS = {'code': '1004', 'msg': '已注册'}

USER_LOGIN_USER_NOT_EXSITS = {'code': '1005', 'msg': '用户未注册，请注册'}
USER_LOGIN_PASSWORD_IS_NOT_VALID = {'code': '1006', 'msg': '用户密码不正确'}

USER_CHANGE_PROFILE_IMAGES = {'code': '1007', 'msg': '上传图片格式不正确'}

DATABASE_ERROR = {'code': '0', 'msg': '数据库不正确'}

USER_CHANGE_PRONAME_IS_INVALID = {'code': '1008', 'msg': '用户名重复'}

USER_AUTH_DATA_IS_NOT_NULL = {'code': '1009', 'msg': '实名认证不能为空'}
USER_AUTH_ID_CARD_IS_NOT_VALID = {'code': '1010', 'msg': '身份证信息错误'}
