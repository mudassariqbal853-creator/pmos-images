# POST-003 visual set — Clarity Path (teal/amber)
# Heroes + 8+8 Instagram carousel. LinkedIn/TikTok skipped unless asked.
# UR art: Urdu script only (چیٹ جی پی ٹی، اے آئی). No Latin islands. No em dashes.
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD = Path(__file__).resolve().parent
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
LOGO_FILE = "file:///" + str((ROOT.parent / "Brand" / "PMOS-logo-mark.png")).replace("\\", "/")

COLORS = {
    "teal": "#0A555C",
    "ink": "#062E32",
    "mist": "#D7E8E6",
    "paper": "#F4F8F7",
    "amber": "#E8B84A",
    "charcoal": "#1A2B2E",
    "white": "#FFFFFF",
    "muted": "#3D6A6E",
    "dash": "#8AA8AB",
}

FONT_CSS = """
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
"""


def chrome_shot(html_path: Path, out_path: Path, w: int = 1080, h: int = 1080) -> None:
    uri = "file:///" + str(html_path).replace("\\", "/")
    subprocess.run(
        [
            CHROME,
            "--headless=new",
            "--disable-gpu",
            "--hide-scrollbars",
            "--force-device-scale-factor=1",
            f"--window-size={w},{h}",
            f"--screenshot={out_path}",
            uri,
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    print("ok", out_path.name)


BASE_CSS = f"""
  {FONT_CSS}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html, body {{ width: 1080px; height: 1080px; overflow: hidden; }}
  body {{
    font-family: "Dubai", "Segoe UI", sans-serif;
    color: {COLORS["charcoal"]};
  }}
  .slide {{
    width: 1080px; height: 1080px;
    position: relative; overflow: hidden;
    padding: 56px 64px 48px;
    display: flex; flex-direction: column;
  }}
  .slide.dark {{
    background:
      radial-gradient(ellipse 80% 50% at 15% 10%, rgba(232,184,74,0.22) 0%, transparent 55%),
      linear-gradient(155deg, {COLORS["ink"]} 0%, {COLORS["teal"]} 55%, #0E6A72 100%);
    color: {COLORS["white"]};
  }}
  .slide.light {{
    background:
      radial-gradient(ellipse 70% 40% at 90% 0%, rgba(10,85,92,0.08) 0%, transparent 60%),
      {COLORS["paper"]};
  }}
  .slide.light::before {{
    content: "";
    position: absolute; left: 0; top: 0; bottom: 0; width: 14px;
    background: {COLORS["teal"]};
  }}
  .topbar {{
    display: flex; align-items: center; justify-content: space-between;
    margin-bottom: 28px; direction: ltr;
  }}
  .badge {{
    display: inline-flex; align-items: center; gap: 8px;
    background: {COLORS["amber"]};
    color: {COLORS["ink"]};
    font-weight: 800; font-size: 20px;
    padding: 8px 18px; border-radius: 999px;
  }}
  .badge.en {{ font-family: "Segoe UI", sans-serif; font-size: 18px; }}
  .badge i {{ width: 8px; height: 8px; border-radius: 50%; background: #E85D04; display: inline-block; }}
  .logo {{ width: 64px; height: 64px; }}
  .content {{ flex: 1; display: flex; flex-direction: column; justify-content: center; }}
  .footer {{
    margin-top: auto;
    padding-top: 20px;
    border-top: 1.5px solid rgba(10,85,92,0.18);
    font-size: 18px; font-weight: 600;
    color: {COLORS["muted"]};
  }}
  .footer.en {{ font-family: "Segoe UI", sans-serif; direction: ltr; }}
  .slide.dark .footer {{
    border-top-color: rgba(255,255,255,0.2);
    color: rgba(255,255,255,0.75);
  }}
  .h1 {{
    font-size: 52px; font-weight: 700; line-height: 1.3;
    margin-bottom: 20px;
  }}
  .slide.dark .h1 {{ font-size: 56px; text-shadow: 0 4px 20px rgba(0,0,0,0.25); }}
  .h1 .hl {{ color: {COLORS["amber"]}; font-weight: 800; }}
  .slide.light .h1 .hl {{ color: {COLORS["teal"]}; }}
  .sub {{ font-size: 30px; font-weight: 500; line-height: 1.4; opacity: 0.92; }}
  .body {{ font-size: 32px; font-weight: 400; line-height: 1.45; }}
  .bullets {{ list-style: none; margin-top: 12px; }}
  .bullets li {{
    font-size: 30px; line-height: 1.35;
    padding: 14px 0;
    border-bottom: 1px solid rgba(10,85,92,0.12);
    display: flex; gap: 14px; align-items: flex-start;
  }}
  .slide.dark .bullets li {{ border-bottom-color: rgba(255,255,255,0.15); }}
  .dot {{
    flex-shrink: 0; width: 14px; height: 14px; margin-top: 12px;
    border-radius: 50%; background: {COLORS["amber"]};
  }}
  .cta-pill {{
    display: inline-block; margin-top: 24px;
    background: {COLORS["amber"]}; color: {COLORS["ink"]};
    font-size: 28px; font-weight: 700;
    padding: 14px 28px; border-radius: 999px;
  }}
  .truths {{ display: flex; flex-direction: column; gap: 16px; margin-top: 12px; }}
  .truth {{
    background: {COLORS["white"]};
    border: 2px solid {COLORS["mist"]};
    border-radius: 18px;
    padding: 20px 22px;
    display: flex; gap: 18px; align-items: center;
    font-size: 28px; font-weight: 600; line-height: 1.3;
    box-shadow: 0 6px 16px rgba(10,85,92,0.06);
  }}
  .truth .n {{
    width: 48px; height: 48px; border-radius: 14px; flex-shrink: 0;
    background: {COLORS["teal"]}; color: #fff;
    font-weight: 900; font-size: 22px;
    display: flex; align-items: center; justify-content: center;
  }}
  .compare-slide {{
    display: flex; gap: 16px; align-items: stretch; margin-top: 8px;
  }}
  .compare-slide.rtl {{ direction: rtl; }}
  .compare-slide.ltr {{ direction: ltr; }}
  .lane {{
    flex: 1; border-radius: 22px; padding: 28px 18px;
    text-align: center; min-height: 280px;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
  }}
  .lane-a {{
    background: linear-gradient(165deg, #0A555C 0%, #0E6A72 100%);
    color: #fff;
  }}
  .lane-b {{
    background: #F4F8F7;
    color: {COLORS["charcoal"]};
    border: 2.5px dashed {COLORS["dash"]};
  }}
  .lane h3 {{ font-size: 28px; font-weight: 700; margin-bottom: 12px; line-height: 1.3; }}
  .lane-b h3 {{ color: {COLORS["muted"]}; }}
  .lane p {{ font-size: 22px; line-height: 1.35; opacity: 0.95; }}
  .lane-b p {{ color: {COLORS["muted"]}; }}
  .lane-tag {{
    font-size: 15px; font-weight: 800;
    padding: 6px 14px; border-radius: 999px;
    margin-bottom: 14px;
  }}
  .lane-a .lane-tag {{ background: {COLORS["amber"]}; color: {COLORS["ink"]}; }}
  .lane-b .lane-tag {{ background: #E2EBEA; color: {COLORS["muted"]}; }}
"""

HERO_CSS = f"""
  {FONT_CSS}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html, body {{ width: 1080px; height: 1080px; overflow: hidden; }}
  body {{ font-family: "Dubai", "Segoe UI", sans-serif; color: #1A2B2E; }}
  .badge {{
    display: inline-flex; align-items: center; gap: 8px;
    background: #E8B84A; color: #062E32;
    font-weight: 800; font-size: 20px;
    padding: 8px 18px; border-radius: 999px;
  }}
  .badge.en {{ font-family: "Segoe UI", sans-serif; font-size: 18px; }}
  .badge i {{ width: 8px; height: 8px; border-radius: 50%; background: #E85D04; display: inline-block; }}
  .logo-lg {{ width: 88px; height: 88px; }}
  .hl {{ color: #E8B84A; font-weight: 800; }}
  .hero {{
    width: 1080px; height: 1080px; position: relative; overflow: hidden;
    background:
      radial-gradient(ellipse 80% 50% at 15% 10%, rgba(232,184,74,0.25) 0%, transparent 55%),
      linear-gradient(155deg, #062E32 0%, #0A555C 50%, #0E6A72 100%);
    color: #fff;
    padding: 48px 52px 40px;
    display: flex; flex-direction: column; justify-content: space-between;
  }}
  .hero-top {{ text-align: center; }}
  .hero .h1 {{
    font-size: 56px; font-weight: 700; line-height: 1.3;
    margin-bottom: 10px;
    text-shadow: 0 4px 20px rgba(0,0,0,0.25);
  }}
  .sub {{ font-size: 28px; font-weight: 500; line-height: 1.4; opacity: 0.92; }}
  .panel {{
    background: rgba(255,255,255,0.97);
    border-radius: 28px;
    padding: 22px 20px 18px;
    color: #1A2B2E;
    box-shadow: 0 18px 40px rgba(0,0,0,0.28);
  }}
  .panel-title {{
    text-align: center; font-size: 24px; font-weight: 700;
    color: #0A555C; margin-bottom: 16px;
  }}
  .compare {{ display: flex; gap: 14px; align-items: stretch; }}
  .compare.rtl {{ direction: rtl; }}
  .compare.ltr {{ direction: ltr; }}
  .lane {{
    flex: 1; border-radius: 22px; padding: 20px 14px 18px;
    text-align: center; min-height: 360px;
    display: flex; flex-direction: column; align-items: center; justify-content: flex-start;
  }}
  .lane-fluent {{
    background: linear-gradient(165deg, #0A555C 0%, #0E6A72 100%);
    color: #fff; box-shadow: 0 8px 20px rgba(10,85,92,0.28);
  }}
  .lane-predict {{
    background: #F4F8F7; color: #1A2B2E; border: 2.5px dashed #8AA8AB;
  }}
  .lane-tag {{
    font-size: 16px; font-weight: 800;
    padding: 5px 14px; border-radius: 999px; margin-bottom: 12px;
  }}
  .lane-fluent .lane-tag {{ background: #E8B84A; color: #062E32; }}
  .lane-predict .lane-tag {{ background: #E2EBEA; color: #3D6A6E; }}
  .lane h3 {{ font-size: 28px; font-weight: 700; line-height: 1.3; margin-bottom: 8px; }}
  .lane-predict h3 {{ color: #3D6A6E; }}
  .lane .desc {{ font-size: 22px; line-height: 1.35; opacity: 0.95; margin-bottom: 16px; }}
  .lane-predict .desc {{ color: #3D6A6E; opacity: 1; }}
  .visual {{
    margin-top: auto; width: 100%;
    display: flex; flex-direction: column; align-items: center; gap: 10px;
  }}
  .speech {{
    background: rgba(255,255,255,0.16);
    border-radius: 16px;
    padding: 14px 16px;
    font-size: 20px; font-weight: 600; line-height: 1.35;
    max-width: 92%;
  }}
  .chain {{
    display: flex; gap: 6px; flex-wrap: wrap; justify-content: center;
    padding: 4px 0;
  }}
  .chain.rtl {{ direction: rtl; }}
  .chain.ltr {{ direction: ltr; }}
  .chip {{
    background: #fff;
    border: 2px dashed #8AA8AB;
    color: #3D6A6E;
    border-radius: 12px;
    padding: 8px 10px;
    font-size: 18px; font-weight: 700;
  }}
  .chip.on {{
    background: #0A555C;
    border-style: solid;
    border-color: #0A555C;
    color: #fff;
  }}
  .arrow-row {{
    font-size: 22px; font-weight: 800; color: #8AA8AB;
  }}
  .status {{
    margin-top: 12px;
    font-size: 18px; font-weight: 700;
    padding: 6px 14px; border-radius: 999px;
  }}
  .lane-fluent .status {{ background: rgba(232,184,74,0.95); color: #062E32; }}
  .lane-predict .status {{ background: #E2EBEA; color: #3D6A6E; }}
  .takeaway {{
    display: block; text-align: center;
    background: #E8B84A; color: #062E32;
    font-size: 26px; font-weight: 700;
    padding: 12px 18px; border-radius: 999px;
    margin: 16px auto 10px; max-width: 96%; line-height: 1.4;
  }}
  .brand-line {{
    text-align: center;
    font-size: 18px; font-weight: 600; color: #3D6A6E;
  }}
  .brand-line.en {{ font-family: "Segoe UI", sans-serif; direction: ltr; }}
"""


def hero_html(lang: str) -> str:
    is_ur = lang == "ur"
    direction = "rtl" if is_ur else "ltr"
    compare_dir = "rtl" if is_ur else "ltr"
    chain_dir = "rtl" if is_ur else "ltr"
    badge_cls = "" if is_ur else " en"
    brand_cls = "" if is_ur else " en"
    badge = "اردو اے آئی لٹریسی · پوسٹ ۳" if is_ur else "AI Literacy · Post 3"
    hook = "چیٹ جی پی ٹی سوچتی ہے؟" if is_ur else 'Does <span class="hl">ChatGPT</span> think?'
    sub = "یا صرف اگلا لفظ جوڑتی ہے؟" if is_ur else "Or only predict the next words?"
    panel = "روانی دیکھیں · اصل طریقہ سمجھیں" if is_ur else "Fluency vs prediction"
    fluent_tag = "لگتا ہے سوچ" if is_ur else "Looks like thinking"
    fluent_h = "پُراعتماد جواب" if is_ur else "Fluent answer"
    fluent_d = "لکھائی صاف · لہجہ پکا" if is_ur else "Clean prose · confident tone"
    fluent_speech = "«ہاں، یہ بالکل درست ہے۔۔۔»" if is_ur else '"Yes, that is exactly right..."'
    fluent_status = "ظاہری شکل" if is_ur else "Appearance"
    pred_tag = "اصل طریقہ" if is_ur else "Actual method"
    pred_h = "اگلا قرین قیاس لفظ" if is_ur else "Next-word prediction"
    pred_d = "سیاق سے اگلا لفظ چننا" if is_ur else "Picks the next likely word"
    chip_w = "لفظ" if is_ur else "word"
    chip_n = "اگلا؟" if is_ur else "next?"
    arrows = "← ← ←" if is_ur else "→ → →"
    pred_status = "پیش گوئی انجن" if is_ur else "Prediction engine"
    take = (
        "روانی سچائی نہیں · پیش گوئی ≠ سوچ"
        if is_ur
        else "Fluency is not truth · Prediction ≠ thinking"
    )
    footer = (
        "پاکستان میڈیا او ایس · اردو اے آئی لٹریسی · پوسٹ ۳"
        if is_ur
        else "Pakistan Media OS · AI Literacy · Post 3"
    )
    return f"""<!DOCTYPE html>
<html lang="{lang}" dir="{direction}">
<head><meta charset="utf-8" /><style>{HERO_CSS}</style></head>
<body>
  <div class="hero" dir="{direction}">
    <div class="hero-top">
      <div style="display:flex;justify-content:space-between;align-items:center;direction:ltr;margin-bottom:18px">
        <div class="badge{badge_cls}" dir="{direction}"><i></i>{badge}</div>
        <img class="logo-lg" src="{LOGO_FILE}" alt="" />
      </div>
      <h1 class="h1">{hook}</h1>
      <p class="sub">{sub}</p>
    </div>
    <div class="panel">
      <div class="panel-title">{panel}</div>
      <div class="compare {compare_dir}">
        <div class="lane lane-fluent">
          <div class="lane-tag">{fluent_tag}</div>
          <h3>{fluent_h}</h3>
          <p class="desc">{fluent_d}</p>
          <div class="visual">
            <div class="speech">{fluent_speech}</div>
          </div>
          <div class="status">{fluent_status}</div>
        </div>
        <div class="lane lane-predict">
          <div class="lane-tag">{pred_tag}</div>
          <h3>{pred_h}</h3>
          <p class="desc">{pred_d}</p>
          <div class="visual">
            <div class="chain {chain_dir}">
              <div class="chip">{chip_w}</div>
              <div class="chip">{chip_w}</div>
              <div class="chip on">{chip_n}</div>
            </div>
            <div class="arrow-row">{arrows}</div>
          </div>
          <div class="status">{pred_status}</div>
        </div>
      </div>
      <div class="takeaway">{take}</div>
      <div class="brand-line{brand_cls}">{footer}</div>
    </div>
  </div>
</body>
</html>"""


def shell(lang: str, dark: bool, title: str, body_html: str, footer: str) -> str:
    direction = "rtl" if lang == "ur" else "ltr"
    theme = "dark" if dark else "light"
    badge_cls = "" if lang == "ur" else " en"
    footer_cls = "" if lang == "ur" else " en"
    series = "اردو اے آئی لٹریسی · پوسٹ ۳" if lang == "ur" else "AI Literacy · Post 3"
    title_block = f'<h1 class="h1">{title}</h1>' if title else ""
    return f"""<!DOCTYPE html>
<html lang="{lang}" dir="{direction}">
<head><meta charset="utf-8" /><style>{BASE_CSS}</style></head>
<body>
  <div class="slide {theme}" dir="{direction}">
    <div class="topbar">
      <div class="badge{badge_cls}" dir="{direction}"><i></i>{series}</div>
      <img class="logo" src="{LOGO_FILE}" alt="" />
    </div>
    <div class="content">
      {title_block}
      {body_html}
    </div>
    <div class="footer{footer_cls}">{footer}</div>
  </div>
</body>
</html>"""


FOOT_UR = "پاکستان میڈیا او ایس · اردو اے آئی لٹریسی · پوسٹ ۳"
FOOT_EN = "Pakistan Media OS · AI Literacy · Post 3"

SLIDES_UR = [
    {
        "name": "POST-003-slide-ur-01.png",
        "dark": True,
        "title": "چیٹ جی پی ٹی سوچتی ہے؟",
        "body": '<p class="sub">یا صرف اگلا لفظ جوڑتی ہے؟</p><p class="sub" style="margin-top:18px">پوسٹ ۳</p>',
    },
    {
        "name": "POST-003-slide-ur-02.png",
        "dark": False,
        "title": "عام غلط فہمی",
        "body": (
            '<p class="body">«جواب درست تھا، تو یہ ذہین ہے۔»</p>'
            '<p class="body" style="margin-top:22px">درست جواب ≠ سمجھ بوجھ</p>'
        ),
    },
    {
        "name": "POST-003-slide-ur-03.png",
        "dark": False,
        "title": "پوسٹ ۲ سے",
        "body": (
            '<p class="body">چیٹ ٹولز <strong>محدود اے آئی</strong> ہیں۔</p>'
            '<p class="body" style="margin-top:22px">آج: وہ کرتے کیا ہیں؟</p>'
        ),
    },
    {
        "name": "POST-003-slide-ur-04.png",
        "dark": False,
        "title": "اصل طریقہ",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>بڑی زبان ماڈل</span></li>'
            '<li><span class="dot"></span><span>سیاق دیکھ کر <strong>اگلا قرین قیاس لفظ</strong> چنتی ہے</span></li>'
            '<li><span class="dot"></span><span>بات چیت لگتی ہے، انجن پیش گوئی ہے</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-003-slide-ur-05.png",
        "dark": False,
        "title": "روانی کا جال",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>شائستہ لہجہ</span></li>'
            '<li><span class="dot"></span><span>لمبا جواب</span></li>'
            '<li><span class="dot"></span><span>پُراعتماد انداز</span></li>'
            "</ul>"
            '<p class="body" style="margin-top:22px;color:#0A555C;font-weight:700">یہ سب سچائی ثابت نہیں کرتے۔</p>'
        ),
    },
    {
        "name": "POST-003-slide-ur-06.png",
        "dark": False,
        "title": "کیا ہو سکتا ہے؟",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>غلط حقیقت، بناوٹی حوالہ</span></li>'
            '<li><span class="dot"></span><span>سننے میں صحیح، جانچنے پر غلط</span></li>'
            '<li><span class="dot"></span><span>پیسہ / صحت / قانون: پہلے تصدیق</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-003-slide-ur-07.png",
        "dark": False,
        "title": "سمجھدار استعمال",
        "body": (
            '<div class="truths">'
            '<div class="truth"><span class="n">۱</span><span>مسودہ، خیال، سوال</span></div>'
            '<div class="truth"><span class="n">۲</span><span>پھر انسان جانچے</span></div>'
            '<div class="truth"><span class="n">۳</span><span>«اے آئی نے کہا» کافی نہیں</span></div>'
            "</div>"
        ),
    },
    {
        "name": "POST-003-slide-ur-08.png",
        "dark": True,
        "title": "یاد رکھیں",
        "body": (
            '<p class="sub" style="font-size:34px">اوزار مددگار ہے۔ سوچ تمہاری ہے۔</p>'
            '<p class="sub" style="margin-top:20px">اگلا: اے آئی ہائپ بمقابلہ حقیقت</p>'
            '<div class="cta-pill">محفوظ کریں · فالو کریں · پوسٹ ۳</div>'
        ),
    },
]

SLIDES_EN = [
    {
        "name": "POST-003-slide-en-01.png",
        "dark": True,
        "title": 'Does <span class="hl">ChatGPT</span> think?',
        "body": '<p class="sub">Or only predict the next words?</p><p class="sub" style="margin-top:18px">Post 3</p>',
    },
    {
        "name": "POST-003-slide-en-02.png",
        "dark": False,
        "title": "Common myth",
        "body": (
            '<p class="body">“It answered correctly, so it understands.”</p>'
            '<p class="body" style="margin-top:22px">A correct answer ≠ understanding</p>'
        ),
    },
    {
        "name": "POST-003-slide-en-03.png",
        "dark": False,
        "title": "From Post 2",
        "body": (
            '<p class="body">Chat tools are <strong>Narrow AI</strong>.</p>'
            '<p class="body" style="margin-top:22px">Today: what do they actually do?</p>'
        ),
    },
    {
        "name": "POST-003-slide-en-04.png",
        "dark": False,
        "title": "The mechanism",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>Large language model</span></li>'
            '<li><span class="dot"></span><span>Picks the <strong>next likely word</strong> from context</span></li>'
            '<li><span class="dot"></span><span>Feels like chat. Engine is prediction.</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-003-slide-en-05.png",
        "dark": False,
        "title": "The fluency trap",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>Polite tone</span></li>'
            '<li><span class="dot"></span><span>Long answer</span></li>'
            '<li><span class="dot"></span><span>Confident voice</span></li>'
            "</ul>"
            '<p class="body" style="margin-top:22px;color:#0A555C;font-weight:700">None of that proves truth.</p>'
        ),
    },
    {
        "name": "POST-003-slide-en-06.png",
        "dark": False,
        "title": "What can go wrong?",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>False “facts,” invented citations</span></li>'
            '<li><span class="dot"></span><span>Sounds right, fails a check</span></li>'
            '<li><span class="dot"></span><span>Money / health / law: verify first</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-003-slide-en-07.png",
        "dark": False,
        "title": "Smart use",
        "body": (
            '<div class="truths">'
            '<div class="truth"><span class="n">1</span><span>Draft, ideas, questions</span></div>'
            '<div class="truth"><span class="n">2</span><span>Then a human checks</span></div>'
            '<div class="truth"><span class="n">3</span><span>“AI said so” is not enough</span></div>'
            "</div>"
        ),
    },
    {
        "name": "POST-003-slide-en-08.png",
        "dark": True,
        "title": "Keep this",
        "body": (
            '<p class="sub" style="font-size:34px">Tool helps. Judgment stays yours.</p>'
            '<p class="sub" style="margin-top:20px">Next: AI hype vs reality</p>'
            '<div class="cta-pill">Save · Follow · Post 3</div>'
        ),
    },
]


