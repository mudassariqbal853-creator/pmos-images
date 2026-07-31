/**
 * POST-001 visual set — brand-aligned (Clarity Path colors)
 * Renders heroes, 8+8 carousel slides, LinkedIn banners via Chrome.
 */
const fs = require("fs");
const path = require("path");
const { execFileSync } = require("child_process");

const ROOT = path.join(__dirname, "..");
const BUILD = __dirname;
const CHROME = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const LOGO = path.join(ROOT, "..", "Brand", "PMOS-logo-mark.png").replace(/\\/g, "/");
const LOGO_FILE = "file:///" + path.join(ROOT, "..", "Brand", "PMOS-logo-mark.png").replace(/\\/g, "/");

const COLORS = {
  teal: "#0A555C",
  ink: "#062E32",
  mist: "#D7E8E6",
  paper: "#F4F8F7",
  amber: "#E8B84A",
  charcoal: "#1A2B2E",
  white: "#FFFFFF",
};

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
  console.log("ok", path.basename(outPath));
}

const baseCss = `
  @font-face {
    font-family: "Dubai";
    src: local("Dubai"), url("file:///C:/Windows/Fonts/DUBAI-REGULAR.TTF") format("truetype");
    font-weight: 400;
  }
  @font-face {
    font-family: "Dubai";
    src: local("Dubai Medium"), url("file:///C:/Windows/Fonts/DUBAI-MEDIUM.TTF") format("truetype");
    font-weight: 500;
  }
  @font-face {
    font-family: "Dubai";
    src: local("Dubai Bold"), url("file:///C:/Windows/Fonts/DUBAI-BOLD.TTF") format("truetype");
    font-weight: 700;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  html, body { width: 1080px; height: 1080px; overflow: hidden; }
  body {
    font-family: "Dubai", "Segoe UI", sans-serif;
    color: ${COLORS.charcoal};
  }
  .slide {
    width: 1080px; height: 1080px;
    position: relative; overflow: hidden;
    padding: 56px 64px 48px;
    display: flex; flex-direction: column;
  }
  .slide.dark {
    background:
      radial-gradient(ellipse 80% 50% at 15% 10%, rgba(232,184,74,0.22) 0%, transparent 55%),
      linear-gradient(155deg, ${COLORS.ink} 0%, ${COLORS.teal} 55%, #0E6A72 100%);
    color: ${COLORS.white};
  }
  .slide.light {
    background:
      radial-gradient(ellipse 70% 40% at 90% 0%, rgba(10,85,92,0.08) 0%, transparent 60%),
      ${COLORS.paper};
  }
  .slide.light::before {
    content: "";
    position: absolute; left: 0; top: 0; bottom: 0; width: 14px;
    background: ${COLORS.teal};
  }
  .topbar {
    display: flex; align-items: center; justify-content: space-between;
    margin-bottom: 28px; direction: ltr;
  }
  .badge {
    display: inline-flex; align-items: center; gap: 8px;
    background: ${COLORS.amber};
    color: ${COLORS.ink};
    font-family: "Segoe UI", sans-serif;
    font-weight: 800; font-size: 18px;
    padding: 8px 18px; border-radius: 999px;
  }
  .badge i { width: 8px; height: 8px; border-radius: 50%; background: #E85D04; display: inline-block; }
  .logo { width: 64px; height: 64px; }
  .logo-lg { width: 88px; height: 88px; }
  .content { flex: 1; display: flex; flex-direction: column; justify-content: center; }
  .footer {
    margin-top: auto;
    padding-top: 20px;
    border-top: 1.5px solid rgba(10,85,92,0.18);
    font-family: "Segoe UI", sans-serif;
    font-size: 18px; font-weight: 600;
    color: #3D6A6E;
    direction: ltr;
  }
  .slide.dark .footer {
    border-top-color: rgba(255,255,255,0.2);
    color: rgba(255,255,255,0.75);
  }
  .h1 {
    font-size: 58px; font-weight: 700; line-height: 1.25;
    margin-bottom: 20px;
  }
  .slide.dark .h1 { font-size: 62px; text-shadow: 0 4px 20px rgba(0,0,0,0.25); }
  .h1 .en { font-family: "Segoe UI", sans-serif; color: ${COLORS.amber}; font-weight: 800; }
  .sub { font-size: 30px; font-weight: 500; line-height: 1.4; opacity: 0.92; }
  .body { font-size: 32px; font-weight: 400; line-height: 1.45; }
  .bullets { list-style: none; margin-top: 12px; }
  .bullets li {
    font-size: 30px; line-height: 1.35;
    padding: 14px 0 14px 0;
    border-bottom: 1px solid rgba(10,85,92,0.12);
    display: flex; gap: 14px; align-items: flex-start;
  }
  .slide[dir="rtl"] .bullets li { padding: 14px 0; }
  .dot {
    flex-shrink: 0; width: 14px; height: 14px; margin-top: 12px;
    border-radius: 50%; background: ${COLORS.amber};
  }
  .flow {
    display: flex; direction: ltr; gap: 12px; align-items: stretch; margin-top: 20px;
  }
  .box {
    flex: 1; border-radius: 22px; padding: 22px 14px; text-align: center; color: #fff;
    min-height: 220px; display: flex; flex-direction: column; align-items: center; justify-content: center;
    position: relative;
  }
  .b1 { background: linear-gradient(160deg, #0A555C, #0E6A72); }
  .b2 { background: linear-gradient(160deg, #0C7A58, #129B6E); }
  .b3 { background: linear-gradient(160deg, #C45C12, #E07A2F); }
  .num {
    position: absolute; top: -12px; left: 14px;
    width: 34px; height: 34px; border-radius: 50%;
    background: ${COLORS.amber}; color: ${COLORS.ink};
    font-family: "Segoe UI", sans-serif; font-weight: 900; font-size: 16px;
    display: flex; align-items: center; justify-content: center;
  }
  .box h3 { font-size: 26px; font-weight: 700; margin: 8px 0 6px; line-height: 1.25; }
  .box p { font-size: 20px; opacity: 0.92; }
  .arrow {
    align-self: center; font-family: "Segoe UI", sans-serif;
    font-weight: 900; font-size: 28px; color: ${COLORS.teal};
  }
  .truths { display: flex; flex-direction: column; gap: 16px; margin-top: 12px; }
  .truth {
    background: ${COLORS.white};
    border: 2px solid ${COLORS.mist};
    border-radius: 18px;
    padding: 20px 22px;
    display: flex; gap: 18px; align-items: center;
    font-size: 28px; font-weight: 600; line-height: 1.3;
    box-shadow: 0 6px 16px rgba(10,85,92,0.06);
  }
  .truth .n {
    width: 48px; height: 48px; border-radius: 14px; flex-shrink: 0;
    background: ${COLORS.teal}; color: #fff;
    font-family: "Segoe UI", sans-serif; font-weight: 900; font-size: 22px;
    display: flex; align-items: center; justify-content: center;
  }
  .cta-pill {
    display: inline-block; margin-top: 24px;
    background: ${COLORS.amber}; color: ${COLORS.ink};
    font-size: 28px; font-weight: 700;
    padding: 14px 28px; border-radius: 999px;
  }
  .en-term { font-family: "Segoe UI", sans-serif; font-weight: 700; }
`;

