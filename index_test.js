    window.RECAPTCHA_SITE_KEY = '6LcrCcYtAAAAAImurcyCcHkt-SY3N2qbFRcHdiMK';
    window.OneSignalDeferred = window.OneSignalDeferred || [];
    OneSignalDeferred.push(function(OneSignal) {
      OneSignal.init({
        appId: "YOUR-ONESIGNAL-APP-ID",
      });
    });
            // Hàm xử lý và resize ảnh trước khi lưu (giảm dung lượng)
            function previewFeedbackImage(event) {
              const file = event.target.files[0];
              if (!file) return;

              const reader = new FileReader();
              reader.onload = function(e) {
                const img = new Image();
                img.onload = function() {
                  // Nén ảnh bằng canvas
                  const canvas = document.createElement('canvas');
                  const MAX_WIDTH = 800;
                  const MAX_HEIGHT = 800;
                  let width = img.width;
                  let height = img.height;

                  if (width > height) {
                    if (width > MAX_WIDTH) {
                      height *= MAX_WIDTH / width;
                      width = MAX_WIDTH;
                    }
                  } else {
                    if (height > MAX_HEIGHT) {
                      width *= MAX_HEIGHT / height;
                      height = MAX_HEIGHT;
                    }
                  }

                  canvas.width = width;
                  canvas.height = height;
                  const ctx = canvas.getContext('2d');
                  ctx.drawImage(img, 0, 0, width, height);

                  // Chuyển thành chuỗi Base64
                  const dataUrl = canvas.toDataURL('image/jpeg', 0.8);
                  
                  // Hiển thị Preview
                  document.getElementById('fbImagePreview').src = dataUrl;
                  document.getElementById('fbImagePreviewContainer').style.display = 'block';
                  
                  // Lưu vào input ẩn
                  document.getElementById('fbImageDataUrl').value = dataUrl;
                };
                img.src = e.target.result;
              };
              reader.readAsDataURL(file);
            }

            function removeFeedbackImage() {
              document.getElementById('fbImage').value = '';
              document.getElementById('fbImageDataUrl').value = '';
              document.getElementById('fbImagePreview').src = '';
              document.getElementById('fbImagePreviewContainer').style.display = 'none';
            }