def write_slide(spec: dict, lang: str, footer: str) -> Path:
    html = shell(lang, spec["dark"], spec["title"], spec["body"], footer)
    html_path = BUILD / spec["name"].replace(".png", ".html")
    html_path.write_text(html, encoding="utf-8")
    return html_path


def assert_no_emdash(text: str, label: str) -> None:
    if "—" in text or "\u2014" in text:
        raise SystemExit(f"em dash found in {label}")


def assert_ur_no_latin(html: str, label: str) -> None:
    body = __import__("re").search(r"(?s)<body>(.*)</body>", html)
    if not body:
        return
    text = __import__("re").sub(r"(?s)<[^>]+>", " ", body.group(1))
    latin = __import__("re").findall(r"[A-Za-z]{2,}", text)
    if latin:
        raise SystemExit(f"Latin in UR art {label}: {sorted(set(latin))}")


def main() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)

    for lang in ("ur", "en"):
        html = hero_html(lang)
        assert_no_emdash(html, f"hero-{lang}")
        if lang == "ur":
            assert_ur_no_latin(html, "hero-ur")
        html_path = BUILD / f"hero-{lang}.html"
        html_path.write_text(html, encoding="utf-8")
        chrome_shot(html_path, ROOT / f"POST-003-hero-{lang}-1080x1080.png")

    for s in SLIDES_UR:
        html_path = write_slide(s, "ur", FOOT_UR)
        html = html_path.read_text(encoding="utf-8")
        assert_no_emdash(html, s["name"])
        assert_ur_no_latin(html, s["name"])
        chrome_shot(html_path, ROOT / s["name"])

    for s in SLIDES_EN:
        html_path = write_slide(s, "en", FOOT_EN)
        html = html_path.read_text(encoding="utf-8")
        assert_no_emdash(html, s["name"])
        chrome_shot(html_path, ROOT / s["name"])

    print("POST-003 visual set complete ->", ROOT)


if __name__ == "__main__":
    main()
