# POST-010 visual set - Clarity Path (teal/amber)
# Heroes + 8+8 Instagram carousel. LinkedIn/TikTok skipped unless asked.
# UR art: Urdu script only. No Latin islands. No em dashes.
# Concept: code shared (control lost) vs code kept (five-check habit)
import re
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
    font-size: 50px; font-weight: 700; line-height: 1.3;
    margin-bottom: 20px;
  }}
  .slide.dark .h1 {{ font-size: 54px; text-shadow: 0 4px 20px rgba(0,0,0,0.25); }}
  .h1 .hl {{ color: {COLORS["amber"]}; font-weight: 800; }}
  .slide.light .h1 .hl {{ color: {COLORS["teal"]}; }}
  .sub {{ font-size: 30px; font-weight: 500; line-height: 1.4; opacity: 0.92; }}
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
  .truths {{ display: flex; flex-direction: column; gap: 12px; margin-top: 12px; }}
  .truth {{
    background: {COLORS["white"]};
    border: 2px solid {COLORS["mist"]};
    border-radius: 18px;
    padding: 16px 20px;
    display: flex; gap: 16px; align-items: center;
    font-size: 26px; font-weight: 600; line-height: 1.3;
    box-shadow: 0 6px 16px rgba(10,85,92,0.06);
  }}
  .truth .n {{
    width: 44px; height: 44px; border-radius: 14px; flex-shrink: 0;
    background: {COLORS["teal"]}; color: #fff;
    font-weight: 900; font-size: 20px;
    display: flex; align-items: center; justify-content: center;
  }}
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
    font-size: 48px; font-weight: 700; line-height: 1.3;
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
  .lane-bold {{
    background: linear-gradient(165deg, #C9A03A 0%, #E8B84A 55%, #F0C96A 100%);
    color: #062E32; box-shadow: 0 8px 20px rgba(200,160,50,0.28);
  }}
  .lane-read {{
    background: linear-gradient(165deg, #0A555C 0%, #0E6A72 100%);
    color: #fff; box-shadow: 0 8px 20px rgba(10,85,92,0.28);
  }}
  .lane-tag {{
    font-size: 16px; font-weight: 800;
    padding: 5px 14px; border-radius: 999px; margin-bottom: 12px;
  }}
  .lane-bold .lane-tag {{ background: rgba(6,46,50,0.12); color: #062E32; }}
  .lane-read .lane-tag {{ background: #E8B84A; color: #062E32; }}
  .lane h3 {{ font-size: 25px; font-weight: 700; line-height: 1.35; margin-bottom: 8px; }}
  .lane .desc {{ font-size: 19px; line-height: 1.35; opacity: 0.95; margin-bottom: 14px; }}
  .visual {{
    margin-top: auto; width: 100%;
    display: flex; flex-direction: column; align-items: center; gap: 10px;
  }}
  .door-sign {{
    width: 88%;
    background: rgba(255,255,255,0.55);
    border: 2px solid rgba(6,46,50,0.2);
    border-radius: 14px;
    padding: 20px 14px;
    box-shadow: inset 0 0 0 1px rgba(255,255,255,0.35);
  }}
  .door-sign .mega {{
    font-size: 25px; font-weight: 900; line-height: 1.3;
    letter-spacing: 0.02em;
  }}
  .door-sign .blank {{
    margin-top: 14px;
    height: 10px; border-radius: 6px;
    background: rgba(6,46,50,0.12);
  }}
  .door-sign .blank.short {{ width: 55%; margin-left: auto; margin-right: auto; }}
  .door-sign .blank.mid {{ width: 78%; margin-left: auto; margin-right: auto; }}
  .door-sign.ltr .mega {{ font-family: "Segoe UI", sans-serif; }}
  .checks {{
    background: rgba(255,255,255,0.14);
    border-radius: 16px;
    padding: 12px 10px;
    width: 92%;
  }}
  .checks.rtl {{ text-align: right; }}
  .checks.ltr {{ text-align: left; }}
  .checks .row {{
    font-size: 19px; font-weight: 700; line-height: 1.4;
    padding: 5px 0;
    border-bottom: 1px solid rgba(255,255,255,0.16);
    display: flex; align-items: center; gap: 10px;
  }}
  .checks .row:last-child {{ border-bottom: none; }}
  .ico {{
    width: 28px; height: 28px; border-radius: 8px; flex-shrink: 0;
    background: rgba(232,184,74,0.95); color: #062E32;
    font-size: 14px; font-weight: 900;
    display: flex; align-items: center; justify-content: center;
  }}
  .status {{
    margin-top: 12px;
    font-size: 18px; font-weight: 700;
    padding: 6px 14px; border-radius: 999px;
  }}
  .lane-bold .status {{ background: rgba(6,46,50,0.88); color: #E8B84A; }}
  .lane-read .status {{ background: rgba(232,184,74,0.95); color: #062E32; }}
  .takeaway {{
    display: block; text-align: center;
    background: #E8B84A; color: #062E32;
    font-size: 24px; font-weight: 700;
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
    badge_cls = "" if is_ur else " en"
    brand_cls = "" if is_ur else " en"
    checks_cls = "rtl" if is_ur else "ltr"
    door_cls = "" if is_ur else " ltr"
    badge = "ڈیجیٹل تحفظ · پوسٹ ۱۰" if is_ur else "Digital Safety · Post 10"
    hook = (
        "او ٹی پی مانگیں تو رکو"
        if is_ur
        else 'If someone asks for your <span class="hl">OTP</span>, stop'
    )
    sub = "کوڈ کبھی ہاتھ سے نہیں نکلنا چاہیے" if is_ur else "The code was never meant to leave your hands"
    panel = "کوڈ بتایا · کوڈ روکا" if is_ur else "Code shared · code kept"
    b_tag = "بتایا؟" if is_ur else "Shared?"
    b_h = "دباؤ میں کوڈ" if is_ur else "Code under pressure"
    b_d = "\"دس منٹ میں بند\"" if is_ur else '"Blocked in ten minutes"'
    b_mega = "اختیار گیا" if is_ur else "Control gone"
    b_status = "خطرناک" if is_ur else "Risky"
    r_tag = "روکا؟" if is_ur else "Kept?"
    r_h = "پانچ چیک کی عادت" if is_ur else "The five-check habit"
    r_d = "خود مانگا · دباؤ · خود کال" if is_ur else "Asked myself · pressure · call back"
    checks = (
        [("۱", "خود مانگا؟"), ("۲", "دباؤ ہے؟"), ("۳", "خود کال کرو")]
        if is_ur
        else [("1", "Asked myself?"), ("2", "Pressure?"), ("3", "Call back")]
    )
    r_status = "محفوظ عادت" if is_ur else "Safe habit"
    take = "کوڈ کبھی ہاتھ سے نہیں نکلنا چاہیے" if is_ur else "The code was never meant to leave your hands"
    footer = (
        "پاکستان میڈیا او ایس · ڈیجیٹل تحفظ · پوسٹ ۱۰"
        if is_ur
        else "Pakistan Media OS · Digital Safety · Post 10"
    )
    check_rows = "".join(
        f'<div class="row"><span class="ico">{n}</span><span>{label}</span></div>'
        for n, label in checks
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
        <div class="lane lane-bold">
          <div class="lane-tag">{b_tag}</div>
          <h3>{b_h}</h3>
          <p class="desc">{b_d}</p>
          <div class="visual">
            <div class="door-sign{door_cls}">
              <div class="mega">{b_mega}</div>
              <div class="blank mid"></div>
              <div class="blank short"></div>
            </div>
          </div>
          <div class="status">{b_status}</div>
        </div>
        <div class="lane lane-read">
          <div class="lane-tag">{r_tag}</div>
          <h3>{r_h}</h3>
          <p class="desc">{r_d}</p>
          <div class="visual">
            <div class="checks {checks_cls}">
              {check_rows}
            </div>
          </div>
          <div class="status">{r_status}</div>
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
    series = "ڈیجیٹل تحفظ · پوسٹ ۱۰" if lang == "ur" else "Digital Safety · Post 10"
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


FOOT_UR = "پاکستان میڈیا او ایس · ڈیجیٹل تحفظ · پوسٹ ۱۰"
FOOT_EN = "Pakistan Media OS · Digital Safety · Post 10"

SLIDES_UR = [
    {
        "name": "POST-010-slide-ur-01.png",
        "dark": True,
        "title": "او ٹی پی مانگیں تو رکو",
        "body": '<p class="sub">کیا خود مانگا تھا؟</p><p class="sub" style="margin-top:18px">پوسٹ ۱۰</p>',
    },
    {
        "name": "POST-010-slide-ur-02.png",
        "dark": False,
        "title": "\u201cدس منٹ میں اکاؤنٹ بند\u201d",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>نام معلوم تھا</span></li>'
            '<li><span class="dot"></span><span>دباؤ میں کوڈ بتا دیا</span></li>'
            '<li><span class="dot"></span><span>کنٹرول ہاتھ سے نکل گیا</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-010-slide-ur-03.png",
        "dark": False,
        "title": "کوڈ = اختیار",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>او ٹی پی ثابت کرتا ہے مالک کون ہے</span></li>'
            '<li><span class="dot"></span><span>پڑھنا مطلب اختیار دینا</span></li>'
            '<li><span class="dot"></span><span>حقیقی ادارے کال پر نہیں مانگتے</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-010-slide-ur-04.png",
        "dark": False,
        "title": "عام شکلیں ۱ تا ۳",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>جعلی بینک کال</span></li>'
            '<li><span class="dot"></span><span>جعلی انعام / لکی ڈرا</span></li>'
            '<li><span class="dot"></span><span>جعلی ڈیلیوری کوڈ</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-010-slide-ur-05.png",
        "dark": False,
        "title": "عام شکلیں ۴ و ۵",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>سم سویپ کی کوشش</span></li>'
            '<li><span class="dot"></span><span>جعلی ٹیکنیکل سپورٹ</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-010-slide-ur-06.png",
        "dark": False,
        "title": "یاد رکھیں",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>نام جاننا مطلب اصلی ہونا نہیں</span></li>'
            '<li><span class="dot"></span><span>"صرف تصدیق" بھی خطرہ ہے</span></li>'
            '<li><span class="dot"></span><span>جلدی، حربہ ہے، حقیقت نہیں</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-010-slide-ur-07.png",
        "dark": False,
        "title": "پانچ سوال",
        "body": (
            '<div class="truths">'
            '<div class="truth"><span class="n">۱</span><span>خود مانگا؟</span></div>'
            '<div class="truth"><span class="n">۲</span><span>کوئی پڑھنے کو کہہ رہا؟</span></div>'
            '<div class="truth"><span class="n">۳</span><span>دباؤ ہے؟</span></div>'
            '<div class="truth"><span class="n">۴</span><span>ادارہ ایسا کرتا ہے؟</span></div>'
            '<div class="truth"><span class="n">۵</span><span>شک ہو تو خود کال کرو</span></div>'
            "</div>"
        ),
    },
    {
        "name": "POST-010-slide-ur-08.png",
        "dark": True,
        "title": "یاد رکھیں",
        "body": (
            '<p class="sub" style="font-size:32px">کوڈ کبھی ہاتھ سے نہیں نکلنا چاہیے۔</p>'
            '<p class="sub" style="margin-top:20px">محفوظ کریں · گھر والوں سے شیئر کریں</p>'
            '<div class="cta-pill">محفوظ کریں · فالو کریں · پوسٹ ۱۰</div>'
        ),
    },
]

SLIDES_EN = [
    {
        "name": "POST-010-slide-en-01.png",
        "dark": True,
        "title": 'If someone asks for your <span class="hl">OTP</span>, stop',
        "body": '<p class="sub">Did you ask for it yourself?</p><p class="sub" style="margin-top:18px">Post 10</p>',
    },
    {
        "name": "POST-010-slide-en-02.png",
        "dark": False,
        "title": '"Account blocked in ten minutes"',
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>They knew your name</span></li>'
            '<li><span class="dot"></span><span>Code read out under pressure</span></li>'
            '<li><span class="dot"></span><span>Control gone</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-010-slide-en-03.png",
        "dark": False,
        "title": "Code = control",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>An OTP proves who is acting</span></li>'
            '<li><span class="dot"></span><span>Reading it out hands over control</span></li>'
            '<li><span class="dot"></span><span>Real organisations don\u2019t call and ask</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-010-slide-en-04.png",
        "dark": False,
        "title": "Common shapes 1-3",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>Fake bank call</span></li>'
            '<li><span class="dot"></span><span>Fake prize / lucky draw</span></li>'
            '<li><span class="dot"></span><span>Fake delivery code</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-010-slide-en-05.png",
        "dark": False,
        "title": "Common shapes 4-5",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>SIM-swap attempt</span></li>'
            '<li><span class="dot"></span><span>Fake tech support</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-010-slide-en-06.png",
        "dark": False,
        "title": "Remember",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>Knowing your name doesn\u2019t prove they\u2019re real</span></li>'
            '<li><span class="dot"></span><span>"Just a verification" is still a risk</span></li>'
            '<li><span class="dot"></span><span>Urgency is a tactic, not a fact</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-010-slide-en-07.png",
        "dark": False,
        "title": "Five questions",
        "body": (
            '<div class="truths">'
            '<div class="truth"><span class="n">1</span><span>Asked for it yourself?</span></div>'
            '<div class="truth"><span class="n">2</span><span>Someone asking to read it?</span></div>'
            '<div class="truth"><span class="n">3</span><span>Under pressure?</span></div>'
            '<div class="truth"><span class="n">4</span><span>Would they actually do this?</span></div>'
            '<div class="truth"><span class="n">5</span><span>Unsure? Call back yourself</span></div>'
            "</div>"
        ),
    },
    {
        "name": "POST-010-slide-en-08.png",
        "dark": True,
        "title": "Remember",
        "body": (
            '<p class="sub" style="font-size:32px">The code was never meant to leave your hands.</p>'
            '<p class="sub" style="margin-top:20px">Save this &middot; share with family</p>'
            '<div class="cta-pill">Save · Follow · Post 10</div>'
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
    body = re.search(r"(?s)<body>(.*)</body>", html)
    if not body:
        return
    text = re.sub(r"(?s)<[^>]+>", " ", body.group(1))
    latin = re.findall(r"[A-Za-z]{2,}", text)
    if latin:
        raise SystemExit(f"Latin in UR art {label}: {sorted(set(latin))}")


def main() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    BUILD.mkdir(parents=True, exist_ok=True)

    for lang in ("ur", "en"):
        html = hero_html(lang)
        assert_no_emdash(html, f"hero-{lang}")
        if lang == "ur":
            assert_ur_no_latin(html, "hero-ur")
        html_path = BUILD / f"hero-{lang}.html"
        html_path.write_text(html, encoding="utf-8")
        chrome_shot(html_path, ROOT / f"POST-010-hero-{lang}-1080x1080.png")

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

    print("POST-010 visual set complete ->", ROOT)


if __name__ == "__main__":
    main()
