// ==============================================================================
// OLION COFFEE — SERVICE WORKER (PWA & OFFLINE CACHING)
// ==============================================================================

const CACHE_NAME = "olion-coffee-v1.6";

const PRECACHE_ASSETS = [
  './',
  './index.html',
  './manifest.json',
  './supabaseClient.js',
  './assets/logo.png',
  './assets/logo-white.png',
  './assets/logo-transparent.png',
  './assets/space-1.webp',
  './assets/space-2.webp',
  './assets/space-3.webp',
  './assets/space-4.webp',
  './assets/menu/ca_phe_muoi.webp',
  './assets/menu/bac_xiu.webp',
  './assets/menu/matcha_latte.webp',
  './assets/menu/americano.webp',
  './assets/menu/espresso.webp',
  './assets/menu/tra_vai_hoa_hong.webp',
  './assets/menu/tra_chanh_day_nhiet_doi.webp'
];

// 1. Cài đặt Service Worker & Lưu trước tài nguyên cốt lõi (Precaching)
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log('⚡ [PWA SW] Đang lưu trước tài nguyên tĩnh cho Olion Coffee...');
      return cache.addAll(PRECACHE_ASSETS);
    }).then(() => self.skipWaiting())
  );
});

// 2. Kích hoạt & Dọn dẹp cache phiên bản cũ
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cache) => {
          if (cache !== CACHE_NAME) {
            console.log('🧹 [PWA SW] Đang dọn dẹp cache cũ:', cache);
            return caches.delete(cache);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

// 3. Chiến lược Fetch thông minh:
// - Đối với API (Supabase, Weather, LLM): Network-first (ưu tiên mạng để dữ liệu mới nhất, rớt mạng thì bỏ qua)
// - Đối với File tĩnh (HTML, CSS, JS, Ảnh Menu): Cache-first with Network Fallback & Cache Update
self.addEventListener('fetch', (event) => {
  const url = new URL(event.request.url);

  // Không can thiệp vào các request không phải GET
  if (event.request.method !== 'GET') return;

  // Với API Supabase hoặc thời tiết: Network first
  if (url.hostname.includes('supabase.co') || url.hostname.includes('open-meteo.com') || url.hostname.includes('googleapis.com')) {
    event.respondWith(
      fetch(event.request).catch(() => {
        return caches.match(event.request);
      })
    );
    return;
  }

  // Với tài nguyên trang web (HTML, JS, Ảnh WebP): Cache first, fallback to network
  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      if (cachedResponse) {
        // Tải trước bản mới ngầm ở background để cập nhật lần sau (Stale-While-Revalidate)
        fetch(event.request).then((networkResponse) => {
          if (networkResponse && networkResponse.status === 200) {
            caches.open(CACHE_NAME).then((cache) => {
              cache.put(event.request, networkResponse);
            });
          }
        }).catch(() => {});

        return cachedResponse;
      }

      // Chưa có trong cache -> Gọi mạng và lưu vào cache
      return fetch(event.request).then((networkResponse) => {
        if (!networkResponse || networkResponse.status !== 200 || networkResponse.type !== 'basic') {
          return networkResponse;
        }

        const responseToCache = networkResponse.clone();
        caches.open(CACHE_NAME).then((cache) => {
          cache.put(event.request, responseToCache);
        });

        return networkResponse;
      }).catch(() => {
        // Rớt mạng: Nếu là request trang chính, trả về index.html từ cache
        if (event.request.headers.get('accept')?.includes('text/html')) {
          return caches.match('./index.html');
        }
      });
    })
  );
});
