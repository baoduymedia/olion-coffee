import re

with open('index.html', 'r') as f:
    c = f.read()

# Remove sessionStorage checks
c = re.sub(r"        // Chỉ hiển thị 1 lần trên mỗi phiên duyệt web\n        if \(sessionStorage.getItem\('olion_welcome_shown'\)\) return;\n\n", "", c)
c = re.sub(r"        sessionStorage.setItem\('olion_welcome_shown', 'true'\);\n", "", c)

# Change pause listener from newUserArea to the entire modal content
# Wait, let's look at the old listener logic.
old_listener = """        // Lắng nghe tương tác trên toàn bộ khu vực Form để HỦY ĐẾM NGƯỢC
        if (newUserArea) {
          const pauseEvents = ['focusin', 'click', 'keydown', 'input'];
          pauseEvents.forEach(evt => {
            newUserArea.addEventListener(evt, pauseWelcomeCountdown, { once: false });
          });
        }"""

new_listener = """        // Lắng nghe tương tác trên toàn bộ Popup để HỦY ĐẾM NGƯỢC
        const modalContent = modal.querySelector('.modal-content');
        if (modalContent) {
          const pauseEvents = ['focusin', 'click', 'keydown', 'touchstart'];
          pauseEvents.forEach(evt => {
            modalContent.addEventListener(evt, pauseWelcomeCountdown, { once: false });
          });
        }"""

c = c.replace(old_listener, new_listener)

with open('index.html', 'w') as f:
    f.write(c)

