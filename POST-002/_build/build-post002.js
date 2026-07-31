/**
 * POST-002 visual set — Clarity Path (teal/amber)
 * Heroes + 8+8 Instagram carousel. LinkedIn/TikTok skipped unless asked.
 * Run: node build-post002.js   OR use build-post002.ps1
 */
const fs = require("fs");
const path = require("path");
const { execFileSync } = require("child_process");

const ROOT = path.join(__dirname, "..");
const BUILD = __dirname;
const CHROME = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const LOGO_FILE =
  "file:///" +
  path.join(ROOT, "..", "Brand", "PMOS-logo-mark.png").replace(/\\/g, "/");

const COLORS = {
  teal: "#0A555C",
  ink: "#062E32",
  mist: "#D7E8E6",
  paper: "#F4F8F7",
  amber: "#E8B84A",
  charcoal: "#1A2B2E",
  white: "#FFFFFF",
  muted: "#3D6A6E",
  dash: "#8AA8AB",
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

const fontCss = `
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
`;

const baseCss = `
  ${fontCss}
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
    color: ${COLORS.muted};
    direction: ltr;
  }
  .slide.dark .footer {
    border-top-color: rgba(255,255,255,0.2);
    color: rgba(255,255,255,0.75);
  }
  .h1 {
    font-size: 54px; font-weight: 700; line-height: 1.25;
    margin-bottom: 20px;
  }
  .slide.dark .h1 { font-size: 58px; text-shadow: 0 4px 20px rgba(0,0,0,0.25); }
  .h1 .en { font-family: "Segoe UI", sans-serif; color: ${COLORS.amber}; font-weight: 800; }
  .sub { font-size: 30px; font-weight: 500; line-height: 1.4; opacity: 0.92; }
  .body { font-size: 32px; font-weight: 400; line-height: 1.45; }
  .bullets { list-style: none; margin-top: 12px; }
  .bullets li {
    font-size: 30px; line-height: 1.35;
    padding: 14px 0;
    border-bottom: 1px solid rgba(10,85,92,0.12);
    display: flex; gap: 14px; align-items: flex-start;
  }
  .slide.dark .bullets li { border-bottom-color: rgba(255,255,255,0.15); }
  .dot {
    flex-shrink: 0; width: 14px; height: 14px; margin-top: 12px;
    border-radius: 50%; background: ${COLORS.amber};
  }
  .en-term { font-family: "Segoe UI", sans-serif; font-weight: 700; }
  .cta-pill {
    display: inline-block; margin-top: 24px;
    background: ${COLORS.amber}; color: ${COLORS.ink};
    font-size: 28px; font-weight: 700;
    padding: 14px 28px; border-radius: 999px;
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
  .truth .x {
    width: 48px; height: 48px; border-radius: 14px; flex-shrink: 0;
    background: #E8ECEB; color: ${COLORS.muted};
    font-family: "Segoe UI", sans-serif; font-weight: 900; font-size: 22px;
    display: flex; align-items: center; justify-content: center;
  }
  .compare-slide {
    display: flex; direction: ltr; gap: 16px; align-items: stretch; margin-top: 8px;
  }
  .lane {
    flex: 1; border-radius: 22px; padding: 28px 18px;
    text-align: center;
    min-height: 320px;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
  }
  .lane-narrow {
    background: linear-gradient(165deg, #0A555C 0%, #0E6A72 100%);
    color: #fff;
  }
  .lane-agi {
    background: #F4F8F7;
    color: ${COLORS.charcoal};
    border: 2.5px dashed ${COLORS.dash};
  }
  .lane h3 { font-size: 30px; font-weight: 700; margin-bottom: 12px; }
  .lane-agi h3 { color: ${COLORS.muted}; }
  .lane p { font-size: 24px; line-height: 1.35; opacity: 0.95; }
  .lane-agi p { color: ${COLORS.muted}; }
  .lane-tag {
    font-family: "Segoe UI", sans-serif;
    font-size: 14px; font-weight: 800; letter-spacing: 0.04em;
    text-transform: uppercase;
    padding: 6px 14px; border-radius: 999px;
    margin-bottom: 14px;
  }
  .lane-narrow .lane-tag { background: ${COLORS.amber}; color: ${COLORS.ink}; }
  .lane-agi .lane-tag { background: #E2EBEA; color: ${COLORS.muted}; }
`;

const heroCss = `
  ${fontCss}
  * { box-sizing: border-box; margin: 0; padding: 0; }
  html, body { width: 1080px; height: 1080px; overflow: hidden; }
  body { font-family: "Dubai", "Segoe UI", sans-serif; color: #1A2B2E; }
  .badge {
    display: inline-flex; align-items: center; gap: 8px;
    background: #E8B84A; color: #062E32;
    font-family: "Segoe UI", sans-serif;
    font-weight: 800; font-size: 18px;
    padding: 8px 18px; border-radius: 999px;
  }
  .badge i { width: 8px; height: 8px; border-radius: 50%; background: #E85D04; display: inline-block; }
  .logo-lg { width: 88px; height: 88px; }
  .en { font-family: "Segoe UI", sans-serif; color: #E8B84A; font-weight: 800; }
  .en-term { font-family: "Segoe UI", sans-serif; font-weight: 700; }
  .hero {
    width: 1080px; height: 1080px; position: relative; overflow: hidden;
    background:
      radial-gradient(ellipse 80% 50% at 15% 10%, rgba(232,184,74,0.25) 0%, transparent 55%),
      linear-gradient(155deg, #062E32 0%, #0A555C 50%, #0E6A72 100%);
    color: #fff;
    padding: 48px 52px 40px;
    display: flex; flex-direction: column; justify-content: space-between;
  }
  .hero-top { text-align: center; }
  .hero .h1 {
    font-size: 58px; font-weight: 700; line-height: 1.25;
    margin-bottom: 10px;
    text-shadow: 0 4px 20px rgba(0,0,0,0.25);
  }
  .sub { font-size: 28px; font-weight: 500; line-height: 1.4; opacity: 0.92; }
  .panel {
    background: rgba(255,255,255,0.97);
    border-radius: 28px;
    padding: 22px 20px 18px;
    color: #1A2B2E;
    box-shadow: 0 18px 40px rgba(0,0,0,0.28);
  }
  .panel-title {
    text-align: center; font-size: 22px; font-weight: 700;
    color: #0A555C; margin-bottom: 16px;
  }
  .compare { display: flex; direction: ltr; gap: 16px; align-items: stretch; }
  .lane {
    flex: 1; border-radius: 22px; padding: 22px 16px 20px;
    text-align: center; min-height: 340px;
    display: flex; flex-direction: column; align-items: center; justify-content: flex-start;
  }
  .lane-narrow {
    background: linear-gradient(165deg, #0A555C 0%, #0E6A72 100%);
    color: #fff; box-shadow: 0 8px 20px rgba(10,85,92,0.28);
  }
  .lane-agi {
    background: #F4F8F7; color: #1A2B2E; border: 2.5px dashed #8AA8AB;
  }
  .lane-tag {
    font-family: "Segoe UI", sans-serif;
    font-size: 13px; font-weight: 800; letter-spacing: 0.04em;
    text-transform: uppercase;
    padding: 5px 12px; border-radius: 999px; margin-bottom: 12px;
  }
  .lane-narrow .lane-tag { background: #E8B84A; color: #062E32; }
  .lane-agi .lane-tag { background: #E2EBEA; color: #3D6A6E; }
  .lane h3 { font-size: 28px; font-weight: 700; line-height: 1.25; margin-bottom: 8px; }
  .lane-agi h3 { color: #3D6A6E; }
  .lane .desc { font-size: 20px; line-height: 1.35; opacity: 0.95; margin-bottom: 18px; }
  .lane-agi .desc { color: #3D6A6E; opacity: 1; }
  .icons {
    display: flex; gap: 10px; justify-content: center; flex-wrap: wrap;
    margin-top: auto; padding-top: 8px;
  }
  .icon {
    width: 64px; height: 64px; border-radius: 16px;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    gap: 2px; font-size: 11px; font-weight: 700; font-family: "Segoe UI", sans-serif;
  }
  .lane-narrow .icon { background: rgba(255,255,255,0.16); color: #fff; }
  .lane-agi .icon {
    background: transparent; border: 2px dashed #8AA8AB; color: #3D6A6E;
    width: 88px; height: 88px; border-radius: 20px; font-size: 13px;
  }
  .status {
    margin-top: 14px; font-size: 18px; font-weight: 700;
    padding: 6px 14px; border-radius: 999px;
  }
  .lane-narrow .status { background: rgba(232,184,74,0.95); color: #062E32; }
  .lane-agi .status { background: #E2EBEA; color: #3D6A6E; }
  .takeaway {
    display: block; text-align: center;
    background: #E8B84A; color: #062E32;
    font-size: 26px; font-weight: 700;
    padding: 12px 18px; border-radius: 999px;
    margin: 16px auto 10px; max-width: 96%; line-height: 1.35;
  }
  .brand-line {
    text-align: center; font-family: "Segoe UI", sans-serif;
    font-size: 17px; font-weight: 600; color: #3D6A6E; direction: ltr;
  }
`;

const iconsNarrow = `
  <div class="icons">
    <div class="icon" aria-hidden="true">
      <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
        <rect x="7" y="2" width="10" height="20" rx="2"/>
        <circle cx="12" cy="18" r="1" fill="currentColor" stroke="none"/>
      </svg>
      phone
    </div>
    <div class="icon" aria-hidden="true">
      <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
        <path d="M4 6h12a2 2 0 0 1 2 2v6a2 2 0 0 1-2 2H9l-4 3v-3H4a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2z"/>
      </svg>
      chat
    </div>
    <div class="icon" aria-hidden="true">
      <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
        <path d="M12 21s7-5.2 7-11a7 7 0 1 0-14 0c0 5.8 7 11 7 11z"/>
        <circle cx="12" cy="10" r="2.2"/>
      </svg>
      map
    </div>
  </div>`;

const iconResearch = `
  <div class="icons">
    <div class="icon" aria-hidden="true">
      <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-dasharray="3 2.5">
        <circle cx="12" cy="12" r="8"/>
        <path d="M12 8v4l2.5 2.5"/>
      </svg>
      research
    </div>
  </div>`;

function heroHtml(lang) {
  const isUr = lang === "ur";
  const dir = isUr ? "rtl" : "ltr";
  const series = isUr ? "Urdu AI Literacy — Post 2" : "AI Literacy — Post 2";
  const hook = isUr
    ? `<span class="en">ChatGPT</span> = <span class="en">General AI</span>؟`
    : `Is <span class="en">ChatGPT</span> <span class="en">General AI</span>?`;
  const sub = isUr
    ? `مختصر جواب: نہیں — فرق سمجھیں`
    : `Short answer: No — know the difference`;
  const panelTitle = "Narrow AI vs General AI (AGI)";
  const narrowDesc = isUr ? `مخصوص کام · آج موجود` : `Specific job · exists today`;
  const agiDesc = isUr
    ? `وسیع صلاحیت · ابھی finished نہیں`
    : `Broad ability · not finished today`;
  const narrowStatus = isUr ? `آج کام کر رہا ہے` : `Working today`;
  const agiStatus = isUr ? `تیار product نہیں` : `Not a finished product`;
  const take = isUr
    ? `Narrow = مخصوص کام · AGI ابھی finished نہیں`
    : `Narrow = specific jobs · AGI not finished today`;
  const footer = isUr
    ? `Pakistan Media OS · Urdu AI Literacy — Post 2`
    : `Pakistan Media OS · AI Literacy — Post 2`;

  return `<!DOCTYPE html>
<html lang="${lang}" dir="${dir}">
<head><meta charset="utf-8" /><style>${heroCss}</style></head>
<body>
  <div class="hero" dir="${dir}">
    <div class="hero-top">
      <div style="display:flex;justify-content:space-between;align-items:center;direction:ltr;margin-bottom:20px">
        <div class="badge"><i></i>${series}</div>
        <img class="logo-lg" src="${LOGO_FILE}" alt="" />
      </div>
      <h1 class="h1">${hook}</h1>
      <p class="sub">${sub}</p>
    </div>
    <div class="panel">
      <div class="panel-title">${panelTitle}</div>
      <div class="compare">
        <div class="lane lane-narrow">
          <div class="lane-tag">Exists today</div>
          <h3><span class="en-term">Narrow AI</span></h3>
          <p class="desc">${narrowDesc}</p>
          ${iconsNarrow}
          <div class="status">${narrowStatus}</div>
        </div>
        <div class="lane lane-agi">
          <div class="lane-tag">Not finished</div>
          <h3><span class="en-term">General AI / AGI</span></h3>
          <p class="desc">${agiDesc}</p>
          ${iconResearch}
          <div class="status">${agiStatus}</div>
        </div>
      </div>
      <div class="takeaway">${take}</div>
      <div class="brand-line">${footer}</div>
    </div>
  </div>
</body>
</html>`;
}

function shell({ lang, dark, title, bodyHtml, footer }) {
  const dir = lang === "ur" ? "rtl" : "ltr";
  const series =
    lang === "ur" ? "Urdu AI Literacy — Post 2" : "AI Literacy — Post 2";
  return `<!DOCTYPE html>
<html lang="${lang}" dir="${dir}">
<head><meta charset="utf-8" /><style>${baseCss}</style></head>
<body>
  <div class="slide ${dark ? "dark" : "light"}" dir="${dir}">
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

const footUr = "Pakistan Media OS · Urdu AI Literacy — Post 2";
const footEn = "Pakistan Media OS · AI Literacy — Post 2";

const slidesUr = [
  {
    name: "POST-002-slide-ur-01.png",
    dark: true,
    title: `<span class="en">ChatGPT</span> = <span class="en">General AI</span>؟`,
    body: `<p class="sub">مختصر جواب: نہیں۔ فرق سمجھیں — Post 2</p>`,
  },
  {
    name: "POST-002-slide-ur-02.png",
    dark: false,
    title: `POST-001 سے یاد`,
    body: `<p class="body">AI مخصوص کام کے لیے ڈیٹا سے سیکھتی ہے۔</p>
    <p class="body" style="margin-top:22px">آج نام: <strong class="en-term">Narrow</strong> vs <strong class="en-term">General</strong></p>`,
  },
  {
    name: "POST-002-slide-ur-03.png",
    dark: false,
    title: `<span class="en-term">Narrow AI</span> کیا ہے؟`,
    body: `<p class="body">ایک کام (یا محدود کاموں) کے لیے بنایا گیا نظام</p>
    <ul class="bullets">
      <li><span class="dot"></span><span>face unlock · spam · keyboard · چیٹ ٹیکسٹ</span></li>
      <li><span class="dot"></span><span>“کمزور” = محدود دائرہ — <strong>بےکار نہیں</strong></span></li>
    </ul>`,
  },
  {
    name: "POST-002-slide-ur-04.png",
    dark: false,
    title: `<span class="en-term">General AI (AGI)</span>`,
    body: `<p class="body">وسیع، انسان جیسی عمومی صلاحیت — کئی شعبے</p>
    <ul class="bullets">
      <li><span class="dot"></span><span>آج: <strong>تیار product نہیں</strong></span></li>
      <li><span class="dot"></span><span>تعریف/ٹیسٹ پر اتفاق مکمل نہیں</span></li>
    </ul>`,
  },
  {
    name: "POST-002-slide-ur-05.png",
    dark: false,
    title: `موازنہ`,
    body: `<div class="compare-slide">
      <div class="lane lane-narrow">
        <div class="lane-tag">Exists today</div>
        <h3><span class="en-term">Narrow</span></h3>
        <p>مخصوص کام · آج موجود</p>
      </div>
      <div class="lane lane-agi">
        <div class="lane-tag">Not finished</div>
        <h3><span class="en-term">AGI</span></h3>
        <p>عمومی ذہانت · ابھی finished نہیں</p>
      </div>
    </div>`,
  },
  {
    name: "POST-002-slide-ur-06.png",
    dark: false,
    title: `آپ کے ارد گرد (سب Narrow)`,
    body: `<ul class="bullets">
      <li><span class="dot"></span><span>فون unlock / suggestions</span></li>
      <li><span class="dot"></span><span>Feed · maps ETA</span></li>
      <li><span class="dot"></span><span>Wallet fraud alerts</span></li>
      <li><span class="dot"></span><span>ChatGPT-class chat</span></li>
    </ul>`,
  },
  {
    name: "POST-002-slide-ur-07.png",
    dark: false,
    title: `غلط فہمیاں`,
    body: `<div class="truths">
      <div class="truth"><span class="x">✗</span><span>ایک ٹاسک میں بہتر = <strong>AGI</strong></span></div>
      <div class="truth"><span class="x">✗</span><span>ChatGPT = انسان جیسی سمجھ</span></div>
      <div class="truth"><span class="x">✗</span><span>“AGI آ گئی” بغیر ثبوت</span></div>
    </div>`,
  },
  {
    name: "POST-002-slide-ur-08.png",
    dark: true,
    title: `سوال یاد رکھیں`,
    body: `<p class="sub" style="font-size:36px"><em>یہ سسٹم کس کام کے لیے ہے؟</em></p>
    <p class="sub" style="margin-top:20px">اگلا: AI hype vs reality</p>
    <div class="cta-pill">Save · Follow · Post 2</div>`,
  },
];

const slidesEn = [
  {
    name: "POST-002-slide-en-01.png",
    dark: true,
    title: `Is <span class="en">ChatGPT</span> <span class="en">General AI</span>?`,
    body: `<p class="sub">Short answer: No. Know the difference — Post 2</p>`,
  },
  {
    name: "POST-002-slide-en-02.png",
    dark: false,
    title: `From Post 1`,
    body: `<p class="body">AI learns from data for specific jobs.</p>
    <p class="body" style="margin-top:22px">Today’s names: <strong class="en-term">Narrow</strong> vs <strong class="en-term">General</strong></p>`,
  },
  {
    name: "POST-002-slide-en-03.png",
    dark: false,
    title: `What is <span class="en-term">Narrow AI</span>?`,
    body: `<p class="body">Built for one job (or a narrow set)</p>
    <ul class="bullets">
      <li><span class="dot"></span><span>face unlock · spam · keyboard · chat text</span></li>
      <li><span class="dot"></span><span>“Weak” = limited scope — <strong>not useless</strong></span></li>
    </ul>`,
  },
  {
    name: "POST-002-slide-en-04.png",
    dark: false,
    title: `<span class="en-term">General AI (AGI)</span>`,
    body: `<p class="body">Broad, human-level ability across domains</p>
    <ul class="bullets">
      <li><span class="dot"></span><span>Today: <strong>not a finished product</strong></span></li>
      <li><span class="dot"></span><span>No single agreed test</span></li>
    </ul>`,
  },
  {
    name: "POST-002-slide-en-05.png",
    dark: false,
    title: `Compare`,
    body: `<div class="compare-slide">
      <div class="lane lane-narrow">
        <div class="lane-tag">Exists today</div>
        <h3><span class="en-term">Narrow</span></h3>
        <p>specific job · exists today</p>
      </div>
      <div class="lane lane-agi">
        <div class="lane-tag">Not finished</div>
        <h3><span class="en-term">AGI</span></h3>
        <p>general ability · not finished today</p>
      </div>
    </div>`,
  },
  {
    name: "POST-002-slide-en-06.png",
    dark: false,
    title: `Around you (all Narrow)`,
    body: `<ul class="bullets">
      <li><span class="dot"></span><span>Phone unlock / suggestions</span></li>
      <li><span class="dot"></span><span>Feed · maps ETA</span></li>
      <li><span class="dot"></span><span>Wallet fraud alerts</span></li>
      <li><span class="dot"></span><span>ChatGPT-class chat</span></li>
    </ul>`,
  },
  {
    name: "POST-002-slide-en-07.png",
    dark: false,
    title: `Myths`,
    body: `<div class="truths">
      <div class="truth"><span class="x">✗</span><span>Better at one task = <strong>AGI</strong></span></div>
      <div class="truth"><span class="x">✗</span><span>ChatGPT = human understanding</span></div>
      <div class="truth"><span class="x">✗</span><span>“AGI is here” with no evidence</span></div>
    </div>`,
  },
  {
    name: "POST-002-slide-en-08.png",
    dark: true,
    title: `Ask this`,
    body: `<p class="sub" style="font-size:36px"><em>What job is this system for?</em></p>
    <p class="sub" style="margin-top:20px">Next: AI hype vs reality</p>
    <div class="cta-pill">Save · Follow · Post 2</div>`,
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

function main() {
  // Heroes (UR already approved; regenerate both for consistency)
  for (const lang of ["ur", "en"]) {
    const htmlPath = path.join(BUILD, `hero-${lang}.html`);
    fs.writeFileSync(htmlPath, heroHtml(lang), "utf8");
    chromeShot(
      htmlPath,
      path.join(ROOT, `POST-002-hero-${lang}-1080x1080.png`),
      1080,
      1080
    );
  }

  for (const s of slidesUr) {
    const htmlPath = writeSlide(s, "ur", footUr);
    chromeShot(htmlPath, path.join(ROOT, s.name), 1080, 1080);
  }
  for (const s of slidesEn) {
    const htmlPath = writeSlide(s, "en", footEn);
    chromeShot(htmlPath, path.join(ROOT, s.name), 1080, 1080);
  }

  console.log("\nPOST-002 visual set complete →", ROOT);
}

main();
