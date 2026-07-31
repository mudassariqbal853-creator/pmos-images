/**
 * POST-002 — Urdu hero only (approval gate before EN / carousel)
 */
const path = require("path");
const { execFileSync } = require("child_process");

const ROOT = path.join(__dirname, "..");
const BUILD = __dirname;
const CHROME = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";

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
    { stdio: "inherit" }
  );
  console.log("ok", path.basename(outPath));
}

const htmlPath = path.join(BUILD, "hero-ur.html");
const outPath = path.join(ROOT, "POST-002-hero-ur-1080x1080.png");
chromeShot(htmlPath, outPath, 1080, 1080);
console.log("POST-002 Urdu hero →", outPath);
