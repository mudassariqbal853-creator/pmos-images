const sharp = require("sharp");
const fs = require("fs");
const path = require("path");
const { execFileSync } = require("child_process");

const ROOT = path.join(__dirname, "..");
const BUILD = __dirname;
const CHROME = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";

function read(name) {
  return fs.readFileSync(path.join(BUILD, name), "utf8");
}

async function svgPng(svgName, outName, w, h) {
  const svg = fs.readFileSync(path.join(BUILD, svgName));
  await sharp(svg, { density: 300 })
    .resize(w, h, { fit: "contain", background: { r: 0, g: 0, b: 0, alpha: 0 } })
    .png()
    .toFile(path.join(ROOT, outName));
  const m = await sharp(path.join(ROOT, outName)).metadata();
  console.log(`logo  ${outName}  ${m.width}x${m.height}`);
}

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

/** Remove near-green chroma background → transparent PNG */
async function chromaToTransparent(inPath, outPath) {
  const { data, info } = await sharp(inPath)
    .ensureAlpha()
    .raw()
    .toBuffer({ resolveWithObject: true });

  for (let i = 0; i < data.length; i += 4) {
    const r = data[i], g = data[i + 1], b = data[i + 2];
    // pure-ish green screen
    if (g > 180 && r < 90 && b < 90) {
      data[i + 3] = 0;
    } else if (g > 140 && r < 120 && b < 120 && g > r + 40 && g > b + 40) {
      data[i + 3] = Math.max(0, 255 - Math.floor((g - Math.max(r, b)) * 3));
    }
  }

  await sharp(data, { raw: { width: info.width, height: info.height, channels: 4 } })
    .png()
    .toFile(outPath);
  const m = await sharp(outPath).metadata();
  console.log(`lockup ${path.basename(outPath)}  ${m.width}x${m.height}`);
}

function writeCoverHtml(fileName, w, h, mark, namePx, urPx, tagPx) {
  let html = read("cover-template.html");
  html = html
    .replace(/VAR_W/g, String(w))
    .replace(/VAR_H/g, String(h))
    .replace(/VAR_MARK/g, mark)
    .replace(/VAR_NAME/g, namePx)
    .replace(/VAR_UR/g, urPx)
    .replace(/VAR_TAG/g, tagPx);
  fs.writeFileSync(path.join(BUILD, fileName), html);
}

