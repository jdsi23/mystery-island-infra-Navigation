#!/bin/bash

echo "🔧 Installing dependencies and generating Tailwind config..."

# Initialize npm if not already
[ ! -f package.json ] && npm init -y

# Install Tailwind CSS + PostCSS
npm install -D tailwindcss postcss autoprefixer

# Generate Tailwind config and PostCSS config if they don't exist
[ ! -f tailwind.config.js ] && npx tailwindcss init -p

echo "✅ Setup complete!"
