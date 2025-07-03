from TikTokApi import TikTokApi
import schedule, time, datetime

# 把 verifyFp 填成你从浏览器 cookie 中获取的 s_v_web_id
VERIFY_FP = "verify_YOUR_S_V_WEB_ID_COOKIE"

# 保存上次检测的视频时间戳
last_ts = 0

def check_updates():
    global last_ts
    api = TikTokApi.get_instance(custom_verifyFp=VERIFY_FP)
    videos = api.byUsername("目标用户名", count=5)
    if not videos:
        print("获取视频失败或用户无作品")
        return
    latest = videos[0]["createTime"]
    if latest > last_ts:
        print(f"✅ 检测到新作品，视频ID：{videos[0]['id']} 时间戳：{latest}")
        last_ts = latest
    else:
        print("暂无新作品 👀")

# 首次执行一次，初始化 last_ts
check_updates()

schedule.every(5).minutes.do(check_updates)

print("开始监听，每5分钟检查一次...")
while True:
    schedule.run_pending()
    time.sleep(1)
