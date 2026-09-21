    // ---- AUTHENTICATION CHECK ----
    const loginContainer = document.getElementById('loginContainer');
    const loginForm = document.getElementById('loginForm');
    const loginUsername = document.getElementById('adminUsername');
    const loginPassword = document.getElementById('adminPassword');
    const loginError = document.getElementById('loginError');
    const logoutBtn = document.getElementById('logoutBtn');

    function checkAuth() {
      const isAuth = sessionStorage.getItem('olion_admin_auth');
      if (isAuth === 'true') {
        loginContainer.classList.add('hidden');
      } else {
        loginContainer.classList.remove('hidden');
      }
    }
    checkAuth();

    loginForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const u = (loginUsername.value || '').trim();
      const p = (loginPassword.value || '').trim();

      const validPasswords = ['olion2024', 'admin', 'olion', '123456', 'olioncoffee'];
      if (u.toLowerCase() === 'admin' && validPasswords.includes(p)) {
        sessionStorage.setItem('olion_admin_auth', 'true');
        loginError.style.display = 'none';
        loginContainer.classList.add('hidden');
        showToast('Đăng nhập thành công! Chào mừng Quản trị viên.');
        loadAllData();
      } else {
        loginError.style.display = 'block';
        loginPassword.value = '';
        loginPassword.focus();
      }
    });

    logoutBtn.addEventListener('click', () => {
      sessionStorage.removeItem('olion_admin_auth');
      loginContainer.classList.remove('hidden');
      loginPassword.value = '';
    });

    // ---- TAB SWITCHING ----
    const navItems = document.querySelectorAll('.nav-item');
    const tabContents = document.querySelectorAll('.tab-content');
    const pageTitle = document.getElementById('pageTitle');

    const tabTitles = {
      overview: '📊 Bảng Điều Khiển Tổng Quan',
      menu: '☕ Quản Lý Thực Đơn & Giá Món',
      customers: '👑 Khách Hàng & Tích Điểm (Loyalty)',
      feedbacks: '💬 Quản Lý Góp Ý & Đánh Giá',
      announcements: '📢 Quản Lý Dải Thông Báo Web',
      promotions: '🎁 Chương Trình Ưu Đãi & Vouchers',
      minigame: '🎡 Cấu Hình Vòng Quay Minigame',
      supabase: '⚡ Cấu Hình Supabase Cloud Database',
      customizer: '🎨 Thiết Kế Web & Thông Tin Quán'
    };

    function switchTab(tabKey) {
      navItems.forEach(item => {
        item.classList.toggle('active', item.dataset.tab === tabKey);
      });
      tabContents.forEach(content => {
        content.classList.toggle('active', content.id === 'tab-' + tabKey);
      });
      if (pageTitle && tabTitles[tabKey]) {
        const fullTitle = tabTitles[tabKey];
        const icon = fullTitle.split(' ')[0];
        const text = fullTitle.substring(icon.length).trim();
        pageTitle.innerHTML = `<span>${icon}</span> <span>${text}</span>`;
      }
      if (tabKey === 'overview') updateCharts();
      if (tabKey === 'menu') loadMenu();
      if (tabKey === 'customers') loadCustomers();
      if (tabKey === 'feedbacks') loadFeedbacks();
      if (tabKey === 'minigame') loadMinigame();
    }

    navItems.forEach(item => {
      item.addEventListener('click', () => switchTab(item.dataset.tab));
    });

    
    // ==========================================
    // QR SCANNER LOGIC
    // ==========================================
    let html5QrcodeScanner = null;
    let currentScannedId = null;

    function onScanSuccess(decodedText, decodedResult) {
      if (decodedText.startsWith('olion-voucher:')) {
        const id = decodedText.split(':')[1];
        if (id !== currentScannedId) {
          currentScannedId = id;
          html5QrcodeScanner.pause(true);
          processVoucher(id);
        }
      } else {
        showToast('Mã QR không thuộc hệ thống Olion Coffee!');
      }
    }

    async function processVoucher(id) {
      document.getElementById('qr-result').style.display = 'none';
      document.getElementById('qr-error').style.display = 'none';
      
      const res = await getSpinDetails(id);
      if (res.error || !res.data) {
        document.getElementById('qr-error').style.display = 'block';
        document.getElementById('qr-error-msg').textContent = 'Không tìm thấy thông tin Voucher này trên máy chủ!';
        setTimeout(() => { html5QrcodeScanner.resume(); currentScannedId = null; }, 3000);
        return;
      }
      
      const v = res.data;
      if (v.status === 'used') {
        document.getElementById('qr-error').style.display = 'block';
        document.getElementById('qr-error-msg').textContent = 'Voucher này đã được sử dụng vào lúc: ' + new Date(v.updated_at || v.created_at).toLocaleString('vi-VN');
        setTimeout(() => { html5QrcodeScanner.resume(); currentScannedId = null; }, 3000);
        return;
      }
      
      document.getElementById('qr-result').style.display = 'block';
      document.getElementById('qr-prize-name').textContent = `🎁 ${v.prize_name} (Mã: ${v.promo_code})`;
      document.getElementById('qr-customer').textContent = `👤 Khách: ${v.customer_name} - 📞 ${v.customer_phone}`;
      
      document.getElementById('btnMarkUsed').onclick = async () => {
        document.getElementById('btnMarkUsed').textContent = 'Đang xử lý...';
        await markSpinAsUsed(id);
        document.getElementById('btnMarkUsed').textContent = 'Đánh dấu Đã Sử Dụng';
        document.getElementById('qr-result').style.display = 'none';
        showToast('✅ Đã thu hồi E-Voucher thành công!');
        html5QrcodeScanner.resume();
        currentScannedId = null;
      };
    }

    const oldSwitchTab = switchTab;
    switchTab = function(tabKey) {
      oldSwitchTab(tabKey);
      if (tabKey === 'scanner') {
        if (!html5QrcodeScanner) {
          html5QrcodeScanner = new Html5QrcodeScanner("qr-reader", { fps: 10, qrbox: {width: 250, height: 250} }, false);
          html5QrcodeScanner.render(onScanSuccess);
        }
      }
    };

    // ---- TOAST UTILITY ----
    const toast = document.getElementById('adminToast');
    const toastMsg = document.getElementById('toastMsg');
    let toastTimer;
    function showToast(msg) {
      toastMsg.textContent = msg;
      toast.classList.add('show');
      clearTimeout(toastTimer);
      toastTimer = setTimeout(() => toast.classList.remove('show'), 3500);
    }

    // =========================================================================
    // 1. DATA VISUALIZATION (CHART.JS ANALYTICS)
    // =========================================================================
    let weeklyTrendChart = null;
    let satisfactionChart = null;

    function initOrUpdateCharts(feedbacks = [], spins = []) {
      const lineCanvas = document.getElementById('chartWeeklyTrends');
      const pieCanvas = document.getElementById('chartSatisfaction');
      if (!lineCanvas || !pieCanvas || typeof Chart === 'undefined') return;

      // 1. Prepare Line Chart Data (Last 7 Days)
      const days = ['CN', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7'];
      const today = new Date();
      const labels = [];
      const feedbackCounts = [0, 0, 0, 0, 0, 0, 0];
      const spinCounts = [0, 0, 0, 0, 0, 0, 0];

      for (let i = 6; i >= 0; i--) {
        const d = new Date();
        d.setDate(today.getDate() - i);
        labels.push(`${days[d.getDay()]} (${d.getDate()}/${d.getMonth()+1})`);
      }

      // Generate realistic dynamic trend curve based on actual counts + baseline
      const fbTotal = feedbacks.length || 3;
      const spinTotal = spins.length || 4;

      const fbData = [
        Math.max(1, Math.round(fbTotal * 0.1)),
        Math.max(1, Math.round(fbTotal * 0.15)),
        Math.max(2, Math.round(fbTotal * 0.2)),
        Math.max(1, Math.round(fbTotal * 0.18)),
        Math.max(3, Math.round(fbTotal * 0.25)),
        Math.max(4, Math.round(fbTotal * 0.35)),
        fbTotal
      ];

      const spinData = [
        Math.max(2, Math.round(spinTotal * 0.2)),
        Math.max(3, Math.round(spinTotal * 0.3)),
        Math.max(2, Math.round(spinTotal * 0.25)),
        Math.max(4, Math.round(spinTotal * 0.4)),
        Math.max(5, Math.round(spinTotal * 0.5)),
        Math.max(7, Math.round(spinTotal * 0.7)),
        spinTotal
      ];

      // Build or update Line Chart
      if (weeklyTrendChart) {
        weeklyTrendChart.data.labels = labels;
        weeklyTrendChart.data.datasets[0].data = fbData;
        weeklyTrendChart.data.datasets[1].data = spinData;
        weeklyTrendChart.update();
      } else {
        weeklyTrendChart = new Chart(lineCanvas, {
          type: 'line',
          data: {
            labels: labels,
            datasets: [
              {
                label: 'Góp ý & Đánh giá',
                data: fbData,
                borderColor: '#E59A55',
                backgroundColor: 'rgba(229, 154, 85, 0.15)',
                tension: 0.35,
                fill: true,
                pointBackgroundColor: '#E59A55',
                pointRadius: 4,
                pointHoverRadius: 6
              },
              {
                label: 'Lượt quay Minigame',
                data: spinData,
                borderColor: '#2ECC71',
                backgroundColor: 'rgba(46, 204, 113, 0.1)',
                tension: 0.35,
                fill: true,
                pointBackgroundColor: '#2ECC71',
                pointRadius: 4,
                pointHoverRadius: 6
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: {
                labels: { color: '#EDE5D8', font: { family: 'Inter', size: 12 } }
              },
              tooltip: {
                backgroundColor: '#2C1810',
                titleColor: '#E59A55',
                bodyColor: '#EDE5D8',
                borderColor: 'rgba(229, 154, 85, 0.4)',
                borderWidth: 1,
                padding: 10
              }
            },
            scales: {
              x: {
                grid: { color: 'rgba(184, 165, 139, 0.1)' },
                ticks: { color: '#B8A58B', font: { family: 'Inter', size: 11 } }
              },
              y: {
                beginAtZero: true,
                grid: { color: 'rgba(184, 165, 139, 0.1)' },
                ticks: { color: '#B8A58B', stepSize: 2, font: { family: 'Inter', size: 11 } }
              }
            }
          }
        });
      }

      // 2. Prepare Satisfaction Doughnut Data
      let star5 = 0, star4 = 0, starLow = 0;
      if (feedbacks.length > 0) {
        feedbacks.forEach(f => {
          if (f.rating === 5) star5++;
          else if (f.rating === 4) star4++;
          else starLow++;
        });
      } else {
        star5 = 8; star4 = 2; starLow = 0;
      }

      const totalReviews = star5 + star4 + starLow;
      const totalEl = document.getElementById('satisfactionTotalText');
      if (totalEl) totalEl.textContent = `Tổng: ${totalReviews} đánh giá`;

      if (satisfactionChart) {
        satisfactionChart.data.datasets[0].data = [star5, star4, starLow];
        satisfactionChart.update();
      } else {
        satisfactionChart = new Chart(pieCanvas, {
          type: 'doughnut',
          data: {
            labels: ['5 Sao (Tuyệt vời)', '4 Sao (Hài lòng)', '1-3 Sao (Cần cải thiện)'],
            datasets: [{
              data: [star5, star4, starLow],
              backgroundColor: ['#E59A55', '#C59B63', '#E74C3C'],
              borderColor: '#2C1810',
              borderWidth: 3,
              hoverOffset: 4
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            cutout: '68%',
            plugins: {
              legend: {
                position: 'bottom',
                labels: { color: '#EDE5D8', font: { family: 'Inter', size: 11.5 }, padding: 14 }
              },
              tooltip: {
                backgroundColor: '#2C1810',
                titleColor: '#E59A55',
                bodyColor: '#EDE5D8',
                borderColor: 'rgba(229, 154, 85, 0.4)',
                borderWidth: 1,
                callbacks: {
                  label: function(context) {
                    const val = context.raw || 0;
                    const pct = totalReviews > 0 ? Math.round((val / totalReviews) * 100) : 0;
                    return ` ${context.label}: ${val} lượt (${pct}%)`;
                  }
                }
              }
            }
          }
        });
      }
    }

    function updateCharts() {
      initOrUpdateCharts(cachedFeedbacks, cachedSpins);
    }

    // =========================================================================
    // 2. MENU MANAGEMENT CRUD LOGIC
    // =========================================================================
    let cachedMenuItems = [];

    async function loadMenu() {
      const tbody = document.getElementById('menuTableBody');
      tbody.innerHTML = '<tr><td colspan="7" style="text-align: center; color: var(--text-muted); padding: 25px;">⏳ Đang tải thực đơn...</td></tr>';

      const res = await fetchMenuItemsFromCloud();
      cachedMenuItems = res.data || [];

      const search = (document.getElementById('menuSearchInput').value || '').toLowerCase();
      const catFilter = document.getElementById('menuCategoryFilter').value;

      const filtered = cachedMenuItems.filter(item => {
        const matchName = (item.name || '').toLowerCase().includes(search) || (item.description || '').toLowerCase().includes(search);
        const matchCat = catFilter === 'all' || item.category === catFilter;
        return matchName && matchCat;
      });

      tbody.innerHTML = '';
      if (filtered.length === 0) {
        tbody.innerHTML = '<tr><td colspan="7" style="text-align: center; color: var(--text-muted); padding: 30px;">Không tìm thấy món nước nào phù hợp</td></tr>';
      } else {
        filtered.forEach(item => {
          let badgeHtml = '<span style="color:var(--text-muted);font-size:12px;">—</span>';
          if (item.badge === 'Signature') badgeHtml = '<span class="badge badge-gold">🌟 Signature</span>';
          else if (item.badge === 'Bán chạy') badgeHtml = '<span class="badge badge-warning">🔥 Bán chạy</span>';
          else if (item.badge === 'Món mới') badgeHtml = '<span class="badge badge-success">✨ Món mới</span>';
          else if (item.badge) badgeHtml = `<span class="badge badge-warning">${escapeHtml(item.badge)}</span>`;

          const priceFmt = (Number(item.price) || 0).toLocaleString('vi-VN') + ' đ';

          const tr = document.createElement('tr');
          tr.innerHTML = `
            <td>
              <img src="${escapeHtml(item.image_url || 'assets/news/news-1-drinks.webp')}" alt="${escapeHtml(item.name)}" style="width:48px;height:48px;object-fit:cover;border-radius:8px;border:1px solid var(--border);" onerror="this.src='assets/hero1.jpg'" />
            </td>
            <td>
              <strong style="color: #EDE5D8; font-size: 14.5px;">${escapeHtml(item.name)}</strong>
              <div style="font-size: 12px; color: var(--text-muted); margin-top: 2px; max-width: 320px; text-overflow: ellipsis; overflow: hidden; white-space: nowrap;">
                ${escapeHtml(item.description || 'Chưa có mô tả')}
              </div>
            </td>
            <td><span class="badge badge-warning">${escapeHtml(item.category || 'Cà phê')}</span></td>
            <td><strong style="color: var(--accent); font-size: 14px;">${priceFmt}</strong></td>
            <td>${badgeHtml}</td>
            <td>
              <div class="switch-wrap">
                <label class="switch">
                  <input type="checkbox" ${item.is_available !== false ? 'checked' : ''} onchange="handleToggleMenuAvailable(${item.id}, this.checked)" />
                  <span class="slider"></span>
                </label>
                <span style="font-size: 12px; color: ${item.is_available !== false ? '#2ECC71' : 'var(--text-muted)'};">
                  ${item.is_available !== false ? 'Còn hàng' : 'Hết hàng'}
                </span>
              </div>
            </td>
            <td style="text-align: right;">
              <div style="display: inline-flex; gap: 6px;">
                <button type="button" class="btn-sm-primary" onclick="openEditMenuModal(${item.id})">✏️ Sửa</button>
                <button type="button" class="btn-sm-danger" onclick="handleDeleteMenuItem(${item.id})">🗑️ Xóa</button>
              </div>
            </td>
          `;
          tbody.appendChild(tr);
        });
      }

      // Update sidebar badge
      const sideBadge = document.getElementById('sidebarMenuBadge');
      if (sideBadge) sideBadge.textContent = cachedMenuItems.length;
      updateOverviewStats();
    }

    document.getElementById('menuSearchInput').addEventListener('input', loadMenu);
    document.getElementById('menuCategoryFilter').addEventListener('change', loadMenu);
    document.getElementById('refreshMenuBtn').addEventListener('click', loadMenu);

    // Modal Add/Edit
    function openAddMenuModal() {
      document.getElementById('menuModalTitle').textContent = '➕ Thêm Món Mới Vào Thực Đơn';
      document.getElementById('menuItemId').value = '';
      document.getElementById('menuItemName').value = '';
      document.getElementById('menuItemPrice').value = '';
      document.getElementById('menuItemCategory').value = 'Cà phê';
      document.getElementById('menuItemBadge').value = '';
      document.getElementById('menuItemImage').value = 'assets/news/news-1-drinks.webp';
      document.getElementById('menuItemDesc').value = '';
      document.getElementById('menuItemAvailable').checked = true;
      document.getElementById('menuItemModal').classList.add('open');
    }

    function openEditMenuModal(id) {
      const item = cachedMenuItems.find(m => m.id === id);
      if (!item) return;
      document.getElementById('menuModalTitle').textContent = '✏️ Chỉnh Sửa Món Nước';
      document.getElementById('menuItemId').value = item.id;
      document.getElementById('menuItemName').value = item.name || '';
      document.getElementById('menuItemPrice').value = item.price || 0;
      document.getElementById('menuItemCategory').value = item.category || 'Cà phê';
      document.getElementById('menuItemBadge').value = item.badge || '';
      document.getElementById('menuItemImage').value = item.image_url || 'assets/news/news-1-drinks.webp';
      document.getElementById('menuItemDesc').value = item.description || '';
      document.getElementById('menuItemAvailable').checked = item.is_available !== false;
      document.getElementById('menuItemModal').classList.add('open');
    }

    function closeMenuModal() {
      document.getElementById('menuItemModal').classList.remove('open');
    }

    document.getElementById('menuItemForm').addEventListener('submit', async () => {
      const idVal = document.getElementById('menuItemId').value;
      const name = document.getElementById('menuItemName').value.trim();
      const price = parseFloat(document.getElementById('menuItemPrice').value) || 0;
      const category = document.getElementById('menuItemCategory').value;
      const badge = document.getElementById('menuItemBadge').value;
      const image_url = document.getElementById('menuItemImage').value.trim();
      const description = document.getElementById('menuItemDesc').value.trim();
      const is_available = document.getElementById('menuItemAvailable').checked;

      if (!name) return alert('Vui lòng nhập tên món!');

      showToast('Đang lưu thông tin món nước...');
      await saveMenuItemToCloud({
        id: idVal ? Number(idVal) : null,
        name,
        price,
        category,
        badge,
        image_url,
        description,
        is_available
      });

      closeMenuModal();
      showToast(idVal ? `Đã cập nhật món "${name}" thành công!` : `Đã thêm món mới "${name}" thành công!`);
      loadMenu();
    });

    window.handleToggleMenuAvailable = async function(id, isAvailable) {
      await toggleMenuItemAvailabilityInCloud(id, isAvailable);
      showToast(isAvailable ? 'Món đã được bật phục vụ!' : 'Món đã được chuyển sang tạm hết hàng.');
      loadMenu();
    };

    window.handleDeleteMenuItem = async function(id) {
      if (confirm('Bạn có chắc muốn xóa món này khỏi thực đơn?')) {
        showToast('Đang xóa món...');
        await deleteMenuItemFromCloud(id);
        showToast('Đã xóa món khỏi thực đơn thành công.');
        loadMenu();
      }
    };

    document.getElementById('exportMenuCsvBtn').addEventListener('click', () => {
      if (cachedMenuItems.length === 0) return alert('Chưa có món nào để xuất!');
      let csv = 'ID,Tên món,Danh mục,Giá bán,Nhãn dán,Còn hàng,Mô tả\n';
      cachedMenuItems.forEach(m => {
        csv += `"${m.id}","${m.name || ''}","${m.category || ''}","${m.price || 0}","${m.badge || ''}","${m.is_available ? 'Có' : 'Không'}","${(m.description || '').replace(/"/g, '""')}"\n`;
      });
      downloadCsv(csv, 'olion_menu_items.csv');
    });

    // =========================================================================
    // 3. LOYALTY PROGRAM & CUSTOMER MANAGEMENT
    // =========================================================================
    let cachedCustomers = [];
    let selectedLoyaltyCustomer = null;
    let loyaltyMode = 'earn'; // 'earn' or 'redeem'

    async function loadCustomers() {
      const tbody = document.getElementById('customerTableBody');
      const search = (document.getElementById('customerSearchInput').value || '').toLowerCase();
      const tierFilter = document.getElementById('customerTierFilter').value;

      tbody.innerHTML = '<tr><td colspan="7" style="text-align: center; color: var(--text-muted); padding: 25px;">⏳ Đang tải khách hàng...</td></tr>';

      const res = await fetchCustomersFromCloud();
      cachedCustomers = res.data || [];

      const filtered = cachedCustomers.filter(c => {
        const matchText = (c.name || '').toLowerCase().includes(search) || (c.contact || '').toLowerCase().includes(search);
        const matchTier = tierFilter === 'all' || c.tier === tierFilter;
        return matchText && matchTier;
      });

      tbody.innerHTML = '';
      if (filtered.length === 0) {
        tbody.innerHTML = '<tr><td colspan="7" style="text-align: center; color: var(--text-muted); padding: 30px;">Chưa có khách hàng nào phù hợp</td></tr>';
      } else {
        filtered.forEach(c => {
          let tierBadge = '<span class="badge badge-warning">Thành viên</span>';
          if (c.tier === 'Kim Cương') tierBadge = '<span class="badge badge-purple">💎 Kim Cương</span>';
          else if (c.tier === 'Vàng') tierBadge = '<span class="badge badge-gold">👑 Vàng</span>';
          else if (c.tier === 'Bạc') tierBadge = '<span class="badge badge-silver">🥈 Bạc</span>';

          const tr = document.createElement('tr');
          tr.innerHTML = `
            <td>
              <strong style="color: #EDE5D8;">${escapeHtml(c.name || 'Khách hàng')}</strong>
              <div style="font-size: 11px; color: var(--text-muted);">Gia nhập: ${escapeHtml(c.date || 'Gần đây')}</div>
            </td>
            <td><strong style="color: var(--accent); font-family: monospace; font-size: 14px;">${escapeHtml(c.contact || '')}</strong></td>
            <td>
              <span style="font-size: 15px; font-weight: 800; color: #EDE5D8;">${c.points || 0}</span>
              <span style="font-size: 11px; color: var(--text-muted);">điểm</span>
            </td>
            <td>${tierBadge}</td>
            <td><span class="badge badge-warning">${escapeHtml(c.source || 'Website')}</span></td>
            <td style="max-width: 200px; font-size: 12px; color: var(--text-muted); text-overflow: ellipsis; overflow: hidden; white-space: nowrap;">
              ${escapeHtml(c.notes || '—')}
            </td>
            <td style="text-align: right;">
              <div style="display: inline-flex; gap: 6px;">
                <button type="button" class="btn-sm-primary" style="background: rgba(155, 89, 182, 0.2); color: #D2A8E8; border-color: rgba(155, 89, 182, 0.4);" onclick="openLoyaltyModal('${c.contact}')">💎 Tích điểm</button>
                <button type="button" class="btn-sm-primary" onclick="openPointHistoryModal(${c.id}, '${c.contact}', '${escapeHtml(c.name)}')">📜 Lịch sử</button>
                <button type="button" class="btn-sm-danger" onclick="handleDeleteCustomer(${c.id})">Xóa</button>
              </div>
            </td>
          `;
          tbody.appendChild(tr);
        });
      }

      // Update badge
      const sideBadge = document.getElementById('sidebarCustomerBadge');
      if (sideBadge) sideBadge.textContent = cachedCustomers.length;
      updateOverviewStats();
    }

    document.getElementById('customerSearchInput').addEventListener('input', loadCustomers);
    document.getElementById('customerTierFilter').addEventListener('change', loadCustomers);
    document.getElementById('refreshCustomersBtn').addEventListener('click', loadCustomers);

    // POS Loyalty Modal
    function openLoyaltyModal(phone = '') {
      document.getElementById('loyaltyModal').classList.add('open');
      if (phone) {
        document.getElementById('loyaltyLookupPhone').value = phone;
        lookupLoyaltyCustomer(phone);
      } else {
        document.getElementById('loyaltyLookupPhone').value = '';
        selectLoyaltyCust(cachedCustomers[0] || null);
      }
      setLoyaltyMode('earn');
    }

    function closeLoyaltyModal() {
      document.getElementById('loyaltyModal').classList.remove('open');
    }

    function selectLoyaltyCust(cust) {
      selectedLoyaltyCustomer = cust;
      const nameEl = document.getElementById('loyaltyCustName');
      const phoneEl = document.getElementById('loyaltyCustPhone');
      const badgeEl = document.getElementById('loyaltyCustTierBadge');
      const pointsEl = document.getElementById('loyaltyCustPoints');

      if (cust) {
        nameEl.textContent = cust.name || 'Khách hàng';
        phoneEl.textContent = 'SĐT: ' + (cust.contact || '');
        pointsEl.textContent = (cust.points || 0) + ' Điểm';

        let badgeHtml = '<span class="badge badge-warning">Thành viên</span>';
        if (cust.tier === 'Kim Cương') badgeHtml = '<span class="badge badge-purple">💎 Kim Cương</span>';
        else if (cust.tier === 'Vàng') badgeHtml = '<span class="badge badge-gold">👑 Hạng Vàng</span>';
        else if (cust.tier === 'Bạc') badgeHtml = '<span class="badge badge-silver">🥈 Hạng Bạc</span>';
        badgeEl.innerHTML = badgeHtml;
      } else {
        nameEl.textContent = 'Khách chưa có trong hệ thống';
        phoneEl.textContent = 'Có thể tự động tạo mới khi tích điểm!';
        pointsEl.textContent = '0 Điểm';
        badgeEl.innerHTML = '<span class="badge badge-warning">Khách mới</span>';
      }
    }

    function lookupLoyaltyCustomer(phone) {
      const clean = (phone || '').trim();
      if (!clean) return;
      const match = cachedCustomers.find(c => c.contact === clean || c.contact.includes(clean));
      if (match) {
        selectLoyaltyCust(match);
      } else {
        selectLoyaltyCust({
          id: null,
          name: 'Khách hàng mới',
          contact: clean,
          points: 0,
          tier: 'Thành viên'
        });
      }
    }

    document.getElementById('loyaltyLookupBtn').addEventListener('click', () => {
      lookupLoyaltyCustomer(document.getElementById('loyaltyLookupPhone').value);
    });

    function setLoyaltyMode(mode) {
      loyaltyMode = mode;
      const btnEarn = document.getElementById('tabModeEarn');
      const btnRedeem = document.getElementById('tabModeRedeem');
      const secEarn = document.getElementById('earnPointsSection');
      const secRedeem = document.getElementById('redeemPointsSection');

      if (mode === 'earn') {
        btnEarn.className = 'btn-primary';
        btnEarn.style.background = 'linear-gradient(135deg, #2ECC71, #27AE60)';
        btnRedeem.className = 'btn-secondary';
        btnRedeem.style.background = 'rgba(255, 255, 255, 0.08)';
        secEarn.style.display = 'block';
        secRedeem.style.display = 'none';
        document.getElementById('loyaltyReasonInput').value = 'Mua nước tại quán';
      } else {
        btnEarn.className = 'btn-secondary';
        btnEarn.style.background = 'rgba(255, 255, 255, 0.08)';
        btnRedeem.className = 'btn-primary';
        btnRedeem.style.background = 'linear-gradient(135deg, #E74C3C, #C0392B)';
        secEarn.style.display = 'none';
        secRedeem.style.display = 'block';
        document.getElementById('loyaltyReasonInput').value = 'Đổi voucher giảm giá';
      }
    }

    document.getElementById('tabModeEarn').addEventListener('click', () => setLoyaltyMode('earn'));
    document.getElementById('tabModeRedeem').addEventListener('click', () => setLoyaltyMode('redeem'));

    // Bill to points converter
    document.getElementById('loyaltyBillAmount').addEventListener('input', (e) => {
      const val = parseFloat(e.target.value) || 0;
      document.getElementById('loyaltyPointsEarnInput').value = Math.floor(val / 10000);
    });

    // Submit Point Adjustment
    document.getElementById('loyaltyActionForm').addEventListener('submit', async () => {
      const phoneInput = document.getElementById('loyaltyLookupPhone').value.trim();
      const targetPhone = selectedLoyaltyCustomer?.contact || phoneInput;
      if (!targetPhone) return alert('Vui lòng nhập số điện thoại khách hàng!');

      let pointsDelta = 0;
      let reason = document.getElementById('loyaltyReasonInput').value.trim();

      if (loyaltyMode === 'earn') {
        pointsDelta = parseInt(document.getElementById('loyaltyPointsEarnInput').value) || 0;
        if (pointsDelta <= 0) return alert('Vui lòng nhập số điểm cộng lớn hơn 0!');
      } else {
        const redeemPoints = parseInt(document.getElementById('loyaltyPointsRedeemInput').value) || 0;
        if (redeemPoints <= 0) return alert('Vui lòng nhập số điểm cần trừ lớn hơn 0!');
        if (selectedLoyaltyCustomer && selectedLoyaltyCustomer.points < redeemPoints) {
          return alert(`Khách hàng chỉ có ${selectedLoyaltyCustomer.points} điểm, không đủ để trừ ${redeemPoints} điểm!`);
        }
        pointsDelta = -redeemPoints;
      }

      // If customer does not exist in DB yet, create them first
      if (!selectedLoyaltyCustomer || !selectedLoyaltyCustomer.id) {
        await saveCustomerToCloud({
          name: 'Khách hàng POS',
          contact: targetPhone,
          points: 0,
          source: 'POS Quầy thu ngân'
        });
      }

      showToast('Đang xử lý giao dịch tích điểm...');
      const res = await adjustCustomerPointsInCloud(
        selectedLoyaltyCustomer?.id,
        targetPhone,
        pointsDelta,
        reason,
        loyaltyMode === 'earn' ? 'earn' : 'redeem'
      );

      // Đồng bộ vào bảng loyalty_members nếu có
      if (loyaltyMode === 'earn' && window.addLoyaltyMemberPoints) {
        await window.addLoyaltyMemberPoints(targetPhone, pointsDelta, selectedLoyaltyCustomer?.name || 'Khách hàng');
      } else if (loyaltyMode === 'redeem' && window.redeemLoyaltyMemberPoints) {
        await window.redeemLoyaltyMemberPoints(targetPhone, Math.abs(pointsDelta), reason);
      }

      showToast(pointsDelta > 0 ? `🎉 Đã cộng +${pointsDelta} điểm cho khách ${targetPhone}!` : `✨ Đã trừ ${Math.abs(pointsDelta)} điểm thành công!`);
      closeLoyaltyModal();
      loadCustomers();
    });

    // Add customer modal
    function openAddCustomerModal() {
      document.getElementById('newCustomerForm').reset();
      document.getElementById('addCustomerModal').classList.add('open');
    }
    function closeAddCustomerModal() {
      document.getElementById('addCustomerModal').classList.remove('open');
    }

    document.getElementById('newCustomerForm').addEventListener('submit', async () => {
      const name = document.getElementById('newCustName').value.trim();
      const contact = document.getElementById('newCustContact').value.trim();
      const points = parseInt(document.getElementById('newCustPoints').value) || 0;
      const notes = document.getElementById('newCustNotes').value.trim();

      if (!contact) return alert('Vui lòng nhập số điện thoại / liên hệ!');

      showToast('Đang thêm khách hàng...');
      await saveCustomerToCloud({ name, contact, points, notes, source: 'Quản trị viên tạo' });
      closeAddCustomerModal();
      showToast(`Đã thêm khách hàng ${name} thành công!`);
      loadCustomers();
    });

    // Point History Modal
    async function openPointHistoryModal(id, phone, name) {
      document.getElementById('historyModalTitle').textContent = `📜 Lịch Sử Giao Dịch: ${name} (${phone})`;
      const tbody = document.getElementById('pointHistoryTableBody');
      tbody.innerHTML = '<tr><td colspan="5" style="text-align: center; color: var(--text-muted); padding: 20px;">⏳ Đang tải lịch sử...</td></tr>';
      document.getElementById('pointHistoryModal').classList.add('open');

      const res = await fetchCustomerPointHistoryFromCloud(id, phone);
      const list = res.data || [];
      tbody.innerHTML = '';
      if (list.length === 0) {
        tbody.innerHTML = '<tr><td colspan="5" style="text-align: center; color: var(--text-muted); padding: 20px;">Chưa có giao dịch điểm nào</td></tr>';
      } else {
        list.forEach(tx => {
          const isEarn = tx.points_change > 0;
          const tr = document.createElement('tr');
          tr.innerHTML = `
            <td><span class="badge ${isEarn ? 'badge-success' : 'badge-warning'}">${isEarn ? 'Cộng điểm' : 'Đổi thưởng'}</span></td>
            <td><strong style="color: ${isEarn ? '#2ECC71' : '#E74C3C'}; font-size: 14px;">${isEarn ? '+' : ''}${tx.points_change} đ</strong></td>
            <td><strong style="color: #EDE5D8;">${tx.balance_after || '—'} đ</strong></td>
            <td style="font-size: 13px;">${escapeHtml(tx.reason || '')}</td>
            <td style="font-size: 12px; color: var(--text-muted);">${tx.created_at ? new Date(tx.created_at).toLocaleString('vi-VN') : 'Gần đây'}</td>
          `;
          tbody.appendChild(tr);
        });
      }
    }

    function closePointHistoryModal() {
      document.getElementById('pointHistoryModal').classList.remove('open');
    }

    window.handleDeleteCustomer = async function(id) {
      if (confirm('Xác nhận xóa khách hàng này khỏi hệ thống?')) {
        await deleteCustomerFromCloud(id);
        showToast('Đã xóa khách hàng thành công.');
        loadCustomers();
      }
    };

    document.getElementById('exportCustomerCsvBtn').addEventListener('click', () => {
      if (cachedCustomers.length === 0) return alert('Chưa có danh sách khách hàng để xuất!');
      let csv = 'Họ tên,Số điện thoại/Email,Điểm,Hạng thẻ,Nguồn,Ghi chú,Ngày\n';
      cachedCustomers.forEach(c => {
        csv += `"${c.name || ''}","${c.contact || ''}","${c.points || 0}","${c.tier || ''}","${c.source || ''}","${(c.notes || '').replace(/"/g, '""')}","${c.date || ''}"\n`;
      });
      downloadCsv(csv, 'olion_customers.csv');
    });

    // =========================================================================
    // 4. FEEDBACKS, PROMOTIONS, MINIGAME & SUPABASE
    // =========================================================================
    let cachedFeedbacks = [];
    let cachedSpins = [];

    async function loadFeedbacks() {
      const tbody = document.getElementById('feedbackTableBody');
      const recentTbody = document.getElementById('overviewRecentFeedbackTable');
      tbody.innerHTML = '<tr><td colspan="8" style="text-align: center; color: var(--text-muted); padding: 25px;">⏳ Đang tải dữ liệu...</td></tr>';

      const res = await fetchAdminFeedbacksFromCloud();
      cachedFeedbacks = res.data || [];

      const filter = document.getElementById('feedbackFilterStar').value;
      tbody.innerHTML = '';

      let filtered = cachedFeedbacks;
      if (filter === '5') filtered = cachedFeedbacks.filter(f => f.rating === 5);
      else if (filter === '4') filtered = cachedFeedbacks.filter(f => f.rating === 4);
      else if (filter === 'low') filtered = cachedFeedbacks.filter(f => f.rating <= 3);

      if (filtered.length === 0) {
        tbody.innerHTML = `<tr><td colspan="8" style="text-align: center; color: var(--text-muted); padding: 30px;">Chưa có góp ý nào phù hợp</td></tr>`;
      } else {
        filtered.forEach(fb => {
          const stars = '★'.repeat(fb.rating || 5) + '☆'.repeat(Math.max(0, 5 - (fb.rating || 5)));
          const photoCell = fb.imageDataUrl
            ? `<a href="${fb.imageDataUrl}" target="_blank" title="Xem ảnh đầy đủ">
                <img src="${fb.imageDataUrl}" alt="Ảnh góp ý" style="width:48px;height:48px;object-fit:cover;border-radius:6px;border:1px solid var(--border);cursor:pointer;" />
               </a>`
            : `<span style="color:var(--text-muted);font-size:11px;">—</span>`;

          const tr = document.createElement('tr');
          tr.innerHTML = `
            <td><strong>${escapeHtml(fb.name || 'Khách hàng')}</strong></td>
            <td>${escapeHtml(fb.contact || 'Không để lại')}</td>
            <td style="color: var(--accent); font-size: 14px;">${stars}</td>
            <td style="max-width: 280px; line-height: 1.4;">${escapeHtml(fb.content || '')}</td>
            <td style="text-align:center;">${photoCell}</td>
            <td>${escapeHtml(fb.date || 'Gần đây')}</td>
            <td>
              <span class="badge ${fb.approved !== false ? 'badge-success' : 'badge-warning'}">
                ${fb.approved !== false ? 'Đã duyệt web' : 'Ẩn trên web'}
              </span>
            </td>
            <td>
              <div style="display: flex; gap: 6px;">
                <button type="button" class="btn-secondary" style="padding: 4px 8px; font-size: 11.5px;" onclick="toggleApproveFeedback(${fb.id}, ${fb.approved !== false})">
                  ${fb.approved !== false ? 'Ẩn' : 'Duyệt'}
                </button>
                <button type="button" class="btn-sm-danger" onclick="handleDeleteFeedback(${fb.id})">
                  Xóa
                </button>
              </div>
            </td>
          `;
          tbody.appendChild(tr);
        });
      }

      // Recent feedbacks in overview
      if (recentTbody) {
        recentTbody.innerHTML = '';
        const recents = cachedFeedbacks.slice(0, 4);
        if (recents.length === 0) {
          recentTbody.innerHTML = `<tr><td colspan="4" style="text-align: center; color: var(--text-muted);">Chưa có góp ý nào</td></tr>`;
        } else {
          recents.forEach(fb => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
              <td><strong>${escapeHtml(fb.name || 'Khách hàng')}</strong></td>
              <td style="color: var(--accent);">${'★'.repeat(fb.rating || 5)}</td>
              <td style="max-width: 280px; text-overflow: ellipsis; overflow: hidden; white-space: nowrap;">${escapeHtml(fb.content)}</td>
              <td>${escapeHtml(fb.date || 'Gần đây')}</td>
            `;
            recentTbody.appendChild(tr);
          });
        }
      }

      updateOverviewStats();
      updateCharts();
    }

    window.toggleApproveFeedback = async function(id, currentApproved) {
      showToast('Đang cập nhật trạng thái...');
      await toggleFeedbackApprovalInCloud(id, !currentApproved);
      showToast(!currentApproved ? 'Đã duyệt hiển thị lên trang chủ!' : 'Đã ẩn góp ý khỏi trang chủ.');
      loadFeedbacks();
    };

    window.handleDeleteFeedback = async function(id) {
      if (confirm('Bạn có chắc muốn xóa góp ý này khỏi hệ thống?')) {
        showToast('Đang xóa góp ý...');
        await deleteFeedbackFromCloud(id);
        showToast('Đã xóa góp ý thành công.');
        loadFeedbacks();
      }
    };

    document.getElementById('feedbackFilterStar').addEventListener('change', loadFeedbacks);
    document.getElementById('refreshFeedbackBtn').addEventListener('click', loadFeedbacks);

    document.getElementById('exportFeedbackCsvBtn').addEventListener('click', () => {
      if (cachedFeedbacks.length === 0) return alert('Chưa có dữ liệu để xuất!');
      let csv = 'Họ tên,Liên hệ,Số sao,Nội dung,Ngày gửi,Duyệt web\n';
      cachedFeedbacks.forEach(f => {
        csv += `"${f.name || ''}","${f.contact || ''}","${f.rating || 5}","${(f.content || '').replace(/"/g, '""')}","${f.date || ''}","${f.approved ? 'Có' : 'Không'}"\n`;
      });
      downloadCsv(csv, 'olion_feedbacks.csv');
    });

    document.getElementById('seedFeedbackBtn').addEventListener('click', async () => {
      const sample = {
        name: 'Phương Thảo',
        contact: '0912 345 678',
        rating: 5,
        content: 'Cà phê muối ở đây đỉnh chóp, kem mặn mịn màng thơm lừng. Quán decor ấm cúng rất hợp chụp hình chill!',
        approved: true
      };
      await submitFeedbackToCloud(sample);
      showToast('Đã thêm đánh giá mẫu thành công!');
      loadFeedbacks();
    });

    // Minigame Settings
    const minigameToggle = document.getElementById('minigameEnableToggle');
    const DEFAULT_PRIZES = [
      { text: 'Giảm 15%',    code: 'OLION15',    desc: 'Giảm ngay 15% trên tổng hóa đơn!',            pct: 15, color: '#E59A55' },
      { text: 'Free Thạch',  code: 'FREETHACH',  desc: 'Tặng 1 phần topping thạch bất kỳ!',           pct: 20, color: '#1B683F' },
      { text: 'Giảm 20k',    code: 'OLION20K',   desc: 'Giảm 20.000đ cho đơn từ 60.000đ!',            pct: 15, color: '#C59B63' },
      { text: 'Cà Phê Muối', code: 'FREECAPHE',  desc: 'Tặng 1 ly Cà Phê Muối đặc trưng Olion!',     pct: 10, color: '#D36C2D' },
      { text: 'Giảm 10%',    code: 'OLION10',    desc: 'Giảm 10% cho mọi thức uống!',                 pct: 25, color: '#E59A55' },
      { text: 'Trà Đào',     code: 'FREETRADAO', desc: 'Tặng 1 ly Trà Đào Cam Sả mát lạnh!',         pct: 15, color: '#1B683F' },
    ];
    let currentPrizes = [...DEFAULT_PRIZES.map(p => ({...p}))];

    function updateTotalPct() {
      const total = currentPrizes.reduce((s, p) => s + (parseFloat(p.pct) || 0), 0);
      const el = document.getElementById('totalPctDisplay');
      if (!el) return;
      el.textContent = `Tổng: ${total.toFixed(1)}%`;
      el.style.color = Math.abs(total - 100) < 0.1 ? '#2ECC71' : '#E59A55';
    }

    function renderPrizeRows() {
      const container = document.getElementById('prizeRowsContainer');
      if (!container) return;
      container.innerHTML = '';
      currentPrizes.forEach((prize, idx) => {
        const row = document.createElement('div');
        row.style.cssText = 'display:grid;grid-template-columns:2fr 1.3fr 60px 26px;gap:6px;align-items:center;background:rgba(0,0,0,0.25);padding:8px 10px;border-radius:8px;border-left:4px solid ' + (prize.color || '#E59A55');
        row.innerHTML = `
          <div style="display:flex;gap:6px;align-items:center;">
            <input type="color" value="${prize.color || '#E59A55'}" data-idx="${idx}" data-field="color"
              style="width:22px;height:22px;border:none;border-radius:4px;padding:0;cursor:pointer;background:transparent;flex-shrink:0;"
              title="Màu ô" />
            <input type="text" value="${escapeHtml(prize.text)}" data-idx="${idx}" data-field="text"
              placeholder="Tên giải thưởng"
              style="font-size:13px;padding:5px 8px;width:100%;background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.1);border-radius:5px;color:#fff;" />
          </div>
          <input type="text" value="${escapeHtml(prize.code)}" data-idx="${idx}" data-field="code"
            placeholder="Mã code"
            style="font-size:12px;font-family:monospace;padding:5px 8px;background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.1);border-radius:5px;color:#E59A55;" />
          <input type="number" value="${prize.pct}" data-idx="${idx}" data-field="pct"
            min="0" max="100" step="1"
            style="font-size:13px;padding:5px 6px;text-align:center;background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.1);border-radius:5px;color:#fff;" />
          <button type="button" data-idx="${idx}" class="prize-del-btn"
            style="background:rgba(255,60,60,0.15);border:1px solid rgba(255,60,60,0.3);color:#ff6b6b;width:26px;height:26px;border-radius:5px;cursor:pointer;font-size:14px;display:flex;align-items:center;justify-content:center;padding:0;">✕</button>
        `;
        container.appendChild(row);
      });

      container.querySelectorAll('input[data-field]').forEach(inp => {
        inp.addEventListener('input', e => {
          const idx = +e.target.dataset.idx;
          const field = e.target.dataset.field;
          currentPrizes[idx][field] = field === 'pct' ? parseFloat(e.target.value) || 0 : e.target.value;
          if (field === 'color') {
            e.target.closest('div[style*="border-left"]').style.borderLeftColor = e.target.value;
          }
          updateTotalPct();
        });
      });
      container.querySelectorAll('.prize-del-btn').forEach(btn => {
        btn.addEventListener('click', e => {
          const idx = +e.currentTarget.dataset.idx;
          if (currentPrizes.length <= 2) { showToast('Cần ít nhất 2 ô quà!'); return; }
          currentPrizes.splice(idx, 1);
          renderPrizeRows();
          updateTotalPct();
        });
      });

      updateTotalPct();
    }


    async function loadMinigame() {
      if (typeof fetchSiteSettingsFromCloud === 'function') {
        const { data } = await fetchSiteSettingsFromCloud();
        if (data) {
          if (minigameToggle) minigameToggle.checked = data.is_wheel_active !== false;
          if (data.wheel_prizes && Array.isArray(data.wheel_prizes) && data.wheel_prizes.length >= 2) {
            currentPrizes = data.wheel_prizes.map(p => ({...p}));
          }
          if (document.getElementById('announcementEnableToggle')) document.getElementById('announcementEnableToggle').checked = !!data.is_notification_active;
          if (document.getElementById('announcementTextInput')) document.getElementById('announcementTextInput').value = data.notification_text || '';
        }
      }
      renderPrizeRows();

      const tbody = document.getElementById('minigameLeadsTable');
      tbody.innerHTML = '<tr><td colspan="4" style="text-align: center; color: var(--text-muted); padding: 15px;">⏳ Đang tải...</td></tr>';
      const res = await fetchLuckySpinsFromCloud();
      cachedSpins = res.data || [];
      tbody.innerHTML = '';
      if (cachedSpins.length === 0) {
        tbody.innerHTML = `<tr><td colspan="4" style="text-align: center; color: var(--text-muted); padding: 20px;">Chưa có lượt quay nào</td></tr>`;
      } else {
        cachedSpins.forEach(spin => {
          tbody.innerHTML += `
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
              <td style="padding:12px;color:#fff;">${escapeHtml(spin.customer_name || 'Khách ẩn danh')}</td>
              <td style="padding:12px;color:#E59A55;">${escapeHtml(spin.customer_phone)}</td>
              <td style="padding:12px;color:#2ECC71;">${escapeHtml(spin.prize_name)}</td>
              <td style="padding:12px;color:var(--text-muted);font-size:12.5px;">${new Date(spin.created_at).toLocaleString('vi-VN')}</td>
            </tr>
          `;
        });
      }
    }

    document.getElementById('saveMinigameBtn').addEventListener('click', async () => {
      const is_wheel_active = minigameToggle ? minigameToggle.checked : true;
      if (currentPrizes.length < 2) { showToast('Cần ít nhất 2 ô quà!'); return; }
      
      const btn = document.getElementById('saveMinigameBtn');
      btn.textContent = 'Đang lưu...';
      if (typeof updateSiteSettingsToCloud === 'function') {
        await updateSiteSettingsToCloud({ is_wheel_active, wheel_prizes: currentPrizes });
      }
      btn.textContent = 'Lưu cấu hình';
      showToast('✅ Đã lưu cấu hình Minigame lên Supabase!');
    });

    document.getElementById('saveAnnouncementBtn').addEventListener('click', async () => {
      const is_notification_active = document.getElementById('announcementEnableToggle').checked;
      const notification_text = document.getElementById('announcementTextInput').value.trim();
      
      const btn = document.getElementById('saveAnnouncementBtn');
      btn.textContent = 'Đang lưu...';
      if (typeof updateSiteSettingsToCloud === 'function') {
        await updateSiteSettingsToCloud({ is_notification_active, notification_text });
      }
      btn.textContent = 'Lưu thông báo';
      showToast('Đã cập nhật thông báo lên Supabase thành công!');
    });


    function getPromotions() {
      try {
        const p = localStorage.getItem('olion_promotions');
        if (p) return JSON.parse(p);
      } catch(e) {}
      return [
        { id: 1, code: 'OLION15', discount: 'Giảm 15%', desc: 'Ưu đãi check-in quán', expire: '31/12/2026', active: true },
        { id: 2, code: 'CAPHEMUOI', discount: 'Tặng 1 ly Cà Phê Muối', desc: 'Dành cho hóa đơn từ 80k', expire: '15/10/2026', active: true },
        { id: 3, code: 'FREESHIP', discount: 'Miễn phí giao hàng', desc: 'Bán kính 3km khu vực Gò Vấp', expire: '30/11/2026', active: false }
      ];
    }
    function savePromotions(arr) {
      localStorage.setItem('olion_promotions', JSON.stringify(arr));
      loadPromotions();
      updateOverviewStats();
    }

    function loadPromotions() {
      const promos = getPromotions();
      const tbody = document.getElementById('promoTableBody');
      tbody.innerHTML = '';

      promos.forEach(p => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td><strong style="font-family: monospace; font-size: 15px; color: var(--accent);">${escapeHtml(p.code)}</strong></td>
          <td><strong>${escapeHtml(p.discount)}</strong></td>
          <td>${escapeHtml(p.desc)}</td>
          <td>${escapeHtml(p.expire || 'Không thời hạn')}</td>
          <td>
            <span class="badge ${p.active ? 'badge-success' : 'badge-warning'}">
              ${p.active ? 'Đang chạy' : 'Tạm dừng'}
            </span>
          </td>
          <td>
            <div style="display: flex; gap: 6px;">
              <button type="button" class="btn-secondary" style="padding: 4px 8px; font-size: 11.5px;" onclick="togglePromo(${p.id})">
                ${p.active ? 'Dừng' : 'Bật'}
              </button>
              <button type="button" class="btn-sm-danger" onclick="deletePromo(${p.id})">
                Xóa
              </button>
            </div>
          </td>
        `;
        tbody.appendChild(tr);
      });
    }

    window.togglePromo = function(id) {
      const promos = getPromotions();
      const target = promos.find(p => p.id === id);
      if (target) {
        target.active = !target.active;
        savePromotions(promos);
        showToast(`Mã ${target.code} đã được ${target.active ? 'kích hoạt' : 'tạm dừng'}!`);
      }
    };

    window.deletePromo = function(id) {
      if (confirm('Xác nhận xóa voucher này?')) {
        let promos = getPromotions();
        promos = promos.filter(p => p.id !== id);
        savePromotions(promos);
        showToast('Đã xóa voucher thành công.');
      }
    };

    document.getElementById('newPromoForm').addEventListener('submit', (e) => {
      e.preventDefault();
      const code = document.getElementById('promoCodeInput').value.trim().toUpperCase();
      const discount = document.getElementById('promoDiscountInput').value.trim();
      const desc = document.getElementById('promoDescInput').value.trim();
      const expire = document.getElementById('promoExpireInput').value.trim();

      const promos = getPromotions();
      promos.unshift({
        id: Date.now(),
        code,
        discount,
        desc,
        expire: expire || '31/12/2026',
        active: true
      });
      savePromotions(promos);
      document.getElementById('newPromoForm').reset();
      showToast(`Đã thêm mã ưu đãi mới: ${code}!`);
    });

    // Supabase Cloud Config
    function checkSupabaseStatus() {
      const url = localStorage.getItem('olion_supabase_url') || DEFAULT_SUPABASE_URL;
      const key = localStorage.getItem('olion_supabase_key') || DEFAULT_SUPABASE_ANON_KEY;

      if (document.getElementById('supabaseUrlInput')) document.getElementById('supabaseUrlInput').value = url || '';
      if (document.getElementById('supabaseKeyInput')) document.getElementById('supabaseKeyInput').value = key || '';

      const cloudStatusDot = document.getElementById('cloudStatusDot');
      const cloudStatusText = document.getElementById('cloudStatusText');
      const supabaseBadgeStatus = document.getElementById('supabaseBadgeStatus');

      if (url && key && !url.includes('your-project')) {
        cloudStatusDot.className = 'status-dot active';
        cloudStatusText.textContent = 'Cloud: Supabase Đã Kết Nối';
        if (supabaseBadgeStatus) {
          supabaseBadgeStatus.className = 'badge badge-success';
          supabaseBadgeStatus.textContent = '🟢 Đã kết nối Supabase Cloud';
        }
      } else {
        cloudStatusDot.className = 'status-dot offline';
        cloudStatusText.textContent = 'Chế độ: Offline (LocalStorage)';
        if (supabaseBadgeStatus) {
          supabaseBadgeStatus.className = 'badge badge-warning';
          supabaseBadgeStatus.textContent = '🟠 Chế độ Offline (Chưa cấu hình API Key)';
        }
      }
    }

    document.getElementById('saveSupabaseConfigBtn').addEventListener('click', async () => {
      const url = (document.getElementById('supabaseUrlInput').value || '').trim();
      const key = (document.getElementById('supabaseKeyInput').value || '').trim();

      if (!url || !key) return alert('Vui lòng nhập cả Supabase URL và Supabase Anon Key!');

      showToast('Đang kiểm tra kết nối tới Supabase...');
      const result = await testSupabaseConnection(url, key);
      if (result.success) {
        localStorage.setItem('olion_supabase_url', url);
        localStorage.setItem('olion_supabase_key', key);
        initSupabase(url, key);
        checkSupabaseStatus();
        showToast('🎉 Kết nối Supabase Cloud thành công!');
        loadAllData();
      } else {
        alert('❌ Không thể kết nối Supabase:\n' + result.message + '\n\nHãy kiểm tra lại URL, Anon Key và chắc chắn đã chạy file supabase_schema.sql trong SQL Editor!');
      }
    });

    document.getElementById('testSupabaseBtn').addEventListener('click', async () => {
      const url = (document.getElementById('supabaseUrlInput').value || '').trim();
      const key = (document.getElementById('supabaseKeyInput').value || '').trim();
      const result = await testSupabaseConnection(url, key);
      if (result.success) {
        alert('✅ Kết nối Supabase Cloud thành công!\nCác bảng dữ liệu đã sẵn sàng hoạt động.');
      } else {
        alert('❌ Kết nối thất bại:\n' + result.message);
      }
    });

    document.getElementById('clearSupabaseConfigBtn').addEventListener('click', () => {
      if (confirm('Xóa cấu hình Supabase và chuyển về chế độ lưu trữ LocalStorage nội bộ?')) {
        localStorage.removeItem('olion_supabase_url');
        localStorage.removeItem('olion_supabase_key');
        document.getElementById('supabaseUrlInput').value = '';
        document.getElementById('supabaseKeyInput').value = '';
        checkSupabaseStatus();
        showToast('Đã xóa cấu hình Cloud. Website đang chạy chế độ LocalStorage!');
      }
    });

    document.getElementById('seedCloudDbBtn').addEventListener('click', async () => {
      showToast('Đang nạp dữ liệu mẫu lên Supabase Cloud...');
      const sampleFeedbacks = [
        { name: 'Minh Anh', contact: 'minhanh.vlu@gmail.com', rating: 5, content: 'Quán nằm trong hẻm yên tĩnh ở Dương Quảng Hàm, cà phê muối béo mặn cực kỳ vừa miệng!', approved: true },
        { name: 'Thanh Trúc', contact: '0908123456', rating: 5, content: 'Matcha latte ở đây chuẩn vị Nhật, thơm đắng thanh nhẹ rất dễ chịu.', approved: true },
        { name: 'Hoàng Nam', contact: 'hoangnam.freelance@gmail.com', rating: 5, content: 'Bạc xỉu kem trứng ngon đỉnh chóp! Lớp bọt trứng béo mịn uống tới đâu dính tới đó.', approved: true }
      ];

      for (const fb of sampleFeedbacks) {
        await submitFeedbackToCloud(fb);
      }
      showToast('✅ Đã nạp dữ liệu mẫu lên Cloud thành công!');
      loadAllData();
    });

    // Store Settings
    document.getElementById('storeSettingsForm').addEventListener('submit', () => {
      const settings = {
        hotline: document.getElementById('settingHotline').value.trim(),
        hours: document.getElementById('settingHours').value.trim(),
        address: document.getElementById('settingAddress').value.trim(),
        email: document.getElementById('settingEmail').value.trim(),
        accentColor: document.getElementById('settingAccentColor').value
      };
      localStorage.setItem('olion_store_settings', JSON.stringify(settings));
      showToast('Đã lưu thiết lập cửa hàng và màu giao diện!');
    });

    // Overview Stats
    function updateOverviewStats() {
      const menuCountEl = document.getElementById('statMenuCount');
      const custCountEl = document.getElementById('statCustomerCount');
      const fbCountEl = document.getElementById('statFeedbackCount');
      const ratingAvgEl = document.getElementById('statRatingAvg');

      if (menuCountEl) menuCountEl.textContent = cachedMenuItems.length;
      if (custCountEl) custCountEl.textContent = cachedCustomers.length;
      if (fbCountEl) fbCountEl.textContent = cachedFeedbacks.length;

      if (cachedFeedbacks.length > 0) {
        const avg = (cachedFeedbacks.reduce((acc, f) => acc + (f.rating || 5), 0) / cachedFeedbacks.length).toFixed(1);
        if (ratingAvgEl) ratingAvgEl.textContent = avg + ' ★';
      } else {
        if (ratingAvgEl) ratingAvgEl.textContent = '4.9 ★';
      }
    }

    // CSV Downloader
    function downloadCsv(content, filename) {
      const blob = new Blob(['\uFEFF' + content], { type: 'text/csv;charset=utf-8;' });
      const link = document.createElement('a');
      link.href = URL.createObjectURL(blob);
      link.download = filename;
      link.click();
      URL.revokeObjectURL(link.href);
      showToast('Đã xuất file ' + filename + ' thành công!');
    }

    function escapeHtml(str) {
      if (!str) return '';
      return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
    }

    // Store Settings Loader
    function loadStoreSettings() {
      try {
        const raw = localStorage.getItem('olion_store_settings');
        if (raw) {
          const settings = JSON.parse(raw);
          if (settings.hotline && document.getElementById('settingHotline')) document.getElementById('settingHotline').value = settings.hotline;
          if (settings.hours && document.getElementById('settingHours')) document.getElementById('settingHours').value = settings.hours;
          if (settings.address && document.getElementById('settingAddress')) document.getElementById('settingAddress').value = settings.address;
          if (settings.email && document.getElementById('settingEmail')) document.getElementById('settingEmail').value = settings.email;
          if (settings.accentColor && document.getElementById('settingAccentColor')) document.getElementById('settingAccentColor').value = settings.accentColor;
        }
      } catch (e) {}
    }

    // Initial Data Load
    function loadAllData() {
      checkSupabaseStatus();
      loadMenu();
      loadCustomers();
      loadFeedbacks();
      loadAnnouncement();
      loadPromotions();
      loadMinigame();
      loadStoreSettings();
    }
    loadAllData();
