// Shared demo data for development and fallback
const DEMO_DATA = {
  colors: [
    { name: 'Primary', rgb: [52, 152, 219], hex: '#3498db' },
    { name: 'Secondary', rgb: [44, 62, 80], hex: '#2c3e50' },
    { name: 'Accent', rgb: [231, 76, 60], hex: '#e74c3c' },
    { name: 'Background', rgb: [236, 240, 241], hex: '#ecf0f1' }
  ],
  menuPages: [
    { 
      filename: 'Page 1', 
      content: '🍕 Margherita Pizza - $15.99\n🥗 Caesar Salad - $12.99\n🍝 Spaghetti Carbonara - $16.99' 
    },
    { 
      filename: 'Page 2', 
      content: '🍰 Chocolate Cake - $8.99\n🍮 Tiramisu - $9.99\n🍦 Ice Cream Sundae - $6.99' 
    },
    { 
      filename: 'Page 3', 
      content: '☕ Espresso - $3.99\n🍵 Green Tea - $2.99\n🥤 Fresh Juice - $5.99' 
    }
  ]
};

// Make available to browser context
if (typeof window !== 'undefined') {
  window.DEMO_DATA = DEMO_DATA;
}

// Make available to Node.js context
if (typeof module !== 'undefined' && module.exports) {
  module.exports = DEMO_DATA;
}
