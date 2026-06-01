# 👻 SnapGhost — Deploy qo'llanmasi
> by Akhmadov

## 🚀 BUGUN ISHGA TUSHIRISH — 3 QADAM

---

### 1️⃣ GitHub ga yuklang (5 daqiqa)
1. github.com → yangi repo oching (istalgan nom)
2. Fayllarni yuklab oling:
   - "uploading an existing file" bosing
   - barcha fayllarni sudrab tashlang
   - "Commit changes" bosing

---

### 2️⃣ Railway ga deploy qiling (5 daqiqa)
1. **railway.app** ga boring → GitHub bilan kiring
2. "New Project" → "Deploy from GitHub repo" → reponi tanlang
3. Deploy tugagach **URL** olasiz:
   ```
   https://snapghost-xxxx.up.railway.app
   ```

### 3️⃣ SERVER_URL ni yangilang
`bot/main.py` faylida:
```python
SERVER_URL = os.environ.get("SERVER_URL", "https://snapghost-xxxx.up.railway.app")
```
Bu qatorni toping va Railway URL ni qo'ying.

Keyin GitHub ga push qiling — Railway avtomatik qayta deploy qiladi.

---

## ✅ Test qilish
Botga /start yozing → tugmani bosing → rasm tushadi → sizga keladi!

