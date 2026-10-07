const fs = require('fs');
const content = fs.readFileSync('index.html', 'utf8');

// find all script tags
const scripts = content.match(/<script[\s\S]*?<\/script>/g);
scripts.forEach((s, i) => {
  if (s.includes('application/ld+json')) {
    try {
      let json = s.replace(/<script[^>]*>/, '').replace(/<\/script>/, '').trim();
      JSON.parse(json);
      console.log(`Script ${i} JSON is valid`);
    } catch(e) {
      console.log(`Script ${i} JSON INVALID: ${e.message}`);
    }
  }
});