function shell({ lang, dark, title, bodyHtml, footer, extraClass = "" }) {
  const dir = lang === "ur" ? "rtl" : "ltr";
  const series =
    lang === "ur" ? "Urdu AI Literacy — Post 1" : "AI Literacy — Post 1";
  return `<!DOCTYPE html>
<html lang="${lang}" dir="${dir}">
<head><meta charset="utf-8" /><style>${baseCss}</style></head>
<body>
  <div class="slide ${dark ? "dark" : "light"} ${extraClass}" dir="${dir}">
    <div class="topbar">
      <div class="badge"><i></i>${series}</div>
      <img class="logo" src="${LOGO_FILE}" alt="" />
    </div>
    <div class="content">
      ${title ? `<h1 class="h1">${title}</h1>` : ""}
      ${bodyHtml}
    </div>
    <div class="footer">${footer}</div>
  </div>
</body>
</html>`;
}

const footUr = "Pakistan Media OS · Urdu AI Literacy — Post 1";
const footEn = "Pakistan Media OS · AI Literacy — Post 1";

const slidesUr = [
  {
    name: "POST-001-slide-ur-01.png",
    dark: true,
    title: `آج صبح آپ نے شاید پہلے ہی <span class="en">AI</span> استعمال کر لی`,
    body: `<p class="sub">مصنوعی ذہانت سمجھنے کی Urdu series — Post 1</p>`,
  },
  {
    name: "POST-001-slide-ur-02.png",
    dark: false,
    title: `ہر جگہ “AI” — الجھن`,
    body: `<ul class="bullets">
      <li><span class="dot"></span><span>اشتہارات، apps، WhatsApp forwards</span></li>
      <li><span class="dot"></span><span>سب ایک جیسی advanced چیز <strong>نہیں</strong></span></li>
      <li><span class="dot"></span><span>پہلے سمجھیں، پھر بھروسہ کریں</span></li>
    </ul>`,
  },
  {
    name: "POST-001-slide-ur-03.png",
    dark: false,
    title: `AI کیا ہے؟ (سادہ)`,
    body: `<p class="body">وہ computer system جو <strong>ڈیٹا سے نمونے سیکھ کر</strong> کوئی <strong>خاص کام</strong> کرتا ہے — جیسے لفظ سجھانا، چہرہ پہچاننا، یا جواب لکھنا۔</p>
    <p class="body" style="margin-top:22px">یہ انسان جیسا <strong>ہر چیز سمجھنے والا دماغ نہیں</strong>۔</p>`,
  },
  {
    name: "POST-001-slide-ur-04.png",
    dark: false,
    title: `ڈیٹا → سیکھنا → کام`,
    body: `<div class="flow">
      <div class="box b1"><span class="num">1</span><h3>ڈیٹا / مثالیں</h3><p>مثالوں سے شروع</p></div>
      <div class="arrow">→</div>
      <div class="box b2"><span class="num">2</span><h3>نمونے سیکھتا ہے</h3><p>نظام پیٹرن بناتا ہے</p></div>
      <div class="arrow">→</div>
      <div class="box b3"><span class="num">3</span><h3>کام</h3><p>تجویز · پہچان · تخلیق</p></div>
    </div>`,
  },
  {
    name: "POST-001-slide-ur-05.png",
    dark: false,
    title: `آپ کے فون میں`,
    body: `<ul class="bullets">
      <li><span class="dot"></span><span>Face unlock</span></li>
      <li><span class="dot"></span><span>Keyboard suggestions</span></li>
      <li><span class="dot"></span><span>Feed recommendations</span></li>
      <li><span class="dot"></span><span>Spam filter</span></li>
    </ul>
    <p class="sub" style="margin-top:24px;color:#0A555C;font-weight:700">نظر نہ آئے — مگر <strong>عام</strong></p>`,
  },
  {
    name: "POST-001-slide-ur-06.png",
    dark: false,
    title: `پاکستان میں بھی`,
    body: `<ul class="bullets">
      <li><span class="dot"></span><span>موبائل والیٹ fraud alerts</span></li>
      <li><span class="dot"></span><span>Ride / delivery time estimate</span></li>
      <li><span class="dot"></span><span>Urdu typing suggestions</span></li>
      <li><span class="dot"></span><span>WhatsApp پر AI text — <strong>تصدیق ضروری</strong></span></li>
    </ul>`,
  },
  {
    name: "POST-001-slide-ur-07.png",
    dark: false,
    title: `یاد رکھیں`,
    body: `<div class="truths">
      <div class="truth"><span class="n">1</span><span>آج کی AI = <strong>Narrow AI</strong> (مخصوص کام)</span></div>
      <div class="truth"><span class="n">2</span><span>ہر “AI” <strong>لیبل</strong> سچ نہیں</span></div>
      <div class="truth"><span class="n">3</span><span>ChatGPT-class tools کبھی <strong>غلط بھی</strong> لکھ سکتی ہیں</span></div>
    </div>`,
  },
  {
    name: "POST-001-slide-ur-08.png",
    dark: true,
    title: `اگلا سبق`,
    body: `<p class="sub" style="font-size:36px">Narrow AI vs General AI — فرق سمجھیں۔</p>
    <div class="cta-pill">Series save کریں · follow رکھیں</div>
    <p class="sub" style="margin-top:28px;opacity:0.85">Pakistan Media OS — Urdu AI Literacy</p>`,
  },
];

