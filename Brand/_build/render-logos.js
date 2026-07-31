const sharp = require("sharp");
const fs = require("fs");
const path = require("path");

const ROOT = path.join(__dirname, "..");
const BUILD = __dirname;

async function svgFile(name, outName, width, height) {
  const svg = fs.readFileSync(path.join(BUILD, name));
  const pipeline = sharp(svg, { density: 300 }).resize(width, height, {
    fit: "contain",
    background: { r: 0, g: 0, b: 0, alpha: 0 },
  });
  await pipeline.png().toFile(path.join(ROOT, outName));
  const meta = await sharp(path.join(ROOT, outName)).metadata();
  console.log(`OK ${outName} ${meta.width}x${meta.height}`);
}

async function main() {
  await svgFile("mark-transparent.svg", "PMOS-logo-mark.png", 1024, 1024);
  await svgFile("mark.svg", "PMOS-avatar-1024.png", 1024, 1024);
  await svgFile("mark.svg", "PMOS-avatar-512.png", 512, 512);
  await svgFile("lockup-en.svg", "PMOS-logo-lockup-en.png", 1600, 420);
  await svgFile("lockup-bilingual.svg", "PMOS-logo-lockup-bilingual.png", 1600, 480);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
