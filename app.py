<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tiệm Chải Lông Mèo</title>
  <style>
    /* ==========================================
       5. BACKGROUND & STYLES (Thẩm mỹ & Ấm cúng)
       ========================================== */
    * {
      box-sizing: border-box;
      user-select: none;
    }
    body {
      margin: 0;
      padding: 0;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: #fdf6ec; /* Màu kem/gỗ ấm cúng */
      color: #4a3b32;
      display: flex;
      flex-direction: column;
      align-items: center;
      min-height: 100vh;
      transition: background 0.5s;
    }

    /* Môi trường bốc quẻ (Hơi tối, huyền bí) */
    body.mystic-mode {
      background: #1a0f2b;
      color: #e2d5f8;
    }

    #game-container {
      width: 100%;
      max-width: 600px;
      padding: 20px;
      text-align: center;
    }

    /* Bảng thông tin số lông */
    .stats-bar {
      background: #ffe3c8;
      border: 3px solid #d49a6a;
      border-radius: 15px;
      padding: 10px 20px;
      font-size: 1.3rem;
      font-weight: bold;
      margin-bottom: 15px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    .mystic-mode .stats-bar {
      background: #2d1b4e;
      border-color: #7b52b9;
    }

    /* Khung hiển thị Mèo */
    #cat-display {
      width: 100%;
      height: 320px;
      background: #fff8f0;
      border: 4px dashed #e0b084;
      border-radius: 20px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      position: relative;
      margin-bottom: 15px;
      overflow: hidden;
    }
    .mystic-mode #cat-display {
      background: #120924;
      border-color: #5c32a3;
    }

    /* Nơi chèn ảnh Mèo */
    #cat-image-placeholder {
      width: 200px;
      height: 200px;
      object-fit: contain;
    }

    /* Cảnh báo & Trạng thái */
    #warning-box {
      font-size: 1.1rem;
      font-weight: bold;
      height: 30px;
      color: #d9534f;
      margin-top: 5px;
    }

    /* Nút chải lông chính */
    #groom-btn {
      width: 100%;
      padding: 18px;
      font-size: 1.4rem;
      font-weight: bold;
      background: #e67e22;
      color: white;
      border: none;
      border-radius: 15px;
      cursor: pointer;
      box-shadow: 0 6px 0 #d35400;
      transition: all 0.1s;
    }
    #groom-btn:active {
      transform: translateY(4px);
      box-shadow: 0 2px 0 #d35400;
    }

    /* Điều hướng Tab (Shop & Bốc quẻ) */
    .nav-tabs {
      display: flex;
      gap: 10px;
      margin-top: 15px;
    }
    .tab-btn {
      flex: 1;
      padding: 10px;
      font-size: 1rem;
      font-weight: bold;
      border: 2px solid #d49a6a;
      background: #fff;
      color: #4a3b32;
      border-radius: 10px;
      cursor: pointer;
    }
    .mystic-mode .tab-btn {
      background: #2a1845;
      color: #e2d5f8;
      border-color: #7b52b9;
    }

    /* Modal / Popup cho Shop & Bốc quẻ */
    .modal {
      display: none;
      position: fixed;
      top: 0; left: 0; width: 100%; height: 100%;
      background: rgba(0,0,0,0.7);
      justify-content: center;
      align-items: center;
      z-index: 100;
    }
    .modal-content {
      background: #fdf6ec;
      padding: 20px;
      border-radius: 15px;
      width: 90%;
      max-width: 450px;
      max-height: 80vh;
      overflow-y: auto;
      text-align: center;
    }
    .mystic-mode .modal-content {
      background: #23123b;
      color: #e2d5f8;
      border: 1px solid #7b52b9;
    }

    /* Vật phẩm trong Shop */
    .shop-item {
      background: #fff;
      border: 2px solid #e0b084;
      border-radius: 10px;
      padding: 10px;
      margin-bottom: 10px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      text-align: left;
    }
    .shop-item button {
      background: #27ae60;
      color: white;
      border: none;
      padding: 8px 12px;
      border-radius: 8px;
      cursor: pointer;
    }

    .close-btn {
      background: #c0392b;
      color: white;
      border: none;
      padding: 8px 15px;
      border-radius: 8px;
      cursor: pointer;
      margin-top: 10px;
    }
  </style>
