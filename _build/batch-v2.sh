#!/bin/bash
for n in 002 003 004 005 006 007 008 009 010 011 012 013; do
  for lang in ur en; do
    OUT="Images/POST-$n/tiktok/POST-$n-tiktok-$lang-1080x1920-v2.mp4"
    if [ -f "$OUT" ]; then
      echo "SKIP POST-$n $lang (exists)"
      continue
    fi
    echo "=== START POST-$n $lang $(date) ==="
    node "Images/_build/build-tiktok-video-v2.js" "POST-$n" "$lang" > "Images/_build/log-$n-$lang.txt" 2>&1
    if [ $? -ne 0 ]; then
      echo "FAILED POST-$n $lang"
    else
      echo "=== DONE POST-$n $lang $(date) ==="
    fi
  done
done
echo "BATCH-V2-ALL-COMPLETE"
