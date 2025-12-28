# Menu2Website Electron Frontend

Electron desktop application for converting physical menus to websites.

## Features

1. **Welcome Screen** - Introduction to the application
2. **Signup** - User registration (TODO - currently click-through)
3. **Photo Upload** - Upload up to 16 menu photos with drag & drop support
4. **Backend Processing** - Calls Python backend to extract colors and menu text
5. **Color Scheme Display** - Shows extracted colors across multiple pages
6. **Menu Navigation** - View menu items and prices with arrow navigation
7. **Email Results** - Send results to user via email (TODO)

## Installation

```bash
cd electron_frontend
npm install
```

## Running the Application

```bash
npm start
```

## Project Structure

```
electron_frontend/
├── main.js              # Main Electron process
├── package.json         # Node.js dependencies
├── pages/              # HTML pages
│   ├── welcome.html    # Welcome screen
│   ├── signup.html     # Signup form
│   ├── upload.html     # Photo upload interface
│   ├── processing.html # Backend processing & results
│   └── results.html    # Final results with navigation
├── css/                # Stylesheets
│   └── styles.css      # Main CSS file
├── js/                 # JavaScript files (if needed)
└── assets/             # Images and other assets
```

## Backend Integration

The Electron app communicates with the Python backend via IPC (Inter-Process Communication):

- **extract-colors**: Calls `python_backend/smart_color.py` to extract color scheme
- **process-images**: Calls `python_backend/smart_menu.py` to extract menu text and prices

## Development Notes

- The application uses Electron's `ipcRenderer` and `ipcMain` for communication between renderer and main processes
- Node integration is enabled for direct access to Node.js APIs
- Session storage is used to pass data between pages
- Demo mode available if backend processing fails

## TODO

- [ ] Implement authentication system
- [ ] Complete email functionality
- [ ] Add more sophisticated menu parsing
- [ ] Implement website export functionality
- [ ] Add configuration for color scheme customization
- [ ] Package application for distribution

## Requirements

- Node.js 14 or higher
- Python 3.8 or higher (for backend)
- Backend dependencies (see `../python_backend/README.md`)