async function main() {
  // --- Logos / avatars ---
  await svgPng("mark-transparent.svg", "PMOS-logo-mark.png", 1024, 1024);
  await svgPng("mark.svg", "PMOS-avatar-1024.png", 1024, 1024);
  await svgPng("mark.svg", "PMOS-avatar-512.png", 512, 512);

  // Lockups via Chrome + chroma
  const lockEnHtml = path.join(BUILD, "lockup-en.html");
  const lockBiHtml = path.join(BUILD, "lockup-bilingual.html");
  const tmpEn = path.join(BUILD, "_tmp-lockup-en.png");
  const tmpBi = path.join(BUILD, "_tmp-lockup-bi.png");
  chromeShot(lockEnHtml, tmpEn, 1600, 420);
  chromeShot(lockBiHtml, tmpBi, 1600, 520);
  await chromaToTransparent(tmpEn, path.join(ROOT, "PMOS-logo-lockup-en.png"));
  await chromaToTransparent(tmpBi, path.join(ROOT, "PMOS-logo-lockup-bilingual.png"));

  // --- Covers ---
  const covers = [
    // Facebook Page cover (recommended upload)
    { file: "cover-fb.html", out: "PMOS-cover-facebook-1640x624.png", w: 1640, h: 624, mark: "200px", name: "56px", ur: "34px", tag: "20px" },
    // LinkedIn company — official upload target is 4200×700 (6:1). 1128×191 is display-only and often fails.
    { file: "cover-li-4200.html", out: "PMOS-cover-linkedin-4200x700.png", w: 4200, h: 700, mark: "420px", name: "120px", ur: "64px", tag: "40px" },
    { file: "cover-li-1128.html", out: "PMOS-cover-linkedin-1128x191.png", w: 1128, h: 191, mark: "120px", name: "36px", ur: "22px", tag: "14px" },
    { file: "cover-li-1584.html", out: "PMOS-cover-linkedin-1584x396.png", w: 1584, h: 396, mark: "160px", name: "44px", ur: "28px", tag: "18px" },
    // X / Twitter header
    { file: "cover-x.html", out: "PMOS-cover-x-1500x500.png", w: 1500, h: 500, mark: "180px", name: "52px", ur: "32px", tag: "18px" },
    // YouTube channel banner
    { file: "cover-yt.html", out: "PMOS-cover-youtube-2560x1440.png", w: 2560, h: 1440, mark: "280px", name: "72px", ur: "44px", tag: "24px" },
    // TikTok — no profile banner; vertical brand card for video/profile use
    { file: "cover-tt.html", out: "PMOS-cover-tiktok-1080x1920.png", w: 1080, h: 1920, mark: "320px", name: "56px", ur: "36px", tag: "20px" },
  ];

  for (const c of covers) {
    writeCoverHtml(c.file, c.w, c.h, c.mark, c.name, c.ur, c.tag);
  }

  // TikTok vertical: stack layout override
  let tt = read("cover-tt.html");
  tt = tt.replace(
    ".safe {",
    `.safe {
      flex-direction: column;
      text-align: center;
      gap: 40px;
      padding-top: 18%;
    }
    .copy { display: flex; flex-direction: column; align-items: center; }
    .ur { text-align: center !important; }
    .SAFE_PATCH_KEEP {
  `);
  // that replace is messy — write dedicated tiktok html instead
  fs.writeFileSync(
    path.join(BUILD, "cover-tt.html"),
    `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<style>
  @font-face {
    font-family: "Dubai";
    src: local("Dubai Bold"), url("file:///C:/Windows/Fonts/DUBAI-BOLD.TTF") format("truetype");
    font-weight: 700;
  }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  html, body { width: 1080px; height: 1920px; overflow: hidden; }
  .canvas {
    width: 1080px; height: 1920px; position: relative; overflow: hidden;
    background:
      radial-gradient(ellipse 80% 40% at 50% 18%, rgba(232,184,74,0.28) 0%, transparent 60%),
      linear-gradient(165deg, #062E32 0%, #0A555C 50%, #0E6A72 100%);
  }
  .canvas::before {
    content: ""; position: absolute; inset: 0;
    background-image:
      linear-gradient(rgba(255,255,255,0.05) 1px, transparent 1px),
      linear-gradient(90deg, rgba(255,255,255,0.05) 1px, transparent 1px);
    background-size: 48px 48px; opacity: 0.4;
  }
  .safe {
    position: relative; z-index: 2; height: 100%;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    gap: 48px; text-align: center; padding: 80px 48px; direction: ltr;
  }
  .mark { width: 360px; height: 360px; filter: drop-shadow(0 20px 40px rgba(0,0,0,0.35)); }
  .name { font-family: "Segoe UI", sans-serif; font-weight: 700; font-size: 64px; color: #fff; }
  .ur {
    font-family: "Dubai", "Segoe UI", sans-serif; font-weight: 700; font-size: 42px;
    color: #F4F8F7; direction: rtl; unicode-bidi: isolate; margin-top: 12px;
  }
  .tag {
    margin-top: 28px; display: inline-block;
    font-family: "Segoe UI", sans-serif; font-weight: 700; font-size: 24px;
    color: #062E32; background: #E8B84A; padding: 12px 28px; border-radius: 999px;
  }
</style>
</head>
<body>
  <div class="canvas">
    <div class="safe">
      <img class="mark" src="mark-transparent.svg" alt="" />
      <div>
        <div class="name">Pakistan Media OS</div>
        <div class="ur">پاکستان میڈیا او ایس</div>
        <div class="tag">Urdu &amp; English AI Literacy</div>
      </div>
    </div>
  </div>
</body>
</html>`
  );

  // LinkedIn short banner: tighter single-row, hide ur if too tight — keep ur small
  fs.writeFileSync(
    path.join(BUILD, "cover-li-1128.html"),
    `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<style>
  @font-face {
    font-family: "Dubai";
    src: local("Dubai Bold"), url("file:///C:/Windows/Fonts/DUBAI-BOLD.TTF") format("truetype");
    font-weight: 700;
  }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  html, body { width: 1128px; height: 191px; overflow: hidden; }
  .canvas {
    width: 1128px; height: 191px; display: flex; align-items: center; gap: 22px;
    padding: 0 40px; direction: ltr;
    background: linear-gradient(100deg, #062E32 0%, #0A555C 55%, #0E6A72 100%);
  }
  .mark { width: 118px; height: 118px; flex-shrink: 0; }
  .name { font-family: "Segoe UI", sans-serif; font-weight: 700; font-size: 34px; color: #fff; line-height: 1.1; }
  .meta { display: flex; align-items: center; gap: 14px; margin-top: 8px; }
  .ur {
    font-family: "Dubai", "Segoe UI", sans-serif; font-weight: 700; font-size: 20px;
    color: #D7E8E6; direction: rtl; unicode-bidi: isolate;
  }
  .tag {
    font-family: "Segoe UI", sans-serif; font-weight: 700; font-size: 14px;
    color: #062E32; background: #E8B84A; padding: 4px 12px; border-radius: 999px;
  }
</style>
</head>
<body>
  <div class="canvas">
    <img class="mark" src="mark-transparent.svg" alt="" />
    <div>
      <div class="name">Pakistan Media OS</div>
      <div class="meta">
        <span class="ur">پاکستان میڈیا او ایس</span>
        <span class="tag">Urdu &amp; English AI Literacy</span>
      </div>
    </div>
  </div>
</body>
</html>`
  );

  for (const c of covers) {
    const htmlPath = path.join(BUILD, c.file);
    const outPath = path.join(ROOT, c.out);
    chromeShot(htmlPath, outPath, c.w, c.h);
    const m = await sharp(outPath).metadata();
    console.log(`cover ${c.out}  ${m.width}x${m.height}`);
  }

  // cleanup temps
  for (const t of [tmpEn, tmpBi]) {
    try { fs.unlinkSync(t); } catch {}
  }

  console.log("\\nBrand kit complete →", ROOT);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