const slidesEn = [
  {
    name: "POST-001-slide-en-01.png",
    dark: true,
    title: `You may have already used <span class="en">AI</span> this morning`,
    body: `<p class="sub">AI literacy series in clear language — Post 1</p>`,
  },
  {
    name: "POST-001-slide-en-02.png",
    dark: false,
    title: `“AI” everywhere — confusion`,
    body: `<ul class="bullets">
      <li><span class="dot"></span><span>Ads, apps, forwarded messages</span></li>
      <li><span class="dot"></span><span>Not all the same advanced thing</span></li>
      <li><span class="dot"></span><span>Understand first, then trust</span></li>
    </ul>`,
  },
  {
    name: "POST-001-slide-en-03.png",
    dark: false,
    title: `What is AI? (simple)`,
    body: `<p class="body">A computer system that <strong>learns patterns from data</strong> to do a <strong>specific job</strong> — suggest a word, recognize a face, or generate text.</p>
    <p class="body" style="margin-top:22px">It is <strong>not</strong> a human-like mind that understands everything.</p>`,
  },
  {
    name: "POST-001-slide-en-04.png",
    dark: false,
    title: `Data → Learning → Task`,
    body: `<div class="flow">
      <div class="box b1"><span class="num">1</span><h3>Data / Examples</h3><p>Start with examples</p></div>
      <div class="arrow">→</div>
      <div class="box b2"><span class="num">2</span><h3>Learns patterns</h3><p>System builds patterns</p></div>
      <div class="arrow">→</div>
      <div class="box b3"><span class="num">3</span><h3>Task</h3><p>suggest · recognize · generate</p></div>
    </div>`,
  },
  {
    name: "POST-001-slide-en-05.png",
    dark: false,
    title: `On your phone`,
    body: `<ul class="bullets">
      <li><span class="dot"></span><span>Face unlock</span></li>
      <li><span class="dot"></span><span>Keyboard suggestions</span></li>
      <li><span class="dot"></span><span>Feed recommendations</span></li>
      <li><span class="dot"></span><span>Spam filter</span></li>
    </ul>
    <p class="sub" style="margin-top:24px;color:#0A555C;font-weight:700">Often invisible — still common</p>`,
  },
  {
    name: "POST-001-slide-en-06.png",
    dark: false,
    title: `Also in Pakistan`,
    body: `<ul class="bullets">
      <li><span class="dot"></span><span>Mobile wallet fraud alerts</span></li>
      <li><span class="dot"></span><span>Ride / delivery time estimates</span></li>
      <li><span class="dot"></span><span>Typing suggestions</span></li>
      <li><span class="dot"></span><span>AI-generated forwards — <strong>verify first</strong></span></li>
    </ul>`,
  },
  {
    name: "POST-001-slide-en-07.png",
    dark: false,
    title: `Remember`,
    body: `<div class="truths">
      <div class="truth"><span class="n">1</span><span>Today’s AI = <strong>Narrow AI</strong> (specific tasks)</span></div>
      <div class="truth"><span class="n">2</span><span>Not every “AI” <strong>label</strong> is true</span></div>
      <div class="truth"><span class="n">3</span><span>ChatGPT-class tools can still be <strong>wrong</strong></span></div>
    </div>`,
  },
  {
    name: "POST-001-slide-en-08.png",
    dark: true,
    title: `Next lesson`,
    body: `<p class="sub" style="font-size:36px">Narrow AI vs General AI — know the difference.</p>
    <div class="cta-pill">Save the series · Follow for Post 2</div>
    <p class="sub" style="margin-top:28px;opacity:0.85">Pakistan Media OS — AI Literacy</p>`,
  },
];

