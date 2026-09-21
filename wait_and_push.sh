#!/bin/bash
echo "Waiting for python3 scripts/batch_generate_pollinations_flux.py to finish..."
while pgrep -f "batch_generate_pollinations_flux.py" > /dev/null; do
  sleep 10
done
echo "Generation finished. Committing and pushing images..."
git add assets/menu/*.webp
git commit -m "chore: add 36 high quality AI studio menu images"
git push
echo "Done!"
