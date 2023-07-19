from pymavlink import mavutil
import time
import sys
import random

master = mavutil.mavlink_connection("tcp:127.0.0.1:5762")

# 風向、風速シミュレーション値をバックアップ
master.mav.param_request_read_send(
    master.target_system, master.target_component,
    b'SIM_WIND_DIR',
    -1
)
message = master.recv_match(type='PARAM_VALUE', blocking=True).to_dict()
SIM_WIND_DIR_backup = message['param_value']

master.mav.param_request_read_send(
    master.target_system, master.target_component,
    b'SIM_WIND_SPD',
    -1
)
message = master.recv_match(type='PARAM_VALUE', blocking=True).to_dict()
SIM_WIND_SPD_backup = message['param_value']

# 風向シミュレーション値を135に設定
master.mav.param_set_send(
    master.target_system, master.target_component,
    b'SIM_WIND_DIR',
    135,
    mavutil.mavlink.MAV_PARAM_TYPE_REAL32
)
print("param set SIM_WIND_DIR")


# arm
master.arducopter_arm()
master.motors_armed_wait()
print("armed")

# フライトモードをGUIDEDに変更
mode = "GUIDED"
if mode not in master.mode_mapping():
    print('Unknown mode : {}'.format(mode))
    print('Try:', list(master.mode_mapping().keys()))
    sys.exit(1)
mode_id = master.mode_mapping()[mode]
master.mav.set_mode_send(
    master.target_system,
    mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
    mode_id
)

# takeoff
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
    0, 0, 0, 0, 0, 0, 0,
    20)
print("takeoff")

time.sleep(15.0)

# waypoint
master.mav.mission_item_send(
    master.target_system,
    master.target_component,
    0,
    3,
    mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,
    2,
    0, 0,
    0, 0, 0,
    35.878570,
    140.340329,
    150)
print("waypoint")

time.sleep(65.0)

# 強制Disarm
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    0,
    21196, # 強制
    0, 0, 0, 0, 0)
print("force disarm")

# 2秒ごとに風速をランダム生成
for i in range(6):
    rand_value = random.random()*15
    master.mav.param_set_send(
        master.target_system, master.target_component,
        b'SIM_WIND_SPD',
        rand_value,
        mavutil.mavlink.MAV_PARAM_TYPE_REAL32
    )
    time.sleep(2.0)

# 風向、風速シミュレーション値を元に戻す
master.mav.param_set_send(
    master.target_system, master.target_component,
    b'SIM_WIND_DIR',
    SIM_WIND_DIR_backup,
    mavutil.mavlink.MAV_PARAM_TYPE_REAL32
)
master.mav.param_set_send(
    master.target_system, master.target_component,
    b'SIM_WIND_SPD',
    SIM_WIND_SPD_backup,
    mavutil.mavlink.MAV_PARAM_TYPE_REAL32
)
print("params rollback")

time.sleep(0.1)

print('script end.')