function writeSlide(spec, lang, footer) {
  const html = shell({
    lang,
    dark: spec.dark,
    title: spec.title,
    bodyHtml: spec.body,
    footer,
  });
  const htmlPath = path.join(BUILD, spec.name.replace(".png", ".html"));
  fs.writeFileSync(htmlPath, html, "utf8");
  return htmlPath;
}

function heroHtml(lang) {
  const isUr = lang === "ur";
  const hook = isUr
    ? `آج صبح <span class="en">AI</span> استعمال کی؟`
    : `Did you use <span class="en">AI</span> this morning?`;
  const sub = isUr
    ? `ڈیٹا سے سیکھنا — جادو نہیں`
    : `Learning from data — not magic`;
  const take = isUr
    ? `AI = سیکھا ہوا نظام — جادو نہیں`
    : `AI = a learned system — not magic`;
  const flowTitle = isUr ? `AI کی سادہ تصویر` : `A simple picture of AI`;
  const boxes = isUr
    ? [
        ["ڈیٹا / مثالیں", "مثالوں سے شروع"],
        ["نمونے سیکھتا ہے", "نظام پیٹرن بناتا ہے"],
        ["کام", "تجویز · پہچان · تخلیق"],
      ]
    : [
        ["Data / Examples", "Start with examples"],
        ["Learns patterns", "System builds patterns"],
        ["Task", "suggest · recognize · generate"],
      ];
  const footer = isUr ? footUr : footEn;
  const series = isUr ? "Urdu AI Literacy — Post 1" : "AI Literacy — Post 1";
  const dir = isUr ? "rtl" : "ltr";

  return `<!DOCTYPE html>
<html lang="${lang}" dir="${dir}">
<head><meta charset="utf-8" /><style>${baseCss}
  .hero {
    width: 1080px; height: 1080px; position: relative; overflow: hidden;
    background:
      radial-gradient(ellipse 80% 50% at 15% 10%, rgba(232,184,74,0.25) 0%, transparent 55%),
      linear-gradient(155deg, ${COLORS.ink} 0%, ${COLORS.teal} 50%, #0E6A72 100%);
    color: #fff;
    padding: 48px 52px 40px;
    display: flex; flex-direction: column; justify-content: space-between;
  }
  .hero-top { text-align: center; }
  .hero .h1 { font-size: 64px; margin-bottom: 12px; }
  .panel {
    background: rgba(255,255,255,0.97);
    border-radius: 28px;
    padding: 22px 18px 18px;
    color: ${COLORS.charcoal};
    box-shadow: 0 18px 40px rgba(0,0,0,0.28);
  }
  .panel-title {
    text-align: center; font-size: 22px; font-weight: 700;
    color: ${COLORS.teal}; margin-bottom: 14px;
  }
  .takeaway {
    display: block; text-align: center;
    background: ${COLORS.amber}; color: ${COLORS.ink};
    font-size: 28px; font-weight: 700;
    padding: 12px 20px; border-radius: 999px;
    margin: 14px auto 10px; max-width: 92%;
  }
  .brand-line {
    text-align: center; font-family: "Segoe UI", sans-serif;
    font-size: 17px; font-weight: 600; color: #3D6A6E; direction: ltr;
  }
</style></head>
<body>
  <div class="hero" dir="${dir}">
    <div class="hero-top">
      <div style="display:flex;justify-content:space-between;align-items:center;direction:ltr;margin-bottom:22px">
        <div class="badge"><i></i>${series}</div>
        <img class="logo-lg" src="${LOGO_FILE}" alt="" />
      </div>
      <h1 class="h1">${hook}</h1>
      <p class="sub">${sub}</p>
    </div>
    <div class="panel">
      <div class="panel-title">${flowTitle}</div>
      <div class="flow">
        <div class="box b1"><span class="num">1</span><h3>${boxes[0][0]}</h3><p>${boxes[0][1]}</p></div>
        <div class="arrow">→</div>
        <div class="box b2"><span class="num">2</span><h3>${boxes[1][0]}</h3><p>${boxes[1][1]}</p></div>
        <div class="arrow">→</div>
        <div class="box b3"><span class="num">3</span><h3>${boxes[2][0]}</h3><p>${boxes[2][1]}</p></div>
      </div>
      <div class="takeaway">${take}</div>
      <div class="brand-line">${footer}</div>
    </div>
  </div>
</body>
</html>`;
}

