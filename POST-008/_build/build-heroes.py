# POST-008 — generate UR hero first (pause for Owner approval), then EN
# Concept: bold headline only vs full-read (issuer · date · scope)
# UR art: Urdu script only. No Latin islands. No em dashes.
# No real agency seals / fake official notices.
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD = Path(__file__).resolve().parent
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
LOGO_FILE = "file:///" + str((ROOT.parent / "Brand" / "PMOS-logo-mark.png")).replace("\\", "/")

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
    font-size: 50px; font-weight: 700; line-height: 1.3;
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
  .lane h3 {{ font-size: 26px; font-weight: 700; line-height: 1.35; margin-bottom: 8px; }}
  .lane .desc {{ font-size: 20px; line-height: 1.35; opacity: 0.95; margin-bottom: 14px; }}
  .visual {{
    margin-top: auto; width: 100%;
    display: flex; flex-direction: column; align-items: center; gap: 10px;
  }}
  .door-sign {{
    width: 88%;
    background: rgba(255,255,255,0.55);
    border: 2px solid rgba(6,46,50,0.2);
    border-radius: 14px;
    padding: 22px 14px;
    box-shadow: inset 0 0 0 1px rgba(255,255,255,0.35);
  }}
  .door-sign .mega {{
    font-size: 28px; font-weight: 900; line-height: 1.3;
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
    font-size: 20px; font-weight: 700; line-height: 1.4;
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


def chrome_shot(html_path: Path, out_path: Path) -> None:
    uri = "file:///" + str(html_path).replace("\\", "/")
    subprocess.run(
        [
            CHROME,
            "--headless=new",
            "--disable-gpu",
            "--hide-scrollbars",
            "--force-device-scale-factor=1",
            "--window-size=1080,1080",
            f"--screenshot={out_path}",
            uri,
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    print("ok", out_path.name)


def hero_html(lang: str) -> str:
    is_ur = lang == "ur"
    direction = "rtl" if is_ur else "ltr"
    compare_dir = "rtl" if is_ur else "ltr"
    badge_cls = "" if is_ur else " en"
    brand_cls = "" if is_ur else " en"
    checks_cls = "rtl" if is_ur else "ltr"
    door_cls = "" if is_ur else " ltr"
    badge = "شہری خواندگی · پوسٹ ۸" if is_ur else "Civic Literacy · Post 8"
    hook = "نوٹس دیکھا یا پڑھا؟" if is_ur else 'Did you <span class="hl">see</span> the notice, or <span class="hl">read</span> it?'
    sub = "سرکاری نوٹس کیسے پڑھیں" if is_ur else "How to read an official notice"
    panel = "موٹی سطر · پورا پڑھنا" if is_ur else "Bold line · full read"
    b_tag = "دیکھا؟" if is_ur else "Seen?"
    b_h = "موٹی سطر" if is_ur else "Bold line only"
    b_d = "عنوان = پورا حکم؟" if is_ur else "Headline = whole rule?"
    b_mega = "ٹائمنگ بدل گئی" if is_ur else "Timing changed"
    b_status = "ناکافی" if is_ur else "Not enough"
    r_tag = "پڑھا؟" if is_ur else "Read?"
    r_h = "پورا پڑھنا" if is_ur else "Full read"
    r_d = "جاری کنندہ · تاریخ · دائرہ کار" if is_ur else "Issuer · date · scope"
    checks = (
        [("۱", "جاری کنندہ"), ("۲", "تاریخ"), ("۳", "دائرہ کار")]
        if is_ur
        else [("1", "Issuer"), ("2", "Date"), ("3", "Scope")]
    )
    r_status = "پڑھنے کی عادت" if is_ur else "Read habit"
    take = "موٹی سطر پورا حکم نہیں" if is_ur else "A bold line is not the whole rule"
    footer = (
        "پاکستان میڈیا او ایس · شہری خواندگی · پوسٹ ۸"
        if is_ur
        else "Pakistan Media OS · Civic Literacy · Post 8"
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
    import sys

    langs = sys.argv[1:] or ["ur"]
    ROOT.mkdir(parents=True, exist_ok=True)
    BUILD.mkdir(parents=True, exist_ok=True)
    for lang in langs:
        html = hero_html(lang)
        assert_no_emdash(html, f"hero-{lang}")
        if lang == "ur":
            assert_ur_no_latin(html, "hero-ur")
        html_path = BUILD / f"hero-{lang}.html"
        html_path.write_text(html, encoding="utf-8")
        chrome_shot(html_path, ROOT / f"POST-008-hero-{lang}-1080x1080.png")
    print("POST-008 hero(s) ready:", ", ".join(langs), "-> pause before carousel.")


if __name__ == "__main__":
    main()
