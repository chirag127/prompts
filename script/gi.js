/**
 * Icon Generation Script (gi.js)
 *
 * Purpose:
 *   Automatically generates PNG icons in multiple sizes (16x16, 48x48, 128x128)
 *   from a single SVG source file for browser extensions.
 *
 * Usage:
 *   1. Place your icon.svg in extension/icons/
 *   2. Install dependencies: npm install sharp --save-dev
 *   3. Run: node script/gi.js
 *
 * Output:
 *   Creates extension/icons/icon16.png, icon48.png, icon128.png
 *
 * Requirements:
 *   - sharp library (npm install sharp --save-dev)
 *   - extension/icons/icon.svg source file
 *
 * Author: Chirag Singhal (@chirag127)
 */

const fs = require('fs');
const path = require('path');
const sharp = require('sharp');

const ICON_SIZES = [16, 48, 128];
const SVG_PATH = path.join(__dirname, '../extension/icons/icon.svg');
const OUTPUT_DIR = path.join(__dirname, '../extension/icons');

async function generateIcons() {
  console.log('Generating extension icons...');

  // Check if SVG file exists
  if (!fs.existsSync(SVG_PATH)) {
    console.error(`SVG file not found: ${SVG_PATH}`);
    process.exit(1);
  }

  // Create output directory if it doesn't exist
  if (!fs.existsSync(OUTPUT_DIR)) {
    fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  }

  // Read SVG file
  const svgBuffer = fs.readFileSync(SVG_PATH);

  // Generate icons for each size
  for (const size of ICON_SIZES) {
    const outputPath = path.join(OUTPUT_DIR, `icon${size}.png`);

    try {
      await sharp(svgBuffer)
        .resize(size, size)
        .png()
        .toFile(outputPath);

      console.log(`Generated ${outputPath}`);
    } catch (error) {
      console.error(`Error generating icon${size}.png:`, error);
    }
  }

  console.log('Icon generation complete!');
}

generateIcons().catch(console.error);