function linkedInHtml(lang) {
  const isUr = lang === "ur";
  const hook = isUr
    ? `آج صبح AI استعمال کی؟ — ڈیٹا سے سیکھنا، جادو نہیں`
    : `Did you use AI this morning? — Learning from data, not magic`;
  const take = isUr
    ? `AI = سیکھا ہوا نظام (Narrow AI)`
    : `AI = a learned system (Narrow AI)`;
  const footer = isUr ? footUr : footEn;
  return `<!DOCTYPE html>
<html lang="${lang}">
<head><meta charset="utf-8" /><style>${baseCss}
  html, body { width: 1200px; height: 627px; }
  .li {
    width: 1200px; height: 627px;
    background: linear-gradient(115deg, ${COLORS.ink}, ${COLORS.teal} 60%, #0E6A72);
    color: #fff; padding: 48px 56px;
    display: flex; align-items: center; gap: 36px; direction: ltr;
  }
  .li .h1 { font-size: 42px; margin: 0 0 14px; line-height: 1.25; }
  .li .sub { font-size: 26px; opacity: 0.92; }
  .pill {
    display: inline-block; margin-top: 22px;
    background: ${COLORS.amber}; color: ${COLORS.ink};
    font-weight: 700; font-size: 22px; padding: 10px 20px; border-radius: 999px;
  }
  .meta { margin-top: 18px; font-family: "Segoe UI", sans-serif; font-size: 16px; opacity: 0.8; }
</style></head>
<body>
  <div class="li">
    <img class="logo-lg" src="${LOGO_FILE}" alt="" style="width:140px;height:140px;flex-shrink:0" />
    <div dir="${isUr ? "rtl" : "ltr"}" style="flex:1">
      <h1 class="h1">${hook}</h1>
      <p class="sub">${take}</p>
      <div class="pill">Post 1 · AI Literacy</div>
      <div class="meta">${footer}</div>
    </div>
  </div>
</body>
</html>`;
}

