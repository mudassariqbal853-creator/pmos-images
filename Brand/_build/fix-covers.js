/**
 * Regenerate LinkedIn cover at official 4200×700 and export JPEG covers
 * (LinkedIn company cover often fails on undersized 1128×191 PNGs).
 */
const sharp = require("sharp");
const fs = require("fs");
const path = require("path");
const { execFileSync } = require("child_process");

const ROOT = path.join(__dirname, "..");
const BUILD = __dirname;
const CHROME = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";

const liHtml = `<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8" />
<style>
  @font-face {
    font-family: "Dubai";
    src: local("Dubai Bold"), url("file:///C:/Windows/Fonts/DUBAI-BOLD.TTF") format("truetype");
    font-weight: 700;
  }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  html, body { width: 4200px; height: 700px; overflow: hidden; }
  .canvas {
    width: 4200px; height: 700px; display: flex; align-items: center; gap: 80px;
    padding: 0 160px; direction: ltr;
    background:
      radial-gradient(ellipse 50% 90% at 8% 50%, rgba(232,184,74,0.25) 0%, transparent 55%),
      linear-gradient(100deg, #062E32 0%, #0A555C 55%, #0E6A72 100%);
  }
  .mark {
    width: 420px; height: 420px; flex-shrink: 0;
    filter: drop-shadow(0 16px 40px rgba(0,0,0,0.35));
  }
  .name {
    font-family: "Segoe UI", sans-serif; font-weight: 700;
    font-size: 120px; color: #fff; line-height: 1.1;
  }
  .meta { display: flex; align-items: center; gap: 36px; margin-top: 28px; }
  .ur {
    font-family: "Dubai", "Segoe UI", sans-serif; font-weight: 700;
    font-size: 64px; color: #D7E8E6; direction: rtl; unicode-bidi: isolate;
  }
  .tag {
    font-family: "Segoe UI", sans-serif; font-weight: 700; font-size: 40px;
    color: #062E32; background: #E8B84A; padding: 16px 40px; border-radius: 999px;
  }
</style></head>
<body><div class="canvas">
  <img class="mark" src="mark-transparent.svg" alt="" />
  <div>
    <div class="name">Pakistan Media OS</div>
    <div class="meta">
      <span class="ur">پاکستان میڈیا او ایس</span>
      <span class="tag">Urdu &amp; English AI Literacy</span>
    </div>
  </div>
</div></body></html>`;

function chromeShot(htmlPath, outPath, w, h) {
  const uri = "file:///" + htmlPath.replace(/\\/g, "/");
  execFileSync(
    CHROME,
    [
      "--headless=new",
      "--disable-gpu",
      "--hide-scrollbars",
      "--force-device-scale-factor=1",
      `--window-size=${w},${h}`,
      `--screenshot=${outPath}`,
      uri,
    ],
    { stdio: "ignore" }
  );
}

async function main() {
  const htmlPath = path.join(BUILD, "cover-li-4200.html");
  fs.writeFileSync(htmlPath, liHtml);

  const pngOut = path.join(ROOT, "PMOS-cover-linkedin-4200x700.png");
  chromeShot(htmlPath, pngOut, 4200, 700);

  const jpgMaps = [
    ["PMOS-cover-linkedin-4200x700.png", "PMOS-cover-linkedin-4200x700.jpg", 90],
    ["PMOS-cover-facebook-1640x624.png", "PMOS-cover-facebook-1640x624.jpg", 92],
    ["PMOS-cover-x-1500x500.png", "PMOS-cover-x-1500x500.jpg", 92],
    ["PMOS-cover-youtube-2560x1440.png", "PMOS-cover-youtube-2560x1440.jpg", 90],
    ["PMOS-cover-linkedin-1584x396.png", "PMOS-cover-linkedin-1584x396.jpg", 92],
  ];

  for (const [src, dest, q] of jpgMaps) {
    const sp = path.join(ROOT, src);
    if (!fs.existsSync(sp)) {
      console.log("skip missing", src);
      continue;
    }
    const dp = path.join(ROOT, dest);
    await sharp(sp).jpeg({ quality: q, mozjpeg: true }).toFile(dp);
    const m = await sharp(dp).metadata();
    const kb = (fs.statSync(dp).size / 1024).toFixed(0);
    console.log(`${dest}  ${m.width}x${m.height}  ${kb}KB`);
  }

  const m = await sharp(pngOut).metadata();
  console.log(
    `LI png  ${m.width}x${m.height}  ${(fs.statSync(pngOut).size / 1024).toFixed(0)}KB`
  );
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
