from flask import Flask, jsonify, request

app = Flask(__name__)

# التقاط طلبات التحليلات والـ Endpoints الخاصة باللعبة
@app.route('/b/ss/<path:subpath>', methods=['GET', 'POST'])
def handle_analytics(subpath):
    print(f"تم استقبال طلب على المسار: /b/ss/{subpath}")
    # الرد المباشر بـ 200 OK مع محتوى 1 تماماً كما تتوقعه اللعبة
    return "1", 200, {'Content-Type': 'text/html; charset=utf-8'}

# نقطة نهاية إضافية لأي بيانات بصيغة JSON قد تطلبها اللعبة لاحقاً
@app.route('/api/config', methods=['GET', 'POST'])
def game_config():
    # هيكل JSON محاكاة لبيانات اللعبة
    response_data = {
        "status": "success",
        "message": "Local server connected successfully"
    }
    return jsonify(response_data), 200

if __name__ == '__main__':
    # تشغيل السيرفر محلياً على المنفذ الافتراضي أو المخصص
    app.run(host='0.0.0.0', port=80)