function main() {
  // Heroes
  for (const lang of ["ur", "en"]) {
    const htmlPath = path.join(BUILD, `hero-${lang}.html`);
    fs.writeFileSync(htmlPath, heroHtml(lang), "utf8");
    chromeShot(htmlPath, path.join(ROOT, `POST-001-hero-${lang}-1080x1080.png`), 1080, 1080);
  }

  // Carousel UR
  for (const s of slidesUr) {
    const htmlPath = writeSlide(s, "ur", footUr);
    chromeShot(htmlPath, path.join(ROOT, s.name), 1080, 1080);
  }
  // Carousel EN
  for (const s of slidesEn) {
    const htmlPath = writeSlide(s, "en", footEn);
    chromeShot(htmlPath, path.join(ROOT, s.name), 1080, 1080);
  }

  // LinkedIn
  for (const lang of ["ur", "en"]) {
    const htmlPath = path.join(BUILD, `linkedin-${lang}.html`);
    fs.writeFileSync(htmlPath, linkedInHtml(lang), "utf8");
    chromeShot(
      htmlPath,
      path.join(ROOT, `POST-001-linkedin-${lang}-1200x627.png`),
      1200,
      627
    );
  }

  console.log("\\nPOST-001 visual set complete →", ROOT);
}

main();