</head>
<body>

  <!-- ==========================================
       6. ÂM THANH NỀN & ÂM THANH HIỆU ỨNG
       ========================================== -->
  <!-- THAY THẾ LINK 'src' BẰNG ĐƯỜNG DẪN ÂM THANH CỦA BẠN -->
  <audio id="bg-music" loop autoplay>
    <source src="b84661dcd63fa90f0d9de65adb314e93.mp4" type="audio/mpeg">
  </audio>

  <div id="game-container">
    <h2>🐾 TIỆM CHẢI LÔNG MÈO 🐾</h2>
    
    <!-- Bảng hiển thị thông số -->
    <div class="stats-bar">
      <span>🪮 Lông mèo: <span id="fur-count">0</span></span>
      <span id="distract-status" style="font-size:0.9rem; color:#27ae60;"></span>
    </div>

    <!-- Khung hiển thị trạng thái Mèo -->
    <div id="cat-display">
      <!-- 6. DÒNG THAY THẾ HÌNH ẢNH MÈO (Đã tích hợp hiển thị tự động) -->
      <img id="cat-image-placeholder" src="" alt="Trạng thái mèo">
      <div id="warning-box"></div>
    </div>

    <!-- Nút hành động chính -->
    <button id="groom-btn" onmousedown="startGrooming()" onmouseup="stopGrooming()" onmouseleave="stopGrooming()" ontouchstart="startGrooming()" ontouchend="stopGrooming()">
      ẤN GIỮ ĐỂ CHẢI LÔNG 🪮
    </button>

    <!-- Nút điều hướng -->
    <div class="nav-tabs">
      <button class="tab-btn" onclick="openShop()">🛒 Cửa Hàng Vật Phẩm</button>
      <button class="tab-btn" onclick="openFortune()">🔮 Bốc Quẻ May Mắn</button>
    </div>
  </div>

  <!-- ==========================================
       3. CHỨC NĂNG SHOP VẬT PHẨM
       ========================================== -->
  <div id="shop-modal" class="modal">
    <div class="modal-content">
      <h3>🛒 CỬA HÀNG CHO MÈO</h3>
      
      <div class="shop-item">
        <div>
          <strong>Pate ăng nhăng nhăng</strong><br>
          <small>Mèo mải ăn trong 50 giây</small><br>
          <b>Giá: 50 Lông</b>
        </div>
        <button onclick="buyItem('pate', 50, 50)">Mua</button>
      </div>

      <div class="shop-item">
        <div>
          <strong>Cục len nát ơi là nát</strong><br>
          <small>Mèo vờn len trong 75 giây (1m15s)</small><br>
          <b>Giá: 100 Lông</b>
        </div>
        <button onclick="buyItem('len', 100, 75)">Mua</button>
      </div>

      <div class="shop-item">
        <div>
          <strong>Cỏ mèo ngon thơm</strong><br>
          <small>Mèo phê cỏ trong 125 giây (2m05s)</small><br>
          <b>Giá: 200 Lông</b>
        </div>
        <button onclick="buyItem('comeo', 200, 125)">Mua</button>
      </div>

      <div class="shop-item" style="border-color: #f1c40f; background: #fffdf0;">
        <div>
          <strong>📱 Điện thoại 17 Pro Max</strong><br>
          <small>Mèo xem đt, hạnh phúc và WIN GAME!</small><br>
          <b>Giá: 1601 Lông</b>
        </div>
        <button onclick="buyPhone()" style="background:#f39c12;">MUA & WIN</button>
      </div>

      <button class="close-btn" onclick="closeShop()">Đóng</button>
    </div>
  </div>

  <!-- ==========================================
       4. CHỨC NĂNG BỐC QUẺ (15-20 CÂU TÍCH CỰC)
       ========================================== -->
  <div id="fortune-modal" class="modal">
    <div class="modal-content">
      <h3>🔮 QUẺ CÁT TƯỜNG 🔮</h3>
      <p id="fortune-text" style="font-size: 1.2rem; min-height: 80px; margin-top:20px;">Hãy ấn nút dưới đây để rút quẻ hôm nay!</p>
      <button class="tab-btn" style="background:#8e44ad; color:white;" onclick="drawFortune()">Rút Quẻ</button>
      <br>
      <button class="close-btn" onclick="closeFortune()">Trở Về Nhà</button>
    </div>
  </div>

  <!-- ==========================================
       LOGIC GAME (JAVASCRIPT)
       ========================================== -->
  <script>
    /* ==========================================
       6. ĐƯỜNG DẪN HÌNH ẢNH MÈO (SỬA NƠI NÀY)
       Hãy thay các link bên dưới bằng file ảnh của bạn
       ========================================== */
    const CAT_IMAGES = {
      BACK: 'Messenger_creation_87363CC6-81AC-4A27-B1B6-A71A26E2108A.jpeg',        // 1. Hình ảnh mèo quay lưng
      FRONT: 'Messenger_creation_CFD5CA99-7601-4461-B619-A9A6B72F7869.png',       // 2. Hình ảnh mèo quay mặt lại
      WEED: '8f33a750c677fe8212c86b86e7390455.jpg',        // 3. Hình ảnh mèo phê cỏ / đang ăn / chơi len
      PHONE: '688d692156fa83219634cd9128a9139a.jpg'        // 4. Hình ảnh mèo xem điện thoại
    };

    // Quản lý biến trạng thái Game
    let furCount = 0;
    let isGrooming = false;
    let isCatFront = false;
    let isDistracted = false; // Trạng thái mèo bị dụ bởi đồ chơi/đồ ăn
    let groomInterval = null;
    let stateTimer = null;
    
    // Tốc độ mèo quay lưng (càng về sau càng nhanh)
    let backTime = 10000; // Khởi đầu 10s (mỗi lượt giảm dần)

    const furDisplay = document.getElementById('fur-count');
    const warningBox = document.getElementById('warning-box');
    const catImg = document.getElementById('cat-image-placeholder');
    const distractStatus = document.getElementById('distract-status');

    // ==========================================
    // 1 & 2. LOGIC MÈO QUAY LƯNG & XOAY MẶT
    // ==========================================
    
    // Khởi tạo vòng lặp trạng thái của Mèo
    function startCatCycle() {
      if (isDistracted) return;

      // Mèo quay lưng
      isCatFront = false;
      catImg.src = CAT_IMAGES.BACK;
      warningBox.innerText = "";

      // Yêu cầu 2: Cảnh báo trước 2 giây khi chuẩn bị quay mặt (Nếu thời gian quay lưng > 2s)
      let warnDelay = Math.max(0, backTime - 2000);
      setTimeout(() => {
        if (!isCatFront && !isDistracted) {
          warningBox.innerText = "⚠️ MÈO SẮP QUAY MẶT LẠI!";
        }
      }, warnDelay);

      // Chờ hết thời gian quay lưng -> Quay mặt lại
      stateTimer = setTimeout(() => {
        turnCatFront();
      }, backTime);
    }

    function turnCatFront() {
      if (isDistracted) return;

      isCatFront = true;
      catImg.src = CAT_IMAGES.FRONT;
      warningBox.innerText = "👀 MÈO ĐANG NHÌN BẠN!";

      // Yêu cầu 1: Nếu người chơi đang chải khi mèo quay mặt -> Bị cào & Trừ 2 lông
      if (isGrooming) {
        catScratch();
      }

      // Yêu cầu 2: Mèo nhìn người chơi ngẫu nhiên từ 30s đến 45s
      let frontTime = Math.floor(Math.random() * (45000 - 30000 + 1)) + 30000;

      stateTimer = setTimeout(() => {
        // Càng về sau mèo quay lưng càng nhanh (giảm 500ms mỗi lượt, tối thiểu 3s)
        backTime = Math.max(3000, backTime - 500);
        startCatCycle();
      }, frontTime);
    }

    // Hành động Mèo cào
    function catScratch() {
      furCount = Math.max(0, furCount - 2);
      furDisplay.innerText = furCount;
      alert("🐱💥 Mèo tức giận cào bạn! Bạn bị mất 2 cái lông mèo!");
    }

    // ==========================================
    // LOGIC CHẢI LÔNG MÈO
    // ==========================================
    function startGrooming() {
      isGrooming = true;

      // Nếu chải lúc mèo đang quay mặt và không bị xao nhãng -> Bị cào
      if (isCatFront && !isDistracted) {
        catScratch();
        return;
      }

      // Chải lông nhận 1 lông mỗi 0.5 giây
      groomInterval = setInterval(() => {
        if (isGrooming && (!isCatFront || isDistracted)) {
          furCount++;
          furDisplay.innerText = furCount;
        }
      }, 500);
    }

    function stopGrooming() {
      isGrooming = false;
      clearInterval(groomInterval);
    }

    // ==========================================
    // 3. LOGIC SHOP & VẬT PHẨM
    // ==========================================
    function openShop() {
      document.getElementById('shop-modal').style.display = 'flex';
    }
    function closeShop() {
      document.getElementById('shop-modal').style.display = 'none';
    }

    function buyItem(name, cost, duration) {
      if (furCount < cost) {
        alert("Bạn không đủ lông mèo để mua vật phẩm này!");
        return;
      }
      furCount -= cost;
      furDisplay.innerText = furCount;
      closeShop();

      // Kích hoạt trạng thái Mèo bị xao nhãng
      isDistracted = true;
      clearTimeout(stateTimer);
      warningBox.innerText = "";
      catImg.src = CAT_IMAGES.WEED; // Dùng ảnh mèo phê cỏ/đang ăn
      
      let timeLeft = duration;
      distractStatus.innerText = `🎁 Mèo đang bận chơi/ăn (${timeLeft}s)`;

      let itemTimer = setInterval(() => {
        timeLeft--;
        distractStatus.innerText = `🎁 Mèo đang bận chơi/ăn (${timeLeft}s)`;
        if (timeLeft <= 0) {
          clearInterval(itemTimer);
          isDistracted = false;
          distractStatus.innerText = "";
          alert("Mèo đã hết hứng thú với đồ chơi và quay lại theo dõi bạn!");
          startCatCycle();
        }
      }, 1000);
    }

    // Mua Điện thoại 17 Pro Max -> WIN GAME
    function buyPhone() {
      if (furCount < 1601) {
        alert("Chưa đủ 1601 lông mèo rồi! Cố gắng chải thêm nhé!");
        return;
      }
      furCount -= 1601;
      furDisplay.innerText = furCount;
      closeShop();

      clearTimeout(stateTimer);
      isDistracted = true;
      catImg.src = CAT_IMAGES.PHONE; // Ảnh mèo xem điện thoại
      warningBox.innerText = "🥰 MÈO HẠNH PHÚC & YÊU BẠN RẤT NHIỀU!";
      alert("🎉 CHÚC MỪNG BẠN! Mèo mải lướt Điện thoại 17 Pro Max nên cực kỳ hạnh phúc và yêu bạn. BẠN ĐÃ THẮNG GAME!");
    }

    // ==========================================
    // 4. LOGIC BỐC QUẺ (20 CÂU TÍCH CỰC)
    // ==========================================
    const fortunes = [
      "🍀 May mắn: Vận may đang mỉm cười với bạn, làm việc gì cũng vô cùng thuận lợi!",
      "💪 Sức khỏe: Cơ thể dẻo dai, năng lượng tràn đầy, luôn tươi trẻ mỗi ngày!",
      "🏡 Gia đình: Gia đình ấm êm, tràn ngập tiếng cười và luôn là chỗ dựa vững chắc.",
      "❤️ Mối quan hệ: Bạn sắp gặp được những người bạn chân thành và yêu thương bạn hết mực.",
      "🚀 Tương lai: Con đường phía trước vô cùng rộng mở, thành công đang chờ đón bạn!",
      "💰 Tiền bạc: Tài lộc dồi dào, tiền túi luôn rủng rỉnh, mua sắm không cần nhìn giá!",
      "🌟 May mắn: Một bất ngờ ngọt ngào sẽ đến với bạn trong vài ngày tới.",
      "🧘 Sức khỏe: Tinh thần minh mẫn, tâm trí bình an, mọi mệt mỏi đều tan biến.",
      "❤️ Mối quan hệ: Tình cảm tiến triển tốt đẹp, bạn luôn nhận được sự trân trọng.",
      "💎 Tiền bạc: Thu nhập gia tăng, đầu tư đúng đắn, tiền đẻ ra tiền!",
      "🌈 Tương lai: Những ước mơ bạn đang ấp ủ sẽ sớm trở thành hiện thực.",
      "🏠 Gia đình: Tình thân gắn kết, mọi thành viên đều khỏe mạnh và hạnh phúc.",
      "🍀 May mắn: Đi đến đâu cũng có quý nhân phù trợ, khó khăn nào cũng vượt qua.",
      "✨ Tương lai: Sự nghiệp phát triển rực rỡ, bước lên những tầm cao mới.",
      "💰 Tiền bạc: Lộc lá đầy nhà, buôn may bán đắt, tài chính luôn vững vàng.",
      "💖 Mối quan hệ: Sự chân thành của bạn sẽ lan tỏa và thu hút những điều tuyệt vời.",
      "🌿 Sức khỏe: Sức đề kháng dồi dào, luôn tràn ngập sức sống tươi mới.",
      "🎉 Gia đình: Nhận được tin vui bất ngờ từ người thân trong gia đình.",
      "🎯 Tương lai: Mọi quyết định của bạn hiện tại đều đang đi đúng hướng.",
      "🔮 May mắn: Vũ trụ đang gửi đến bạn năng lượng tích cực nhất!"
    ];

    function openFortune() {
      document.body.classList.add('mystic-mode'); // Chuyển sang nền tối huyền bí
      document.getElementById('fortune-modal').style.display = 'flex';
    }

    function closeFortune() {
      document.body.classList.remove('mystic-mode'); // Trở lại nền ấm cúng
      document.getElementById('fortune-modal').style.display = 'none';
    }

    function drawFortune() {
      const randomIndex = Math.floor(Math.random() * fortunes.length);
      document.getElementById('fortune-text').innerText = fortunes[randomIndex];
    }

    // Bắt đầu game khi tải xong
    window.onload = () => {
      startCatCycle();
    };
  </script>
</body>
</html>
